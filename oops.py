class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def power(self,a,b):
        return a**b
    def div(self,a,b):
        return a/b
    def floor_div(self,a,b):
        return a//b
    def mod(self,a,b):
        return a%b
n1=calculator()
n2=calculator()
# n1
print(n1.add(20,4))
print(n1.sub(20,4))
print(n1.mul(20,4))
print(n1.div(20,4))
print(n1.mod(20,4))
print(n1.floor_div(20,4))
print(n1.power(20,4))
# n2
print(n2.add(4,1))
print(n2.sub(4,1))
print(n2.mul(4,1))
print(n2.div(4,1))
print(n2.mod(4,1))
print(n2.floor_div(4,1))
print(n2.power(4,1))

n1.model_num="S2114"
n1.made_in="india"
n1.color="pink"
n1.discount="10%"

n2.model_num="B1404"
n2.made_in="PARIS"
n2.color="black"
n2.discount="10%"

# ----n1----
print(n1.model_num)
print(n1.made_in)
print(n1.color)
print(n1.discount)
# ----n2----
print(n2.model_num)
print(n2.made_in)
print(n2.color)
print(n2.discount)


