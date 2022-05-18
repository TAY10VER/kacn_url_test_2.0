from base.base import Base
import page


class Page_02(Base):
    # 获取商品名称
    def page_get_wxdf_name(self):
        return self.base_get_text(page.pc_wxdf_name)

    # 输入面额
    def page_input_price(self, wxdf_price):
        self.base_input(page.wxdf_input, wxdf_price)

    # 点击立即充值按钮
    def page_click_buy_btn(self):
        self.base_click(page.pc_landing_buy_btn)

    # 组合业务方法
    def page_pc_landing_wxdf(self, wxdf_price):
        goods_name = self.page_get_wxdf_name()
        print("商品名称：", goods_name)
        self.page_input_price(wxdf_price)
        self.page_click_buy_btn()
        print("下载按钮存在，可正常点击")
