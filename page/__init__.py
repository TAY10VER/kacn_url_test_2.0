from selenium.webdriver.common.by import By


"""测试账号"""
username = "ad_url_test@kacn.com"
pwd = "111111"


"""page01: pc landing index涉及元素 配置信息"""
# 直播商品
landing_tab_zb = (By.XPATH, "//div[@class='m_landTabRoom']")
# 代购代付商品
landing_tab_dgdf = (By.XPATH, "//div[@class='m_landTabBuy']")
# 所有商品名称
landing_all_goods = (By.XPATH, "//div[@class='landing_sp_bt']/p[1]")
# 所有商品href
landing_goods_hrefs = (By.XPATH, "//div[@class='landing_list']/a")
# 充值类型
landing_goods_type = (By.XPATH, "//div[contains(@id,'show_mode')]")

"""page_02:pc landing 支付宝代付页面涉及元素 配置信息"""
# 商品名称
pc_wxdf_name = (By.XPATH, "//div[@id='tubiao_wxdf']/div/p[1]")
# 充值类型
pc_landing_czlx = (By.XPATH, "//div[@id='show_mode1']")
# 金额输入框
wxdf_input = (By.ID, "other")
# 立即充值按钮
pc_landing_buy_btn = (By.ID, "BuyButton")

"""page_03:pc landing抖音商品页面涉及元素 配置信息"""
# 商品名称
pc_dy_name = (By.XPATH, "//div[@id='tubiao_dy']/div/p[1]")
# 充值类型
pc_goods_account_type = (By.XPATH, "//div[@id='show_mode1']")
# 全部面值
pc_goods_values = (By.ID, "show1")

"""page_04:pc landing苹果商品涉及元素 配置信息"""
# 商品名称
pc_pg_name = (By.XPATH, "//div[@id='tubiao_pg']/div/p[1]")
# 账号所属地区
pc_pg_show_mode = (By.XPATH, "//div[contains(@id,'show_mode')]")
# 中国区代充
pc_apple_china = (By.XPATH, "//div[@id='show_mode1']")
# 100面值
pc_apple_value = (By.XPATH, "//li[@id='show1']/div[2]")
# 所有面值
pc_apple_random_value = (By.XPATH, "//li[@id='show1']/div")
# 数量
pc_apple_num = (By.XPATH, "//input[@id='num']")
# 立即购买按钮
pc_buy_btn = (By.ID, "BuyButton")

"""page_05:pc 国际服商品页面涉及元素 配置信息"""
# 商品名称
pc_guojifu_names = (By.XPATH, "//div[@class='landing_sp_bt']/p[1]")
# 所有商品href
pc_guojifu_hrefs = (By.XPATH, "//div[@class='landing_list']/a")
# 充值类型
pc_guojifu_types = (By.XPATH, "//div[contains(@id,'show_mode')]")

"""page_06:pc 手游专题页面涉及元素 配置信息"""
# 过滤器A-Z
pc_mobile_game_filter = (By.XPATH, "//dl[@class='game_dl js_gameName']/dd")

"""page_07: mobile landing index页涉及元素 配置信息"""
# 明星商品--商品名称
mlanding_star_titles = (By.XPATH, "//p[@class='star_textTitle']")
# 明星商品--商品url
mlanding_star_hrefs = (By.XPATH, "//a[@class='star_content']")
# 热门充值--main--商品名称
mlanding_hot_main_titles = (By.XPATH, "//a[@class='hot_goodsMain']/p")
# 热门充值--main--商品url
mlanding_hot_main_hrefs = (By.XPATH, "//a[@class='hot_goodsMain']")
# 热门充值——more--商品名称
mlanding_hot_more_titles = (By.XPATH, "//div[@class='hot_goodsMoreText']/span")
# 热门充值——more--商品url
mlanding_hot_more_hrefs = (By.XPATH, "//a[@class='hot_goodsMoreContent']")
# 代购代付--商品名称
mlanding_buy_titles = (By.XPATH, "//div[@class='buy_goodsBox']/div/a/p")
# 代购代付--商品url
mlanding_buy_hrefs = (By.XPATH, "//a[@class='buy_goodsContent']")
# 视频直播--商品名称
mlanding_video_titles = (By.XPATH, "//div[@class='video_goodsBox']/a/p")
# 视频直播--商品url
mlanding_video_hrefs = (By.XPATH, "//a[@class='video_content']")

"""page_08: mobile landing 抖音商品涉及元素 配置信息"""
# 商品名称 -- mlanding抖音、微信代付、苹果共用
mlanding_goods_name = (By.XPATH, "//p[@class='newLanding_goodsTitle']")
# 充值类型
mlanding_goods_type = (By.XPATH, "//li[@id='show_mode1']/span")
# 充值面额
mlanding_goods_values = (By.XPATH, "//ul[@id='show1']")
# 购买按钮
mlanding_goods_buy_byn = (By.ID, "BuyButton")

"""page_09: mobile landing 微信代付商品涉及元素 配置信息"""
# 充值数量输入框
mlanding_wxdf_input = (By.ID, "other")
# 代购备注输入框
mlanding_goods_textarea = (By.NAME, "newLanding_dgTextarea")

"""page_10: mobile landing 苹果商品涉及元素 配置信息"""
# 账号所属地区
mlanding_pg_show_mode = (By.XPATH, "//li[contains(@id,'show_mode')]")

"""page_11: mobile 国际服涉及元素 配置信息"""
# 商品名称
m_guojifu_goods_names = (By.XPATH, "//dd[@class='newLanding_itemDd']")
# 所有商品href
m_guojifu_goods_hrefs = (By.XPATH, "//div[@class='newLanding_tabItem']/a")
# 充值类型
m_guojifu_goods_types = (By.XPATH, "//li[contains(@id,'show_mode')]")

"""page_12:mobile 手游专题页涉及元素 配置信息"""
m_mobile_game_all_goods = (By.XPATH, "//dd[@class='newLanding_itemDd']")

