# Logging

import logging

"""
logging level - logging levels allow us to specify exactly what we want to log by seperating these into categories  

There are 5 standard logging levels  

1. DEBUG - Detailed information, typically of interest when diagnosing problems
2. INFO - Confirmation that things are working as expected 
3. WARNING - Indication that something unexpected happened or indicative of some problems in the near future. Software is still working as expected 
4. ERROR - Due to more serious problem, the software has not been able to perform some functions.
5. CRITICAL - Serious error, indicating that the program itself may be unable to continue running
"""

"""
_default level of logging is set to warning_  
what that means is that it will capture everything that is warning or above. So warning, error and critical
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


num_1 = 10
num_2 = 5


add_res = add(num_1, num_2)
logging.debug("Add: {} + {} = {}".format(num_1, num_2, num_1 + num_2))

sub_res = subtract(num_1, num_2)
logging.debug("Subtract: {} - {} = {}".format(num_1, num_2, sub_res))

mul_res = multiply(num_1, num_2)
logging.debug("Multiply: {} * {} = {}".format(num_1, num_2, mul_res))

div_res = divide(num_1, num_2)
logging.debug("Divide: {} / {} = {}".format(num_1, num_2, div_res))

"""
_logging.debug_ has similar syntax as print. just instead of print we are writing logging.debug  

but this will not log anything as the default level is warning
"""

## Change Config of Logging

"""
so to alter the behaviour we can use ***logging.basicConfig(level=)*** to change the level of logging

also a filename to specify which file to the output to

"""

num_1 = 20
num_2 = 10

add_res = add(num_1, num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_res))

sub_res = subtract(num_1, num_2)
logging.debug('Subtract: {} - {} = {}'.format(num_1, num_2, sub_res))

mul_res = multiply(num_1, num_2)
logging.debug('Multiply: {} * {} = {}'.format(num_1, num_2, mul_res))

div_res = divide(num_1, num_2)
logging.debug('Divide: {} / {} = {}'.format(num_1, num_2, div_res))