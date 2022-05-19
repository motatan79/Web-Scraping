import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixture_demo(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixture_demo2(self):
        print("I will execute steps in fixtureDemo method2")

    def test_fixture_demo3(self):
        print("I will execute steps in fixtureDemo method3")

    def test_fixture_demo4(self):
        print("I will execute steps in fixtureDemo method4")