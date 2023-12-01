class BaseCalc:

    # return sum of two numbers
    def sum(a, b):
        return a+b

    # return the subtraction of two numbers
    def sub(a, b):
        return a-b

    # return the rest of the division of two numbers
    def rest(a, b):
        while(a>b):
            a = a - b
        return a

    # return the multiply of two numbers
    def mult(a,b):
        for i in range(1,b-1):
            a+=a
        return a
        
class AdvCalc(BaseCalc):
    
    # return a binary integer number
    def bin(a):
        return int('{:b}'.format(a))
    
    # return a hexadecimal string number
    def hex(a):
        return str.upper('{:x}'.format(a))
        
    # return a octal integer number
    def oct(a):
        return int('{:o}'.format(a))

# functions execution
print(BaseCalc.sum(1,5))
print(BaseCalc.rest(10,3))
print(BaseCalc.mult(5,4))
print(AdvCalc.bin(10))
print(AdvCalc.oct(10))
print(AdvCalc.hex(10))