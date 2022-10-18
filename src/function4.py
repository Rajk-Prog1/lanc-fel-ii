def function4(input_int1: int, input_int2: int) -> int:
    for x in range (0, input_int1):
        if (input_int1 - x) % x == 0 and (input_int2 - x) % x == 0:
            return(input_int1 - x)

            
