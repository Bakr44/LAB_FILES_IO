"""# LAB_FILES_IO

## Using what you learned about Python File I/O , we want to make a progeram called To-Do List , this program should do the following:
- Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
- If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
- If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no. 
- If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
- Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"
"""
while True:
    input_from_user= input("do you want to add a new To-Do item? answer by \"y\" for yes and \"n\" for no: ")
    if input_from_user.lower()=="y":
        new_item=input("write in your To-Do list: ")
        file = open("to_do.txt", "a", encoding="utf-8")
        file.write("\n"+new_item)
        file.close()
    elif input_from_user.lower()=="n":
        input_from_user=input("do you want to list your To-Do items ? answer \"y\" for yes and \"n\" for no: ")
        if input_from_user.lower()=="y":
            file=open("to_do.txt","r",encoding="utf-8")
            content=file.read()
            print(content)
            file.close()
        elif input_from_user.lower() == "exit":
            print("thank you for using the To-Do program, come back again soon")
            break 
    elif input_from_user.lower() =="exit":
        print("thank you for using the To-Do program, come back again soon")
        break



    