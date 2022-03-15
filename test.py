class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __scared__(self, first, last, pay):
        print('in init')
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
    # __init__ = __boo__

    def __scared__(self, facts):
        self.facts = 'I am not scared'
        self.opinions = 'right'
        print(self.opinions)
        def whatever():
            self.opinions = 'wrong'
        whatever()
        print(self.opinions)
        
        
    __init__ = __scared__

    

# roberto = Employee('roberto')


# Python program to illustrate functions
# Functions can return another function
 
def create_adder(func,):
    def adder(y):
        y = func(y)
        return y
    return adder

# @create_adder
def add_15(x):
    return x

get = create_adder(add_15)

print(get(15))