from datetime import datetime
from typing import List, Dict, Any, Optional
from pathlib import Path
import json

# Try to import Django models only when available. Importing Django at
# module import time breaks the frontend app when Django settings are
# not configured (common when running the PyQt frontend standalone).
DJANGO_AVAILABLE = True
try:
    from django.contrib.auth import get_user_model
    from backend.apps.Messaging.models import MessageThread, ThreadParticipant, Message
    User = get_user_model()
except Exception:
    DJANGO_AVAILABLE = False


class DataManager:
    """DataManager for Messaging UI.

    When Django is available (running integrated), this proxies to the
    real database models. When not available (standalone frontend run)
    it falls back to lightweight JSON-backed read-only data so the UI
    can start without a backend.
    """

    def __init__(
        self,
        username: str = None,
        roles: list = None,
        primary_role: str = None,
        token: str = None
    ):
        self.username = username
        self.roles = roles if roles else []
        self.primary_role = primary_role
        self.token = token
        self.current_user = username

        # Paths to local frontend data (used as a safe fallback)
        repo_root = Path(__file__).resolve().parents[3]
        self._mock_users_path = repo_root / "frontend" / "services" / "Academics" / "data" / "users_data.json"
        self._mock_members_path = repo_root / "frontend" / "Mock" / "members.json"

        self._load_local_users()

    # ---------------------------
    # User Management
    # ---------------------------
    def create_user(self, user_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if DJANGO_AVAILABLE:
            new_user = User.objects.create_user(
                username=user_data.get('username'),
                email=user_data.get('email'),
                password=user_data.get('password')
            )
            new_user.first_name = user_data.get('first_name', '')
            new_user.last_name = user_data.get('last_name', '')
            new_user.save()
            return {
                'id': new_user.id,
                'username': new_user.username,
                'email': new_user.email,
                'created_at': str(new_user.date_joined)
            }

        # Fallback: append to in-memory users list (does not persist)
        u = {
            'id': max([x.get('id', 0) for x in self._local_users] or [0]) + 1,
            'username': user_data.get('username'),
            'email': user_data.get('email'),
            'first_name': user_data.get('first_name', ''),
            'last_name': user_data.get('last_name', ''),
            'created_at': datetime.utcnow().isoformat(),
        }
        self._local_users.append(u)
        return u

    def get_user(self, user_id: int) -> Optional[Dict[str, Any]]:
        if DJANGO_AVAILABLE:
            try:
                user = User.objects.get(pk=user_id)
                return {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                }
            except User.DoesNotExist:
                return None

        return next((u for u in self._local_users if u.get('id') == user_id), None)

    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        if DJANGO_AVAILABLE:
            user = User.objects.filter(email=email).first()
            if user:
                return {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                }
            return None

        return next(({
            'id': u.get('id'), 'username': u.get('username'), 'email': u.get('email')
        } for u in self._local_users if (u.get('email') or '').lower() == (email or '').lower()), None)

    def get_all_users(self) -> List[Dict[str, Any]]:
        if DJANGO_AVAILABLE:
            return [
                {
                    'id': u.id,
                    'username': u.username,
                    'email': u.email
                }
                for u in User.objects.all()
            ]

        return [
            {'id': u.get('id'), 'username': u.get('username'), 'email': u.get('email')}
            for u in self._local_users
        ]

    def update_user(self, user_id: int, updated_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if DJANGO_AVAILABLE:
            try:
                user = User.objects.get(pk=user_id)
                for key, value in updated_data.items():
                    setattr(user, key, value)
                user.save()
                return {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                }
            except User.DoesNotExist:
                return None

        u = next((x for x in self._local_users if x.get('id') == user_id), None)
        if not u:
            return None
        u.update(updated_data)
        return u

    def delete_user(self, user_id: int) -> bool:
        if DJANGO_AVAILABLE:
            try:
                user = User.objects.get(pk=user_id)
                user.delete()
                return True
            except User.DoesNotExist:
                return False

        before = len(self._local_users)
        self._local_users = [x for x in self._local_users if x.get('id') != user_id]
        return len(self._local_users) < before

    # ---------------------------
    # Message Management
    # ---------------------------
    def create_message(self, message_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        # Finds the thread and sender, creates new message
        if DJANGO_AVAILABLE:
            try:
                thread = MessageThread.objects.get(pk=message_data['thread_id'])
                sender = User.objects.get(pk=message_data['sender_id'])
                msg = Message.objects.create(
                    thread=thread,
                    sender=sender,
                    content=message_data['content']
                )
                return {
                    'id': msg.id,
                    'thread_id': msg.thread.id,
                    'sender_id': msg.sender.id,
                    'content': msg.content,
                    'created_at': str(msg.sent_at)
                }
            except Exception as e:
                print(f"Error creating message: {e}")
                return None

        # Fallback: not implemented for standalone frontend
        print("create_message: Django not available, operation skipped")
        return None

    def get_message(self, message_id: int) -> Optional[Dict[str, Any]]:
        if DJANGO_AVAILABLE:
            msg = Message.objects.filter(pk=message_id).first()
            if msg:
                return {
                    'id': msg.id,
                    'thread_id': msg.thread.id,
                    'sender_id': msg.sender.id,
                    'content': msg.content,
                    'created_at': str(msg.sent_at)
                }
            return None
        return None

    def get_messages_by_user(self, user_id: int) -> List[Dict[str, Any]]:
        if DJANGO_AVAILABLE:
            return [
                {
                    'id': m.id,
                    'thread_id': m.thread.id,
                    'sender_id': m.sender.id,
                    'content': m.content,
                    'created_at': str(m.sent_at)
                }
                for m in Message.objects.filter(sender__id=user_id)
            ]
        return []

    def update_message(self, message_id: int, updated_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if DJANGO_AVAILABLE:
            msg = Message.objects.filter(pk=message_id).first()
            if msg:
                for key, value in updated_data.items():
                    setattr(msg, key, value)
                msg.save()
                return {
                    'id': msg.id,
                    'thread_id': msg.thread.id,
                    'sender_id': msg.sender.id,
                    'content': msg.content,
                    'created_at': str(msg.sent_at)
                }
        return None

    def delete_message(self, message_id: int) -> bool:
        if DJANGO_AVAILABLE:
            msg = Message.objects.filter(pk=message_id).first()
            if msg:
                msg.delete()
                return True
        return False

    # ---------------------------
    # Conversation & Thread Management
    # ---------------------------
    def create_conversation(self, conversation_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if DJANGO_AVAILABLE:
            try:
                thread = MessageThread.objects.create(
                    subject=conversation_data.get('subject', '')
                )
                participants = conversation_data.get('participants', [])
                for user_id in participants:
                    user = User.objects.get(pk=user_id)
                    ThreadParticipant.objects.create(thread=thread, user=user)
                return {
                    'id': thread.id,
                    'subject': thread.subject,
                    'created_at': str(thread.created_at)
                }
            except Exception as e:
                print(f"Error creating conversation or thread: {e}")
                return None
        # Fallback: not available in standalone frontend
        return None

    def get_conversation(self, conversation_id: int) -> Optional[Dict[str, Any]]:
        if DJANGO_AVAILABLE:
            thread = MessageThread.objects.filter(pk=conversation_id).first()
            if thread:
                return {
                    'id': thread.id,
                    'subject': thread.subject,
                    'participants': [p.user.id for p in thread.participants.all()],
                    'created_at': str(thread.created_at)
                }
        return None

    # --- Local JSON helpers for standalone frontend ---
    def _load_local_users(self):
        self._local_users = []
        # Prefer the users_data.json used by frontend services, fallback to Mock members
        paths = [self._mock_users_path, self._mock_members_path]
        for p in paths:
            try:
                if p.exists():
                    with open(p, "r", encoding="utf-8") as fh:
                        data = json.load(fh)
                        # data may be a dict with key 'users' or a list
                        if isinstance(data, dict):
                            # try common keys
                            for key in ("users", "members", "data", "items"):
                                if key in data and isinstance(data[key], list):
                                    self._local_users = data[key]
                                    return
                            # otherwise try to find list values
                            lists = [v for v in data.values() if isinstance(v, list)]
                            if lists:
                                self._local_users = lists[0]
                                return
                        elif isinstance(data, list):
                            self._local_users = data
                            return
            except Exception:
                continue

        # final fallback: empty list
        self._local_users = []

    def get_conversations_by_user(self, user_id: int) -> List[Dict[str, Any]]:
        return [
            {
                'id': thread.id,
                'subject': thread.subject,
                'created_at': str(thread.created_at)
            }
            for thread in MessageThread.objects.filter(participants__user__id=user_id).distinct()
        ]

    # ---------------------------
    # Notification Management
    # ---------------------------
    # For notification logic, recommend making a Django model for Notification
    # Example:
    # class Notification(models.Model):
    #     user = models.ForeignKey(User, on_delete=models.CASCADE)
    #     content = models.TextField()
    #     is_read = models.BooleanField(default=False)
    #     created_at = models.DateTimeField(auto_now_add=True)

    # Then adapt corresponding CRUD logic similar to above.

    # ---------------------------
    # Utility Methods
    # ---------------------------
    # Reload and session helper logic can be updated similarly if needed,
    # but session management would be handled by Django's authentication framework.

    # Inquiry helpers would create or query threads/messages/participants similarly.

    # Use Django ORM filters for all list, get, and update operations.

