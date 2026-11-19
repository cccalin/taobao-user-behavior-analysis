"""DuckDB 连接入口。"""
from __future__ import annotations

import duckdb

from src.config import DB_FILE


def get_con(read_only: bool = True) -> duckdb.DuckDBPyConnection:
    """打开 taobao.duckdb 连接。

    - 文件不存在时抛出带提示的 FileNotFoundError;
    - 返回连接对象,调用方负责 con.close()。
    """
    if not DB_FILE.is_file():
        raise FileNotFoundError(
            f"数据库不存在:{DB_FILE}\n"
            "请先运行 01_build_database.ipynb 生成数据库,"
            "或运行 scripts/build_database.py。"
        )
    return duckdb.connect(str(DB_FILE), read_only=read_only)