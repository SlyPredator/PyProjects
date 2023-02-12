weight = input("Enter your weight. ")
if int(weight) > 1000:
    kgw = int(weight) / 1000
else:
    kgw = weight
letter = input("Should I display it in (K)gs or (G)rams? ")
if letter == "K" or letter == "k":
    print("Your weight in kgs is:", kgw)
else:
    new = int(kgw) * 1000
    print("Your weight in grams is:", new)
