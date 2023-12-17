"""page 1"""
import dash
from dash import html

from components.button_with_modal import button_with_modal


dash.register_page(
    __name__,
    path="/",
    title='Home',
)


def layout():
    return html.Div(
        children=[
            html.Div("Page1"),
            button_with_modal(
                btn="Modal 1",
                identifier="modal-1",
                children=[html.Div("Page 1 modal 1 content")]
            ),
            button_with_modal(
                btn="Modal 2",
                identifier="modal-2",
                children=[html.Div("Page 1 modal 2 content")]
            )
        ]
    )