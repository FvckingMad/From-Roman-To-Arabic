roman_symbols = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
}
forbidden_symbols = {'IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD', 'MMMM',
                     'IL', 'IC', 'ID', 'IM',
                     'VX', 'VL', 'VC', 'VD', 'VM',
                     'XD', 'XM',
                     'LC', 'LD', 'LM',
                     'DM'
                     }
def test_errors(s, mode):
    if mode == 1:
        if len(s) == 0 or s[0] == ' ' or s[0] == '\t':
            return 'Ошибка: значение не получено'
        for symbol in s:
            if symbol not in roman_symbols.keys():
                if symbol == ' ' or symbol == '\t':
                    return f'Ошибка: недопустимый символ - <пробел>'
                return f'Ошибка: недопустимый символ - "{symbol}"'
        for symbols in forbidden_symbols:
            if symbols in s:
                return f'Ошибка: недопустимое сочетание символов - "{symbols}"'
    if mode == 2:
        try: int(s)
        except:
            return f'Ошибка: введённое значение не является натуральным числом'
        if int(s) not in range(1, 4000):
            return f'Ошибка: число {s} не входит в допустимый диапазон [1 - 3999]'
def roman_to_int(s):
    if test_errors(s, mode = 1) is not None: return test_errors(s, mode = 1)
    for i in s:
        s = s.replace(i, str(roman_symbols[i]) + ' ')
    s_list = [int(i) for i in s.split()]
    for i in range(len(s_list)):
        try:
            while s_list[i] < s_list[i + 1]:
                s_list[i + 1] = s_list[i + 1] - s_list[i]
                s_list.pop(i)
        except: pass
    return sum(s_list)
def int_to_roman(s):
    if test_errors(s, mode = 2) is not None: return test_errors(s, mode = 2)
    s = int(s)
    output = ''
    count_digits = {
        1000: [0, 'M'],
        900: [0, 'CM'],
        500: [0, 'D'],
        400: [0, 'CD'],
        100: [0, 'C'],
        90: [0, 'XC'],
        50: [0, 'L'],
        40: [0, 'XL'],
        10: [0, 'X'],
        9: [0, 'IX'],
        5: [0, 'V'],
        4: [0, 'IV'],
        1: [0, 'I']
    }
    for i in count_digits.keys():
            while s // i > 0:
                count_digits[i][0] += 1
                s = s - i
    for i in count_digits.values(): output += i[1] * i[0]
    return output
def menu():
    print('Возможные действия:')
    print('1) Из римского в арабское')
    print('2) Из арабского в римское')
    print('3) Выход')
    print('Выберите действие: ', end = '')
    s = input()
    if s == '1':
        print('Введите число римскими цифрами: ', end = '')
        roman = input()
        print(roman_to_int(roman))
        print()
    elif s == '2':
        print('Введите число: ', end = '')
        arabic = input()
        print(int_to_roman(arabic))
        print()
    elif s == '3':
        print()
        return False
    else:
        print()

while True:
    if menu() is False:
        break