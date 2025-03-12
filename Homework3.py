import re
import urllib.request
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

def get_unique_words(url):
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')

    start_index = text.find("*** START OF THIS PROJECT GUTENBERG EBOOK")
    end_index = text.find("*** END OF THIS PROJECT GUTENBERG EBOOK")
    text = text[start_index:end_index]

    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word not in stop_words]

    return set(filtered_words)

book1_url = "https://www.gutenberg.org/files/1342/1342-0.txt"
book2_url = "https://www.gutenberg.org/files/2701/2701-0.txt"

book1_words = get_unique_words(book1_url)
book2_words = get_unique_words(book2_url)

print(f"Unique words in Pride and Prejudice (filtered): {len(book1_words)}")
print(f"Unique words in Moby-Dick (filtered): {len(book2_words)}")

if len(book1_words) > len(book2_words):
    print("Jane Austen used more unique words.")
else:
    print("Herman Melville used more unique words.")
