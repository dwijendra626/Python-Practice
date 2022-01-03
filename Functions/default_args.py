# Default Arguments

'''
In function definition, the function may/may not have some default values.If during the function
call, if argument does not have values, then the default values is to be considered.

'''
def student(firstname, lastname ='Mark', standard ='Fifth'):
     print(firstname, lastname, 'studies in', standard, 'Standard')

student(firstname='Dwayne')

# o/p --> Dwayne Mark studies in Fifth Standard


student(firstname='Dwayne',lastname='Smith')

# o/p --> Dwayne Smith studies in Fifth Standard
