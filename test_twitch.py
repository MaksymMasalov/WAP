import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", {"deviceName": "Pixel 2"})
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


def test_twitch_stream_screenshot(driver):
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    # Step 1: Go to Twitch mobile site
    driver.get("https://m.twitch.tv/")

    # Step 2: Click the search icon
    search_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/search']"))
    )
    search_icon.click()

    # Step 3: Input StarCraft II
    search_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='search']"))
    )
    search_input.send_keys("StarCraft II")
    search_input.send_keys(Keys.RETURN)

    # Step 4: Scroll down 2 times
    time.sleep(2)
    for _ in range(2):
        driver.execute_script("window.scrollBy(0, window.innerHeight);")
        time.sleep(2)

    # Step 5: Select one streamer
    streamer = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[@alt='StarCraft II']"))
    )
    if streamer:
        streamer.click()

    # Handle potential modal/pop-up
    try:
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-a-target='modal-close-button']"))
        )
        close_button.click()
    except Exception as e:
        print("No modal to close")

    # Step 6: On the streamer page wait until all is loaded and take a screenshot
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//img[@class='tw-image']"))
    )
    time.sleep(5)  # Wait for the video to load completely
    driver.save_screenshot("screenshots/streamer_screenshot.png")
    assert True


if __name__ == "__main__":
    pytest.main()
