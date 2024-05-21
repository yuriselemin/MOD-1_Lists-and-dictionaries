
# Практическое задание по теме: "Списки и словари"




# 1 Работа со списками

my_list = ['Яблоко', 'Банан', 'Вишня', 'Груша', 'Дыня', 'Ежевика', 'Смородина']
print('List:',my_list)
print('First element:', my_list[0])
print('Last element: ', my_list[-1])
print('Sublist:', my_list[2:5])
my_list[2] = 'Арбуз'
print('Modified list: ', my_list)




# 2 Работа со словарями

my_dict = {'apple': 'яблоко', 'banana': 'банан', 'cherry': 'вишня'}
print('Dictionary: ', my_dict)
print('Translation:', my_dict['apple'])
my_dict['apple'] = 'большое яблоко'
my_dict.update({'orange': 'апельсин',
                'grape': 'виноград'})
print('Modified dictionary:', my_dict)


                                 # использование методов
print(my_dict.get('груша'))
my_dict.pop('orange')
print(my_dict)
print(my_dict.keys())
print(my_dict.items())



# ///
