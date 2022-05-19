# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# you can run any specific file with py.test <filename>
# you can mark(tags) tests @pytest.mark.smoke and then run with -m
# you can skip test with @pytest.mark.skip
# fixtures are used as setup and tear down methods for tests cases -conftest file to
# generalize fixture and make it available to all tests cases
# Data Driven and parametrization can be done with return statement in tuple format
# When you define a fixture scope to class only, it will be run once before class is initiated and at the end
import pytest


@pytest.mark.smoke
def test_first_program(setup):
    print("Hello")

@pytest.mark.xfail
def test_Greet():
    print("Good Morning")


def test_Cross_Browser(cross_Browser):
    print(cross_Browser[1])
