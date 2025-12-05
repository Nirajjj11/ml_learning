person = ['hi','how are you',"good",'i am happy','i am sad','how are you working']

bot = ['Hello','I am Fine, You?',"Nice to Here! :) ",'Wooohooo,',"Don't fell sad ! Chat with me\nGera up",'I am on training']

print("-"*30,"Welcome to chat bot","-"*30)
print("\n\tTo Start Chat write any thing !\n\n")

a = True
while(a):
    a = input("\t\t\t\t\t\tYou : ").lower()
    if a == '0' or a == 'thanks' :
        a = False
        print("\n\n\t\t\tOK Thanks ! Have a Good Day. :) \n")
        print("-"*20,"Chat bot End","-"*20)
    
    # print("\tBot : Hello")
    for i in range(len(person)):
        if a == person[i]:
            print("\tBot : ",bot[i])

        
    
