#variables
major_or_auxiliary = ""
direction = ""
#ask for user input
num = int(input("Input Highway Number: "))
#Error Checking
while (num <= 0 or num % 100 == 0 or num >= 1000):
    print("Invalid Highway Number.")
    num = int(input("Input Highway Number: "))
#output highway type and direction
if num % 5 == 0:
    major_or_auxiliary = "a major"
else:
    major_or_auxiliary = "an auxiliary"
if num % 2 == 0:
    direction = "east/west."
else:
    direction = "north/south."
print(f"Highway {num} is {major_or_auxiliary} highway that runs {direction}")