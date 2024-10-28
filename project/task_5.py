given_list = ["Welcome", "Ali", "Hi", "Ali", "No", "Hi", "No", "Ali", "No", "Ali"]
def count_in_list(given_list):
    c_dict = dict()
    for i in  given_list:
        if i in c_dict.keys():
            c_dict[i] += 1
        else:
            c_dict[i] = 1
    return c_dict

print(count_in_list(given_list))