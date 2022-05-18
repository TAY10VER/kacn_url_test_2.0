
from base.base import Base
import page


class Page_09(Base):

    # 获取商品名称
    def page_get_goods_name(self):
        return self.base_get_text(page.mlanding_goods_name)

    # 输入充值数量、代购备注
    def page_input_goods_values(self):
        self.base_input(page.mlanding_wxdf_input, "100")
        self.base_input(page.mlanding_goods_textarea, "测试")

    # 点击购买按钮
    def page_click_buy_btn(self):
        self.base_click(page.mlanding_goods_buy_byn)

    # 组合业务方法
    def page_mlanding_wxdf(self):
        # 获取商品信息
        goods_name = self.page_get_goods_name()
        print("商品名称：", goods_name)
        # 输入充值数量、代购备注
        self.page_input_goods_values()
        # 点击购买按钮
        if self.base_element_is_exist(page.pc_buy_btn):
            self.page_click_buy_btn()
            print("购买按钮存在，可正常点击")
            return True
        else:
            print("出错啦！未识别到购买按钮")
            return False






