phone = input("Phone number: ")
numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
final = ""
for num in phone:
    final += numbers.get(num, "!") + " "
print(final)