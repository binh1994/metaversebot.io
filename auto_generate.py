#!/usr/bin/env python3
import os, datetime, random, json, requests
DOMAINS = ["bottradingai.com", "botgame.io", "metaversebot.io", "nftgameai.com", "hubgaming.io", "botdefi.io", "esportsai.io", "nftgamepro.com", "botesports.com", "aiesports.io", "pronftgame.com", "botplay.io", "botweb3ai.com", "botblockchain.io"]
TOPICS = [
  "New AI Avatar Interaction Patterns in 2025",
  "Designing Responsible Agents for Virtual Worlds",
  "Optimizing NPC Pipeline with Edge AI",
  "Tokenized Economies: AI & Virtual Commerce",
  "Real-time Personalization with Agents"
]
IMAGES = [
  "https://images.pexels.com/photos/8132695/pexels-photo-8132695.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop",
  "https://images.pexels.com/photos/12483956/pexels-photo-12483956.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop",
  "https://images.pexels.com/photos/844124/pexels-photo-844124.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop"
]
def pick_backlinks():
    others = DOMAINS[:]
    random.shuffle(others)
    return others[:3]
def slugify(t): return t.lower().replace(' ','-').replace('/','-')
def create_post():
    title = random.choice(TOPICS)
    date = datetime.date.today().isoformat()
    slug = slugify(title)
    fname = "_posts/{}-{}.md".format(date, slug)
    image = random.choice(IMAGES)
    backlinks = pick_backlinks()
    content = "---\nlayout: post\ntitle: \"{}\"\ndate: {}\nauthor: \"Alex Reed – AI Metaverse Analyst\"\ndescription: \"{} — quick insights\"\nimage: \"{}\"\n---\n\n_In today’s fast-moving AI-driven metaverse, creators and users adapt quickly._\n\n{% include ad.html %}\n\n### Highlights\n- Bullet 1\n- Bullet 2\n\n---\n\n## Friendly Network Links\n".format(title, date, title, image)
    for b in backlinks:
        content += "- https://{}\n".format(b)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Wrote', fname)
    sitemap = 'https://metaversebot.io/sitemap.xml'
    try:
        requests.get('https://www.google.com/ping', params={'sitemap': sitemap}, timeout=10)
        print('Pinged Google sitemap:', sitemap)
    except Exception as e:
        print('Ping failed', e)
if __name__ == '__main__':
    create_post()
