from byotest import assert_equal

def add(x,y):
    return x+y
    
    
assert_equal(add(5,3), 8)   
assert_equal(add(2,2), 4)   
assert_equal(add(-1,-6),-7)
assert_equal(add(-7,2),-5)
assert_equal(add(0,0),0)
assert_equal(add(65535,1),65536)


print("All test pass")