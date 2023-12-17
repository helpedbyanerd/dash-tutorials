
"""page 2"""

import dash
from dash import html

from components.button_with_modal import button_with_modal

dash.register_page(
    __name__,
    path="/page2",
    title="Page 2"
)


def layout():
    return html.Div(
        children=[
            html.Div("Page 2"),
            button_with_modal(
                btn="Button Page 2",
                identifier="Page-2",
                children=[html.Div("Page 2 modal content")]
            ),
        ]
    )