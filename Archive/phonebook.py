phonebook = {}

print("""

Select an option below:
====================
1. Loook up an entry
2. Add an entry
3. Delete an entry
4. List all entries
5. Quit
""")

while True:
    usr_in = int(input("Entry:"))
    if usr_in == 1:
        entry_search = input("Who would you like to look up?")
        searching = phonebook.get(str(entry_search))
        print(searching)
    elif usr_in == 2:
        name = input("Name?")
        number = input("Number?")
        phonebook[str(name)] = number
        print(phonebook)
    elif usr_in == 3:
        delete = input("Who would you like to delete?")
        del phonebook[delete]
        print(f'{delete} Has been removed.')
    elif usr_in == 4:
        print(phonebook)
    elif usr_in == 5:
        print("Thank you!")
        break
    else:
        print("You must select 1-5")
