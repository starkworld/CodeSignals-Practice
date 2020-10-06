"""An IP address is a numerical label assigned to each device
    (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication.
    There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.
    Given a string, find out if it satisfies the IPv4 address naming rules."""


def isIPv4Address(inputString):
    a = inputString.split('.')
    if len(a) != 4:
        return False
    if a[0] == '01':
        return False
    for x in a:
        if not x.isdigit() or x == '01':
            return False
        if x == '00':
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


print(isIPv4Address("172.316.254.1"))
