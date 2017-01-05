# this shows how to calculate the discount of a sale

totalSales = float(input("Enter the price:"))
if totalSales >100.0:
    discount = totalSales *0.05
    totalSales = totalSales - discount
    round(discount,3)
    print("You received a discount of", discount)
    
