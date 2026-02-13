import string
from sklearn.feature_extraction.text import TfidfVectorizer


def extract_keywords(text, num_keywords=5):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(
        stop_words='english',
        ngram_range=(1, 2),
        max_features=100
    )

    # Fit and transform text
    tfidf_matrix = vectorizer.fit_transform([text])

    # Get feature names
    feature_names = vectorizer.get_feature_names_out()

    # Get scores
    scores = tfidf_matrix.toarray()[0]

    # Pair words with scores
    word_score_pairs = list(zip(feature_names, scores))

    # Sort by score descending
    sorted_words = sorted(word_score_pairs, key=lambda x: x[1], reverse=True)

    # Extract top keywords
    top_keywords = [word for word, score in sorted_words[:num_keywords]]

    return top_keywords


if __name__ == "__main__":
    print("Enter your text (Press Enter twice to finish):")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    user_text = " ".join(lines)

    keywords = extract_keywords(user_text, 5)

    print("\nExtracted Keywords:")
    for keyword in keywords:
        print("-", keyword)
