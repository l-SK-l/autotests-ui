import pytest


@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Sending the data to the analytics service")


@pytest.fixture(scope='session')
def settings():
    print("[SESSION] Initializing the autotest settings")


@pytest.fixture(scope='class')
def user():
    print("[CLASS] Creating user data once per test class")


@pytest.fixture(scope='function')
def browser():
    print("[FUNCTION] We open the browser for each autotest")


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        pass

    def test_user_can_create_course(self, settings, user, browser):
        pass


class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        pass