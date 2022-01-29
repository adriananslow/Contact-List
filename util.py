def verify_phone_number(phone_number):
    if len(phone_number) > 0 and (len(phone_number) != 10 or not phone_number.isdigit()):
        return False
    
    return True


def verify_email_address(email):
    if len(email) == 0:
        return True

    if "@" not in email:
        return False

    split_email = email.split("@")
    identifier = "".join(split_email[:-1])
    domain = split_email[-1]

    if len(identifier) < 1:
        return False

    if "." not in domain:
        return False

    split_domain = domain.split(".")

    for section in split_domain:
        if len(section) == 0:
            return False

    return True


def check_for_contact_by_name(contacts, first_name, last_name):
    for contact in contacts:
        if contact['first_name'] == first_name and contact['last_name'] == last_name:
            return contact
