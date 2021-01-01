from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

name = "tuple"

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://jp.finalfantasyxiv.com/lodestone/character/23240790/")

character_detail = browser.find_element_by_class_name("character__profile__data")
character_detail.screenshot(f"screenshots/{name}.png")


# for index, search_result in enumerate(search_results):
#     class_name = search_result.get_attribute("class")
#     if "kno-kp mnr-c g-blk" not in class_name:
#         search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")

# browser.quit()