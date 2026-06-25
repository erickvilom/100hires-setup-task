from youtube_transcript_api import YouTubeTranscriptApi
import os

videos = [
    {
        "expert": "lily-ray",
        "video_id": "J7ayY_Mdk4w",
        "title": "What IS and ISN'T Working in SEO in 2024 - Aleyda Solis and Lily Ray"
    },
    {
        "expert": "koray-tugberk-gubur",
        "video_id": "mSHq_HxOyTA",
        "title": "AI Agents Semantic SEO and Fortune 500 Secrets - Koray Tugberk"
    },
    {
        "expert": "nathan-gotch",
        "video_id": "Y88G1JbGsEE",
        "title": "Building AI SEO SaaS - Nathan Gotch"
    },
    {
        "expert": "aleyda-solis",
        "video_id": "NNl9sRCv3q8",
        "title": "How to Prepare for AI Search - Aleyda Solis"
    },
    {
        "expert": "alex-birkett",
        "video_id": "nQv2o2X7DDU",
        "title": "SEO Strategy 2026 - The Shift Most B2B SaaS Are Missing"
    },
]

output_dir = "research/youtube-transcripts"
os.makedirs(output_dir, exist_ok=True)

for video in videos:
    expert = video["expert"]
    video_id = video["video_id"]
    title = video["title"]
    filename = f"{output_dir}/{expert}_{video_id}.md"

    print(f"Fetching transcript for {expert}: {title}...")

    try:
        ytt = YouTubeTranscriptApi()
        transcript = ytt.fetch(video_id)
        full_text = " ".join([entry.text for entry in transcript])

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"**Expert:** {expert}\n")
            f.write(f"**Video ID:** {video_id}\n")
            f.write(f"**URL:** https://www.youtube.com/watch?v={video_id}\n\n")
            f.write("---\n\n")
            f.write("## Transcript\n\n")
            f.write(full_text)

        print(f"  ✓ Saved: {filename}")

    except Exception as e:
        print(f"  ✗ Error for {expert}: {e}")

print("\nDone.")
