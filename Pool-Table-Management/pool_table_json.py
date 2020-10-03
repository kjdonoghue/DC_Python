import datetime
from datetime import timedelta
import json

class PoolTable:
    def __init__(self, name):
        self.name = name
        self.is_occupied = False
        self.start_time = None
        self.start_str = None
        self.end_time = None
        self.end_str = None
        self.total_time = None
        self.total_str = None
        self.customer_name = ""
        self.time_played = None
        self.cost = ""

    def show_tables(self, filter):
        if self.is_occupied == True:
            status = "Occupied"
            current_time = datetime.datetime.now()
            time = current_time - self.start_time
            time_played = round((timedelta.total_seconds(time)/60),2)
        else:
            status  = "Available"
            time_played = ""
        
        if filter == "All":
            print (f"{i + 1}: \tTable {self.name} \t{status} \t{self.customer_name} \t\t{self.start_str} \t\t{time_played}")
        elif table.is_occupied == filter:
            print (f"{i + 1}: \tTable {self.name} \t{status} \t{self.customer_name} \t\t{self.start_str} \t\t{time_played}")

def select_table():
    pt_index = input("Enter Table Number: ")
    try:
        pt_index = int(pt_index)
        if pt_index in range(1, len(pt_list)+1):  
            table_num = pt_list[(pt_index)-1]
            return table_num
        else:
            print("Please enter a number 1-12")
    except ValueError:
        print("You must enter a number 1-12")
    except:
        print("That is not a valid entry")

def print_current_status():
    current_status = []         
    for i in range(0, len(pt_list)):
        table = pt_list[i]
        if table.is_occupied == True:
            status = "Occupied"
        else:
            status = "Available"
        table_status = {"Table Number": table.name, "Status": status, "Customer Name": table.customer_name, "Start Time": table.start_str}
        current_status.append(table_status)
                                                    
    with open("current_status.json", "w") as file_object:
        json.dump(current_status, file_object)
    
    
#LISTS
pt_list = []
all_transactions = []

#RATES
rate_minute = .50

#MAKE POOL TABLES
for index in range(1,13):
    pool_table = PoolTable(index)
    pt_list.append(pool_table)


#MAIN APPLICATION
while True:
    print("""*****Pool Table Management Menu*****
    1: Sign Out Table
    2. Return Table
    3. View Status of All Tables
    4. Quit""")
    
    action = input("What would you like to do: ")
    
    #SIGN OUT POOL TABLE
    if action == "1": 
        print("Available Tables: ")
        print("Index \tTable \t\tStatus \t\tName") #Header
        for i in range(0, len(pt_list)):
            table = pt_list[i]
            table.show_tables(False)
        
        #SELECT TABLE
        table = select_table()

        #CHECK OUT TABLE
        if table != None:
            if table.is_occupied == False:
                table.customer_name = input("Customer's Name: ").title()
                table.start_time = datetime.datetime.now()
                table.start_str = table.start_time.strftime("%H:%M")
                table.is_occupied = True
                
                print(f"Table number {table.name} is checked out to {table.customer_name}")
            else:
                print(f"Table number {table.name} is not available")
        
        #UPDATE CURRENT STATUS LIST
        print_current_status()

    #RETURN POOL TABLE      
    elif action == "2": #return pool table
        print("Occupied Tables: ")
        print("Index \tTable \t\tStatus \t\tName \t\tStart \t\tMinutes Played") #Header
        for i in range(0, len(pt_list)):
            table = pt_list[i]
            table.show_tables(True)
        
    
        #SELECT TABLE
        table = select_table()
        
        if table != None:
            if (table.is_occupied == True):

                #CALCULATE TIME
                table.end_time = datetime.datetime.now()
                table.end_str = table.end_time.strftime("%H:%M")
                table.total_time = table.end_time - table.start_time
                table.total_str = str(table.total_time)
                time_in_sec = timedelta.total_seconds(table.total_time)
                print(f"Total time played for Table {table.name}: {table.total_str}")

                #CALCULATE COST
                table.cost = round(((time_in_sec/60.00) * rate_minute), 2)
                print(f"The cost is : ${table.cost}")          
                                
                #UPDATE TRANSACTION TO ARRAY
                table_transaction = {"Table Number": table.name, "Start Time": table.start_str, "End Time": table.end_str, "Total Time Played": table.total_str, "Cost": table.cost}
                all_transactions.append(table_transaction)

                #NAME THE FILE
                now = datetime.datetime.now()
                today = now.strftime("%Y-%m-%d")
                filename = today + ".json"
                
                #PRINT TRANSACTIONS TO FILE
                with open(filename, "w") as file_object:
                    json.dump(all_transactions, file_object)
                                
                #RESET TABLE STATUS
                table.is_occupied = False    
                table.start_time = ""
                table.end_time = ""
                table.total_time = ""
                table.customer_name = ""
                table.time_played = ""
                table.cost = ""
                print(f"Table {table.name} is returned to inventory")

                #UPDATE CURRENT STATUS LIST
                print_current_status()

            else:
                print(f"Table {table.name} is not currently occupied")
       

    #VIEW ALL STATUS
    elif action == "3":
        print("Table Status:")
        print("Index \tTable \t\tStatus \t\tName \t\tStart \t\tMinutes Played") #Header
        for i in range(0, len(pt_list)):
            table = pt_list[i]
            table.show_tables("All")
     
    #QUIT    
    elif action == "4":
        break
    else:
        print("Not a valid option")










