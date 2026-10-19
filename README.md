# Agentic Large Language Models — 中文翻译

《Agentic Large Language Models》（[arXiv:2610.13455](https://arxiv.org/abs/2610.13455)，Leiden University）的中文 LaTeX 翻译项目。在原书 LaTeX 源文件基础上翻译，保持原排版：公式、图表、交叉引用、超链接、目录与书签均按原样保留，部分图片内的英文标签另行汉化。

> 本仓库仅供学习交流使用。原书版权归原作者所有，如需引用请引用原论文。

## 获取成品 PDF

编译好的中文版 PDF 可在 [Releases](../../releases) 页面下载，无需自行编译。

## 目录结构

| 目录 | 用途 |
|---|---|
| `src/` | LaTeX 中文翻译源文件 |
| `assets/` | 汉化后的图片资源 |
| `config/` | 术语表与翻译风格约定 |
| `tools/` | 翻译辅助脚本（图片汉化需设置 `NOTO_CJK_FONT_DIR` 环境变量指向 Noto Sans CJK SC 字体目录；中文校验、英文扫描） |

## 本地编译

依赖 MiKTeX（XeLaTeX），中文排版由 `ctex` 宏包提供，字体使用系统字体，无需额外安装。`minted` 代码高亮需要 `pygmentize`（见 `requirements.txt`）。

```bash
cd src
xelatex -shell-escape -interaction=nonstopmode agenticbook.tex
```

## 翻译约定

术语对照见 `config/glossary.md`，翻译风格约定见 `config/translation-style.md`。

## License

原书内容版权归原作者所有（arXiv.org perpetual, non-exclusive license 1.0）；本仓库的译文与汉化图片以 CC BY-NC-SA 4.0 授权。详见 [LICENSE.md](LICENSE.md)。

