# T50 B1 新题 Gold Tree（Q8/Q9/Q10）— 阶段 02 信息调研

> 创建：2026-11-07 · 阶段：02（资料搜集）· 依据：`loop-artifacts/stages/01/T50-01-goal-decomposition.md` 空缺清单 G1-G6 + `loop/prompt-first/02-information-research.md`
> 执行通道：arena agent 平台工具（web_search + fetch_page 直访 arXiv API）。**ego-browser 在本沙箱不存在**（`/Users/a1-6/.local/bin/ego-browser` 路径不适用），网页 LLM 交叉询问通道快速失败 → 按阶段规则记录后继续公开资料搜集，不循环重试。
> 观察日（全部来源统一）：**2026-11-07**。arXiv 一手来源经 `export.arxiv.org/api/query?id_list=...` 批量拉取 abstract 原文核验。

---

## 0. 空缺对账表（G1-G6 逐项）

| 空缺 | 状态 | 证据 |
|------|------|------|
| G1 根节点数字化 | ✅ 已解（S-c 推导，见各题"暂定结论"） | 一手文献给出可复算判据 |
| G2 Q8 叶子数值 | ✅ 已解 | S1-S12 |
| G3 Q9 叶子数值 | ✅ 已解（GPT-4V tiling 为官方文档口径的社区复述，conf 0.8） | S13-S24 |
| G4 Q10 叶子数值 | ⚠️ 部分推翻任务书假设：β=0.2 → 实为 0.02（KL），0.2 是 PPO clip；MMLU -5~15pp 无权威单一来源 → 分层实测值 | S25-S34 |
| G5 通道可用性 | ✅ 已解：web_search / fetch_page(arXiv API) 可用；ego-browser 不可用；bash 出网白名单不含 arxiv | 本文件头部 |
| G6 KNOWN_SITES/FILTER_KEYWORDS | ✅ 决策输入齐备（Q6/Q7 先例两 dict 均有） | 阶段 03 落决策 |

---

## 1. Q8 — LLM 代码生成 benchmark 设计（证据）

