from jersey import Jersey
from team import Team
from colourscheme import ColourScheme
from customization import Customization


def test_default_customizations():
    jersey = Jersey()
    toronto_raptors_lowry_standard = Customization()

    raptors = Team("Toronto Raptors")
    raptors.set_colours(ColourScheme("red", "black"))

    toronto_raptors_lowry_standard.add_team(raptors)
    assert toronto_raptors_lowry_standard.add_name("Kyle Lowry"), "name not valid"
    assert toronto_raptors_lowry_standard.add_number(7), "number not valid"
    assert toronto_raptors_lowry_standard.add_branding("path/nike/logo.png"), "logo not valid"

    jersey.add_customizations(toronto_raptors_lowry_standard)

    assert jersey.modifications.verify_customizations(), "jersey customizations are not valid!"
    assert jersey.is_modified, "jersey must reflect status as modified"

