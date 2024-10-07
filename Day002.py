print("welcome to the tip calculater! $")

total_bill = float(input("Whant was the total bill?"))
total_tip = int(input("who much tip you want to give?"))
split = float(input("who many people to split the bill?"))

math = round(total_tip / 100 * total_bill + total_bill, 2)
res = math/split

print(f"${res}")

