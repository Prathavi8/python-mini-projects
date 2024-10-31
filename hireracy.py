x = 10

def my_function ():
    x = 20
    print("my_function x = {}" .format(x)) 


    def my_inner_function ():
        x = 30
        print("my_inner_function x = {}" .format(x)) 

    my_inner_function()


my_function()
print("global x = {}".format(x))