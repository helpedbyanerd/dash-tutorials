from dash import Dash, dcc, html, Input, Output, ALL, callback

app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.Input(id={"type": "input", "index": 0}),
        dcc.Input(id={"type": "input", "index": 1}),
        html.Div(id="output")
    ]
)

@callback(
    Output("output", "children"),
    Input({"type": "input", "index": ALL}, "value"),
    prevent_initial_call=True
)
def update_output(values):
    values = [val for val in values if val is not None]
    return f"Input values: {' '.join(values)}"

if __name__ == "__main__":
    app.run_server(debug=True)