from base.base import Base
import page


class Page_01(Base):

    # 获取landing所有商品名称
    def page_get_all_goods_name(self):
        list = []
        all_goods = self.base_find_items(page.landing_all_goods)
        for i in range(len(all_goods)):
            list.append(all_goods[i].text)
        return list

    # 点击landing直播商品
    def page_click_tab_zb(self):
        self.base_click(page.landing_tab_zb)

    # 点击landing代购商品
    def page_click_tab_dgdf(self):
        self.base_click(page.landing_tab_dgdf)

    # 组合业务方法
    def page_pc_landing_index(self):
        hot_goods = self.page_get_all_goods_name()
        print("热门商品个数：", len(hot_goods))
        print("热门商品：", hot_goods)

        self.page_click_tab_zb()
        zb_goods = self.page_get_all_goods_name()
        print("直播商品个数：", len(zb_goods))
        print("直播商品：", zb_goods)

        self.page_click_tab_dgdf()
        dgdf_goods = self.page_get_all_goods_name()
        print("代购代付商品个数：", len(dgdf_goods))
        print("代购代付商品：", dgdf_goods)
