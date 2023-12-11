'''
Define a function that converts fluid ounces to milliliters knowing that 1 fluid ounce is equal to 29.57353 milliliters. 
For example, I was to call your function with foo(1) I would get an output of 29.57353. 
If I called it with  foo(5) I would get 147.86765, and so on.
'''


def fluid_to_ounces(ounce):
    milliliters = ounce * 29.57353
    return milliliters

print(fluid_to_ounces(1))
print(fluid_to_ounces(5))