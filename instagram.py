views = int(input("Enter the number of views : "))
likes = int(input("Enter the number of likes : "))
comments = int(input("Enter the number of comments : "))

rate = (likes + comments) / views * 100

print("Performance Report")
print("Views :", views)
print("Likes :", likes)
print("Comments :", comments)
print("Engagement Rate :", rate)    