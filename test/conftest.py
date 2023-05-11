import pytest
from selene import browser

@pytest.fixture
def window_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture
def hold_browser(window_size):
    browser.config.hold_browser_open = True