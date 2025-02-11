def almost_there(number: int) -> bool:
    hundred = range(90, 111)
    two_hundred = range(190, 211)

    return number in hundred or number in two_hundred


#####
print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
