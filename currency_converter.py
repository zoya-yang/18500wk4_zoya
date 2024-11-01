conversion_rate = {
    'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
    'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
    'PHP': {'CNY': 0.12, 'GBP':0.01, 'INR': 1.45},
    'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
}

def currency_converter(amount, from_currency, to_currency):
    if amount < 0:
        return 0.0

    if from_currency == to_currency:
        return 0.0

    
    if from_currency == to_currency:
        return round(float(amount), 2)
    
    if from_currency in conversion_rate and to_currency in conversion_rate[from_currency]:
        rate = conversion_rate[from_currency][to_currency]
        converted_amount = amount * conversion_rate
        return round(converted_amount, 2)

    return 0.0
