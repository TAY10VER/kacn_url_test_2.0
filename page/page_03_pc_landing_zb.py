from base.base import Base
import page


class Page_03(Base):

    # 获取商品名称、充值类型、面值
    def page_get_dy_values(self):
        list = []
        # 获取商品名称
        dy_name = self.base_get_text(page.pc_dy_name)
        list.append("商品名称：{}".format(dy_name))
        # 获取充值类型
        dy_account_type = self.base_get_text(page.pc_goods_account_type)
        list.append("充值类型：{}".format(dy_account_type))
        # 获取面值
        pc_dy_values = self.base_get_text(page.pc_goods_values)
        list.append(pc_dy_values.replace("\n"," "))
        return list

    # 点击立即购买按钮
    def page_click_buy_btn(self):
        self.base_click(page.pc_buy_btn)

    # 组合业务方法
    def page_pc_landing_dy(self):
        # 获取商品信息
        value_list = self.page_get_dy_values()
        # 点击购买按钮
        if self.base_element_is_exist(page.pc_buy_btn):
            self.page_click_buy_btn()
            print("购买按钮存在，可正常点击")
        else:
            print("出错啦！未识别到购买按钮")
        return value_list

