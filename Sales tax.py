SALES_TAX = 0.07
item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))
item4 = float(input("Enter price of item 4: "))
item5 = float(input("Enter price of item 5: "))
total = ((item1 + item2 + item3 + item4 + item5)* SALES_TAX)+item1 + item2 + item3 + item4 + item5
print(total)
