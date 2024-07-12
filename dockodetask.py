rows=int(input("enter the number of rows"))
column=int(input("Enter the number of colunms"))

line1="  --- "* column
line2=" /  \ "*column
line3=" \  / "*column
line4="  --- "*column

for row in range(0,rows):
        print(line1)
        print(line2)
        print(line3)
        print(line4)
