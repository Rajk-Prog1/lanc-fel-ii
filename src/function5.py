def function5(input_string: str, input_int: int) -> str:
    lista = []
    for i in range(1, int(len(input_string)/input_int) + 1):
        lista.append(input_string[input_int*i - 1])
    lovak = "".join(lista)

    return(lovak)

    pass
