import pytest

# para que corra una sola vez, al inicio y final del test colocamos scope="class"
@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")


# Para definirlo como un fixture
@pytest.fixture()
def data_load():
    print("user profile data is being created")
    return ["Moises", "Pire", "rahulshettyacademy.com"]

@pytest.fixture(params=[("Chrome", "Moi", "Pire"),("Firefox", "Mou"),("IE","SS")])
def cross_Browser(request):
    return request.param