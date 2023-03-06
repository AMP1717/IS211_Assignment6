def convertCelsiusToKelvin(cel):
    return round(cel + 273.15, 2)

def convertCelsiusToFahrenheit(cel):
    return cel * (9/5) + 32


def convertKelvinToCelsius(kel):
    return kel - 273.15

def convertKelvinToFahrenheit(kel):
    return (9/5) * (kel - 273.15) + 32


def convertFahrenheitToCelsius(fah):
    return (fah - 32) * (5/9)

def convertFahrenheitToKelvin(fah):
    return ((fah - 32) / (9 / 5)) + 273.15