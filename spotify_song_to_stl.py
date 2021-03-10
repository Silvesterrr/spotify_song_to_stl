import time
import os
import sys
from selenium import webdriver
from pil import Image, ImageDraw
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains


def check_exists_by_xpath(xpath, driver):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def wait_till_download(file_n):
    while True:
        time.sleep(1)
        if os.path.isfile(file_n):
            time.sleep(2)
            return


def clear_folder(dir_path):
    for file in os.listdir(dir_path):
        if (file.startswith("spcode") or file.startswith('output')) and not file.startswith('spotify_code-'):
            os.remove(file)


def get_png_code(driver, url, file_name):
    driver.get("https://www.spotifycodes.com/")
    spotify_url = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div[2]/input')
    spotify_url.send_keys('')
    spotify_url.send_keys(url)

    get_code_btn = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div[2]/button')
    get_code_btn.click()
    time.sleep(2)

    open_color_men = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/div[2]/div[1]/span')
    open_color_men.click()

    bg_col = driver.find_element_by_xpath(
        '/html/body/div[2]/div[4]/div[1]/div/div[2]/div[1]/div/div/div[2]/span[1]/div/span/div')
    bg_col.click()

    bar_col = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/div[2]/div[2]/input')
    bar_col.click()
    time.sleep(0.1)

    bar_black = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/div[2]/div[2]/div/div[2]')
    bar_black.click()

    format_lst = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/div[2]/div[4]/input')
    format_lst.click()
    time.sleep(0.1)

    format_png = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/div[2]/div[4]/div/div[2]')
    format_png.click()

    download = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/div[1]/a')
    download_btn = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[1]/div/div[1]/a/button")

    while True:
        href = str(download.get_attribute('href'))
        print('slow internet meh')
        if href is not None and href != 'https://www.spotifycodes.com/#create' \
                and href != 'https://www.spotifycodes.com/' \
                and href != 'https://www.spotifycodes.com/#':
            break
    download_btn.click()
    wait_till_download(f'{os.path.dirname(os.path.realpath(__file__))}/{file_name}')


def get_transparent(driver, file_name):
    driver.get('https://onlinepngtools.com/create-transparent-png')

    input_color = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div[3]/div/div[3]/div[2]/div/div[1]/div[1]/input')
    input_color.clear()
    input_color.send_keys('black')
    precentage = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div[3]/div/div[3]/div[2]/div/div[1]/div[2]/input')
    precentage.clear()
    precentage.send_keys('100%')

    input_file = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[3]/div/div[3]/div[1]/div[1]/div/'
                                              'div[2]/div[1]/div[1]/input')
    input_file.send_keys(os.getcwd() + f"/{file_name}")
    time.sleep(2)

    save = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div[3]/div/div[3]/div[1]/div[2]/div/div[2]/div[1]/div[3]')
    save.click()

    download_transparent = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[3]/div/div[3]/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]')))
    time.sleep(0.1)
    download_transparent.click()

    wait_till_download(f'{os.path.dirname(os.path.realpath(__file__))}/output-onlinepngtools.png')


def get_stl(driver, inside_h, base_h,file_name2):
    driver.get('https://imagetostl.com/pl')
    input_file = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/div[1]/div/div/div/div/label/input')
    input_file.send_keys(os.getcwd() + f"/output-onlinepngtools.png")

    inside_height = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/form/div/div[2]/div[2]/div[2]/div[3]/div/input')
    inside_height.clear()
    inside_height.send_keys(inside_h)

    base_height = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/form/div/div[2]/div[2]/div[2]/div[5]/div/input')
    base_height.clear()
    base_height.send_keys(base_h)

    convert = driver.find_element_by_xpath('//*[@id="form0"]/div/div[3]/div[1]/input[4]')
    convert.click()

    download = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="targetFile"]')))
    download.click()

    actionchains = ActionChains(driver)
    button_xpath = '//*[@id="targetFile"]'
    button = driver.find_element_by_xpath(button_xpath)
    actionchains.move_to_element(button).click().perform()
    wait_till_download(f'{os.path.dirname(os.path.realpath(__file__))}/output-onlinepngtools.stl')
    os.rename('output-onlinepngtools.stl', file_name2)


def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im


def round_img(f_name, rad):
    im = Image.open(f_name)
    im = add_corners(im, rad)
    im.save(f_name)


def main():
    try:
        url = str(sys.argv[1])
        ins_h = str(sys.argv[2])
        base_h = str(sys.argv[3])

        track_name = url[14:]
        file_name = f"spcode-{track_name}.png"
        file_name2 = f"spotify_code-{track_name}.stl"
        dir_path = os.path.dirname(os.path.realpath(__file__))

        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--headless")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                             " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
        options.add_experimental_option("prefs", {
            "download.default_directory": dir_path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        driver = webdriver.Chrome(options=options)

        clear_folder(dir_path)
        get_png_code(driver, url, file_name)
        round_img(file_name, 70)
        get_transparent(driver, file_name)
        get_stl(driver, ins_h, base_h,file_name2)
        clear_folder(dir_path)
        print("DONE")
    finally:
        driver.close()


if __name__ == '__main__':

    main()
