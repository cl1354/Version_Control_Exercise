from flask import Blueprint, request, render_template
import requests

drink_routes = Blueprint("drink_routes", __name__)

def fetch_drinks_json():
    request_url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic"

    response = requests.get(request_url)

    parsed_response = response.json()

@drink_routes.route("/drinks")
def drinks():
    try:
        drinks = fetch_drinks_json()
        return render_template("drinks.html")
    except Exception as err:
        print('OOPS', err)
        return {"message":"Drinks Data Error. Please try again."}, 404