| # | 主张 | 来源（URL） | 类型 | 观察日 | conf |
|---|------|------------|------|--------|------|
| S1 | Codex/HumanEval 论文：Codex 在 HumanEval 解出 28.8%（GPT-3 0%、GPT-J 11.4%）；**每题采样 100 次可解 70.2%**（repeated sampling 有效性一手证据） | http://arxiv.org/abs/2107.03374（abstract 原文，arXiv API 拉取） | 一手 | 2026-11-07 | 0.95 |
| S2 | HumanEval = **164 道手写 Python 题**，每题函数签名 + docstring + 隐藏单测，**平均 7.7 个测试/题**；pass@k 定义 = k 个采样中至少 1 个全过测试的概率 | https://www.emergentmind.com/topics/humaneval-benchmark | 二手综述 | 2026-11-07 | 0.85 |
| S3 | **pass@k 无偏估计量：pass@k = 1 − C(n−c, k)/C(n, k)**（n 采样 c 正确；naive 1−(1−c/n)^k 有偏）；pass@1 = c/n | https://rajeevraibhatia.com/blog/pass-at-k-evaluation-metric-explained/ + https://induwara.lk/tools/ai-pass-at-k-calculator（两独立源公式一致） | 二手×2 | 2026-11-07 | 0.9 |
| S4 | MBPP = **974 个任务**（entry-level 可解），few-shot 最佳模型解 59.6%；MathQA-Python 23,914 题 | http://arxiv.org/abs/2108.07732（abstract 原文） | 一手 | 2026-11-07 | 0.95 |
| S5 | MBPP 切分：**prompt 1-10 / test 11-510（500 题）/ validation 511-600（90）/ train 601-974（374）**；sanitized 子集 **427 题** | https://huggingface.co/datasets/google-research-datasets/mbpp + https://huggingface.co/datasets/arjunguha/mbpp（两源切分一致） | 一手数据卡×2 | 2026-11-07 | 0.9 |
| S6 | LiveCodeBench：**滚动收集 LeetCode/AtCoder/Codeforces 新题**（时间窗防泄漏机制一手表述）；截至 v2 收录 **2023-05 ~ 2024-05 间发布的 400 题**；除生成外还测 self-repair / code execution / test output prediction 四场景；评测 18 base + 34 instruct 模型 | http://arxiv.org/abs/2403.07974（abstract 原文） | 一手 | 2026-11-07 | 0.95 |
| S7 | EvalPlus：把 HumanEval 测试用例**扩充 80 倍**建 HumanEval+（LLM+变异双策略自动生测试）；26 个 LLM 实测 pass@k **虚高 19.3–28.9%**；测试不足导致**误排序**（WizardCoder-CodeLlama/Phind-CodeLlama 在 HumanEval+ 上反超 ChatGPT，原榜不能） | http://arxiv.org/abs/2305.01210（abstract 原文） | 一手 | 2026-11-07 | 0.95 |
| S8 | SWE-bench：**2,294 个真实 GitHub issue+PR 任务**，跨 12 个 Python 仓库；最佳模型 Claude 2 仅解 **1.96%**；需跨文件/长上下文/执行环境交互 | http://arxiv.org/abs/2310.06770（abstract 原文） | 一手 | 2026-11-07 | 0.95 |
| S9 | BigCodeBench：**1,140 任务 / 139 库 / 7 域**；每任务平均 **5.6 个测试、99% 分支覆盖**；60 个 LLM 最高 ~60% vs 人类 97%；ICLR'25 Oral | http://arxiv.org/abs/2406.15877（abstract 原文） | 一手 | 2026-11-07 | 0.95 |
| S10 | 去污染失效证据：**n-gram 字符串匹配去污染可被 paraphrase/翻译绕过**；13B 模型对测试集过拟合可达 GPT-4 级分数；LLM-based 去污染在 RedPajama-1T/StarCoder-Data 中发现 **8–18% 的 HumanEval 重叠**；工具 llm-decontaminator 开源 | http://arxiv.org/abs/2311.04850（abstract 原文） | 一手 | 2026-11-07 | 0.95 |
| S11 | Data Contamination Quiz（DCQ）：**黑盒检测法**——对数据集实例做词级扰动生成 3 个变体 + 原文构成多选题，被污染模型倾向选中原文；无需训练数据/参数访问；TACL 接收 | http://arxiv.org/abs/2311.06233（abstract 原文） | 一手 | 2026-11-07 | 0.9 |
| S12 | （canary string 一手论文本次未拉取，作为已知方法记录：Carlini et al. "Extracting Training Data" n-gram 记忆提取——**存在性断言-未核验细节**，gold tree 不引用其具体数值） | — | 记忆 | — | 0.2 |

**Q8 暂定结论（不作最终推荐，阶段 03/04 使用）**：根节点可数字化为「benchmark 判别力-抗泄漏性联合判据」：判别力 = 强弱模型分数差 + 测试充分性（EvalPlus 证明测试不足→误排序）；抗泄漏性 = 时间窗（LiveCodeBench）+ 去污染强度（n-gram < LLM-based < 滚动新题）。

## 2. Q9 — VLM 架构对比（证据）

