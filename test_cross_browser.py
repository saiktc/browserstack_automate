import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.safari.options import Options as SafariOptions

# BrowserStack credentials
browserstack_user = 'saikatchowdhury_EQobvF'
browserstack_key = 'cVdxJzcgLRkUn7xTdzFR'

# BrowserStack capabilities (using options instead of desired_capabilities)
browsers = [
    {
        'browserName': 'chrome',
        'platform': 'Windows 10',
        'browser_version': 'latest'
    },
    {
        'browserName': 'firefox',
        'platform': 'Windows 10',
        'browser_version': 'latest'
    },
    {
        'browserName': 'safari',
        'platform': 'macOS',
        'browser_version': 'latest'
    }
]

@pytest.mark.parametrize('browser_config', browsers)
def test_browserstack_login(browser_config):
    if browser_config['browserName'] == 'chrome':
        options = ChromeOptions()
        options.add_argument('--headless')  # Run Chrome in headless mode for remote testing
    elif browser_config['browserName'] == 'firefox':
        options = FirefoxOptions()
        options.headless = True  # Run Firefox in headless mode for remote testing
    elif browser_config['browserName'] == 'safari':
        options = SafariOptions()
        # Safari has limited capabilities through options, so we leave it basic
        # For headless Safari, you'll need macOS 11+ and Safari 13+.

    # Setup WebDriver for BrowserStack using remote connection
    driver = webdriver.Remote(
        command_executor=f'https://{browserstack_user}:{browserstack_key}@hub-cloud.browserstack.com/wd/hub',
        options=options
    )

    # Opening BrowserStack
    driver.get("https://www.browserstack.com")
    
    # Get the title of the page
    page_title = driver.title
    print(f"Page Title: {page_title}")

    # Assert page title to verify successful navigation
    assert "BrowserStack" in page_title

    driver.quit()

