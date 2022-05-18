from base.base import Base
import page


class Page_12(Base):

    # 获取手游专题页所有商品名称
    def page_get_all_goods(self):
        list = []
        all_goods = self.base_find_items(page.m_mobile_game_all_goods)
        print("商品个数：", len(all_goods))
        for i in range(len(all_goods)):
            list.append(all_goods[i].text)
        return list


