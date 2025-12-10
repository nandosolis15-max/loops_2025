# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]

# Challenge:
# Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])
for fruit in fruits:
    print(fruit)
# i just worked with loops

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:
    print(subject)
# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"


# Given:
numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.



subjects = ["Math", "Science", "History", "Art"]
# for subject in subjects: 
#     print(subjects)



for subject in subjects:
    if subjects == "History":
        break
    print(subjects)


for subject in subjects:
    if subject == "Science":
        continue
    print (subject)


# list1000 = list(range(1, 1000))

# # for number in list1000:
# #     if number > 599:
# #         break
# #     print(number)

# for number in list1000:
#     if 300 < number < 599:
#         break
#     print(number)

for index in range(len(subjects)):
    print("Subject " + str(index) + ": " + subjects[index])


numbers =[5, 10, 15, 20]
total = 0
for number in numbers:
    total += number
    print("total: ", total)

new_numbers = list(range(1,261))
total = 0
for number in new_numbers:
    total += number
print("total sum frm 1 to 260 ", total)

colors = ["red", "blue", "green", "yellow", "purple"]

print(len(colors))
index = 0
while index < len(colors):
    if colors[index] == "yellow":
        break
    print(colors[index])
    index += 1
    