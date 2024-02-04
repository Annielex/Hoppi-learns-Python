def cooking_time(eggs):
# 8 eggs fit the pot at a time
# 5min to boil an egg
# water is boiling at all times
# no time considered for input or output of eggs
    import math
    #eggs = input("How many eggs?" )
    egg_time = math.ceil(int(eggs) / 8) * 5
    return egg_time
    #print(egg_time)
    pass
