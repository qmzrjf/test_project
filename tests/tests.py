from django.urls import reverse
import pytest

from uuid import uuid4
from profile_app.models import Customer


@pytest.mark.django_db
def test_index_avaiability(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
