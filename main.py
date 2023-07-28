import re

contact = { }
def home_page():
    print(" 1. Add a contact \n 2. View Contact List \n 3.Search Contact\n 4.Delete contact  \n 5. Edit contact\n 6.Exit\n")
def display_contact():

    print("ID\t\tName\t\tContact Number\t\temail")
    print("--------------------------------------------------\n")
    for key in contact:
        vals = list(contact.get(key))
        vals = str(vals)
        vals = vals.strip("[")
        vals = vals.strip("'")
        vals = vals.strip("'")
        vals = vals.strip("]")
        vals = vals.strip("'")
        vals = vals.strip("'")
        vals = re.sub(",","",vals)
        vals = vals.strip("'")
        vals = vals.strip("'")
        print("{}\t\t{}".format(key,vals))

print("Contact Book \n------------")
home_page()
while (True):

    choice = int(input( "\nEnter your choice (1-6): "))

    if choice == 1:
        print("\nEnter contact details:\n")
        id = input("ID:")
        if id in contact:
            print("**************************this Id already used please try another Id**************************")
            continue
            home_page()
        name = input("Name:")
        phone = input("phone Number:")
        email = input("Email:")
        print("Contact added successfully!")
        contact[id] = name,phone,email


    elif choice == 2:
        if not contact:
            print("empty contact book")
        else:
            print("Contact List:\n--------------\n")
            display_contact()

    elif choice == 3:
        print("Search Contact:")
        search_id = input("Enter the ID to search: ")
        if search_id in contact:
            print("Search Result:\n--------------")

            print("ID\t\tName\t\tContact Number\t\temail")
            print("--------------------------------------------------\n")

            print(search_id,"\t",contact[search_id])
        else:
            print("ID is not found in contact book")

    elif choice == 4:
        del_contact = input("Enter the contact ID to delete :")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n? ")
            if confirm =='y' or confirm =='Y':
                contact.pop(del_contact)
                print("Contact deleted successfully!")

        else:
            print("ID is not found in contact book")

    elif choice == 5:
        edit_contact = input("Enter the contact ID to be edited ")
        if edit_contact in contact:
            phone = input("enter mobile number")
            contact[edit_contact]=phone
            print("contact updated")
            display_contact()
        else:
            print("ID is not found in contact book")
    elif choice == 6:
          print("Exiting...")
    else:
        break

