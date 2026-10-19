# 术语表（英 → 中）

> **术语来源**：核心术语以**全国科学技术名词审定委员会**（cnterm.cn）审定发布为准；其余以中文 AI 领域主流教材、论文与官方技术文档的通行译法为准。**禁止自创译名。**
>
> **已核实的权威定名**（2026-10-14 查证）：
> - `token` → **词元**：全国科技名词委 2026-03-25 正式公告（优先推荐）
> - `agent` → **智能体**：全国科技名词委审定规范译名
>
> **新增核实**（2026-10-14 修订）：
> - `layer normalization` → **层归一化**（Transformer 图中 `Norm` 即 Layer Norm，不可简写为"归一化"）
> - `BERT` → **基于 Transformer 的双向编码器表示**（用"基于"，不用"来自"）
> - `GPT` → **生成式预训练 Transformer**（generative，不是 generalized；原书作 "generalized" 属作者笔误）
> - `BLEU` → **双语评估替补**（Bilingual Evaluation Understudy，知乎/CSDN 通行译法）
> - `N×` → Transformer 图中重复层标记，保留数学符号写作 **N×**，不写成 "Nx"
> - `shifted target sequence` → **移位后的目标序列**
> - `extractive / abstractive` → **抽取式 / 生成式**（文本摘要领域的标准对译）

## 核心概念

| English | 中文 | 说明 |
|---|---|---|
| agent | 智能体 | 全书核心词，统一用「智能体」，不用「代理」 |
| agentic | 智能体式 | 作形容词时用「智能体式」，如 agentic LLM → 智能体式大语言模型 |
| Agentic Large Language Models | 智能体大语言模型 | 书名/标题 |
| large language model (LLM) | 大语言模型 | 简称 LLM 保留 |
| foundation model | 基础模型 | |
| token | 词元 | 不用「令牌」 |
| tokenization | 分词 | |
| embedding | 嵌入 | 不用「嵌入向量」除非强调是向量 |
| attention | 注意力 | |
| self-attention | 自注意力 | |
| multi-head attention | 多头注意力 | |
| cross-attention | 交叉注意力 | |
| transformer | Transformer | 专有架构名，保留英文首字母大写 |
| encoder | 编码器 | |
| decoder | 解码器 | |
| positional encoding | 位置编码 | |
| context window | 上下文窗口 | |
| emergent behavior | 涌现行为 | |

## 学习与训练

| English | 中文 | 说明 |
|---|---|---|
| pretraining | 预训练 | |
| finetuning / fine-tuning | 微调 | |
| inference | 推理 | |
| supervised learning | 监督学习 | |
| unsupervised learning | 无监督学习 | |
| self-supervised learning | 自监督学习 | |
| reinforcement learning (RL) | 强化学习 | |
| autoregressive | 自回归 | |
| reward | 奖励 | |
| reward function | 奖励函数 | |
| policy | 策略 | |
| state | 状态 | |
| action | 动作 | |
| environment | 环境 | |
| credit assignment | 信用分配 | |
| Markov decision process (MDP) | 马尔可夫决策过程 | |
| exploration / exploitation | 探索 / 利用 | |
| scaling | 规模化 | scaling law → 规模化规律 |
| benchmark | 基准 | 作测试集时用「基准测试」 |
| dataset | 数据集 | |
| overfitting | 过拟合 | |
| gradient | 梯度 | |
| loss | 损失 | |
| LoRA (Low-Rank Adaptation) | 低秩适配（LoRA） | 首次全称，之后用 LoRA |
| MoE (Mixture of Experts) | 混合专家（MoE） | |
| RLHF | 基于人类反馈的强化学习 | |

## 提示与推理

| English | 中文 | 说明 |
|---|---|---|
| prompt | 提示词 | 动词 prompt → 提示 |
| prompting | 提示 | |
| in-context learning | 上下文学习 | |
| chain-of-thought (CoT) | 思维链 | |
| tree-of-thought (ToT) | 思维树 | |
| few-shot | 少样本 | |
| zero-shot | 零样本 | |
| retrieval-augmented generation (RAG) | 检索增强生成 | |
| tool use | 工具使用 | |
| function calling | 函数调用 | |
| scratchpad | 草稿区 | |
| self-consistency | 自洽性 | |

## 智能体与社会

