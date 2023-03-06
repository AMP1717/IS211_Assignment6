conversion = {
    'celsius': {
        'celsius': lambda x: 1,
        'kelvin': lambda x: round(x + 273.15, 2),
        'fahrenheit': lambda x: x * (9/5) + 32
    },

    'kelvin': {
        'kelvin': lambda x: 1,
        'celsius': lambda x: x - 273.15,
        'fahrenheit': lambda x: (9/5) * (x - 273.15) + 32
    },

    'fahrenheit': {
        'fahrenheit': lambda x: 1,
        'celsius': lambda x: (x - 32) * (5/9),
        'kelvin': lambda x: ((x - 32) / (9 / 5)) + 273.15
    },



    'meter': {
        'meter': lambda x: 1,
        'mile': lambda x: x / 1609.344,
        'yard': lambda x: x * 1.09361
    },

    'mile': {
        'mile': lambda x: 1,
        'meter': lambda x: x * 1609.344,
        'yard': lambda x: x * 1760
    },
    
    'yard': {
        'yard': lambda x: 1,
        'mile': lambda x: x / 1760,
        'meter': lambda x: x / 1.09361 
    }
}

class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()

    if fromUnit not in conversion:
        raise ConversionNotPossible()
    
    conv = conversion[fromUnit]
    if toUnit not in conv:
        raise ConversionNotPossible()
    
    f = conv[toUnit]
    
    return round(f(value), 2)
    