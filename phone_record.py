import menu


def phone_operations():

    # dictionary to hold phone records
    record = {}

    while True:
        # call options
        entry = menu.options()

        # List condition
        if entry == 1:
            # List items
            if bool(record) != False:
                for key, item in record.items():
                    print(key, ':', item)

             # No record
            else:
                print('phonebook is empty')
        # Create
        elif entry == 2:
            # Request for phone number and contact data
            phone_number = input('Please Enter a number: ')
            first_name = input('Please Enter Firstdata : ')
            last_name = input('Please Enter Lastdata : ')

            # Check if the contact number already exits in Phonebook
            # If it does not, update current contact list in PhoneBook
            if phone_number not in record.items():
                record.update({first_name+","+last_name: phone_number})
                # Print a success message
                print('Contact ', first_name, ',', last_name,
                      ' : ', phone_number, ' successfully saved')

            # Contact exist
            else:
                print('That contact already exits in your Phonebook')
                confirm = input('Record already exist as ' +
                                record[phone_number]+'Update contact as '+first_name+","+last_name+' ? Y/N: ')
                if confirm.capitalize() == 'Y':
                    record.update({first_name+","+last_name: phone_number})
                    # Print a success message
                    print('Contact updated successfully saved')

        # Find
        elif entry == 3:

            # take search string
            search = input(
                'Enter search: ')

            # filter records for search item
            filter = {key: item for key,
                      item in record.items() if search in key}
            if len(filter) > 0:
                # Print list of matching items
                print('<<< Matching records are>>>')
                for key, item in filter.items():
                    print(key, ':', item)
                    data = input('Enter the full data to view full details: ')
                    # Create a condition to check if the entered data is in the phonebook
                    if data in record:
                        # If yes, print the required contact
                        print('The contact is', data, ':', record[data])

                        # Else inform the user that the contact does not exist
                    else:
                        print(
                            'That contact does not exist! Return to the main menu to enter the contact')

                # Inform no matching items
            else:
                print(
                    'No record found! for the search parameter')

                # Modify
        elif entry == 4:
            # initiate a data variable which user wishes to view
            data = input(
                'Enter the data of the contact details you wish to modify: ')
            # check record
            if data in record:
                # If yes, print the required contact
                print('The contact current info is', data, ':', record[data])
                print('Please Enter new information. Press enter to skip')
                print('Phone number: ', record[data])
                phone_number = input('Please Enter a number: ')
                print('First Name: ', data.split(',')[0])
                first_name = input('Please Enter FirstName : ')
                print('Last Name: ', data.split(',')[1])
                last_name = input('Please Enter LastName : ')
                if(len(phone_number) > 0):
                    record[data] = phone_number
                if(len(first_name) == 0 and len(last_name) > 0):
                    record[data.split(',')[0]+','+last_name] = record.pop(data)
                if(len(last_name) == 0 and len(first_name) > 0):
                    record[first_name+',' +
                           data.split(',')[1]] = record.pop(data)
                if(len(last_name) > 0 and len(first_name) > 0):
                    record[first_name+','+last_name] = record.pop(data)

                # Else inform the user that the contact does not exist
            else:
                print(
                    'That contact does not exist! Return to the main menu to enter the contact')

         # Delete
        elif entry == 5:
            # Initiate a data variable
            data = input('Enter the data of the contact you wish to delete: ')
            # check if contact exists
            if data in record:
                # print the required contact
                print('The contact is', data, ':', record[data])

                # Else inform the user that the contact does not exist
            else:
                print(
                    'That contact does not exist! Return to the main menu to enter the contact')

            # validate delete
            confirm = input(
                'Confirm record? Y/N: ')

            # Action based on input
            if confirm.capitalize() == 'Y':

                # Remove record
                record.pop(data, None)

                # Show the rest of the records
                for key, item in record.items():
                    print(key, ':', item)

            # Return to menu
            else:
                print('Return to Main Menu')

        # exit Application
        elif entry == 6:
            print('Thanks for using the Py Contact Book')
            break

        # Invalid input
        else:
            print('Incorrect Entry!')
