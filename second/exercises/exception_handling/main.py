def first():
    try:
        for i in ["a", "s", "d"]:
            print(i ** 2)
    except TypeError:
        print("i cached this exception")
    finally:
        print("good job")


def second(number):
    is_error = False
    is_running = True

    while is_running:
        try:
            print(number ** 3)
        except TypeError:
            is_error = True
            print("i cached this exception")
        else:
            is_running = False
            print("run without exception")
        finally:
            if not is_error:
                is_running = False
            if type(number) is str:
                number = int(number)
                print("modify str to int")


second("2")
