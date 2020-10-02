"""
Created on Monday 29 feb 16:53:34 2020

@author: nkalyan🤠
        '''Implementing Python Scripts for finding unique senders in mailbox.txt file '''
"""


class MailValueError(Exception):
    """This class create an object and returns the message objects"""
    def __init__(self, msg='Wrong format of mails.'):
        super().__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg


def get_line(path):
    """Open file and if file not found then it raises error"""

    try:
        fp = open(path, 'r')

    except FileNotFoundError:
        print('Cannot open ', path, ' , plz check. ')

    else:
        with fp:
            for line in fp:
                string = 'From:'
                if line.find(string) >= 0:
                    email = line[len(string):].strip()
                    yield email


def check_mail(mail):
    """This method checks the unique mail in file and returns boolean value"""

    check = [True, True]

    for item in mail:
        if item == '@':
            check[0] = False
        if item == '.':
            check[1] = False

    if not any(check):
        return True

    else:
        raise MailValueError()


def save_and_count(path):
    """This method count the number of unique mails from the file"""

    mail_set = set()

    for mail in get_line(path):
        mail_set.add(mail)

    for mail in mail_set:
        try:
            check_mail(mail)
        except MailValueError as m:
            print(m)

    return list(mail_set), len(mail_set)


def main():
    """This method calls the all the methods to perform the operations"""

    path = input("Enter the File name: ")
    mails, numbers = save_and_count(path)
    print(f"The numbers of Unique mails in {path}: ", numbers)

    path1 = input("Enter the another file name: ")
    mails, numbers = save_and_count(path1)
    print(f'The numbers of Unique mails in {path1}: ', numbers)


if __name__ == '__main__':
    main()
