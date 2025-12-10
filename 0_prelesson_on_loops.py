# # # # Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
# # # # While loops  

# # # for x in reverse(range(1, 11)):
# # #     print(x)

# # # Print("happy new years")

# # name = input("enter your name: ")

# # while name == "":
# #     print("YOU DID NOT ENTER YOUR NAME")
# #     name = input ("Enter your name: ")
# # print(f"Hello {name}")

# # age = int(input("Enter your age: ")
        
# # while age < 0:
# #     print


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
    