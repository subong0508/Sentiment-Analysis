import re
import pandas as pd

def preprocess(file):
    reviews = []
    scores = []

    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith("영화제목") or line.strip("\n") == '':
                continue
            else:
                score = line[:6].lstrip("평점: ").rstrip()
                scores.append(1 if int(score) > 7 else 0)
                idx = line.find("리뷰")
                review = line[idx:].strip("리뷰:").strip("\n").strip("\t")
                cleaned_review = re.sub(r'[^\w\d\s]','', review)
                reviews.append(cleaned_review)

    return reviews, scores

review1, score1 = preprocess("final_movie1.txt")
review2, score2 = preprocess("final_movie2.txt")
review3, score3 = preprocess("final_movie3.txt")
review4, score4 = preprocess("final_movie4.txt")
review5, score5 = preprocess("final_movie5.txt")

total_review = []
total_scores = []

reviews = (review1, review2, review3, review4, review5)
scores = (score1, score2, score3, score4, score5)

for review, score in zip(reviews, scores):
    total_review.extend(review)
    total_scores.extend(score)


df = pd.DataFrame({'review': total_review, 'sentiment': total_scores})
df.to_csv("movie.csv", index=False)
print("Done.")
