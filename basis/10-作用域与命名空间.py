def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:%s" % spam)
    do_nonlocal()
    print("After nonlocal assignment:%s" % spam)
    do_global()
    print("After global assignment:%s" % spam)


scope_test()
print("hello, In global scope:%s" % spam)
