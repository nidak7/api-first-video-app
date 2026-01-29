from extensions import db
from bson import ObjectId
from datetime import datetime

class Video:
    def __init__(self, title, description, youtube_id, thumbnail_url, is_active=True, video_filename=None):
        self.title = title
        self.description = description
        self.youtube_id = youtube_id
        self.thumbnail_url = thumbnail_url
        self.is_active = is_active
        self.created_at = datetime.utcnow()
        self.video_filename = video_filename

    def save(self):
        return db.videos.insert_one({
            "title": self.title,
            "description": self.description,
            "youtube_id": self.youtube_id,
            "thumbnail_url": self.thumbnail_url,
            "is_active": self.is_active,
            "created_at": self.created_at
        })

    @staticmethod
    def get_dashboard_videos(limit=2):
        from extensions import db
        videos = list(db.videos.find({"is_active": True}).limit(limit))
        for v in videos:
            if "video_filename" in v:
                v["video_url"] = f"http://127.0.0.1:5000/static/videos/{v['video_filename']}"
        return videos
    
    @staticmethod
    def find_by_id(video_id):
        return db.videos.find_one({"_id": ObjectId(video_id)})
