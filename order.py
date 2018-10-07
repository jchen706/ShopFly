
class Order:

    def __init__(self, aitem,  aquantity, acustomer,  aLoc ,aprice ):
        self.itemNum = aitem
        self.quantity = aquantity
        self.price = aprice
        self.customer = acustomer
        self.location = aLoc



    def __str__(self):
        return self.customer + " orders " + self.quantity + " number of Item Id: " +  self.itemNum + " at " + self.price


    def getPrice(self):
        return self.price

    def getTotalPrice(self):
        return  round(self.quantity * self.price, 2)

    def getCustomer(self):
        return  self.customer

    def getId(self):
        return  self.itemNum

    def getLocation(self):
        return self.location

    def payload(self):
        pay ={}

         #"{\"totalModifiers\":[{\"amount\":"+ #str(self.getTotalPrice())+",\"description\":\""+str(self.constumer)"\",#\"referenceId\":\""+str(self.itemNum)+"\",\"lineId\":\"String\"}],}"
        #pay["customer"] = str(self.customer)
        #pay["pickUpLocation"] = str(self.location)
        #pay["quantity"] = str(self.quantity)
        #pay["itemID"] = str(self.itemNum)
        #pay["unitPrice"] = str(self.price)
        #pay["totalPrice"] = str(self.getTotalPrice())

        return pay
