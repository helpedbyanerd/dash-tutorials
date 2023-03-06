from dash import Dash, html, dcc, Input, Output, callback
import dash_mantine_components as dmc

from data import get_game_options

app = Dash(__name__)


app.layout = dmc.MantineProvider(
    id="app",
    theme={
        "fontFamily": "'Inter', sans-serif",
        "primaryColor": "indigo",
        "theme": "dark"
    },
    inherit=True,
    withGlobalStyles=True,
    withNormalizeCSS=True,
    children=[
        html.Div(id="dummy-div"),
        dmc.Container(children=[
                dmc.Title("Dash Core Components Dropdown With Badges", order=3),
                dcc.Dropdown(
                    id="dropdown-with-icons",
                ),
            ],
            style={"paddingTop": "90px"}
        ),
    ],
)


@callback(
    Output("dropdown-with-icons", "options"),
    Input("dummy-div", "n_clicks")
)
def load_options(n):
    options = get_game_options()
    return options


if __name__ == "__main__":
    app.run_server(debug=True)