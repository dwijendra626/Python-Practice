'''
Here, in keyword arguments, already default values are present in function definitions.
But, if we pass any new value to the present argument (e.g., state = 'a stiff' is already 
there  but in function call, we r passing a new value to the state argument ie, a flexible
), then new value is updated and returned(see the 1st parrot function call)

Also, placing/order of the arguments is not necessary as we change the order of voltage
and state(see the 2nd parrot function call)
'''

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(voltage=2000,state='a flexible')     #new state value is overwritten
parrot(state='a flexible',voltage=1000)