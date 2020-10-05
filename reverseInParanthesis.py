def reverseInParentheses(inputString):
    return eval('"' + inputString.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')


print(reverseInParentheses("foo(bar)baz(blim)"))