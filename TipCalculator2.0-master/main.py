# ---Tip Calculator---
# Welcome greeting
print("Welcome to the Tip Calculator")
#request user input for total bill
total_bill=float(input("What was the total bill? $"))
#request user input for tip percentage as integer
tip=int(input("What percentage tip would you like to give(e.g.:10, 12, or 15)? %"))
#request user input on how many people split bill as integer
total_ppl=int(input("How many people will split the bill? "))
#convert numbers to proper type and store as variable
tip_pct=tip/100
#calculate totals and round if needed
total_tip=round(total_bill*tip_pct,2)
tip_per_person=round(total_tip/total_ppl,2)
total_payment=total_bill+total_tip
payment_per_person=round(total_payment/total_ppl,2)
#format all totals to output 2 decimal points even if ending with a zero
total_payment="{:.2f}".format(total_payment)
total_tip="{:.2f}".format(total_tip)
tip_per_person="{:.2f}".format(tip_per_person)
payment_per_person="{:.2f}".format(payment_per_person)
#output total payment for each individual as f-string
print(f"your total payment is: ${total_payment}\nEach person should pay: ${payment_per_person}\n\
Total Tip: ${total_tip}\nTip per person: ${tip_per_person}")


