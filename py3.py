def createstack():
    stack=[]
    return (stack)
def push(stack):
    v=int(input("enter the elements into stack\n"))
    stack.append(v)
    return (stack)
def poped(stack):
    if(len(stack)==0):
        print("no elements to delete in stack\n")
        return stack
    stack.pop()
    return stack
def display(stack):
    if(len(stack)==0):
        print("no elements to print in stack\n")
        return stack
    print(stack)
    return stack
def sorting(stack,top):
    l=[]
    for i in range(0,top,1):
        for j in range(top-1,0,-1):
       #     print(j)
            if(stack[j]<stack[j-1]):
                print("before swapimg \n" ,stack[j-1],stack[j])
                temp=stack[j]
                print("temp=",temp)
                stack[j]=stack[j-1]
                print("stack of j",stack[j])
                stack[j-1]=temp
                print("stack of j-1",stack[j-1]) 
                print("after swapimg \n",stack[j-1],stack[j])
                #stack.insert(j,stack[j-1])
                #stack.insert(j-1,temp)
                #l.insert(j,stack[j-1])
                #l.insert(j-1,temp)
            print("i th sorting list is\n",i,stack)
    return stack
s=createstack()
while(1):
    print("1.push\n2.pop\n3.display\n4.exit\n")
    choice=int(input("enter the choice\n"))
    if(choice==1):
 #       v=int(input("ente the element into stack\n"))
        s=push(s)
    if(choice==2):
        s=poped(s)
    if(choice==3):
        s=display(s)
    if(choice==4):
        exit()
    if(choice==5):
        top=len(s)
        s=sorting(s,top)
