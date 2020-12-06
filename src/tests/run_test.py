import pytest,requests,json
def test_valid_api_health(supply_url):
    url = supply_url + "/api/Grover-de"
    resp = requests.get(url)
    assert resp.status_code == 200, resp.text

def test_invalid_store_health(supply_url):
    url = supply_url + "/api/Grover-dee"
    resp = requests.get(url)
    assert resp.status_code == 200, resp.text

