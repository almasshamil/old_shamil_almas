data_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(data_list):
     first_symbol = data_list[i][0]
     if data_list[i].isdigit() or ((first_symbol == '-' or first_symbol == '+') and data_list[i][1:].isdigit()):
         if first_symbol == '-' or first_symbol == '+':
             data_list[i] = first_symbol + data_list[i][1:].zfill(2)
         else:
             data_list[i] = data_list[i].zfill(2)
         data_list.insert(i, '"')
         data_list.insert(i + 2, '"')
         data_list[i] = ''.join(data_list[i: i + 3])
         data_list.remove(data_list[i + 1])
         data_list.remove(data_list[i + 1])
     i += 1
print(' '.join(data_list))