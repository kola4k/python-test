import re

f = open("text.txt", "r")
text = f.read()

text = re.sub(r'\W', ' ', text)
worlds = text \
    .replace(",", " ").replace(".", " ").replace(":", " ") \
    .replace("!", "").replace("?", "") \
    .replace("(", " ").replace(")", " ") \
    .replace("[", " ").replace("]", " ") \
    .split(" ")

avg_len = 0
for w in worlds:
    avg_len += len(w)
avg_len /= len(worlds)
avg_len_half = avg_len / 2

worlds = sorted(list(map(lambda s: s.strip().lower(), worlds)), key=lambda s: -len(s))
counts = {}
scores = {}

for world in worlds:
    counts[world] = counts.get(world, 0) + 1

for w, c in counts.items():
    score = scores.get(w, 0)
    if len(w) > avg_len + avg_len_half:
        score += 1
    if len(w) > avg_len:
        score += 1
    if len(w) > avg_len - avg_len_half:
        score += 1
    if len(w) > avg_len + avg_len_half * 2 and c > 3:
        score += 4
    if len(w) > avg_len and c > 5:
        score += 4
    if len(w) > avg_len + avg_len_half and c == 1:
        score += 2
    if c <= 1:
        score += 1

    scores[w] = score

i = 0
for w, score in sorted(scores.items(), key=lambda t: -t[1]):
    # if i < 10:
    print("[score:" + str(score) + "]", w)
    i += 1
