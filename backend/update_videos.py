
from extensions import init_db
from flask import Flask

app = Flask(__name__)
init_db()

from extensions import db

video_files = {
    "Python for Beginners": "python_intro.mp4",
    "SQL for Beginners": "sql_intro.mp4",
    "How Startups Fail": "startup_fail.mp4"
}

for title, filename in video_files.items():
    result = db.videos.update_one(
        {"title": title},
        {"$set": {"video_filename": filename}}
    )
    if result.modified_count:
        print(f"Updated: {title} → {filename}")
    else:
        print(f"Skipped (maybe already updated): {title}")

print("All videos updated with filenames")
