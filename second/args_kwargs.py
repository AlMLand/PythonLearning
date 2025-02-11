def get_percent_from_sum(a, b) -> float:
    # in sum kommt ein tuple rein
    return sum((a, b)) * 0.05


print(get_percent_from_sum(40, 60))


##### *args -> build a tuple
# *args to zhe chto w java args parameter, zdes wse preobrazuetsja pod kapotom w tuple
def get_percent_from_sum_args(*args) -> float:
    print(f"the type of *args is -> {type(args)}")
    return sum(args) * 0.05


print(get_percent_from_sum_args(40, 62, 54))


##### **kwargs -> build a dictionary of key:value pairs

def with_star_star_kwargs(**kwargs):
    print(f"the type of *kwargs is -> {type(kwargs)}")
    if "fruit" in kwargs:
        print("aaaaaa: " + kwargs["fruit"])


with_star_star_kwargs(fruit="apple", meat="cow")


#####

def all_together(*args, **kwargs):
    print(f"current args: {args}, current kwargs: {kwargs}")


all_together(1, 2, 3, bear="qwe", cow="ölkj", snake=222)
