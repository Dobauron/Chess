
def allowed_moves(list):
    true_list = []
    for el in list:
        if el[0] <= 7 and el[0] >= 0 and el[1] >= 0 and el[1] <= 7:
            true_list.append(el)


    return true_list

