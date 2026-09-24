expenses = []
total = 0

while True:
    print("\n========================================================")
    print("Expense Tracker")
    print("========================================================\n")
    print("1.\tAdd Expense")
    print("2.\tView all Expenses")
    print("3.\tShow total spent")
    print("4.\tExit\n")
    print("--------------------------------------------------------")
    print("Made by: Ganzon, John Kervin M. Ganzon | installment 1")
    print("========================================================")

    choice = input("input your action: ")

    if choice == "1":
        item = input("\nWhat did you buy? : ")
        amount = int(input("How much did it cost? : "))

        expense = {
            "item": item,
            "amount": amount,
        }

        expenses.append(expense)
        print("\nExpense is Added!")

    elif choice == "2":
        print("\nYour expenses: ")

        for expense in expenses:
            print(
                expense["item"], " - ", expense["amount"]
            )

    elif choice == "3":
        for expense in expenses:
            total += expense["amount"]
        print("\nNumber of items: ", len(expenses))
        print("Your total expense: ", total)

    elif choice == "4":
        print("\nGoodbye!")
        expenses.clear()
        break

    else:
        print("\nInvalid option")