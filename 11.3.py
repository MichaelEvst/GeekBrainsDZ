class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f'Недопустимое значение - str и boolean')
                y_or_n = input(f'Попробовать еще раз? Ведите yes или no ')

                if yes_or_no == 'Yes' or yes_or_nn == 'yes':
                    print(try_except.my_input())
                elif yes_or_no == 'No' or yes_or_no == 'no':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'

try_except = Error(1)
print(try_except.my_input())
