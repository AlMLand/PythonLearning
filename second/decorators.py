def old_original_method():
    print("original logic 1")


def new_decorator_method(original_method):
    def wrap_method():
        print("some new code before")
        original_method()
        print("some new code after\n")

    return wrap_method


new_decorator_method(old_original_method)()
# or
decorated_method = new_decorator_method(old_original_method)
decorated_method()


# or
@new_decorator_method
def old_original_method2():
    print("original logic 2")


old_original_method2()
