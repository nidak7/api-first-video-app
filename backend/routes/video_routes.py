from flask import Blueprint, jsonify, request
from models.video import Video
import uuid

video_bp = Blueprint('video', __name__, url_prefix='/video')

@video_bp.route("/create", methods=["POST"])
def create_video():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid payload"}), 400

    required_fields = ["title", "description", "youtube_id", "thumbnail_url"]
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"{field} is required"}), 400

    video = Video(
        title=data["title"],
        description=data["description"],
        youtube_id=data["youtube_id"],
        thumbnail_url=data["thumbnail_url"]
    )

    video.save()

    return jsonify({"message": "Video created successfully"}), 201


@video_bp.route('/dashboard', methods=['GET'])
def dashboard():
    videos = Video.get_dashboard_videos()
    result = []
    for v in videos:
        result.append({
            "id": str(v["_id"]),
            "title": v["title"],
            "description": v["description"],
            "thumbnail_url": f"http://127.0.0.1:5000/static/thumbnails/{v['thumbnail_url']}",
            "video_url": f"http://127.0.0.1:5000/static/videos/{v['video_filename']}"
        })

    return jsonify(result), 200


@video_bp.route('/<video_id>/stream', methods=['GET'])
def stream_video(video_id):
    video = Video.find_by_id(video_id)
    if not video or not video.get("is_active"):
        return jsonify({"error": "Video not found"}), 404
    
    import uuid

    playback_token = str(uuid.uuid4())
    video_url = f"http://127.0.0.1:5000/static/videos/{video['video_filename']}"
    
    return jsonify({
        "video_id": str(video["_id"]),
        "playback_token": playback_token,
        "video_url": video_url
    }), 200