| English | 中文 | 说明 |
|---|---|---|
| multi-agent system | 多智能体系统 | |
| cooperation / competition | 合作 / 竞争 | |
| role-based | 基于角色的 | |
| society simulation | 社会模拟 | |
| agent-based model (ABM) | 基于智能体的模型 | |
| alignment | 对齐 | |
| hallucination | 幻觉 | |
| interpretability | 可解释性 | |
| mechanistic interpretability | 机制可解释性 | |
| guardrail | 护栏 | |

## 智能体架构与记忆（第 9、10 章）

| English | 中文 | 说明 |
|---|---|---|
| interaction style | 交互范式 | 五种智能体范式 A–E |
| agent type | 智能体类型 | |
| query prompt | 查询式提示 | 范式 A |
| in-context learning (ICL) | 上下文学习 | 范式 B |
| in-context reinforcement learning (ICRL) | 上下文强化学习 | |
| self-reflection | 自反思 | 范式 D |
| reinforcement finetuning (ReFT) | 强化微调 | 范式 E |
| harness | 运行框架 | 管理提示词的外部算法 |
| prompt builder | 提示词构建器 | |
| policy improver | 策略改进器 | |
| behavior policy | 行为策略 | $\pi$ |
| optimal policy | 最优策略 | $\pi^*$ |
| transition function | 转移函数 | $T$ |
| reward function | 奖励函数 | $R$ |
| memory architecture | 记忆架构 | |
| long context window | 长上下文窗口 | |
| soft prompt | 软提示 | |
| explicit memory management | 显式记忆管理 | |
| vector database | 向量数据库 | |
| continual learning | 持续学习 | |
| catastrophic forgetting | 灾难性遗忘 | |
| model context protocol (MCP) | 模型上下文协议 | |
| belief-desire-intention (BDI) | 信念-愿望-意图 | |
| swarm agent | 集群智能体 | |
| robotic assistant | 机器人助手 | |
| ant colony optimization | 蚁群优化 | |
| super-organism | 超有机体 | |

## 案例研究（第 10 章）

| English | 中文 | 说明 |
|---|---|---|
| knowing-doing gap | 知行差距 | |
| credit assignment | 信用分配 | |
| reward landscape | 奖励地形 | |
| progression percentage | 推进百分比 | BALROG 的评测指标 |
| base learner | 基学习器 | |
| grid world | 网格世界 | |
| planner / executor | 规划器 / 执行器 | |
| leaderboard | 排行榜 | |

## 助手与检索（第 11–14 章）

