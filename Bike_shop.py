class Bike_Rentalshop:
    compName="Welcome to Patel and sons Bike Rental Company !!!"
    dayrent="we provide bikes for rent, per Day bike rent charge is 500 Rupees"
    
    def __init__(self,stock):
        self.stock = stock
        
    def displaystock(self):
        print(f"Total stock Bikes: {self.stock}")
        
    def bikeforrent(self,q):
         if q<=0:
             print("pls Enter number greater than zero")
             
         elif q>self.stock:
             print("Enter the Qunatity in limit in stocks")
             print(f"We have only {self.stock} bikes Available")
         else:
            self.stock = self.stock-q
            print(f"You rented {q} bikes and total payable price is:",q*500)
            print("Available Bikes in stokes:",self.stock)
            
            
while True:
    
    o1=Bike_Rentalshop(500)
    print(o1.compName)
    print(o1.dayrent)
    
    # uc means UsER CHOICE
    uc=int(input('''                
                 choose the option among of them
                 1.Display stocks
                 2.Rent Bikes
                 3.Exit\n'''
                 ))
    
    if uc==1:
        o1.displaystock()
    if uc==2:
        o1.bikeforrent(int(input("Enter the Quantity of bikes:")))
        
    else:
        break
        
    
        
        
        