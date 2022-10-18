def function4(input_int1: int, input_int2: int) -> int:
    maxi = 1
    for i in range(2, input_int1):
        if input_int1 % i == 0 and input_int2 % i == 0:
            maxi = i
    return maxi

function4(12, 42)