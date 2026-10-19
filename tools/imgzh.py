"""图片标签汉化工具：按列重建底色（保留渐变/纹理），再叠加中文。

字体通过环境变量 NOTO_CJK_FONT_DIR 指定，指向 Noto Sans CJK SC 字体文件所在目录。
"""

import os
import statistics
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = os.environ.get("NOTO_CJK_FONT_DIR", "")
FONT_BOLD = os.path.join(FONT_DIR, "NotoSansCJKsc-Bold.otf") if FONT_DIR else ""
FONT_REG = os.path.join(FONT_DIR, "NotoSansCJKsc-Regular.otf") if FONT_DIR else ""


def _font_path(bold):
    path = FONT_BOLD if bold else FONT_REG
    if not path:
        raise RuntimeError(
            "未配置字体路径：请设置环境变量 NOTO_CJK_FONT_DIR，"
            "指向包含 NotoSansCJKsc-Bold.otf / NotoSansCJKsc-Regular.otf 的目录"
        )
    return path


def _is_dark(px, thr=110):
    return all(c < thr for c in px)


def erase(im, box, margin=3, probe=7):
    """按列用上下两侧的背景色重建 box 区域，保留横向/纵向渐变。"""
    x0, y0, x1, y1 = box
    px = im.load()
    W, H = im.size
    x0 = max(0, x0 - margin); y0 = max(0, y0 - margin)
    x1 = min(W - 1, x1 + margin); y1 = min(H - 1, y1 + margin)
    for x in range(x0, x1 + 1):
        samples = []
        for dy in range(1, probe + 1):
            for y in (y0 - dy, y1 + dy):
                if 0 <= y < H:
                    p = px[x, y]
                    if not _is_dark(p):
                        samples.append(p)
        if not samples:
            samples = [(255, 255, 255)]
        col = tuple(int(statistics.median([s[i] for s in samples])) for i in range(3))
        for y in range(y0, y1 + 1):
            px[x, y] = col


def put(im, box, text, size, bold=True, fg=(20, 20, 20)):
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(_font_path(bold), size)
    bb = d.textbbox((0, 0), text, font=f)
    cx = (box[0] + box[2]) / 2
    cy = (box[1] + box[3]) / 2
    d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]),
           text, font=f, fill=fg)


def apply(src, dst, jobs, margin=3):
    """jobs: [(box, text, size, bold), ...]"""
    im = Image.open(src).convert("RGB")
    for job in jobs:
        box, text, size = job[0], job[1], job[2]
        bold = job[3] if len(job) > 3 else True
        erase(im, box, margin=margin)
        put(im, box, text, size, bold=bold)
    im.save(dst)
    return im.size
