export default async function handler(req, res) {
  const videoId = req.query.videoId;
  if (!videoId) {
    return res.status(400).json({ error: "videoId missing" });
  }

  const r = await fetch(
    `https://youtubetranscript.p.rapidapi.com/?id=${videoId}`,
    {
      headers: {
        "X-RapidAPI-Key": process.env.RAPIDAPI_KEY,
        "X-RapidAPI-Host": "youtubetranscript.p.rapidapi.com"
      }
    }
  );

  const data = await r.json();
  res.status(200).json(data);
}
