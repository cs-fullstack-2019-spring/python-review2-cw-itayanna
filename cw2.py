# Create a task list. A user is presented with the text below. Let them select an option to list all of their tasks, add a task to their list, delete a task, or quit the program. Make each option a different function in your program. Do <strong>NOT</strong> use Google. Do <strong>NOT</strong> use other students. Try to do this on your own.


toDoList= ["laundry", "dishes", "homework"]

def option1():
    for x in toDoList:
        print(x)

def option2():
    addedTask= input("What would you like to add? ")
    toDoList.append(addedTask)


def option3():
    deleteTask= input("What would you like to delete? ")
    if deleteTask in toDoList:
        toDoList.remove(deleteTask)
    else:
        print("That item is not available in your list")





userInput=''


while userInput != "0":
    userInput= input("What would you like to do next?\n1. List all tasks\n2. Add a task to the list\n3. Delete a task from the list\n0. To quit the program")
    if userInput == "1":
        option1()
    elif userInput == "2":
        option2()
    elif userInput == "3":
        option3()
    elif userInput == "0":
        break
    else:
        userInput= input("Please select one of the followung:\n1. List all tasks\n2. Add a task to the list\n3. Delete a task from the list\n0. To quit the program")