| English | 中文 | 说明 |
|---|---|---|
| assistant | 助手 | |
| conversational assistant | 对话助手 | |
| thinking assistant | 思考助手 | 以提问代替作答 |
| shopping assistant | 购物助手 | |
| flight operations assistant | 航班运行助手 | |
| medical assistant | 医疗助手 | |
| trading assistant | 交易助手 | |
| coding assistant | 编程助手 | |
| instruction tuning | 指令微调 | |
| retrieval augmentation | 检索增强 | |
| human in the loop | 人机在环 | |
| high-risk domain | 高风险领域 | |
| graceful degradation | 优雅降级 | |
| abstention | 弃答 | 模型拒绝作答 |
| lost-in-the-middle | 中间迷失 | |
| EU AI Act | 《欧盟人工智能法案》 | |
| arrival-slot allocation | 到达时隙分配 | |
| confusion matrix | 混淆矩阵 | |
| precision / recall / F1 | 精确率 / 召回率 / F1 | |
| ground truth | 金标准 | |
| routing | 路由 | 指分派到正确路径 |
| triage | 分诊 | |
| planner agent | 规划器智能体 | |
| executor agent | 执行器智能体 | |
| shared context | 共享上下文 | |
| information retrieval (IR) | 信息检索 | |
| inverse document frequency (IDF) | 逆文档频率 | |
| term frequency (TF) | 词频 | |
| vector space model | 向量空间模型 | |
| latent semantic analysis (LSA) | 潜在语义分析 | |
| dense passage retrieval (DPR) | 稠密段落检索 | |
| approximate nearest neighbor (ANN) | 近似最近邻 | |
| cross-encoder | 交叉编码器 | |
| re-ranking | 重排序 | |
| grounded generation | 接地生成 | |
| attribution | 归因 | |
| faithfulness | 忠实度 | |
| helpfulness | 有用性 | |
| query rewriting | 查询重写 | |
| gated retrieval | 门控检索 | |
| agentic RAG | 智能体式 RAG | |
| streaming RAG | 流式 RAG | |
| neuro-symbolic | 神经—符号 | |
| synthetic data | 合成数据 | |
| distillation | 蒸馏 | |
| knowledge distillation | 知识蒸馏 | |
| teacher / student | 教师 / 学生 | |
| off-policy / on-policy | 离策略 / 在策略 | |
| self-distillation | 自蒸馏 | |
| exposure bias | 暴露偏差 | |
| model collapse | 模型崩塌 | |
| data curation | 数据筛选 | |
| data contamination | 数据污染 | |
| backtranslation | 回译 | |
| human-in-the-loop | 人在回路 | |
| red teaming | 红队测试 | |
| differential privacy | 差分隐私 | |
| machine-psychological | 机器心理学 | |
| negativity bias | 负面性偏差 | |
| memory stream | 记忆流 | |
| cognitive architecture | 认知架构 | |
| generative agents | 生成式智能体 | |
| Turing completeness | 图灵完备性 | |
| decision trace | 决策轨迹 | |
| looped transformer | 循环 Transformer | |
| in-context reinforcement learning (ICRL) | 上下文内强化学习 | |
| self-modifying | 自我修改 | |
| harness | 执行框架 | |
| meta-harness | 元框架 | |
| metalearning | 元学习 | |
| mechanistic interpretability (MI) | 机制可解释性 | |
| residual stream | 残差流 | |
| logit lens / tuned lens | logit 透镜 / 调优透镜 | |
| direct logit attribution (DLA) | 直接 logit 归因 | |
| polysemanticity | 多义性 | |
| superposition | 叠加 | |
| sparse autoencoder (SAE) | 稀疏自编码器 | |
| dictionary learning | 字典学习 | |
| monosemanticity | 单义性 | |
| circuit | 回路 | |
| induction head | 归纳头 | |
| activation patching | 激活修补 | |
| path patching | 路径修补 | |
| attribution patching | 归因修补 | |
| causal mediation | 因果中介 | |
| causal scrubbing | 因果清洗 | |
| linear probing | 线性探针 | |
| shadow model | 影子模型 | |
| transcoder | 转码器 | |
| coreference resolution | 共指消解 | |
| grokking | grokking | 保留原文 |
| construct validity | 构念效度 | |
| competence / performance | 能力 / 表现 | |
| 4-E view of cognition | 认知的 4E 观点 | |
| anthropomorphism | 拟人化 | |
| anthropodenial | 拟人否定 | |
| anthropocentric bias | 人类中心偏差 | |
| grounding | 接地 | |
| symbol-grounding problem | 符号接地问题 | |
| reversal curse | 反转诅咒 | |
| Potemkin understanding | 波将金式理解 | |
| knowing-doing gap | 知行差距 | |
| cognitive map | 认知地图 | |
| theory-theory | 理论论 | |
| simulation-theory | 模拟论 | |
| metacognition | 元认知 | |
| introspection | 内省 | |
| calibration / sensitivity | 校准 / 敏感度 | |
| concept injection | 概念注入 | |
| phenomenal consciousness | 现象意识 | |
| access consciousness | 通达意识 | |
| sentience | 感受性 | |
| functionalism | 功能主义 | |
| biological naturalism | 生物自然主义 | |
| intentional stance | 意向立场 | |
| indicator properties | 指标属性 | |
| global workspace theory | 全局工作空间理论 | |
| Jacobian Lens / J-space | 雅可比透镜 / J 空间 | |
| substrate independence | 基质无关 | |
| gaming problem | 博弈问题 | |
| role-play account | 角色扮演解释 | |
| extended mind | 延展心智 | |
| overthinking | 过度思考 | |
| curriculum learning | 课程学习 | |
| open world model | 开放世界模型 | |
| vision-language-action (VLA) | 视觉—语言—行动（VLA） | |

## 不译项（保持原样）

- 模型/产品名：ChatGPT、Claude、GPT-4、LLaMA、BERT、ELIZA、AlphaGo 等
- 论文标题、作者名、机构名
- 代码、变量名、函数名、命令行
- URL、DOI、邮箱
- 数学符号与公式
- 参考文献条目（`.bib` / `.bbl` 内容）
- 引用键（`\label{}` / `\ref{}` / `\cite{}` 的花括号内容）
