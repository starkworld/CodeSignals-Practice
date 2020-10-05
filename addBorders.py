def addBorder(picture):
    a = len(picture[0]) + 2
    picture.insert(0, a * '*')
    picture.append(a * '*')
    j = 1
    for i in picture[1:-1]:
        picture.pop(j)
        picture.insert(j, f'*{i}*')
        j += 1
    return picture


print(addBorder(["aa",
                 "**",
                 "zz"]))
