def check_scope():
    def do_local():
        test = "local test"
        # this test is only avilable from inside it

    def do_non_local():
        nonlocal test  # this test become below test(test=default)
        test = "non local test"  # so calling test changes the value default

    def do_global():
        global test  # this test become part of main root function
        test = "global test"

    test = "default"

    do_local()
    print("test value after do local: " + test)

    do_non_local()
    print("test value after do non local: " + test)

    # after calling do_non_local test value change to non local test

    do_global()
    print("test value after do global: " + test)  # this test is just ordinary test

    # value changes to non local test because previously we call do_non_local function
    # whhich changes the value of test from default to non local test


check_scope()

print("test value after main : " + test)  # this test is global test
