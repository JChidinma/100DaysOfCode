# Create a max function
scores = [123, 452, 234, 142, 861, 1450]

max_score = 0
for score in scores:
    if score > max_score:
        max_score = score

print(max_score)
