measurements = [18, 21, 24, 19]
review_threshold_text = "20"

review_threshold = int(review_threshold_text)
total = 0
review_count = 0

for measurement in measurements:
    total += measurement
    if measurement >= review_threshold:
        review_count+= 1
        print(f"Measurement: {measurement} review")
    else:
        print(f"Measurement: {measurement} within range")

count_value = len(measurements)
mean_value = total/count_value

# Replace this scaffold output with your calculation, loop, decision, and summary.
print("Count:", len(measurements))
print("Total:", total)
print("Mean:", mean_value)
print("Review count:", review_count)
