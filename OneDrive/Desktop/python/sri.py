def check_even_list(num_list):
    even_number = []
    for number in num_list:
        if number % 2 == 0:
            even_number.append(number) 
        else:
            pass
    return even_number