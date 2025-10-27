# python
import pytest
from payments_api import app

def test_health_endpoint():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, dict)
    assert data.get("service") == "PaymentMicroservice"
    assert data.get("status") == "running"
