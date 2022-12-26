from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
import pytest
from model_bakery import baker
from store.models import Collection, Product

@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post(path='/store/collections/', data=collection)
    return do_create_collection

@pytest.mark.django_db
class TestCreateCollection:
    #@pytest.mark.skip(reason="no way of currently testing this")
    # def test_if_user_is_anonymous_returns_401(self):
    #     # Arrange

    #     # Act
    #     client = APIClient()
    #     response = client.post('/store/collections/', {'title':'a'})

    #     # Assert
    #     assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    # old
    # def test_if_user_is_not_admin_returns_403(self, api_client, create_collection):
    #     api_client.force_authenticate(user={})
    #     response = create_collection({'title':'a'})
        
    #     assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_if_user_is_anonymous_returns_401(self, create_collection):
        response = create_collection({'title':'a'})
        
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def test_if_user_is_not_admin_returns_403(self, authenticate, create_collection):
        # Arrange
        authenticate()
        
        # Act
        response = create_collection({'title':'a'})
        
        # Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN
        
    def test_if_data_is_invalid_returns_400(self, authenticate, create_collection):
        authenticate(is_staff=True)
        
        response = create_collection({'title':''})
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None
    
    def test_if_data_is_valid_returns_201(self, authenticate, create_collection):
        authenticate(is_staff=True)

        response = create_collection({'title':'a'})
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0
        

@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_returns_200(self, api_client):
        # Arrange
        # same forienkey 
        collection = baker.make(Collection)
        #baker.make(Product, collection=collection, _quantity=10)
        
        response = api_client.get(f'/store/collections/{collection.id}/')
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,
            'title': collection.title,
            'products_count': 0
            
        }