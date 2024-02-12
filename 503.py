def cust_data():
    name=input("Enter name=")
    age=input("Enter age=")
    f=open("customer.txt","a")
    f.write(name+"-"+age+"\n")
    f.close()
cust_data()
cust_data()
cust_data()
