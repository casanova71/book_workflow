from scraping.scraper import scrape_chapter
from agents.writer_agent import spin_chapter
from agents.reviewer_agent import review_text
from rl.reward_model import calculate_reward
from my_chromadb.chroma_ops import store_version

url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

text, _ = scrape_chapter(url)

spun = spin_chapter(text)

reviewed = review_text(spun)

reward = calculate_reward(reviewed)
print(f"RL Reward Score: {reward:.2f}")

store_version(reviewed, {"source": url, "reward": reward, "id": "chapter_1_v1"})

print("✅ Pipeline complete. Reviewed text stored.")
