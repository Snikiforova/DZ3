import pytest
import requests

def test_california_breweries_status_code():
    response = requests.get('https://api.openbrewerydb.org/breweries?by_state=California')
    assert response.status_code == 200


@pytest.mark.parametrize("city_name, brewery_type", [("Portland", "micro"), ("Portland", "regional")])
def test_portland_breweries_by_type(city_name, brewery_type):
    response = requests.get(f'https://api.openbrewerydb.org/breweries?by_city={city_name}&by_type={brewery_type}')
    assert response.status_code == 200


@pytest.mark.parametrize("state_name", [("New York"), ("Texas"), ("Oregon")])
def test_all_breweries_by_state(state_name):
    response = requests.get(f'https://api.openbrewerydb.org/breweries?by_state={state_name}')
    assert response.status_code == 200


i

def test_breweries_by_coordinates():
    lat = 40.730610
    long = -73.935242
    response = requests.get(f'https://api.openbrewerydb.org/breweries?by_dist={lat},{long}')
    assert response.status_code == 200