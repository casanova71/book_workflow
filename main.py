from scraping.scraper import scrape_chapter
from agents.writer_agent import spin_chapter
from agents.reviewer_agent import review_text
from rl.reward_model import calculate_reward
from my_chromadb.chroma_ops import store_version

# URL to scrape
url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"

# Step 1: Scrape the content
text, _ = scrape_chapter(url)

# Step 2: Spin the content using the AI writer
spun = spin_chapter(text)

# Step 3: Review the spun content
reviewed = review_text(spun)

# Step 4: Score using RL reward model
reward = calculate_reward(reviewed)
print(f"RL Reward Score: {reward:.2f}")

# Step 5: Save to ChromaDB
store_version(reviewed, {"source": url, "reward": reward, "id": "chapter_1_v1"})

print("✅ Pipeline complete. Reviewed text stored.")
