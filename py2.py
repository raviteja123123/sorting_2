import sys
class stacks:
    stack=[]
    top=0
    def __init__(self):
        print(type(stack))
    def push(self,i):
       # print("enter the element into stack\n")
        self.stack.append(i)
    def poped(self):
      #  top=len(self.stack)
        self.stack.pop()
    def display(self):
        print(self.stack)   
    def exit():
        sys.exit()
s=stacks
top=len(s.stack)
#print(top)
#print(len(s.stack))
while(1):
    print("1.push\n2.pop\n3.display\n4.exit\n")
    choice=int(input("enter the choice\n"))
    if(choice==1):
        v=int(input("ente the element into stack\n"))
        s.push(stacks,v)
    if(choice==2):
        s.poped(stacks)
    if(choice==3):
        s.display(stacks)
    if(choice==4):
        s.exit()
#    if(choice==5):
 #       s.sorting(stacks,top)

