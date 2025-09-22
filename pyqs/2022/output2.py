def some_function(p):
    dp ={}
    for order in p:
        if not order==0:
            dp[order-1] = order * p[order]
        
    return dp
        
print(some_function({0:-3,3:2,5:-1}))