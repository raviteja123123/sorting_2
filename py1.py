//january
//programe starts and ends here
//june
import sys
class stacks:
    stack=[]
    def __init__(self):
        print(type(stack))
    def push(self,i):
        self.stack.append(i)
    def poped(self):
        if(len(self.stack)==0):
            print("no data in stack to delete\n")
            return
        self.stack.pop()
    def display(self):
        if(len(self.stack)==0):
            print("no data in stack to print\n")
        print(self.stack)
    def sorting(self,):
        top=len(self.stack)
        for i in range(0,len(self.stack),1):
            #for j in range(len(self.stack)-1,0,-1):
            for j in range(top-1,0,-1):
                if ((self.stack[j]) < (self.stack[j-1])):
                    temp=self.stack[j]
                    self.stack[j]=self.stack[j-1]
                    self.stack[j-1]=temp
                
    def exit():
        sys.exit()
s=stacks
top=0
while(1):
    print("1.push\n2.pop\n3.display\n4.exit\n")
    choice=int(input("enter the choice\n"))
    if(choice==1):
        v=int(input("ente the element into stack\n"))
        s.push(stacks,v)
        top=top+1
    if(choice==2):
        s.poped(stacks)
    if(choice==3):
        s.display(stacks)
    if(choice==4):
        s.exit()
    if(choice==5):
      #  top=len(s.stack)
        s.sorting(stacks)

