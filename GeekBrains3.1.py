def num_translate(user_req):
    start_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                  'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    for req, translate_value in start_dict.items():
        if user_req.lower() == req:
            if user_req.title() == user_req:
                return translate_value.title()
            else:
                return translate_value
    return 'None'


print(num_translate("One"))

