# Expence Calculater
print("="*50)
print("Welcome sir in Expence calculater")
print("="*50)

expences = []

while True:

# user select his choise

    choise = int(input("Select your choise\n1. Add Expence\n2. View all Expence\n3. View Total Expence\n4. Exit\nEnter Your choise : "))

# user selects 1. Add expence

    if (choise == 1):
        date = input("\nEnter your expence date : ")
        cata = input("Enter your spended catagory : ")
        des = input("Enter some more details about spending : ")
        amount = float(input("Enter your spend amount : "))

        expence = { "Date" : date,
                   "Catagory" : cata,
                   "Description" : des,
                   "Amount" : amount
                   }
# here add all the details in expences list by using append methord
        expences.append(expence)
        print("\nYour Data is sucessfully listed\n")
#user select 2. View all expence

    elif (choise == 2) :
        if (len(expences) == 0):
            print("\n\tNothing purchased today\n")
        else :
            print("Your expence is\n")
            count = 1
            for i in expences :
                print(f"Spending list {count}\n\tSpensing Date : {i["Date"]}\n\tSpended Catagory : {i["Catagory"]}\n\tSpended Description : {i["Description"]}\n\tSpended amount : {i["Amount"]} ")
                count += 1
            print("\nHere is your all expences details")

# user select 3. means total spended money

    elif (choise == 3) :
        if len(expences) == 0 :
            print("\n\tYou did not spend money yet\n")
        else :
            print("Here is your all spended money\n")
            count = 1
            amount = 0
            for i in expences :
                print(f"Here is your {count} Amount : {i["Amount"]}")
                amount = amount + i["Amount"]
                count += 1
            print(amount)

# user want to exit this program

    elif (choise == 4) :
        break

# if user choose 5 or abcd so this code run

    else :
        print("\n\tInvalid input, choose only [1,2,3,4] only\n")