from storage import read_contacts, write_contacts
from util import verify_phone_number, verify_email_address, check_for_contact_by_name


CONTACT_FILE_PATH = "contacts.json"


def add_contact(contacts):
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    mobile = input('Mobile Phone Number: ')
    home = input('Home Phone Number: ')
    email = input('Email Address: ')
    address = input('Address: ')
    
    valid_data = True
    if len(first_name) == 0 or len(last_name) == 0:
        valid_data = False
        print('First Name and Last Name are required.')
    if not verify_phone_number(mobile):
        valid_data = False
        print('Invalid mobile phone number.')
    if not verify_phone_number(home):
        valid_data = False
        print('Invalid home phone number.')
    if not verify_email_address(email):
        valid_data = False
        print('Invalid email address.')
    if check_for_contact_by_name(contacts, first_name, last_name) != None:
        valid_data = False
        print('A contact with this name already exists')
    if valid_data:
        new_entry = {
                        'first_name': first_name,
                        'last_name': last_name,
                        'mobile_phone_number': mobile,
                        'home_phone_number': home,
                        'email': email,
                        'address': address
                    }
        contacts.append(new_entry)
        print('Contact Added!')
    else:
        print('You entered invalid information, this contact was not added.')
    return contacts


def search_for_contact(contacts):
    first_name = input('First Name: ').lower()
    last_name = input('Last Name: ').lower()
    found_contacts = []
    for contact in contacts:
        if first_name in contact['first_name'].lower() and last_name in contact['last_name'].lower():
            found_contacts.append(contact)
    return found_contacts


def delete_contact(contacts):
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    contact = check_for_contact_by_name(contacts, first_name, last_name)
    if contact != None:
        confirm_delete = input('Are you sure you would like to delete this contact (y/n)? ')
        if confirm_delete == 'y':
            contacts.remove(contact)
            print('Contact deleted!')
    else:
        print('No contact with this name exists.')
    return contacts


def list_contacts(contacts):
    contacts.sort(key=lambda x: x.get('first_name', '') + x.get('last_name', ''))
    for i, contact in enumerate(contacts):
        print(f'{i + 1}. {contact["first_name"]} {contact["last_name"]}')
        for key, value in list(contact.items())[2:]:
            if len(value) > 0:
                label_idx = ['mobile_phone_number', 'home_phone_number', 'email', 'address'].index(key)
                labels = ['Mobile', 'Home', 'Email','Address']
                print(f'    {labels[label_idx]}: {value}')


def main(contacts_path):
    print('Welcome to your contact list!')
    print('The following is a list of useable commands:')
    print('"add": Adds a contact.')
    print('"delete": Deletes a contact.')
    print('"list": Lists all contacts.')
    print('"search": Searches for a contact by name.')
    print('"q": Quits the program and saves the contact list.')

    contacts = read_contacts(contacts_path)

    while True:
        command = input('Type a command: ')
        if command == 'q':
            write_contacts(contacts_path, contacts)
            print('Contacts were saved successfully.')
            break
        elif command == 'add':
            contacts = add_contact(contacts)
        elif command == 'delete':
            delete_contact(contacts)
        elif command == 'list':
            list_contacts(contacts)
        elif command == 'search':
            found_contacts = search_for_contact(contacts)
            print(f'Found {len(found_contacts)} matching contact{"s" if len(found_contacts) > 1 else ""}.')
            list_contacts(found_contacts)
        else:
            print('Unknown command.')


if __name__ == "__main__":
    main(CONTACT_FILE_PATH)
