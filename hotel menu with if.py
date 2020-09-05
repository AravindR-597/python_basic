food = ["idly", "masala dosa", "appam", 'chappathi', "porota"]
print(food)
menu = input("Enter the food from the menu ")

if menu == "idly":
    print("total amount=RS 8")
elif menu == "masala dosa":
    print("total amount=RS 45")
elif menu == "appam":
    print("total amount=Rs 10")
elif menu == "chappathi":
    print("total amount=Rs 15")
elif menu == "porota":
    print("total amount=RS 12")
else:
    print("enterd dish is not in the menu")
    print("please try again")
