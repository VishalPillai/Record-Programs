import pickle
def add_order():
    f = open("Orders.dat","ab")
    while True:
        oid = int(input("Enter order id: "))
        name = input("Enter customer name: ")
        date = input("Enter order date: ")
        amount = float(input("Enter total amount: "))
        rec = (oid, name,date,amount)
        pickle.dump(rec,f)
        ch = input("Add another order? (Y/N):")

        if ch.upper()=="N":
            break
    f.close()
def update_order_amount():
    f = open("Orders.dat","rb")
    data = []
    try :
         while True:
             rec = pickle.load(f)
             oid,name.date,amount = rec
             amount  = amount + amount*10/100
             rec = (oid,name,date,amount)
             data.append(rec)
    except EOFError:
        f.close()
    f = open("Orders.dat","wb")
    for rec in data:
        pickle.dump(rec,f)
    f.close()
    print("Order amounts updated succesfully")
add_order()
update_order_amount()