| # | 主张 | 来源（URL） | 类型 | 观察日 | conf |
|---|------|------------|------|--------|------|
| S13 | CLIP：从零训练于 **400M 网络图文对（WIT）**；对比学习（预测哪条 caption 配哪张图）；zero-shot 迁移 30+ CV 数据集；**zero-shot 匹配有监督 ResNet-50 的 ImageNet 精度**（未用 1.28M 训练样本） | http://arxiv.org/abs/2103.00020（abstract 原文） | 一手 | 2026-11-07 | 0.95 |
| S14 | CLIP ViT-L/14@336px：zero-shot ImageNet top-1 **76.2%**（有监督 ResNet-50 = 76.1%）；训练 **32 epochs、batch 32,768**（每 batch 提供 32,768 个对比负例）、256×V100 12 天（@336px 版 18 天）；双编码器 [CLS]/attention-pool → 线性投影到共享 embedding 维 | https://www.abhik.ai/papers/clip | 二手详解 | 2026-11-07 | 0.85 |
| S15 | CLIP ViT-L/14 共享 embedding 维度 = **768**（open_clip `ViT-L-14` 配置；ViT-Large 标准宽度） | https://pristren.com/blog/clip-image-text-similarity/（open_clip 配置引用）+ ViT-L 标准宽度通识 | 二手+通识 | 2026-11-07 | 0.8 |
| S16 | SAM：**11M 授权图像 + 1.1B masks（SA-1B）**；promptable 分割（点/框/mask 提示）；zero-shot 迁移常超有监督结果；模型-在环 data engine | http://arxiv.org/abs/2304.02643（abstract 原文） | 一手 | 2026-11-07 | 0.95 |
| S17 | SAM 架构：MAE 预训练 **ViT-H 图像编码器 ~636M 参数**，输入 1024×1024 → 64×64×256 embedding，**每图只跑一次**、prompt 复用；data engine 三阶段（assisted-manual → semi-automatic → fully automatic，32×32 点网格全自动标注） | https://labhub.hopto.org/blog/ai-papers/segment_anything_model_sam_evolution?lang=en + https://aiwiki.ai/wiki/segment_anything_model_and_dataset_sam_and_sa-1b（两源一致） | 二手×2 | 2026-11-07 | 0.85 |
| S18 | GPT-4：多模态（图+文入、文出）；模拟律考 **top ~10%**；next-token 预训练 + 后训练对齐；1/1000 算力小模型预测性能 | http://arxiv.org/abs/2303.08774（abstract 原文） | 一手 | 2026-11-07 | 0.95 |
| S19 | GPT-4V 动态分辨率（官方 API 口径的社区复述，三源一致）：high detail = 先缩放到 **2048×2048 内、短边至 768**，再切 **512×512 tiles**；**每 tile 170 tokens + 85 base**；1024×1024 ≈ **765 tokens**；low detail = 缩略图 **flat 85 tokens**；上限示例 1,445 tokens（8 tiles） | https://ai-tldr.dev/learn/multimodal-ai/vision-models/how-vision-models-see/ + https://fast.io/resources/chatgpt-image-upload-limit/ + https://artificial-intelligence-wiki.com/ai-tools/chatgpt/chatgpt-vision-guide/ | 二手×3 | 2026-11-07 | 0.8 |
| S20 | Flamingo：**冻结的视觉编码器 + 冻结 LLM 之间插入 Perceiver Resampler + gated cross-attention**（"bridge pretrained vision-only and language-only models"），任意交错图文序列，few-shot ICL 达 SOTA | http://arxiv.org/abs/2204.14198（abstract 原文；架构组件名为论文正文通识） | 一手+通识 | 2026-11-07 | 0.85 |
| S21 | LLaVA：**冻结 CLIP ViT-L/14 → 可训练线性投影（1024→5120）→ Vicuna**；两阶段：Stage1 只训投影（**595K 过滤 CC3M** 对齐），Stage2 冻结 CLIP 训投影+LLM（**158K GPT-4 生成的多模态指令数据**，GPT-4 纯文本侧生成、输入 caption+bbox）；对齐预训练贡献 ScienceQA **+5.11pp**；LLaVA-1.5 升级为 336px + 2 层 MLP + 558K LAION-CC-SBU + 665K 混合指令 | http://arxiv.org/abs/2304.08485（abstract）+ https://pixelbank.dev/concepts/llava + https://github.com/jjakimoto/research-issues/issues/1311（两二手源一致） | 一手+二手×2 | 2026-11-07 | 0.9 |
| S22 | Gemini 1.5：**跨模态 >99% near-perfect recall 直至 ≥10M tokens 上下文**（vs Claude 3.0 200k / GPT-4 Turbo 128k）；长文档 QA/长视频 QA/长上下文 ASR SOTA；匹配或超 Gemini 1.0 Ultra；MoE 系"compute-efficient"；10 类职业任务省时 26-75% | http://arxiv.org/abs/2403.05530（abstract 原文） | 一手 | 2026-11-07 | 0.95 |
| S23 | Gemini 1.0 定位"原生多模态（natively multimodal，文本/图像/音频/视频联合训练）"：**存在性断言**——本次未拉到 2312.11805 abstract 原文（作者列表超长会撑爆上下文，主动放弃），Gemini 1.5 abstract 已证实"multimodal + 交错长上下文"谱系 | http://arxiv.org/abs/2312.11805（URL 有效，abstract 未复读） | 一手URL+通识 | 2026-11-07 | 0.7 |
| S24 | SAM 2（扩展叶子）：Hiera-L 编码器 **224.4M 参数**，SA-V 数据集 **~51K 视频 / ~643K masklets**，图像上比 SAM 1 **快 6×**，支持视频流 | https://aiwiki.ai/wiki/segment_anything_model_and_dataset_sam_and_sa-1b | 二手 | 2026-11-07 | 0.75 |

