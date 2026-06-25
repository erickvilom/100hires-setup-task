from youtube_transcript_api import YouTubeTranscriptApi
import os

videos = [
    {
        "expert": "mike-king",
        "video_id": "vhZS8trALwQ",
        "title": "Decoding the Future of SEO Measurement with Mike King"
    },
    {
        "expert": "koray-tugberk-gubur",
        "video_id": "5PAoIhyalsg",
        "title": "Technical SEO and Semantic SEO with Koray Tugberk Gubur"
    },
    {
        "expert": "nathan-gotch",
        "video_id": "7mtCa8sqjBo",
        "title": "AI Changed SEO Forever - How to Win in 2025"
    },
    {
        "expert": "alex-birkett",
        "video_id": "L_WeZSgFe5I",
        "title": "SEO Strategies For The New Search World with Alex Birkett"
    },
    {
        "expert": "aleyda-solis",
        "video_id": "qHXh09fnRcE",
        "title": "SEO Reloaded - Adapting Old SEO Rules in the New AI World"
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