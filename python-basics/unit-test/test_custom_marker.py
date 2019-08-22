import pytest

@pytest.mark.windows
def test_windows_1():
	assert True

@pytest.mark.windows
def test_windows_2():
	assert True

@pytest.mark.mac
def test_mac_1():
	assert True

@pytest.mark.mac
def test_mac_2():
	assert True

#custom marker: pytest -m mac -v
#pytest test_custom_marker.py -m mac -v

