print("""HI there everyone!!!
 I am Jayesh! :)""")

for c in range(6):
    if c==0:
        print("  *    *\n","000  000")
    elif c==1:
        print(" 00000000")
    else:
        print(" "*(c-1),"0"*(2*(5-c)))
