scores = []
for i in range(3):
	x = int(input("Input the number"))
	scores.append(x)

# # Print the average
# average = sum(scores) / len(scores)
# print(f"Average: {average}")

# Dict
# people = [
# 	{"name" : "Jokowi", "status" : "President"},
# 	{"name" : "Prabowo", "status" : "Minister of Defense"},
# 	{"name" : "Ceb", "status" : "Just s normal person"}
# ]

# # Search for a name
# name = input("Name: ")
# for person in people:
# 	if person['name'] == name:
# 		print(f"Found {person['name']} : {person['status']}")
# 		break
# else:
# 	print("Not found")


# people = {
# "Jokowi" : "President",
# "Prabowo" : "Minister of Defense",
# "Ceb" : "Just a normal person"
# }

# # We can iterate by the object dictionary rather than object list of dictionary
# name = input("Name: ")
# if name in people:
# 	print(f"Found {name} : {people[name]}")
# else:
# 	print("Not found")