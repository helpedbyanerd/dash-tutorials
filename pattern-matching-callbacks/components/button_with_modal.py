"""Module with custom component"""

from typing import List
import dash_mantine_components as dmc

from dash import ALL, MATCH, Input, Output, State, callback, html
 

ID_MODAL = "modal-simple"
ID_BUTTON = "modal-demo-button"
INPUT_OPEN_MODAL = Input({"type": ID_BUTTON, "identifier": MATCH}, "n_clicks")

 

def button_with_modal(btn: str, identifier: str, children: List) -> html.Div:
    """
    Creates an (button) affix to the lower right corner of the identifier to open a modal.

    Parameters:
    identifier (str): Identifier for the identifier where the button and modal will be used.
    children (List): A list of children elements to be included in the modal.

    Returns:
    html.Div
    """
    return html.Div(
        children=[
            dmc.Button(children=btn, id={"type": ID_BUTTON, "identifier": identifier}),
            add_modal(identifier, children),
        ],
    )

 

def add_modal(identifier: str, children: List):
    """
    Returns a modal component with the specified children.

    Parameters:
    identifier (str): Identifier for the identifier where the modal will be used.
    children (List): A list of children elements to be displayed inside the modal.

    Returns:
    dmc.Modal: A modal component with the given children and properties.
    """
    return dmc.Modal(
        title="Help",
        id={"type": ID_MODAL, "identifier": identifier},
        zIndex=10000,
        size="80%",
        children=children,
    )

 
@callback(
    Output({"type": ID_MODAL, "identifier": MATCH}, "opened"),
    Input({"type": ID_BUTTON, "identifier": MATCH}, "n_clicks"),
    State({"type": ID_MODAL, "identifier": ALL}, "opened"),
    prevent_initial_call=True,
)
def modal_demo(n, opened):
    """Toggles the state of the modal (open/close) based on user interactions."""
    return [not opened[0]]