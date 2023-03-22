import qdarktheme
from constraints import (COLOR_WHITE, DARKER_PRIMARY_COLOR,
                         DARKEST_PRIMARY_COLOR, PRIMARY_COLOR)

qss = f"""
    PushButton[cssClass="specialButton"] {{
        color: {COLOR_WHITE};
        background: {PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:hover {{
        color: {COLOR_WHITE};
        background: {DARKER_PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:pressed {{
        color: {COLOR_WHITE};
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


def setupTheme():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}",
            },
            "[light]": {
                "primary": f"{PRIMARY_COLOR}",
            },
        },
        additional_qss=qss
    )
