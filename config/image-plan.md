# 图片汉化方案

## 分类框架

全书 131 个图片资源（`figures/` 103、`part1/visuals/` 24、`part6/visuals/` 4）。按「是否含可译英文」分四类：

| 类型 | 特征 | 处理策略 | 工作量 |
|---|---|---|---|
| ① 无文字 | 纯图形/数学符号（如 RNN/LSTM 展开图） | **不动** | 0 |
| ② 简单标签 | 少量英文单词（≤6 个） | 遮盖原文字 + 叠加中文（保持字体/位置） | 小 |
| ③ 复杂示意图 | 多标签框图、坐标轴图表 | 逐图重绘（优先用源码重生成） | 中–大 |
| ④ 第三方截图 | 论文页、网页/终端截图 | **建议保留原样**（版权 + 外部内容） | — |
| ⑤ tikz 源码 | `figures/*.tex`、`tikz/*.tex` | 直接改源码里的 `\node{...}` 文字 | 极小 |

## 样章（part1/02_lang.tex）图片清单

| # | 文件 | 内容 | 分类 | 处理 |
|---|---|---|---|---|
| 1 | `part1/visuals/ELIZA_conversation.jpg` | ELIZA 终端对话，全英文 | ④ | 保留原样 |
| 2 | `part1/visuals/nlp_pipeline.pdf` | ACL 2014 CoreNLP 论文**整页** | ④ | 保留原样 |
| 3 | `part1/visuals/Word_vector_illustration.jpg` | word2vec 向量算术，标签 King/Man/Queen/Woman | ② | 4 标签替换 |
| 4 | `figures/rl.tex`（tikz，`\input`） | 强化学习示意图 | ⑤ | 改源码 |
| 5 | `part1/visuals/skipgram.png` | skip-gram，标签 the/man/his/son/loves | ② | 5 标签替换 |
| 6 | `part1/visuals/cbow.png` | CBOW，标签 loves/the/man/his/son | ② | 5 标签替换 |
| 7 | `figures/RNNcolah.png` | RNN 展开图，仅数学符号 | ① | 不动 |
| 8 | `figures/LSTMcolah.png` | LSTM 模块，仅数学符号 | ① | 不动 |
| 9 | `figures/encdec.png` | Encoder-Decoder，标签 Input text/Encoder/Decoder/Translated text | ② | 4 标签替换 |
| 10 | `part1/visuals/enc_dec.png` | BLEU 曲线，轴标签 + 图例 | ③ | 需重绘 |
| 11 | `part1/visuals/transformer_full_architecture.png` | Transformer 架构图，10+ 英文标签 | ③ | 需重绘 |

## 已确认决策（2026-10-14）

1. ②类简单标签图：**汉化标签**
2. 图内英文示例词（the/man/his/son/loves、King/Queen）：**保留英文**
3. `nlp_pipeline.pdf`（ACL 论文整页）：**保留原样**

## 样章（part1/02_lang.tex）实际需处理清单

按上述决策收敛后，**11 张图里只有 3 张 + 1 个 tikz 需要动手**：

| # | 文件 | 分类 | 处理 | 工作量 |
|---|---|---|---|---|
| 1 | `part1/visuals/ELIZA_conversation.jpg` | ④ | 保留原样 | 0 |
| 2 | `part1/visuals/nlp_pipeline.pdf` | ④ | 保留原样 | 0 |
| 3 | `part1/visuals/Word_vector_illustration.jpg` | ② | **无需改动**（King/Man/Queen/Woman 均为示例词） | 0 |
| 4 | `figures/rl.tex`（tikz） | ⑤ | 改源码中的文字节点 | 极小 |
| 5 | `part1/visuals/skipgram.png` | ② | **无需改动**（the/man/his/son/loves 均为示例词） | 0 |
| 6 | `part1/visuals/cbow.png` | ② | **无需改动**（同上） | 0 |
| 7 | `figures/RNNcolah.png` | ① | 不动 | 0 |
| 8 | `figures/LSTMcolah.png` | ① | 不动 | 0 |
| 9 | `figures/encdec.png` | ② | **需汉化**：Input text / Encoder / Decoder / Translated text | 小 |
| 10 | `part1/visuals/enc_dec.png` | ③ | 需汉化坐标轴：BLEU score / Sentence length / 图例 | 中 |
| 11 | `part1/visuals/transformer_full_architecture.png` | ③ | 需汉化 10+ 标签 | 中–大 |

**结论**：示例词保留英文这一条，直接省掉了 3 张图的处理。真正需要动手的是 `encdec.png`、`enc_dec.png`、`transformer_full_architecture.png` 三张位图 + 一个 tikz 文件。

## 待定问题（已解决）

