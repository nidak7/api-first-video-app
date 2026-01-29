const BASE_URL = "http://127.0.0.1:5000";

export async function fetchDashboardVideos() {
  const response = await fetch(`${BASE_URL}/video/dashboard`);
  if (!response.ok) {
    throw new Error("Failed to fetch videos");
  }
  return response.json();
}
