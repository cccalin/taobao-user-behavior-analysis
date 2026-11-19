"""行为类型相关常量。"""
BEHAVIOR_TYPES = ("pv", "cart", "fav", "buy")
BEHAVIOR_LABELS = {
    "pv": "浏览",
    "cart": "加购",
    "fav": "收藏",
    "buy": "购买",
}
# 用于 SQL 里统一排序
BEHAVIOR_ORDER_SQL = (
    "CASE behavior_type "
    "WHEN 'pv' THEN 1 WHEN 'cart' THEN 2 "
    "WHEN 'fav' THEN 3 WHEN 'buy' THEN 4 END"
)