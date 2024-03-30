def weight_conversion(weight, current_unit):
    """
    Converts weight from one unit to another.

    Parameters:
        weight (float): The weight to be converted.
        current_unit (str): The current unit of the weight ('kg' or 'lb').

    Returns:
        float: The converted weight.

    Raises:
        ValueError: If the current_unit is not 'kg' or 'lb'.
    """
    if current_unit.lower() == 'kg':
        return weight * 2.20462
    elif current_unit.lower() == 'lb':
        return weight * 0.453592
    else:
        raise ValueError("Invalid unit entered for weight. Please enter 'kg' or 'lb'.")


def length_conversion(length, current_unit):
    """
    Converts length from one unit to another.

    Parameters:
        length (float): The length to be converted.
        current_unit (str): The current unit of the length ('m' or 'ft').

    Returns:
        float: The converted length.

    Raises:
        ValueError: If the current_unit is not 'm' or 'ft'.
    """
    if current_unit.lower() == 'm':
        return length * 3.28084
    elif current_unit.lower() == 'ft':
        return length * 0.3048
    else:
        raise ValueError("Invalid unit entered for length. Please enter 'm' or 'ft'.")


def main():
    """
    Main function to handle unit conversion based on user input.
    """
    while True:
        try:
            conversion_type = int(input("What do you want to convert? Enter 1 for weight or 2 for length: ").strip())
            if conversion_type not in [1, 2]:
                raise ValueError("Invalid conversion type entered. Please enter 1 for weight or 2 for length.")

            if conversion_type == 1:
                weight = float(input("Enter the weight: ").strip())
                if weight <= 0:
                    raise ValueError("Weight must be greater than zero.")

                while True:
                    current_unit = input("Enter the current unit used for the weight (kg or lb): ").strip().lower()
                    if current_unit in ['kg', 'lb']:
                        converted_weight = weight_conversion(weight, current_unit)
                        print("Converted weight:", format(converted_weight, ".2f"), "lb" if current_unit == 'kg' else "kg")
                        break
                    else:
                        print("Invalid unit entered for weight. Please enter 'kg' or 'lb'.")

                break

            elif conversion_type == 2:
                length = float(input("Enter the length: ").strip())
                if length <= 0:
                    raise ValueError("Length must be greater than zero.")

                while True:
                    current_unit = input("Enter the current unit used for the length (m or ft): ").strip().lower()
                    if current_unit in ['m', 'ft']:
                        converted_length = length_conversion(length, current_unit)
                        print("Converted length:", format(converted_length, ".2f"), "ft" if current_unit == 'm' else "m")
                        break
                    else:
                        print("Invalid unit entered for length. Please enter 'm' or 'ft'.")

                break

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