1. ~~③类位图的处理方式~~ → **已定：遮盖 + 叠字**（保留原构图，覆盖英文标签后叠加中文）。理由：构图零偏差、工作量可控。
2. ~~需要图像处理能力~~ → **已解决**：`work` 环境已装 Pillow 12.3.0（注意 conda 的 pillow **不带 numpy**，脚本须用纯 Pillow 的 `point()` + `getbbox()`）。
3. ~~③类是否全部处理~~ → **已定（2026-10-15，用户选择方案 1「分级处理」）**：只汉化「纯标注型」图；论文截图、复杂多面板图、照片一律保留原样。

## 最终分级策略（2026-10-15 用户确认）

| 级别 | 判定标准 | 处理 | 估计数量 |
|---|---|---|---|
| **T1 汉化** | 白底线框图/流程图，英文标签独立且可安全遮盖替换（不切断图形线条） | 遮盖 + 叠中文 | 约 50–60 |
| **T2 保留** | 多面板实验图、坐标轴密集图表、UI/终端/论文页截图、表格截图 | 原样保留 | 约 25–30 |
| **T3 保留** | 照片、AI 生成图像（DALL·E / Stable Diffusion 输出）、游戏画面 | 原样保留 | 约 10 |
| **⑤ tikz** | `figures/*.tex` 源码 | 直接改 `\node{}` 文字 | 14（已做 9） |

## 位图盘点（`src/figures/` 共 99 张，含扩展名）

按颜色特征自动初筛（颜色数 / 白底占比）后，**T1 候选**（白底为主、颜色数低，多为框图）：

`rl.png`、`webdreamer.png`、`worldcoder.png`、`worldgpt.png`、`mctssteps.png`、`cartpole.png`、
`assistant.png`、`balrog.png`、`balrogarch.png`、`vlm.png`、`zero.png`、`tot.png`、`tot-ex.png`、
`reflexion3.png`、`reflexion-code.png`、`assist.png`、`pddl.png`、`evolutionary1.png`、`agent.png`、
`struct.png`、`stable.png`、`bot.png`、`react.png`、`least.png`、`chateval.png`、`radar.png`、
`selfref.png`、`selfrefine2.png`、`webrl.png`、`sc.png`、`cliport1.png`、`cliport2.png`、
`metaharness.png`、`progressive.png`、`cot-tot.png`、`cot.jpg`、`shepherd.png`、`rainbow.png`、
`rainbow2.png`、`madaan.png`、`pal.png`、`sokoban.png`、`totcode.png`、`agentverse.png`、
`oasis.png`、`som.png`、`MI-concepts.png`、`alpha.png`、`webarena.png`、`mobility.png`、
`abm.png`、`inner.png`、`magma.png`、`rt2.png`、`tombench.png`、`swe.png`、`maoverview.png`、
`flava.png`、`stepbystep.png`、`saycan.png`、`egosocialarena.png`、`medco.png`、`pizero.png`、
`oh2017core.png`、`virtuous.png`、`virtuous2.png`、`virtuous3.png`、`virtuous5.png`、
`virtuous6.png`、`virtuouscover.png`、`virtuouscover2.png`、`Virtuouscover.jpg`、
`llmcoordinationbank.jpg`、`sotopia.jpg`

**T3 明确保留**（照片 / AI 生成图 / 游戏画面）：
`dalle.png`、`dalle.jpg`、`dalle3.png`、`stablediff.png`、`VQAbanana.png`、`captioning.png`、
`alfworld.png`、`vlas.jpg`、`vla.jpg`、`agent-smith.jpeg`、`ChatGPT_Image_Jun_7...jpg`、
`water.png`、`simulacra1.png`、`simulacra2.png`、`lmnav.png`、`chatdev1.jpg`、`chatdev2.jpg`

**① 无文字，不动**：`RNNcolah.png`、`LSTMcolah.png`（仅数学符号）

> 注：上表 T1 候选为**自动初筛结果**，每张图动手前仍需**人工目视确认**：若标签与图形线条/曲线重叠，则降级为 T2 保留（避免切断线条——第 2 章曾把绿虚线、黄虚线切断，需重新测量避让）。

## 已完成的图片汉化

