def resistor_label(colors):
    color_to_digit = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }
    tolerance_rates = {
        "grey": "±0.05%", "violet": "±0.1%", "blue": "±0.25%", "green": "±0.5%",
        "brown": "±1%", "red": "±2%", "gold": "±5%", "silver": "±10%"
    }

    if len(colors) == 1:
        return "0 ohms" if colors[0] == "black" else "Invalid color"

    significant_digits = ''.join(str(color_to_digit[color]) for color in colors[:-2])
    multiplier = 10 ** color_to_digit[colors[-2]]
    tolerance = tolerance_rates[colors[-1]]

    resistance_value = int(significant_digits) * multiplier


    if resistance_value >= 1_000_000:
        formatted_value = f"{resistance_value / 1_000_000:.2f}".rstrip('0').rstrip('.') + " megaohms"
    elif resistance_value >= 1_000:
        formatted_value = f"{resistance_value / 1_000:.2f}".rstrip('0').rstrip('.') + " kiloohms"
    else:
        formatted_value = f"{resistance_value} ohms"

    return f"{formatted_value} {tolerance}"