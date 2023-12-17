from dash import Dash, dcc, html, Input, Output, MATCH, callback

app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.Input(id={"type": "input", "index": 0}),
        dcc.Input(id={"type": "input", "index": 1}),
        html.Div(id={"type": "output", "index": 0}),
        html.Div(id={"type": "output", "index": 1}),
    ]
)

@callback(
    Output({"type": "output", "index": MATCH}, "children"),
    Input({"type": "input", "index": MATCH}, "value"),
    prevent_initial_call=True
)
def update_output(values):
    return f"Input values: {values}"

if __name__ == "__main__":
    app.run_server(debug=True)