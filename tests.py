import conversions
from  conversions_refactored import convert, ConversionNotPossible

def test(actual, expected):
    if actual != expected:
        return f"Test FAILED, got <{actual}>, expected <{expected}>."
    return f"Test passes, <{actual}> and <{expected}> match."


def testC2K():
    print("Testing Celsius to Kelvin conversion.")
    print(test(conversions.convertCelsiusToKelvin(100), 373.15))
    print(test(conversions.convertCelsiusToKelvin(50), 323.15))
    print(test(conversions.convertCelsiusToKelvin(0), 273.15))
    print(test(conversions.convertCelsiusToKelvin(-50), 223.15))
    print(test(conversions.convertCelsiusToKelvin(-100), 173.15))
    print()

def testC2F():
    print("Testing Celsius to Fahrenheit conversion.")
    print(test(conversions.convertCelsiusToFahrenheit(100), 212.00))
    print(test(conversions.convertCelsiusToFahrenheit(50), 122.00))
    print(test(conversions.convertCelsiusToFahrenheit(0), 32.00))
    print(test(conversions.convertCelsiusToFahrenheit(-50), -58.00))
    print(test(conversions.convertCelsiusToFahrenheit(-100), -148.00))
    print()

def othertests():
    print("Testing other conversion.")
    print(test(conversions.convertKelvinToCelsius(283.15), 10))
    print(test(conversions.convertKelvinToFahrenheit(293.15), 68))
    print(test(conversions.convertFahrenheitToCelsius(14), -10.0))
    print(test(conversions.convertFahrenheitToKelvin(14), 263.15))

def refactoredTests():
    print()
    print("Testing refactored functions:")
    print(test(convert("celsius", "celsius", 1), 1))
    print(test(convert("celsius", "kelvin", 1), 274.15))
    print(test(convert("celsius", "fahrenheit", 1), 33.8))

    print(test(convert("kelvin", "celsius", 1), -272.15))
    print(test(convert("kelvin", "kelvin", 1), 1))
    print(test(convert("kelvin", "fahrenheit", 1), -457.87))

    print(test(convert("fahrenheit", "celsius", 1), -17.22))
    print(test(convert("fahrenheit", "kelvin", 1), 255.93))
    print(test(convert("fahrenheit", "fahrenheit", 1), 1))

    print()

    print(test(convert("mile", "mile", 1), 1))
    print(test(convert("mile", "meter", 1), 1609.34))
    print(test(convert("mile", "yard", 1), 1760))

    print(test(convert("meter", "mile", 100000), 62.14))
    print(test(convert("meter", "meter", 1), 1))
    print(test(convert("meter", "yard", 1), 1.09))

    print(test(convert("yard", "mile", 1000), 0.57))
    print(test(convert("yard", "meter", 1), 0.91))
    print(test(convert("yard", "yard", 1), 1))

    try:
        convert("yard", "celsius", 1)
        print("No exception raised.")
    except ConversionNotPossible:
        print("Correct exception raised.")
    except: 
        print("Incorrect exception raised.")

testC2K()
testC2F()
othertests()
refactoredTests()