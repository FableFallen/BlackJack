global a
a = ''
def run_once(f):
    def wrapper(*args,**kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args,**kwargs)
        
    wrapper.has_run = False
    return wrapper

@run_once
def setWord(t):
    global a
    a = t
    print(a)
while 1:
    setWord('Hello')
    