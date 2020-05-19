# Tokenize and print all words in german_text
import re
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize,regexp_tokenize
german_text=("Wann gehen wir Pizza essen? 🍕 Und fährst du mit Über? 🚕")
all_words = word_tokenize(german_text)
print(all_words)

# Tokenize and print only capital words
capital_words = r"[A-ZÜ]\w+"
print(regexp_tokenize(german_text,capital_words ))

# Tokenize and print only emoji
emoji = "['\U0001F300-\U0001F5FF'|'\U0001F600-\U0001F64F'|'\U0001F680-\U0001F6FF'|'\u2600-\u26FF\u2700-\u27BF']"
print(regexp_tokenize(german_text,emoji))
all_words = word_tokenize(german_text)
print(all_words)

