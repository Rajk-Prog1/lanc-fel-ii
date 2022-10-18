input_list1 = [6, 8, 6]
input_list2 = [12, 45, 40]
start_of_the_course = [18, 0, 0]

def function3(input_list1: list, input_list2: list, start_of_the_course: list):
    
    kezdet = int(start_of_the_course[0]) * 3600 + int(start_of_the_course[1]) * 60 + int(start_of_the_course[2])
    elso = int(input_list1[0]) * 3600 + int(input_list1[1]) * 60 + int(input_list1[2])
    masodik = int(input_list2[0]) * 3600 + int(input_list2[1]) * 60 + int(input_list2[2])

    return(kezdet - elso, kezdet - masodik)
    
    pass