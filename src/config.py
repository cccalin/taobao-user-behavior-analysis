"""项目路径与常量配置(单一事实来源)。

所有 notebook 和脚本都从这里导入路径,禁止再手写 "../data/..."。
"""
from pathlib import Path

# __file__ 是 src/config.py,parent 是 src,parent.parent 是仓库根
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = Path(r"C:/Users/Eli'ce/taobao-user-behavior-analysis/data")

RAW_FILE = DATA_DIR / "raw" / "UserBehavior.csv"
DB_FILE = DATA_DIR / "database" / "taobao.duckdb"
PROCESSED_DIR = DATA_DIR / "processed"
TEMP_DIR = DATA_DIR / "temp"

FIGURE_DIR = PROJECT_ROOT / "outputs" / "figures"
DOCS_DIR = PROJECT_ROOT / "docs"

# 时间窗口(UTC+8 秒级):含 2017-11-25 00:00,不含 2017-12-04 00:00
WINDOW_START = 1511539200
WINDOW_END = 1512316800