
from base.base import Base
import page


class Page_08(Base):

    # 获取商品名称、充值类型、面值
    def page_get_goods_values(self):
        list = []
        list.append("商品名称：")
        list.append(self.base_get_text(page.mlanding_goods_name))
        list.append("充值类型：")
        list.append(self.base_get_text(page.mlanding_goods_type))
        values = self.base_get_text(page.mlanding_goods_values)
        list.append("面值：")
        list.append(values.replace("\n"," "))
        return list

    # 点击购买按钮
    def page_click_buy_btn(self):
        self.base_click(page.mlanding_goods_buy_byn)

    # 组合业务方法
    def page_mlanding_dy(self):
        # 获取商品信息
        value_list = self.page_get_goods_values()
        # 点击购买按钮
        if self.base_element_is_exist(page.pc_buy_btn):
            self.page_click_buy_btn()
            print("购买按钮存在，可正常点击")
        else:
            print("出错啦！未识别到购买按钮")
        return value_list






