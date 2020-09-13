#To Do List

#LIST
list_of_tasks = [{"Finish To Do List": "High"}]


#FUNCTIONS:

#function to add task
def add_tasks():
    task = {}
    title = input("Enter the task that you would like to add: ").title()
    print()
    print("What is the priority of this task:")
    print("\t1: High")
    print("\t2: Medium")
    print("\t3: Low")
    while True:
        priority_level = input("Choose a priority level - 1, 2, or 3: ")
        print()
        if priority_level == "1":
            priority = "High"
            break
        elif priority_level == "2":
            priority = "Medium"
            break
        elif priority_level == "3":
            priority = "Low"
            break
        else:
            print("That option is not valid.")
            
    task[title] = priority #create dictionary
    list_of_tasks.append(task) # add to list of tasks
    
    print("Success! Your task has been added to your to do list.")

#function for deleting a task
def delete_tasks():
    print()
    print(">>>To Do List<<<")
    print()
    #check for empty to do list
    if len(list_of_tasks) == 0:
        print("There are no items in your To Do List.")
    else:  #print to do list
        print()
        for i, task in enumerate(list_of_tasks):
            for key, value in task.items():
                print(f"\t{i} - {key}")
        #select item to delete
        while True:
            print()
            delete_this = input("Enter the number of the task that you would like to delete: ")
            print()
            if delete_this.isdigit():
                i = int(delete_this)
                if i in range(0,len(list_of_tasks)):
                    del list_of_tasks[i]
                    if len(list_of_tasks) > 0: 
                        print("Success! Your task has been deleted.")
                        break
                    else:
                        print("Your task has been deleted. \n\nCongratulations! Your To Do List is complete!")
                        break
                else:
                    print("That is not a valid option.")
            else:
                print("That is not a valid option.")
   

#function to view list
def view_tasks():
    print()
    print(">>>To Do List<<<")
    if len(list_of_tasks) == 0:
        print()
        print("There are no items in your To Do List.")
    #print to do list  
    for i, task in enumerate(list_of_tasks):
        for key, value in task.items():
            print(f"{i+1} - {key} - {value}")
    print()


#MAIN FUNCTION - Use the To Do List
print()
print("Welcome to your To Do List")
print("Let's Get to Work!")
print()

while True:
    print()
    print("What would you like to do:")
    print()
    print("\t1: Add a task to your list")
    print("\t2: Delete a task from your list")
    print("\t3: View your list")
    print()
    print("\tpress 'q' to exit")
    print()

    answer = input("Enter your selection: ")

    if answer == "1":
        add_tasks()
    
    elif answer == "2":
        delete_tasks()
        
    elif answer == "3":
        view_tasks()

    elif answer == "q" or answer == "Q":
        break

    else:
        print()
        print("That is not a valid option")
        print()
    
print("Goodbye!")



