class CalcTask:

    # Create a function that calculates the percentage
    def percentage(self, value1, value2):
        return (value1 / value2) * 100

    def is_number_divisible(self, value1, value2):
        if value1 % value2 == 0:
            return True
        else:
            return False

    def cm_to_inches(self, value1):
        return value1 * 0.39370079

    def area_of_triangle(self, height, base):
        return 1 / 2 * height * base
