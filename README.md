# AI-Powered SEO Content Production — Research Project

**Topic:** AI-Powered SEO Content Production for B2B SaaS  
**Phase:** Portfolio Task — 100Hires Junior Growth Marketing Specialist  
**Researcher:** Erick Villarce  
**Completed:** June 2026

---

## Why This Topic

100Hires is an ATS built for startups and small businesses. The most direct growth lever for a company like this is organic visibility — appearing when founders and hiring managers search for "best ATS for startups" or "hiring software for small teams." AI-powered SEO content production is exactly the discipline that makes that happen at scale, and it's changing fast enough that having a current, practitioner-sourced playbook matters.

---

## What I Collected

### Experts Researched — 15 Total

I identified 15 practitioners (not theorists) who actively publish, experiment, and share real data on AI-powered SEO and content production for B2B SaaS. The full list with profiles, roles, and selection reasoning is in [`/research/sources.md`](research/sources.md).

Selection criteria:
- Active content creators (YouTube, LinkedIn, newsletters) — not just authors of one article
- Practitioners with real client data or case studies, not just opinions
- Mix of technical SEO, content strategy, and GEO (Generative Engine Optimization) perspectives
- Avoided the obvious "famous" names (Neil Patel, Brian Dean) that industry sources themselves have flagged as no longer active practitioners

### YouTube Transcripts — 10 Videos

Collected via the `youtube-transcript-api` Python library (no API key required). Transcripts are organized by expert in [`/research/youtube-transcripts/`](research/youtube-transcripts/).

| Expert | Video | Topic |
|--------|-------|-------|
| Mike King | [Decoding the Future of SEO Measurement](https://youtube.com/watch?v=vhZS8trALwQ) | AI disruption of SEO metrics |
| Koray Tuğberk Gübür | [Technical & Semantic SEO](https://youtube.com/watch?v=5PAoIhyalsg) | Semantic SEO and entity optimization |
| Nathan Gotch | [AI Changed SEO Forever](https://youtube.com/watch?v=7mtCa8sqjBo) | How to win in AI search era |
| Alex Birkett | [SEO Strategies for the New Search World](https://youtube.com/watch?v=L_WeZSgFe5I) | B2B SaaS organic growth |
| Aleyda Solis | [SEO Reloaded](https://youtube.com/watch?v=qHXh09fnRcE) | Adapting SEO rules for AI world |
| Lily Ray | [What IS and ISN'T Working in SEO](https://youtube.com/watch?v=J7ayY_Mdk4w) | Current SEO landscape |
| Koray Tuğberk Gübür | [AI Agents & Semantic SEO](https://youtube.com/watch?v=mSHq_HxOyTA) | Fortune 500 SEO secrets |
| Nathan Gotch | [Building AI SEO SaaS](https://youtube.com/watch?v=Y88G1JbGsEE) | AI SEO product development |
| Aleyda Solis | [How to Prepare for AI Search](https://youtube.com/watch?v=NNl9sRCv3q8) | AI search roadmap |
| Alex Birkett | [SEO Strategy 2026](https://youtube.com/watch?v=nQv2o2X7DDU) | The shift most B2B SaaS are missing |

### LinkedIn Posts — 3 Experts, 7 Posts

Collected manually (LinkedIn API requires enterprise-level approval — documented as a limitation). Posts are in [`/research/linkedin-posts/`](research/linkedin-posts/).

- **Kevin Indig** — 3 posts: AI prompt tracking framework for B2B SaaS, SEO vs AEO comparison, AI Mode vs AI Overviews user behavior study (846k sessions)
- **Ben Goodey** — 1 live case study (3 parts): translating 14 blog posts → 5.33x AI visibility increase in 60 days for a B2B SaaS client
- **Lily Ray** — 3 posts: why "best [category]" listicles hurt more than help in AI Overviews, the AI Slop Loop experiment (fake update adopted by LLMs in under 24h), Google's review system and listicle risk

---

## Key Insights from the Research

After reviewing transcripts and posts across all 15 experts, three themes came up consistently:

**1. Traditional SEO and AI visibility are correlated but not identical**
Kevin Indig's data and Ben Goodey's case study both show that Google rankings and clicks still influence AI citation rates — but the relationship varies by platform. Perplexity and ChatGPT behave differently, and optimizing for one doesn't guarantee the other.

**2. Self-promotional content is losing its AI search effectiveness**
Lily Ray's data (100 B2B queries) shows brands are excluded from actual recommendations 69% of the time when their own listicle is cited as a source. Google has decoupled citation from recommendation. Real authority — what the rest of the web says about you — matters more than what you say about yourself.

**3. The shift is from page-level SEO to entity and brand authority**
Mike King (Relevance Engineering), Koray Tuğberk Gübür (semantic SEO), and Aleyda Solis all point to the same direction: AI systems evaluate brands and entities holistically, not just individual pages. Content production needs to build topical authority across a cluster, not just rank individual articles.

---

## Repository Structure

```
100hires-setup-task/

├── README.md                          # This file
└── research/
├── sources.md                     # 15 experts with profiles and selection reasoning
├── fetch_transcripts.py           # Script used to collect YouTube transcripts via API
├── linkedin-posts/
│   ├── kevin-indig.md             # 3 posts
│   ├── ben-goodey.md              # Live AEO case study (3 parts)
│   └── lily-ray.md                # 3 posts
└── youtube-transcripts/
├── mike-king_vhZS8trALwQ.md
├── koray-tugberk-gubur_5PAoIhyalsg.md
├── nathan-gotch_7mtCa8sqjBo.md
├── alex-birkett_L_WeZSgFe5I.md
├── aleyda-solis_qHXh09fnRcE.md
├── lily-ray_J7ayY_Mdk4w.md
├── koray-tugberk-gubur_mSHq_HxOyTA.md
├── nathan-gotch_Y88G1JbGsEE.md
├── aleyda-solis_NNl9sRCv3q8.md
└── alex-birkett_nQv2o2X7DDU.md
```

---

## Data Collection Methods

- **YouTube transcripts:** Python script using `youtube-transcript-api` library — no API key required, fetches auto-generated or manual captions directly from YouTube
- **LinkedIn posts:** Manual collection — LinkedIn's API requires enterprise approval and is not available for individual use. Posts were selected based on recency (last 3-6 months) and relevance to AI-powered SEO content production for B2B SaaS
- **Expert selection:** Cross-referenced against multiple industry sources (Search Engine Land, Clutch rankings, community recommendations) to prioritize practitioners over theorists