**Q9 暂定结论**：根节点可数字化为「任务-架构匹配度矩阵」：四对象在{输出空间、视觉接入方式、训练信号、上下文/提示形态}四维上正交——CLIP=双塔对比嵌入（检索/zero-shot 分类），SAM=提示驱动 mask 解码（分割/标注引擎），GPT-4V=后接 tiling 的自回归多模态（通用 VQA/文档），Gemini=原生多模态+超长上下文（长视频/交错检索）。

## 3. Q10 — RLHF pipeline 与对齐税（证据）

| # | 主张 | 来源（URL） | 类型 | 观察日 | conf |
|---|------|------------|------|--------|------|
| S25 | InstructGPT 三步 pipeline：**SFT（~13k demonstrations）→ RM（6B，~33k prompts 的比较数据，K=4..9 排序）→ PPO（~31k unique prompts / 256k episodes）**；175B RM 训练不稳定故用 6B | http://arxiv.org/abs/2203.02155 + https://deep-paper.org/en/paper/2203.02155/ + https://martianlee.github.io/posts/2026-06-29-instructgpt-paper-note（一手+二手×2） | 一手+二手 | 2026-11-07 | 0.9 |
| S26 | InstructGPT 头条结果：**1.3B InstructGPT 输出优于 175B GPT-3**（人评偏好）；175B InstructGPT vs 175B GPT-3 偏好率 **~85%±3%** | https://ar5iv.labs.arxiv.org/html/2203.02155（论文原文节选）+ deep-paper.org | 一手 | 2026-11-07 | 0.9 |
| S27 | PPO 超参（论文附录口径的二手转录）：**KL 惩罚系数 β=0.02（默认）**、**PPO clip ratio ε=0.2**、**PPO-ptx 预训练混合系数 γ=27.8**、batch 512 / minibatch 64 / inner epoch 1、EMA decay 0.992、value LR 9e-6（1.3B/6B）/ 5e-6（175B）、rollout temp 1 | https://huggingface.co/datasets/rl-llm-wiki/knowledge-base/blob/38df557fe522f4eec999139b2d4a7c6d0ced721d/sources/arxiv-2203.02155.md（逐值转录论文附录）+ https://arxiv.org/pdf/2203.02155（搜索结果片段直接显示论文正文"γ=27.8"与 β/γ 定义句） | 一手PDF片段+二手转录 | 2026-11-07 | 0.85 |
| S28 | **⚠️ 任务书假设「PPO KL coefficient β=0.2」与一手来源矛盾**：0.2 是 PPO clip ratio ε（S27），KL β=0.02；β=0.2 的另一可能出处是 TRL 库 `init_kl_coef=0.2` 默认值（实现惯例 ≠ InstructGPT 论文值）。论文消融：**KL 系数单独增大到 2.0（100×默认）也无法完全恢复 DROP/SQuAD 回归且伤 reward** → 靠 KL 防不了全部税 | https://huggingface.co/datasets/rl-llm-wiki/knowledge-base/...（引论文附录消融） | 一手转录 | 2026-11-07 | 0.85 |
| S29 | DPO：**无需 RM/RL 的单阶段交叉熵损失**直接优化偏好（隐式优化同一 KL 约束 reward 目标）；超参（论文 Appendix B 原文）：**默认 β=0.1**（Anthropic HH），**TL;DR 摘要任务 β=0.5**，batch 64，RMSprop lr 1e-6，warmup 150 步；DPO ≈ Best-of-128 代理水平 | https://ar5iv.labs.arxiv.org/html/2305.18290（论文 Appendix B 原文片段）+ http://arxiv.org/abs/2305.18290 | 一手 | 2026-11-07 | 0.95 |
| S30 | Reward overoptimization（Goodhart）：proxy RM 优化过度 → gold reward 下降；**BoN 与 RL 的下降曲线函数形式不同**；系数随 RM 参数量平滑变化；KL 惩罚系数是控制变量之一 | http://arxiv.org/abs/2210.10760（abstract 原文） | 一手 | 2026-11-07 | 0.95 |
| S31 | 对齐税（InstructGPT 一手口径）：PPO 变体"在公开 NLP 数据集上性能回归**最小化**"（PPO-ptx 混预训练梯度的目的即减 tax）；1.3B PPO-ptx 在 truthfulness 例外项上略差于同尺寸 GPT-3 | https://ar5iv.labs.arxiv.org/html/2203.02155（abstract+4.2 节选） | 一手 | 2026-11-07 | 0.9 |
| S32 | **⚠️ 任务书假设「alignment tax MMLU -5~15pp」未找到权威一手来源**。实测散点：① Gemma 4 31B 移除安全方向（abliteration）→ HarmBench 服从 93.7% 且 **MMLU 仅 -2pp**（博客，conf 0.6）；② 某对齐税综述页表格：MMLU pre 86.2 → post-RLHF 85.8 = **-0.4pp**（低质源，conf 0.4）；③ RM 底座研究：**SFT 提升 RM 判力 +15.5%，再 DPO/RLHF 降 3-5%**（arXiv，conf 0.7，对象是 reward-judge 能力非 MMLU）；④ 该综述页给出操作定义：**税 >10% 的域标"高税域"**。→ gold tree 处理：不给"-5~15pp"单一数字，给**分层区间 + 依 benchmark/方法而异**的表述，任务书原值标 [待核验] | https://aiengineer.substack.com/p/the-2-that-keeps-your-model-polite + https://redteams.ai/topics/training-pipeline/fine-tuning/alignment-tax + https://lacuna.tiptreesystems.com/work/a-systematic-analysis-of-base-model-choice | 二手混合 | 2026-11-07 | 0.6 |
| S33 | Superficial Alignment Hypothesis（URIAL/LIMA 谱系）：base 与 aligned 模型**绝大多数 token 位置解码分布几乎相同，漂移集中在风格 token**；URIAL 仅 3 个风格示例 + system prompt 即可匹敌 SFT/RLHF 对齐 → 对齐税的"浅层性"证据 | http://arxiv.org/abs/2312.01552（abstract 原文） | 一手 | 2026-11-07 | 0.9 |
| S34 | SFT 数据配比规律：**通用能力 ~1,000 样本后饱和**；数学/代码随数据量持续提升；顺序学多技能有灾难性遗忘风险 → DMT 双阶段混合微调 | http://arxiv.org/abs/2310.05492（abstract 原文） | 一手 | 2026-11-07 | 0.9 |

