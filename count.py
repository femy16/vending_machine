from byotest import assert_equal

def foo2(text):
    
   return(len([c for c in text if c.isupper()]))
    
assert_equal(foo2("LoooL"),2)
assert_equal(foo2(""),0)
assert_equal(foo2(""),0)

print("All test pass")