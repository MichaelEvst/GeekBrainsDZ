def thesaurus(*names):
    res_dict = {}
    for name in names:
        key = name[0].capitalize()
        if key not in res_dict:
            res_dict[key] = []
        res_dict[key].append(name)
    return res_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
