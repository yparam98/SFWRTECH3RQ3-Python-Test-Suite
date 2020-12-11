from name import Name


def test_name_clean():
    illegal_words = [
        "gadzooks",  # trigger
        "barnacles",
        "William Shatner",
        "cowabunga",
        "zoinks",  # trigger
        "crikey",  # trigger
    ]

    name = Name()

    for word in illegal_words:
        assert name.is_clean(name) == True, "name shouldn't contain profanity!"


def test_name_length():
    short_and_long_words = [
        "sweaterdresses",  # trigger
        "bob",
        "incomprehensibilities",  # trigger
        "croissants",
        "otorhinolaryngological",  # trigger
    ]

    name = Name()

    for word in short_and_long_words:
        assert name.verify_name(word) == True, "name shouldn't be too long!"
