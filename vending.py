from byotest import assert_equal

def get_change(amount):
    coins=[ 200, 100, 50, 20, 10, 5, 2, 1]
    if amount==0:
       return []
    if amount in coins:
        return[amount]
    change=[]
    for c in coins:
        while c<=amount:
            change.append(c)
            amount = amount - c
    return change
assert_equal(get_change(0),[])
assert_equal(get_change(1),[1])
assert_equal(get_change(2),[2])
assert_equal(get_change(5),[5])
assert_equal(get_change(10),[10])
assert_equal(get_change(20),[20])
assert_equal(get_change(50),[50])
assert_equal(get_change(100),[100])
assert_equal(get_change(200),[200])
assert_equal(get_change(3),[2,1])
assert_equal(get_change(79),[50,20,5,2,2])

print("all tests pass")



# def get_change(amount):
    
   
#     coins=[200, 100, 50, 20, 10, 5, 2, 1]
#     change = []
   
#     for num in coins:
#         while num<=amount:
#             change.append(num)
#             amount=amount-num
#     return change
            
                
            
# print(get_change(95))       
        
       
