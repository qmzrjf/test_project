from django.urls import reverse
import pytest

from uuid import uuid4
from profile_app.models import Customer


@pytest.mark.django_db
def test_user_create():
    Customer.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    assert Customer.objects.count() == 1


@pytest.mark.django_db
def test_index_avaiability(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_auth_view(auto_login_user):
    client, user = auto_login_user()
    url = reverse('signup')
    response = client.get(url)
    assert response.status_code == 200
