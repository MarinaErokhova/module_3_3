def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params('cat')
print_params(23, [5, 6])
print_params(23, [5, 6], 'flowers')
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [5 , 'like' , [1, 23]]
values_dict = { 'a':'python', 'b': 1.5, 'c':9}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['25', 2.5]
print_params(*values_list_2, 42)