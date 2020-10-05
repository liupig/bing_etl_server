import json
import pytest
from run_server import APP
import pkg_resources

types = ["succeed"]
cases = [
    {"path": pkg_resources.resource_filename("tests.integration_test",
                                             "/request_data/json_sort_api.json"), "code": None,
     "errorCode": None}
]


@pytest.fixture(params=cases, ids=types)
def iter_case(request):
    return request.param


@pytest.fixture
def test_client():
    client = APP.test_client()

    yield client


def test_one_api(test_client, iter_case):
    data = json.load(open(iter_case["path"], 'rb'))
    resp = test_client.post(f"/v1/bing/etl/jsonsort", json=data).data.decode()
    resp = json.loads(resp)
    assert resp is not None
