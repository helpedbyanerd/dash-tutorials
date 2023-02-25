from dash_extensions.enrich import DashProxy, Input, html, NoOutputTransform
import dash_mantine_components as dmc
from dash import Input, html
from dash_iconify import DashIconify


app = DashProxy(transforms=[NoOutputTransform()])


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
                                dmc.Group(
                                    [
                                        dmc.Text("ANALYTICS", weight=700, style={"fontSize": 16}),
                                        dmc.ActionIcon(
                                            DashIconify(icon="carbon:overflow-menu-horizontal"),
                                            color="gray",
                                            variant="transparent",
                                        ),
                                    ],
                                    position="apart",
                                    mt="md",
                                    mb="xs",
                                ),
                                dmc.CardSection(
                                    dmc.Image(
                                        src="https://images.unsplash.com/photo-1543286386-713bdd548da4?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80",
                                        height=480,
                                    )
                                ),
                                dmc.Group(
                                    [
                                        dmc.Text("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.", weight=400, style={"fontSize": 12}),
                                    ],
                                    position="left",
                                    mt="md",
                                    mb="xs",
                                ),
                                dmc.Button(
                                    "Update",
                                    id="update-analytics",
                                    variant="light",
                                    color="blue",
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


@app.callback(Input("update-analytics", "n_clicks"), prevent_intital_call=True)  # no Output is OK
def func(n_clicks):
    print(f"background magic happens here")


if __name__ == "__main__":
    app.run_server(debug=True)