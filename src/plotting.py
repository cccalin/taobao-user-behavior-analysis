"""Matplotlib 中文与绘图通用配置。"""
from __future__ import annotations

import matplotlib as mpl
from matplotlib import font_manager


def setup_chinese_font() -> None:
    """跨平台设置中文字体,避免中文显示为方块。

    候选顺序刻意把 SimHei 放前面:Microsoft YaHei 在部分 matplotlib
    版本下会反复报 "Failed to find font weight normal" 警告,
    SimHei 通常更干净。
    """
    candidates = [
        "SimHei",              # Windows,且无 weight 警告
        "Microsoft YaHei",     # Windows
        "PingFang SC",         # macOS
        "Heiti SC",            # macOS
        "Noto Sans CJK SC",    # Linux
        "Source Han Sans SC",  # Linux
        "WenQuanYi Zen Hei",   # Linux
    ]
    available = {f.name for f in font_manager.fontManager.ttflist}

    for name in candidates:
        if name in available:
            mpl.rcParams["font.sans-serif"] = [name]
            mpl.rcParams["font.family"] = "sans-serif"
            print(f"中文字体:{name}")
            break
    else:
        print("⚠️ 未找到可用中文字体,图中中文可能显示为方块。")

    mpl.rcParams["axes.unicode_minus"] = False