'''
*args & **kwargs
----------------
*args    --> It receives the arguments in tuple form.
**kwargs --> It receives the arguments in dictionary form.

In function call, kind (arg) takes the value 'Limburger',
next two values taken by arguments,
and (keyword-value) pairs taken by keywordargs
'''


def cheeseshop(kind, *arguments, **keywordargs):
    print('Do u have any',kind,'?')
    print('Im sorry, we are all out of',kind)

    for args in arguments:
        print(args)
    print(type(arguments))

    print('-'*40)
    for kw in keywordargs:
        print(kw,':',keywordargs[kw])
    
    print(type(keywordargs))

cheeseshop('Limburger','Its very runny,sir',"It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

'''
output
-------
Do u have any Limburger ?
Im sorry, we are all out of Limburger
Its very runny,sir
It's really very, VERY runny, sir.
<class 'tuple'>
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
<class 'dict'>
'''

def cheeseshop(kind, *arguments, **keywordargs):
    print('Do u have any',kind,'?')
    print('Im sorry, we are all out of',kind)

    for args in arguments:
        print(args)
    print(type(arguments))

    print('-'*40)
    for kw in keywordargs:
        print(kw,':',keywordargs[kw])
    
    print(type(keywordargs))

cheeseshop('Limburger',
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch",
           'Its very runny,sir',"It's really very, VERY runny, sir.") 
           
'''
output
------
error-positional argument follows keyword argument
'''


def cheeseshop(kind, **keywordargs, *arguments):
    print('Do u have any',kind,'?')
    print('Im sorry, we are all out of',kind)

    for args in arguments:
        print(args)
    print(type(arguments))

    print('-'*40)
    for kw in keywordargs:
        print(kw,':',keywordargs[kw])
    
    print(type(keywordargs))

cheeseshop('Limburger','Its very runny,sir',"It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

'''
error
----
In function definition, *arguments should come before **keywordargs.
'''