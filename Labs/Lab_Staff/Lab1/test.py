#function defintion here
def sum_gp_test(a,r,n):
    #start your code here
    sum = 0
    i = 0
    while i < n :
        sum = sum + a
        a = a * r
        i = i + 1
     
    return sum