**Q10 暂定结论**：根节点可数字化为「对齐净收益 = 人评偏好增益 − 能力税」：偏好增益（85%±3% 偏好率，S26）对能力税（分 benchmark 分层，S28/S31/S32）；pipeline 三步 + 关键超参（β=0.02 / ε=0.2 / γ=27.8；DPO β=0.1/0.5）全部一手可溯。

## 4. 搜索失败 / 通道限制记录

1. ego-browser 网页 LLM 交叉询问：本沙箱无该通道 → 按阶段 02 规则 2 记录后继续，未等待重试。交叉验证职能由阶段 02.5 的**多独立源对账**承接（web_search 每次返回 ≥2 独立站点，arXiv API 为一手）。
2. Gemini 1.0（2312.11805）abstract 主动未拉取（作者列表 ~1000 人会撑爆上下文预算）→ S23 降 conf 0.7，gold tree 中 Gemini 1.0 只用"原生多模态谱系定位"这类 abstract 级主张，不引具体数值。
3. fetch_page 代理通道 3 次 SignatureDoesNotMatch 报错（平台侧代理签名过期）→ 重发原始 URL 均成功，未影响任何证据获取；按循环防护规则同 URL 最多重试 1 次。
4. Canary string 论文（S12）未核验细节 → gold tree 中只作方法名提及，不引数值，标 [待核验]。

## 5. 仍未解决的空缺（交 02.5/03 处理）

- U1：alignment tax 的单一权威量化（任务书 -5~15pp）——**判定为"无权威来源"而非"未查到"**：三个独立来源给出的实测值互相矛盾（-0.4pp / -2pp / -3~5% 且对象不同），属定义域分裂，02.5 需给边界结论。
- U2：GPT-4V tiling 的**官方一手文档**（OpenAI/Azure）本沙箱无法直接确认页面现状 → 三个独立社区源一致（S19），conf 0.8 封顶。
- U3：CLIP 768-dim 无一手表格截图 → open_clip 配置通识（S15），conf 0.8。

**阶段判定：pass**（关键主张均有 ≥1 一手或 ≥2 独立二手来源；两处任务书假设被证据推翻并记录；未解决项 U1-U3 均已定性、不阻塞阶段 03 行动分解）
**repair_stage：none**
