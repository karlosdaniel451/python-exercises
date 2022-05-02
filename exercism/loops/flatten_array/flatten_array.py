def flatten(iterable):
    flatten_list = []

    for i in iterable:
        if type(i) is list:
            flatten_list += flatten(i)
        elif i is not None:
            flatten_list.append(i)

    return flatten_list
