import dash_mantine_components as dmc
from dash import html


from typing import Dict, List

def get_badge(genre: str):
    genre_color_mapping = {
        'MMOARPG': "gray",
        'MMORPG': "red",
        'Shooter': "pink",
        'Social':"grape",
        'ARPG':  "violet",
        'Action RPG':  "indigo",
        'Racing': "blue",
        'Card Game': "lime",
        'Battle Royale': "yellow",
        'MMO': "orange",
        'Fantasy': "grape",
        'Fighting': "pink",
        'MOBA': "yellow",
        'Strategy': "orange",
        'MMORPG': "gray",
        'Sports': "yellow"
    }
    badge = dmc.Badge(genre, variant="dot", color=genre_color_mapping.get(genre))
    return badge

def preprocess_game_options(df) -> List[Dict]:
  titles = df["title"].tolist()
  genres = df["genre"].tolist()
  options = [
        {
            "label": html.Div(
                [
                    get_badge(genre),
                    html.Div(title, style={'font-size': 12, "padding-left": "10px"}),
                    
                ],
                style={"display": "flex"}
            ), 
            "value": title
        }
        for title, genre in zip(titles, genres)
    ]
  return options


