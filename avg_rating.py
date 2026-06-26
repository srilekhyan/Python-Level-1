ratings = []

num = int(input("How many ratings? "))

for i in range(num):
    rating = float(input("Enter rating: "))
    ratings.append(rating)

average = sum(ratings) / len(ratings)

print("ratings:", ratings)
print("average rating:", average)