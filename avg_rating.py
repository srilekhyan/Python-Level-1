user_input = input("Enter all ratings separated by spaces: ")

ratings = list(map(float, user_input.split()))

if ratings:
    average = sum(ratings) / len(ratings)
    print("ratings:", ratings)
    print("average rating:", average)
else:
    print("No ratings were entered.")
