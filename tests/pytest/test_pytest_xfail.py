import pytest


@pytest.mark.xfail(reason='Bag id = 123')
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason='Bag id = 124(closed)')
def test_without_bug():
    pass


@pytest.mark.xfail(reason='External Service unavailable')
def test_external_services_is_unavailable():
    assert 1 == 2