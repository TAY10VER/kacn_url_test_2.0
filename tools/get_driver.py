from selenium import webdriver
import page

class GetDriver:
    # 1.声明变量
    driver = None
    mobile_driver = None

    # 2.获取driver方法
    @classmethod
    def get_web_driver(cls, url):
        if cls.driver is None:
            cls.option = webdriver.ChromeOptions()
            cls.option.add_argument('start-maximized')
            cls.option.add_experimental_option('excludeSwitches', ['enable-automation'])
            # cls.option.add_experimental_option("excludeSwitches", ["enable-logging"])
            cls.driver = webdriver.Chrome(options=cls.option)
            cls.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
            })
            cls.driver.get(url)
        # 返回driver
        return cls.driver

    # 3.退出driver方法
    @classmethod
    def quit_web_driver(cls):
        if cls.driver:
            # 退出操作
            cls.driver.quit()
            # 置空操作
            cls.driver = None

    @classmethod
    def get_mobile_driver(cls, mobile_url):
        cls.option = webdriver.ChromeOptions()
        width = 390
        height = 844
        PIXEL_RATIO = 3.0
        UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        mobileEmulation = {"deviceMetrics": {"width": width, "height": height, "pixelRatio": PIXEL_RATIO},"userAgent": UA}
        # mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
        cls.option.add_experimental_option('mobileEmulation', mobileEmulation)
        cls.option.add_experimental_option('excludeSwitches', ['enable-automation'])
        # cls.option.add_argument('--ignore-certificate-errors')
        # cls.option.add_experimental_option("excludeSwitches",["enable-logging"])
        cls.driver = webdriver.Chrome(options=cls.option)
        cls.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
        })

        cls.driver.get(mobile_url)
        return cls.driver

    @classmethod
    def quit_mobile_driver(cls):
        # 退出操作
        cls.mobile_driver.quit()
        # 置空操作
        cls.mobile_driver = None





