print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("\nWhat is your age? "))

    if 45 <= age <= 55:
        print("Fine! You can have a free ride.")
    elif age > 18:
        bill = 20
        print(f"Adult tickets ₹{bill}.")
    elif age >= 12:
        bill = 12
        print(f"Youth tickets ₹{bill}.")
    else:
        bill = 7
        print(f"Child tickets are ₹{bill}.")

    wants_photo = input("Do you want to have a photo? (y/n): ")
    if wants_photo.lower() == "y":
        bill += 20

    print(f"Please pay ₹{bill}.")
else:
    print("\nSorry, you have to grow taller before you can ride.")
