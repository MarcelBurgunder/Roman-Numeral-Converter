import sys

# Arabic equivalents of Roman numeral characters
roman_to_arabic = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# Arabic equivalents of Roman numeral subtractions 
roman_subs_to_arabic = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}

def main() -> None:
    """
    Main routine for the Roman to Arabic numeral converter.
    Accepts and requires one argument that denotes a Roman numeral string.
    Validates the input and prints the corresponding arabic numeral.
    """
    roman = sys.argv[1] if len(sys.argv) > 1 else ""
    if roman == "":
        print("Error: No Roman numeral input was provided.")
        return

    arabic = get_arabic(roman)
    if arabic == -1:
        return

    print("Roman: " + roman)
    print("Arabic: " + str(arabic))
    return

def get_arabic(roman: str) -> int:
    """
    Returns the Arabic numeral (as an integer) corresponding to some Roman numeral input.
    1) Any input that includes an invalid character, such as A, v, ~, V̅, will be evaluated as an invalid input, raise an error, and return -1.
    2) Character ordering is not validated, meaning numerals such as XVX, VIIIIII won't raise an error and will return some integer that isn't -1.
    """
    total = 0
    i = 0 
    n = len(roman)
    while i < n: 
        if roman[i:i+2] in roman_subs_to_arabic: # subtraction
            total += roman_subs_to_arabic[roman[i:i+2]]
            i += 2
        elif roman[i] in roman_to_arabic: # regular character
            total += roman_to_arabic[roman[i]]
            i += 1
        else: # invalid character
            print("Error: " + roman[i] + " is an invalid Roman numeral character. Only 'I', 'V', 'X', 'L', 'C', 'D', 'M' are valid.")
            return -1

    return total

main()
