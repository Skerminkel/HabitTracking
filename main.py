import requests
import os
from dotenv import load_dotenv as lenv
import datetime

lenv("C:/env/.env.txt")
TOKEN = os.getenv("api_key_pixela")
USERNAME = "skerminkel"

ENDPOINT_PIXELA = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

parameters = {
    "token": TOKEN,
    "username": "skerminkel",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=endpoint_pixela, json=parameters)
# response.raise_for_status()
# print(response.text)


def create_graph(id="code", name="HoursOfCode", unit="hours", type="float", color="shibafu"):

    endpoint_graph = f"{ENDPOINT_PIXELA}/{USERNAME}/graphs"

    graph_params = {
        "id": id,
        "name": name,
        "unit": unit,
        "type": type,
        "color": color
    }

    create_graph = requests.post(url=endpoint_graph, json=graph_params, headers=headers)
    print(create_graph.text)


def update_pixel(quantity: str, delete: bool = False, date=None):

    pixel_params = {
        "date": date,
        "quantity": quantity
    }

    if not delete:
        if date is None:
            today = datetime.datetime.today().date()
            today_date = today.strftime('%Y%m%d')
            pixel_params["date"] = today_date

        pixel_url = f"{ENDPOINT_PIXELA}/{USERNAME}/graphs/code"
        post_pixel = requests.post(url=pixel_url, json=pixel_params, headers=headers)
        print(post_pixel.text)

    def delete_pixel(date_del):

        delete_pixel = requests.delete(url=f"{pixel_url}/{date_del}", headers=headers)
        print(delete_pixel.text)

    if delete:
        delete_pixel(date)


update_pixel("2.5", False)
