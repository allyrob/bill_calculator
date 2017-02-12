# i work! add me to GitHub

def calculate_tip(bill_amount, tip_percentage):
    return bill_amount * tip_percentage * .01

def calculate_total(tip, bill_amount):
    return tip + bill_amount

def calculate_split(total, people):
    return total / people

def main():
    print "Please choose from the following:"
    print "1 - calculate tip"
    print "2 - split the bill"
    print "3 - dine and dash"
    choice = int(raw_input())

    if choice == 1:
        bill_amount = float(raw_input("How much was your bill?"))
        tip_percentage = float(raw_input("What '%' would you like to tip? in decimals:"))
        tip = calculate_tip(bill_amount, tip_percentage)
        total = calculate_total(tip, bill_amount)
        print "The tip should be $ %f" %(tip) 
        print "The grand total is $ %f" %(total)  
        split_bill = raw_input("Would you like to split the bill: Y/N?")
        if (split_bill.upper() == "Y"):
            people = int(raw_input("How many people in your party?"))
            split_amount = calculate_split(total, people)               
            print "Each person owes $ %f." %(split_amount)
        elif (split_bill.upper() == "N"):
            print "Wow, that is so generous of you"
    elif choice == 2:
        bill_amount = float(raw_input("How much was your bill?"))
        tip = float(raw_input("How much did you tip?"))
        people = float(raw_input("How many ways will you split the bill?"))
        total = calculate_total(bill_amount, tip)
        split_amount = calculate_split(total, people)
        print "Your total bill is $%f" %(total)
        print "Each guest owes $%f" %(split_amount)
    elif choice == 3:
        print "What a jerk!"


if __name__ == '__main__':
    print __name__
    main()


#global scope practice
TIP_PERCENTAGE = 18

def calculate_bill(original_bill_amount, split_number = 1):
    total_tip = original_bill_amount *  TIP_PERCENTAGE * .01
    total_bill = total_tip + original_bill_amount
    return calculate_bill(total_bill, split_number)
















