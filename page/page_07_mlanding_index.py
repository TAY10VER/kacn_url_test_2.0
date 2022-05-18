from base.base import Base
import page


class Page_07(Base):

    # 获取明星产品 商品名称
    def page_get_star_titles(self):
        eles = self.base_find_items(page.mlanding_star_titles)
        star_titles = []
        for i in range(len(eles)):
            star_titles.append(eles[i].text)
        return star_titles

    # 获取热门充值--main 商品名称
    def page_get_hot_main_titles(self):
        eles = self.base_find_items(page.mlanding_hot_main_titles)
        hot_main_titles = []
        for i in range(len(eles)):
            hot_main_titles.append(eles[i].text)
        return hot_main_titles

    # 获取热门充值--more 商品名称
    def page_get_hot_more_titles(self):
        eles = self.base_find_items(page.mlanding_hot_more_titles)
        hot_more_titles = []
        for i in range(len(eles)):
            hot_more_titles.append(eles[i].text)
        return hot_more_titles

    # 获取代购代付 商品名称
    def page_get_buy_titles(self):
        eles = self.base_find_items(page.mlanding_buy_titles)
        buy_titles = []
        for i in range(len(eles)):
            buy_titles.append(eles[i].text)
        return buy_titles

    # 获取视频直播 商品名称
    def page_get_video_titles(self):
        eles = self.base_find_items(page.mlanding_video_titles)
        video_titles = []
        for i in range(len(eles)):
            video_titles.append(eles[i].text)
        return video_titles

    # 组合业务方法--获取m_landing index 所有商品名称
    def page_get_mlanding_goods(self):
        all_goods = []
        all_goods.append("明星产品：")
        all_goods.append(self.page_get_star_titles())
        all_goods.append("热门充值商品：")
        all_goods.append(self.page_get_hot_main_titles())
        all_goods.append(self.page_get_hot_more_titles())
        all_goods.append("代购代付商品：")
        all_goods.append(self.page_get_buy_titles())
        all_goods.append("视频直播商品：")
        all_goods.append(self.page_get_video_titles())
        return all_goods
