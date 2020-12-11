from number import Number


def test_number_validity():
    small_big_numbers = [
        12,
        1473,  # trigger
        2,
        8,
        19,
        2477,  # trigger
        3,
    ]

    number = Number()

    for my_number in small_big_numbers:
        assert number.verify_number(my_number) == True, "number must be less than 100!"
