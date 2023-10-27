def roman_numerals_to_int(roman_numeral):
    roman_to_int = {  # Реализовываю через словарь
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    prev_value = 0
    for numeral in roman_numeral[::-1]:
        value = roman_to_int.get(numeral)
        if value is None:
            return None
        elif value >= prev_value:
            result += value
        else:
            result -= value
        prev_value = value
    return result


print(roman_numerals_to_int('IV'))
print(roman_numerals_to_int('MCMXCIX'))
print(roman_numerals_to_int('abc'))
