import re
from collections import Counter

def analyze_keyword_density(text):
    words = re.findall(r'\b\w+\b', text.lower())
    total_words = len(words)
    word_count = Counter(words)
    keyword_density = {}
    for word, count in word_count.items():
        keyword_density[word] = (count / float(total_words)) * 100
    return keyword_density
