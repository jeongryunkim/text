with open("C:/Users/KDA/OneDrive/Python/Scripts/260910/Lotto & Updown.txt", "r", encoding="utf-8") as file:
	lines = file.readlines()

# print(lines)

for line in lines:
	print(line.strip())