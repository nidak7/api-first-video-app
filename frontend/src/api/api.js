const BASE_URL = "https://video-backend-d3i5.onrender.com";

export async function fetchDashboardVideos() {
  const response = await fetch(`${BASE_URL}/video/dashboard`);
  if (!response.ok) {
    throw new Error("Failed to fetch videos");
  }
  return response.json();
}
