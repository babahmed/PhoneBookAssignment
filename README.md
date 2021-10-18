# PhoneBookAssignment

Python Phone Book Assignment Essexx University

Application uses a dictionary to store a list of contacts with the contacts name (a comma delimeted string ) as key and phone number as value.

The insert operation is at amortized constant time and linear time if the capaicty is reached.

List is at linear time as we transverse the complete record.

Search the data is also at linear time with an extra space complexity so to the memory allocated to the new filtered dictionary.

Modify is at constant time with no space impact as we replace the value at an index directly.

Delete will be at constant time with no space impact. The record is being accessed using the index.

Entry Point is Phone.py with main function calling phone record module.

Phone Record module references the menu module to load the menu items

Functions available are 1. List 2. Create 3. Find 4. Modify 5. Delete 6. Exit

List: provides a list of all contacts:
Create: to add a new contact. Provides option to update if contact conflicts.
Find: search a list of contact by keyword
Modify: update an existing contact
Delete: remove a contact.
Exit: end process.

Test Strategy:
Created record should appear when list menu is called.
Ensure deleted record do not appear in list.
Modified record should have updated value in list.
