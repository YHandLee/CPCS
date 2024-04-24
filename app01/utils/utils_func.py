from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep


# 提取字符串中的连续数字
def draw_num(str_data):
    """
    :param str_data: 字符串类型
    :return: 只含数字的字符串
    """
    num_filter = filter(str.isdigit, str_data)
    num_list = list(num_filter)
    num_str = "".join(num_list)
    return num_str


# 无头浏览与规避检测
def avoid_check():
    """
    :return: 浏览器窗口
    """
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    bro = webdriver.Chrome(service=Service('./../../chromedriver.exe'), options=option)
    return bro


# 获取cookies
def get_cookies(url):
    bro = avoid_check()
    bro.get(url)
    sleep(20)
    # 滑动验证
    # 查找拖动按钮和目标位置
    # slid_btn = bro.find_element('id', value='nc_1_n1z')
    # target = bro.find_element(By.ID, 'nc_1__bg')
    # # 获取拖动按钮的位置和大小
    # slid_btn_size = slid_btn.size
    # slid_btn_loc = slid_btn.location
    # # 计算目标位置的x坐标
    # target_x = target.location['x'] - slid_btn_loc['x'] + slid_btn_size['width'] - 10
    # # 创建ActionChains对象，执行拖动操作
    # actions = ActionChains(bro)
    # actions.click_and_hold(slid_btn).move_by_offset(target_x, 0).release().perform()
    cookies = bro.get_cookies()
    return cookies


if __name__ == "__main__":
    url = 'https://login.taobao.com/member/login.jhtml'
    get_cookies(url)
