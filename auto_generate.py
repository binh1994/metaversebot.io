#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auto-generate daily SEO article for metaversebot.io
✅ Fixed KeyError (% include ad.html %)
✅ Neon Metaverse theme
✅ Includes backlinks, SEO description, ping Google
"""

import os
import datetime
import random
import requests

DOMAINS = [
    "botgame.io", "metaversebot.io", "nftgameai.com", "hubgaming.io", "botdefi.io",
    "esportsai.io", "nftgamepro.com", "botesports.com", "aiesports.io", "pronftgame.com",
    "botplay.io", "botweb3ai.com", "botblockchain.io", "bottradingai.com"
]

TOPICS = [
    "Metaverse economy trends 2025",
    "AI + Web3 transforming virtual worlds",
    "Digital identity and ownership in Metaverse",
    "How NFT avatars redefine creativity",
    "AI-driven game design and immersive worlds",
    "Virtual finance and decentralized social spaces",
    "Top Metaverse startups shaping 2025"
]

IMAGE_SOURCES = [
    "https://images.pexels.com/photos/8132695/pexels-photo-8132695.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop",
    "https://source.unsplash.com/1200x630/?metaverse,ai",
    "https://picsum.photos/1200/630?random={}"
]

def pick_image():
    img = random.choice(IMAGE_SOURCES)
    if "picsum" in img:
        img = img.format(random.randint(1, 999999))
    return img

def make_backlinks():
    random.shuffle(DOMAINS)
    selected = DOMAINS[:5]
    return "\n".join([f"- [{d}](https://{d})" for d in selected])

def create_post():
    today = datetime.date.today()
    date_str = today.isoformat()
    topic = random.choice(TOPICS)
    img = pick_image()
    desc = f"{topic} — insights for the AI-powered Metaverse world."
    backlinks = make_backlinks()

    # escaped Jekyll syntax safely
    content = """---
layout: post
title: "{title}"
date: {date}
author: "Alex Reed – AI Metaverse Analyst"
description: "{desc}"
image: "{image}"
---

In today’s fast-moving AI-driven Metaverse, creators, investors, and players are shaping the future of digital life.

{{% include ad.html %}}

### Key Insights
- Innovation through AI, VR, and blockchain
- Decentralized finance in digital realms
- Virtual economies powering real growth

### Why it matters
The Metaverse is not just entertainment — it’s the next digital frontier for creativity, commerce, and connection.

---

## Related Articles
{{% for p in site.posts limit:4 %}}
{{% if p.url != page.url %}}
- [{{{{ p.title }}}}]({{{{ p.url }}}})
{{% endif %}}
{{% endfor %}}

## Friendly Network Links
{backlinks}

---

### 🛒 Domain for Sale
This premium domain is available for acquisition:  
👉 [Buy metaversebot.io on Afternic](https://afternic.com/domain/metaversebot.io)

""".format(title=topic, date=date_str, desc=desc, image=img, backlinks=backlinks)

    os.makedirs("_posts", exist_ok=True)
    filename = f"_posts/{date_str}-{topic.lower().replace(' ', '-')}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Generated: {filename}")
    return filename


def ping_google():
    try:
        url = "https://www.google.com/ping?sitemap=https://metaversebot.io/sitemap.xml"
        requests.get(url, timeout=10)
        print("📡 Pinged Google successfully.")
    except Exception as e:
        print("⚠️ Ping failed:", e)


def main():
    print("🚀 Auto-generating Metaverse post...")
    create_post()
    ping_google()


if __name__ == "__main__":
    main()
