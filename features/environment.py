from selenium import webdriver
import os

def before_scenario(context, scenario):
    browser = context.config.userdata.get("browser", "chrome").lower()
    if browser == "firefox":
        context.driver = webdriver.Firefox()
    else:
        context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def after_step(context, step):
    if step.status == "failed":
        screenshot_dir = "features/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        file_name = f"{step.name.replace(' ', '_')}.png"
        path = os.path.join(screenshot_dir, file_name)
        context.driver.save_screenshot(path)

def after_scenario(context, scenario):
    context.driver.quit()
