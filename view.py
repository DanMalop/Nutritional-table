import flet as ft
from models import (Product,
                    Table_vertical_standar,
                    Table_simplified,
                    Table_tubular_linear)
from flet import (
    Checkbox,
    Column,
    FloatingActionButton,
    IconButton,
    OutlinedButton,
    Page,
    Row,
    Tab,
    Tabs,
    Text,
    TextField,
    UserControl,
    colors,
    icons,
) 

class Nutri_table(UserControl):
    def build(self):

        return Column(
            width=600,
            controls=[
                 Row([Text(value="Todos", style="headlineMedium")], alignment="center"),
                 Row([Text(value="Todos", style="headlineMedium")], alignment="center"),
                 Row([Text(value="Todos", style="headlineMedium")], alignment="center"),

                Column(
                    width=300,
                    controls=[
                        Row([Text(value="eeeoooo", style="headlineMedium")], alignment="center"),
                        Row([Text(value="oooaaa", style="headlineMedium")], alignment="center"),
                        Row([Text(value="iiiiiiuuuuu", style="headlineMedium")], alignment="center",),
                    ],
                ), 

                Column(
                    width=700,
                    controls=[
                        Row([Text(value="eeeoooo", style="headlineMedium")], alignment="center"),
                        Row([Text(value="oooaaa", style="headlineMedium")], alignment="center"),
                        Row([Text(value="iiiiiiuuuuu", style="headlineMedium")], alignment="center",),
                    ],
                ),
        
            ],
        )