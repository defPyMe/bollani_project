
def multiple_args(**kwargs):
    args_ = kwargs
    print(type(args_))
    for i in args_:
        print(args_[i])
     
     
multiple_args( f =1, d = 2,g= ["d", "d"], l = 4, m= "e", fffff = "ww")
