
def set_func(func):
    def run_func():
        print("权限认证1")
        print("权限认证2")
        func()
    return run_func

@set_func
def testDecora():
    print("----------test-------------")

testDecora()

#test = set_func(testDecora)
#test()