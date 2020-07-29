class product:
    def __init__(self,productId,ProductName,price,availableQuantity):
        self.productId=productId
        self.ProductName=ProductName
        self.price=float(price)
        self.availableQuantity=int(availableQuantity)
    def getProductId(self):
        return self.productId
    def getProductName(self):
        return self.ProductName
    def getPrice(self):
        return self.price
    def getAvailableQuantity(self):
        return self.availableQuantity
    def setProductId(self,pId):
        self.productId=pId
    def setProductName(self,name):
        self.ProductName=name
    def setPrice(self,price):
        self.price=float(price)
    def setAvilableQuantity(self,aq):
        self.availableQuantity=int(aq)
    def ShowDetails(self):
        print("Product Id: %s\nProduct Name: %s\nProduct Price: %d\nAvailable Quantity: %d\n" %(self.productId,self.ProductName,self.price,self.availableQuantity))

p1=product("1","pen",10.0,500)
p2=product("2","Marker",20.0,100)
p3=product("3","Duster",30.0,50)
p4=product("4","Pencil",15.0,200)

pList=[p1,p2,p3,p4]
for p in pList:
    p.ShowDetails()