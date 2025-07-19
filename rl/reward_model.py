def calculate_reward(text):
    word_count = len(text.split())
    unique_words = len(set(text.split()))
    return (unique_words / word_count) * 100 if word_count > 0 else 0

