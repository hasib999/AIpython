cost=24.95
discount=.4
dis=round(24.95*.4,2)
costDis=round(cost-dis,2)
numBook=60
price=costDis*60
print("Total cost not inc delivery->",price)
delPrice=3+59*.75+price
print("Total cost with Delivery->",delPrice)

