db={101:{"name":"bhushan","position":"software developer","salary":40000}}
print("-"*90)
print("Employee Management System".center(85))
print("-"*90)
print("\nDashboard")

def dashboard():

    return """
    1.Add employee details
    2.Display employee details
    3.update employee details
    4.delete employee details
    5.filter employee details
""" 
def add_details(id,name,position,salary):
    #var[key]=value
    db[id]={"name":name,"position":position,"salary":salary}
    return "added successfully"

def display():

    table="|{:^20}|{:^20}|{:^20}|{:^20}|".format("id","name","position","salary")+"\n"+"-"*85
    
    for i in db:
      table=table+"\n|{:^20}|{:^20}|{:^20}|{:^20}|".format(i,db[i]["name"],db[i]["position"],db[i]["salary"])+"\n"+"-"*85
    return "-"*85+'\n'+table
    

def update(id):
    print(""" 
      1.Name
      2.position
      3.Salary
           """)
    ch=eval(input("enter your choice: "))
    if ch==1:
        db[id]["name"]=input("enter your name: ")
        return "updated successfully...."
    elif ch==2:
        db[id]["position"]=input("enter your position: ")
        return "updated successfully...."
    elif ch==3:
        db[id]["salary"]=input("enter your salary: ")
        return "updated successfully...."
    else:
        return "invalid input...."
    
def delete(id):
    if id in db:
       del db[id]
       return "deleted successfully...."
    else:
        return "id not present"
    
while True:
   print(dashboard())
   ch=int(input("enter your choice: "))
   if ch==1:
        id=int(input("enter id: "))
        name=input("enter name: ")
        position=input("enter position: ")
        salary=eval(input("enter salary: "))
        print(add_details(id,name,position,salary))
   elif ch==2:
        print(display())
   elif ch==3:
        id=int(input("enter id: "))
        print(update(id))
   elif ch==4:
        id=int(input("enter id: "))
        print(delete(id))
   elif ch==6:
       break
   else:
       print("invalid")
       