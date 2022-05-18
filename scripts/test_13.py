from tools.get_driver import GetDriver
from tools.read_txt import read_txt


def get_url():
    arrs = []
    for data in read_txt("m_urls.txt"):
        arrs.append(data.strip())
    return arrs[8]

class Test_13():
    # 初始化
    def setup_class(self):
        url = get_url()
        self.driver = GetDriver().get_mobile_driver(url)

    # 结束
    def teardown_class(self):
        # 关闭driver
        self.driver.quit()

    def test_m_kacn_com(self):
        """测试URL: https://m.ka-cn.com"""

        url = get_url()
        print("测试URL：", url)

        # 判断页面是否跳转
        if url == self.driver.current_url:
            print("页面未发生跳转")
        else:
            print("页面发生跳转，跳转后的页面：{}".format(self.driver.current_url))

        assert "https://www.ka-cn.com/mobile/" == str(self.driver.current_url)