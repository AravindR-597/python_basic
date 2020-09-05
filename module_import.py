
import file_import_function_test

file_import_function_test.if_fun(10)

print(__name__) # to find we are in which module

#giving a name to the fun and calling using the name

check =file_import_function_test.if_fun
check(-200)

#only importing a function from a module
from file_import_function_test import if_fun

if_fun(3)

#assigning a name to the module

import file_import_function_test as file

file.if_fun(-987)


#python modules import

import platform
print(platform.system())
print(platform.processor())
print(platform.python_compiler())