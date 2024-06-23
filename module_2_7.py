def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b=25)

values_list = [10, 'hello', False]
values_dict = {'a': 20, 'b': 'world', 'c': True}
print_params(*values_list)
print_params(**values_dict)

def print_params(a=1, b='строка', c=True):
    print(a, b, c)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
