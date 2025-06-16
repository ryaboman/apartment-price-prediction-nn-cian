import requests

flat_me = [
    {
        'total_area': 63,
        'house_age': 2024-1985,
        'floors_total': 9,
        'rooms': 3,
        'gas_supply': 'Центральное',
        'passenger_elevator': 1,
        'region': 'Приокский',
        'ref_liv_kitch': 3.6,
        'ref_area': 11,
        'renovation': 'Евроремонт',
        'floor': 7,
        'type_of_building': 'Панельный',
        'logie': 1,
        'balcony': 1,
        'number_of_bathrooms': 1,
        'studio': 0,
        'service_elevator': 0
    },
    {
        'total_area': 63,
        'house_age': 2024-1985,
        'floors_total': 9,
        'rooms': 3,
        'gas_supply': 'Центральное',
        'passenger_elevator': 1,
        'region': 'Приокский',
        'ref_liv_kitch': 3.6,
        'ref_area': 11,
        'renovation': 'Евроремонт',
        'floor': 7,
        'type_of_building': 'Панельный',
        'logie': 1,
        'balcony': 1,
        'number_of_bathrooms': 1,
        'studio': 0,
        'service_elevator': 0
    }
]

BASE = "http://localhost:5000"

response = requests.post(BASE + "/predict", json=flat_me)

print(response.json())
