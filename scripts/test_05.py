from page.page_05_pc_guojifu import Page_05
from tools.get_driver import GetDriver
from tools.read_txt import read_txt
import page
from time import sleep


def get_url():
    arrs = []
    for data in read_txt("pc_urls.txt"):
        arrs.append(data.strip())
    return arrs[7]


class Test_05():
    # 初始化
    def setup_class(self):
        url = get_url()
        self.driver = GetDriver().get_web_driver(url)
        self.pc_guojifu = Page_05(self.driver)

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver().quit_web_driver()

    def test_pc_guojifu(self):
        """测试pc 国际服"""

        # 判断页面是否跳转
        url = get_url()
        print("测试URL：", url)
        if url == self.driver.current_url:
            print("页面未发生跳转")
        else:
            print("页面发生跳转，跳转后的页面：{}".format(self.driver.current_url))
        # 断言url，如果发生跳转，不继续执行
        assert url == self.driver.current_url

        # 断言 cookie_T
        cookie_T = self.driver.get_cookie("t").get("value")
        print("预期T值：30，实际T值:{}".format(cookie_T))
        assert '30' == cookie_T

        # 获取所有商品名称
        goods_names = self.pc_guojifu.page_get_all_goods_name()
        print("所有商品：", goods_names)

        # 获取所有商品链接
        links = self.pc_guojifu.page_get_all_links()
        # 循环访问所有链接，获取页面元素
        for link in links:
            goods_value = []
            self.driver.get(link)
            sleep(3)
            goods_value.append(goods_names[links.index(link)])
            goods_value.append(self.pc_guojifu.page_get_goods_values_list(self.driver))
            print(goods_value)

