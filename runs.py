import checks_for_field

# []
numbers = '123456789'
latin_lower = 'abcdefghijklmnopqrstuvwxyz'
latin_upper = latin_lower.upper()
cyrillic = 'абвгдеєжзиіїйклмнопрстуфхцчшщюяъьэё'
cyrillic_upper = cyrillic.upper()
symbols = ['!', '@', '#', '№', '&', '*', '_', '-', '=', '/', '?', '.', ',', '|', '[', ']', ':']

checks_for_field.input_field_check(latin_lower)

# checks_for_field.number_buttons_check()
