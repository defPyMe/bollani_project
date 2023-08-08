
def multiple_args(*args):
    args_ = args
    #the first is a dict
    print(type(args_[1]))
     
multiple_args("driver", {"mm" : "dd", "ss": 3, "rty": 32})
