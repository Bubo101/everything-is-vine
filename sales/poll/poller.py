import os
import django
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sales_project.settings")
django.setup()

from sales_rest.models import WineVO

def get_wines():
    response = requests.get("http://winery:8000/api/wines/")
    content = json.loads(response.content)
    for wine in content["wines"]:
        WineVO.objects.update_or_create(
            id = wine["id"],
            # import_href=wine["href"],
            defaults={
                # "id": wine["id"],
                "winery_id": wine["winery"]["id"],
                "brand": wine["brand"],
                "year": wine["year"],
                "varietal": wine["varietal"],
                "description": wine["description"],
                "region": wine["region"],
                "abv": wine["abv"],
                "volume": wine["volume"],
                "city_state": wine["city_state"],
                "price": wine["price"],
                "picture_url": wine["picture_url"],
                "quantity": wine["quantity"],
                "import_href": '/wines/' + str(wine["id"]) + '/'
                },
        )

def poll():
    while True:
        print("Service poller polling for data")
        try:
            get_wines()
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(3)
if __name__ == "__main__":
    poll() 