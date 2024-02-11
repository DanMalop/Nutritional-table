from models import Product, Table_vertical_standar, Ingredient
from services import API_service
import flet as ft
from view import Nutri_table

formula = [["turmeric", 0.3], ["broccoli", 0.7],]

API_KEY = "2928ddbc61d24951b20a43dc2db7a8bb"
# you can get an test api key if you sign up on https://spoonacular.com/food-api/ 
URL_API = "https://api.spoonacular.com/food/ingredients/"

route = lambda id: f'{id}/information'
spoonacular_api = API_service(url_api=URL_API, 
                              route=route, 
                              needed_params= {'apiKey': API_KEY})



#vegetables_mix = Product("vegetable mix", formula, 10, 250)
#vegetables_mix.create_ingredients_list(spoonacular_api)
#vegetables_mix.added_sugar("sucralosa", 0.05)
#vegetables_mix.generate_all_data()
#print(vegetables_mix.get_nutritional_std_data()['Calories'])

#table = Table_vertical_standar(vegetables_mix,".\\", "B2", 10)
#table.create_table()


def main(page: ft.Page):
    page.title = "Nutri Table"
    page.horizontal_alignment = "left"
    page.scroll = "adaptative"
    page.update()

    app = Nutri_table()

    page.add(app)

ft.app(target=main)