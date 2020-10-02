"""
Author : nkalyan🤠
implementing Python Scripts on reading and returning the name and max no of mails that sent by a person
"""

from collections import defaultdict

from pip._vendor.pep517.compat import FileNotFoundError


def get_line(fp):
    """This method yields the each mail at a time and gives input to mail_counter method"""
    with fp:
        for line in fp:
            string = 'From:'
            if line.find(string) >= 0:
                email = line[len(string):].strip()
                yield email


def check_mail(mail):
    """just simply check the format of emails.
     So every email should contain '@' and '.' at least, or I would raise MailValueError"""
    check = [True, True]
    for item in mail:
        if item == '@':
            check[0] = False
        if item == '.':
            check[1] = False
    if not any(check):
        return True


def mail_counter(path):
    """Which returns the name and count of max no of mails sent by the person"""
    email_dict = defaultdict(int)
    for mail in get_line(path):
        check_mail(mail)
        email_dict[mail] += 1

    return sorted(email_dict.items(), key=lambda x: x[1], reverse=True)[0]


def main():
    """Calls the method and prints the output statements"""

    path = input("Please enter file name..: ")
    # Catching exceptions in opening of file
    try:
        fp = open(path, 'r')
        get_line(fp)
        counter = mail_counter(fp)
        print(f'Max no of mails sent from Mail ID: {counter[0]}\nNumber of sent mails are: {counter[1]}')

    except FileNotFoundError:
        print(f'Cannot open {path}  plz check. ')

    except IndexError:
        print("No mail indexes are found in this file")


if __name__ == '__main__':
    main()
