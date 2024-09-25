#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#contact book
contact={}
def display_contact():
    print("Name\t\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
        print("{}\t\t{}".format(key,contact.get(key)))
while True:
    print("1. ADD NEW CONTACT")
    print("2. SEARCH CONTACT")
    print("3. DISPLAY CONTACT")
    print("4. EDIT CONTACT")
    print("5. DELETE CONTACT")
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        name=input("ENTER THE CONTACT NAME:")
        phone=input("ENTER THE MOBILE NUMBER:")
        email=input("ENTER THE EMAIL ID:")
        contact[name]=phone
        contact[name]=email
        
    elif choice==2:
        search_name=input("ENTER THE CONTACT NAME:")
        if search_name in contact:
            print(search_name,"'s contact number is",contact[search_name])
        else:
            print("CONTACT NOT FOUND")
    elif choice==3:
        if not contact:
            print("EMPTY CONTACT BOOK")
        else:
            display_contact()
    elif choice==4:
        update_contact=input("ENTER THE CONTACT TO BE UPDATED")
        if update_contact in contact:
            phone=input("ENTER MOBILE NUMBER")
            contact[update_contact]=phone
            print("CONTACT UPDATED")
            display_contact()
        else:
            print("NAME IS NOT FOUND IN CONTACT BOOK")
    elif chice==5:
        del_contact=input("ENTER THE CONTACT TO BE DELETED")
        if del_contact in contact:
            confirm=input("DO YOU WANT TO DELETE THIS CONTACT Y/N?")
            if confirm=="Y" or confirm =="y":
                contact.pop(del_contact)
            display_contact()
        else:
            print("NAME IS NOT FOUND IN CONTACT BOOK")
    else:
        break
           


# In[ ]:


# Initialize an empty contact book
contact_book = []

# Function to add a new contact
def add_contact():
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")
    
    contact = {
        'Name': name,
        'Phone Number': phone_number,
        'Email': email,
        'Address': address
    }
    
    contact_book.append(contact)
    print(f"Contact for {name} has been added!")

# Function to view all contacts
def view_contacts():
    if not contact_book:
        print("Contact book is empty.")
    else:
        print("\nContacts in the contact book:")
        for index, contact in enumerate(contact_book, start=1):
            print(f"Contact {index}:")
            for key, value in contact.items():
                print(f"{key}: {value}")
            print()

# Function to search for a contact by name
def search_contact():
    name = input("Enter the name to search: ")
    found_contacts = []

    for contact in contact_book:
        if contact['Name'].lower() == name.lower():
            found_contacts.append(contact)

    if found_contacts:
        print("\nFound contacts:")
        for contact in found_contacts:
            for key, value in contact.items():
                print(f"{key}: {value}")
            print()
    else:
        print(f"No contacts found with the name '{name}'.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    
    for contact in contact_book:
        if contact['Name'].lower() == name.lower():
            print("\nCurrent contact information:")
            for key, value in contact.items():
                print(f"{key}: {value}")
            
            print("\nEnter updated information:")
            contact['Name'] = input("Enter the updated name: ")
            contact['Phone Number'] = input("Enter the updated phone number: ")
            contact['Email'] = input("Enter the updated email address: ")
            contact['Address'] = input("Enter the updated address: ")
            
            print(f"Contact for {name} has been updated!")
            return
    
    print(f"No contacts found with the name '{name}'.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    
    for contact in contact_book:
        if contact['Name'].lower() == name.lower():
            contact_book.remove(contact)
            print(f"Contact for {name} has been deleted!")
            return
    
    print(f"No contacts found with the name '{name}'.")

# Main program loop
while True:
    print("\nContact Book Menu:")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


# In[ ]:




