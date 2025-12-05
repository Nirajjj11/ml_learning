l1 = ['A','B','C','D','E','F']
l2 = ['a','b','c','d','e','f']

a = input("Enter any thing").upper()

print(l1[1])

if a in l1 :
    print("Yes")
    
    for i in range (len(l1)):
        if l1[i] == a:
            print("Your Position is :",i)
            print("Bot : ",l2[i])
