def loginRequired(func):
    
    
    def inner(**kwargs):
        #{'isLogin':True,'admin':True'}
        if kwargs['isLogin']==True and kwargs['admin']==True:
            kwargs['name'] = "raj" #update dictionary
            return func(**kwargs)
        else:
            print('You are not admin')
    
    return inner


@loginRequired
def callView(**kwrags):
    print('View called',kwrags)
    
    
callView(isLogin=True,admin=True) #    

            