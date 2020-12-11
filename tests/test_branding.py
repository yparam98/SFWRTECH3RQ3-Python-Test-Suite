from branding import Branding


def test_branding_transparency():
    branding = Branding("path/to/logo.png")

    assert branding.is_transparent() == True, "logo must have a clear background!"


def test_branding_filetype():
    branding = Branding("path/to/logo.png")

    assert branding.getType() == "png", "logo must be of a PNG type!"
