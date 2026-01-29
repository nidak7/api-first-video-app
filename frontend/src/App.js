import { useEffect, useState } from "react";
import { fetchDashboardVideos } from "./api/api";

function App() {
  const [videos, setVideos] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
  fetchDashboardVideos()
    .then(data => {
      console.log("VIDEOS:", data);
      setVideos(data);
    })
    .catch(err => setError(err.message));
}, []);

  const handlePlay = async (videoId) => {
    try {
      const res = await fetch(`http://127.0.0.1:5000/video/${videoId}/stream`);
      const data = await res.json();
      console.log("Playback token:", data);
    } catch (err) {
      console.error("Failed to play video");
    }
  };

  const [selectedVideo, setSelectedVideo] = useState(null);


  return (
    <div style={{ padding: "20px" }}>
      <h1>Video Dashboard</h1>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {videos.length === 0 && <p>No videos found</p>}

      {videos.map(video => (
        <div key={video.id} style={{ marginBottom: "15px" }}>
          <h3>{video.title}</h3>
          <p>{video.description}</p>
          <img src={video.thumbnail_url} style={{ display: "block", marginBottom: "10px" }} alt={video.title} width="300" />
          <video
            controls
            width="600"
            poster={video.thumbnail_url}
          >
            <source src={video.video_url} type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
      ))}

    </div>
  );
}

export default App;
