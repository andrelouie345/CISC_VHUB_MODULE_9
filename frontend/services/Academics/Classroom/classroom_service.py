import json
from pathlib import Path


class ClassroomService:
    def __init__(self):
        # Resolve data file relative to the frontend package so the service
        # works regardless of current working directory.
        try:
            base = Path(__file__).resolve().parents[4]  # repo_root/frontend
        except Exception:
            base = Path(".")

        self.data_file = base / "services" / "Academics" / "data" / "classroom_data.json"
        self.data = {"classes": [], "topics": [], "posts": []}
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            # Safe fallback when the data file is missing; keeps the app
            # from crashing and presents an empty dataset instead.
            self.data = {"classes": [], "topics": [], "posts": []}
        except Exception:
            # Any other error -> keep empty dataset but do not raise.
            self.data = {"classes": [], "topics": [], "posts": []}

    def load_classes(self):
        # No exception raised here; returns empty list if no data.
        return self.data.get("classes", [])

    def load_topics(self, class_id):
        return [t for t in self.data.get("topics", []) if t.get("class_id") == class_id]

    def load_posts(self, class_id, filter_type="all", topic_id=None):
        posts = [p for p in self.data.get("posts", []) if p.get("class_id") == class_id]
        if filter_type != "all":
            posts = [p for p in posts if p.get("type") == filter_type]
        if topic_id is not None:
            posts = [p for p in posts if p.get("topic_id") == topic_id]
        return posts