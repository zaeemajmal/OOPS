print("--Welcome to Number to roman number converter!--")
print("--For numbers more than 4000 brackets are used...--")

class RomanConverter:
    def __init__(self):
        self.value_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

    def convert_number_to_roman(self, number):
        result = ""

        while number > 0:
            if number >= 4000:
                thousands = number // 1000
                number = number % 1000

                temp = ""
                n = thousands

                for value, symbol in self.value_map:
                    while n >= value:
                        temp += symbol
                        n -= value

                result += "(" + temp + ")"
            else:
                for value, symbol in self.value_map:
                    while number >= value:
                        result += symbol
                        number -= value

        return result

number = int(input("Enter a number: "))
converter = RomanConverter()

if number > 0:
    print("Roman numeral:", converter.convert_number_to_roman(number))
else:
    print("Enter positive number only")