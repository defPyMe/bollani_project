
def multiple_args(*args):
    args_ = args
    return args_
     
     
d = multiple_args(1,2,["d", "d"], 4)
print(d[1])