
from dash.exceptions import PreventUpdate
from dash import Dash, Input, html, Output, Input

import dash_mantine_components as dmc


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
        html.Div(
            [
                html.Div(
                    [
                        dmc.Card(
                            children=[
                                dmc.CardSection(
                                    dmc.Image(
                                        id="card-img",
                                        src="https://images.unsplash.com/photo-1543286386-713bdd548da4?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80",
                                        height=480,
                                    )
                                ),
                                dmc.Group(
                                    [
                                        dmc.Text("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt "
                                                 "ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. "
                                                 "Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.", weight=400, style={"fontSize": 12}),
                                    ],
                                    position="left",
                                    mt="md",
                                    mb="xs",
                                ),
                                dmc.Button(
                                    "Select Image 1",
                                    id="change-to-img-1",
                                    variant="light",
                                    color="blue",
                                    fullWidth=True,
                                    mt="md",
                                    radius="md",
                                ),
                                dmc.Button(
                                    "Select Image 1",
                                    id="change-to-img-2",
                                    variant="light",
                                    color="red",
                                    fullWidth=True,
                                    mt="md",
                                    radius="md",
                                ),
                            ],
                            withBorder=True,
                            shadow="sm",
                            radius="md",
                            style={"width": 960, "margin": "32px auto"}
                        ),
                    ],
                )
            ],
            style={"height": "100vh", "width": "100vw"}
        )
    ],
)


@app.callback(
    Output('card-img', 'src', allow_duplicate=True),
    Input('change-to-img-1', 'n_clicks'),
    prevent_initial_call=True
)
def change_to_img_1(n_clicks):
    if not n_clicks:
        raise PreventUpdate()
    return "https://images.unsplash.com/photo-1605379399642-870262d3d051?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1806&q=80"

@app.callback(
    Output('card-img', 'src'),
    Input('change-to-img-2', 'n_clicks'),
)
def change_to_img_2(n_clicks):
    if not n_clicks:
        raise PreventUpdate()
    return "https://images.unsplash.com/photo-1564865878688-9a244444042a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80"



if __name__ == "__main__":
    app.run_server(debug=True)