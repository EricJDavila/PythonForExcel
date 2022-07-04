TEMPERATURE_SCALES = ("fahrenheit", "kelvin", "celsius")


def convierte_a_celsius(degrees, source="fahrenheit"):
    if source.lower() == "fahrenheit":
        return (degrees-32) * (5/9)
    elif source.lower() == "kelvin":
        return degrees - 273.15
    else:
        return f"No sé como convertir de {source}"


print("Este es el módulo de temperatura.")