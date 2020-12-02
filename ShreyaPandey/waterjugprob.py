n1=int(input("Enter the capacity of first jug: "))
n2=int(input("Enter the capacity of second jug: "))
n3=int(input("In which jug to be filled :"))
n4=int(input("How much to be filled: "))
class Waterjug:
    def __init__(self,am,bm,a,b,g):
        self.a_max = am;
        self.b_max = bm;
        self.a = a;
        self.b = b;
        self.goal = g;
    def fillA(self):
        self.a = self.a_max;
        print ('(', self.a, ',',self.b, ')')
    def fillB(self):
        self.b = self.b_max;
        print ('(', self.a, ',', self.b, ')')
    def emptyA(self):
        self.a = 0;
        print ('(', self.a, ',', self.b, ')')
    def emptyB(self):
        self.b = 0;
        print ('(', self.a, ',', self.b, ')')
    def transferAtoB(self):
        while (True):
            self.a = self.a - 1
            self.b = self.b + 1
            if (self.a == 0 or self.b == self.b_max):
                break
        print ('(', self.a, ',', self.b, ')')
    def main(self):
        while (True):
            if (self.a == self.goal or self.b == self.goal):
                break
            if (self.a == 0):
                self.fillA()
            elif (self.a > 0 and self.b != self.b_max):
                self.transferAtoB()
            elif (self.a > 0 and self.b == self.b_max):
                self.emptyB()
def pour(jug1, jug2):
       max1, max2, fill = n1, n2, n4  
       print("%d\t%d" % (jug1, jug2))
       if jug2 is fill:
         return       elif jug2 is max2:

          pour(0, jug1)
       elif jug1 != 0 and jug2 is 0:          
          pour(0, jug1)
       elif jug1 is fill:         
         pour(jug1, 0)
       elif jug1 < max1:        
        pour(max1, jug2)
       elif jug1 < (max2-jug2):        
        pour(0, (jug1+jug2))
       else:        
        pour(jug1-(max2-jug2), (max2-jug2)+jug2) 
print("JUG1\tJUG2")
if(n3==2):
    pour(0, 0)
elif(n3==1):
  print ('(', '0',',', '0', ')')
  waterjug=Waterjug(n1,n2,0,0,n4);
  waterjug.main();