| 图 | 处理 |
|---|---|
| `part1/visuals/encdec.png` | Input text/Encoder/Decoder/Translated text → 输入文本/编码器/解码器/译文文本 |
| `part1/visuals/enc_dec.png` | BLEU score/Sentence length → BLEU 分数/句子长度 |
| `part1/visuals/transformer_full_architecture.png` | 15 个标签全部汉化 |
| `figures/rl.tex` + `rl-llm` / `rl-llm2` / `rl2` / `rlA`–`rlE`（tikz） | 节点文字汉化 |
| `figures/assistant.png`（第 13 章） | User Input/LLM Agent/Tools/Memory/Planning → 用户输入/LLM 智能体/工具/记忆/规划 |
| `figures/chateval.png`（第 16 章） | 摘要者、共 N 轮 ×3、(a) 逐一发言、(b) 同时发言、(c) 同时发言 + 摘要者 |
| `figures/chatdev2.jpg`（第 16 章） | 阶段/子任务/指导者/对话链/助手/设计/编码/测试/程序员/审查者/测试员 |
| `figures/MI-concepts.png`（第 21 章） | Behavioral/Attributional/Concept-based/Mechanistic/probe → 行为式/归因式/基于概念/机制式/探针 |
| `figures/virtuouscover2.png`（封面循环图） | acting/reasoning/interacting → 行动/推理/交互 |
| `figures/virtuous5.png`（第 1 章） | 12 个色框标签 + 3 处 new data → 自我反思/多步/检索/推理/世界模型、VLA/社会能力/交互/行动/机器人、工具/基于角色的交互/开放社会/助手/新数据 |
| `figures/alpha.png`（第 11 章） | Single LLM/Instruction/Tools/Planner/Caller/Summarizer/Guidance & control/Feedback → 单一 LLM/指令/工具/规划器/调用器/摘要器/引导与控制/反馈 |
| `figures/selfref.png`（第 6 章） | Input/Feedback/Refine/Model M + 两句说明 → 输入/反馈/精炼/模型 M + 中文说明 |
| `figures/simulacra1.png`（第 17 章） | Perceive/Plan/Memory Stream/Retrieve/Retrieved Memories/Act/Reflect/Generative Agent Memory → 感知/规划/记忆流/检索/检索到的记忆/行动/反思/生成式智能体记忆 |

## 全书位图分类结果（2026-10-18，107 张被引用）

用「联系表」分批目视分类（每张表 12 个缩略图，一次读取即可判 12 张）。

**T1（纯标注型，可汉化）** —— 约 25 张：
`MI-concepts`、`virtuous5`、`virtuouscover2`、`alpha`、`selfref`、`simulacra1`、`simulacra2`（部分）、`cot-tot`、`tot-ex`、`grpo`、`glm_spike`、`rlhf_loop`、`lmnav`、`metaharness`、`student_learner`、`data_stock`、`unnatural`、`self-instruct`、`sample_efficiency_tokens`、`Word_vector_illustration`、`Grokking_modular_addition`、`moe`、`rl`（位图版，第 7 章）、`evolutionary1`、`struct`、`swe`、`rainbow2`、`abm`、`agentverse`、`isoflop`、`scaling`、`token_edit`、`negative_scaling`、`the_pile`、`rainbow`

**T2（保留原文）**：论文多面板截图、终端/代码截图、照片与渲染图、纯符号图。例：`react`、`balrog`、`pdr`、`stable`、`water`、`sotopia`、`CAMEL`（含代码面板）、`llmcoordinationbank`、`tombench`、`egosocialarena`、`oasis`、`mobility`、`rt2`、`pizero`、`saycan`、`webarena`、`medco`、`reflexion`、`reflexion-code`、`totcode`、`webdreamer`、`ollamalogprobs`、`ELIZA_conversation`、`python_exel2`、`magma`、`smollm3_mixture`、`worldgpt`、`som`、`shepherd`、`transformer_full_architecture`（已完成）

**① 无文字，不动**：`agent`、`cbow`、`skipgram`、`ttt`、`leiden`、`dalle`、`dalle3`、`stablediff`、`cartpole`、`oh2017core`、`lora`、`enc_dec`（已完成）

> 注：上表 T1 候选为**自动初筛 + 目视确认**结果，每张图动手前仍需确认标签与线条是否重叠。

## 工具与经验

- 矢量 PDF → PNG 预览：MiKTeX 自带 `pdftocairo`
- 位图遮盖+叠字：Pillow（`work` 环境，纯 Pillow 实现），脚本 `cache/imgzh.py`
- **关键经验**：
  1. 遮盖框**不能一律用白色**——在彩色底色上会留下白块。`imgzh.erase()` 改为**按列采样上下两侧背景色**（取中位数），可保留渐变底色，不出现矩形边缘。
  2. 遮盖框**必须避开图形线条**——先用程序测出线条精确坐标，再设定遮盖边界。
  3. **测量框要留余量**：多次出现「框比文字窄 10–20px」导致残留尾字（`t`、`nal`、`tic`）。测完应向外扩 3–5px，或在成品上放大复核。
  4. 文字与线条混在一起时（如弧线上的 `new data`），用**连通域按字形尺寸过滤**（高度 12–50、宽 2–60）可把字形从线条中分离出来。
