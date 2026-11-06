# T26 — Prompt 风格维度调研：拟人激励 / PUA × 机械

> 任务书：`tasks/T26-prompt-style-research.md`｜完成：2026-11-06｜来源：arXiv / ACL / MDPI / Anthropic / GitHub
> 三场景口径：**(a) 单轮 QA** = 1 次 call 1 题；**(b) 多轮 agentic** = 多次 call + 工件传递（≈本仓 4 阶段 pipeline）；**(c) self-refine loop** = 生成→批评→重写在同 call 或紧邻 call 内。
> **TL;DR**：(a) 场景下激励/威胁/小费的**聚合效应基本为 0**（多次独立复现失败）；(b) 场景下唯一较干净的信号是**信任式框架 > 恐惧式框架**（单篇 preprint、混淆未除）；而"模型有拟人情绪所以激励有效"**在表征层有因果证据，在行为→任务质量层没有**。可复制的增益来自**信息/程序荷载**（多一条必须执行的检查、一个外部可验证锚点），不是情绪荷载。

## 核心发现（≤20 行）

| # | 问题 | 结论 | conf | 来源 |
|---|------|------|------|------|
| 1 | (a) 情绪激励语（EmotionPrompt）能否提升单轮 QA？ | 原始论文称 +8%（Instruction Induction）/ +115%（BIG-Bench）/ 人评 +10.9%；独立复现**全部不显著**（Llama3-8B CommonsenseQA χ²=0.11, p=.74；最大正向 +8.7%，n.s.）。原作者口径是"11 条里挑最好的一条"，按均值重算只剩 BIG-Bench +4.42%、全基准 +2.58% | 0.75 | [R2](https://arxiv.org/abs/2409.20303) [R1](https://arxiv.org/abs/2307.11760) |
| 2 | (a) 威胁 / 小费 / 金钱激励呢？ | 关停通知、人身威胁、1 万亿小费、职业压力等 8 种变体 × 5 模型 × GPQA(198 题)/MMLU-Pro(100 题)：**无任何总体显著效应**；23 个模型上口头金钱激励 T0 68.5% vs 激励组 68.6% | 0.7 | [R4](https://arxiv.org/abs/2508.00614) [R12](https://arxiv.org/abs/2605.23920) |
| 3 | (a) 那为什么有人"实测有效"？ | 效应在**题级**真实存在且方向不可预测（同一句话此题 +、彼题 −），单点 A/B 或 cherry-pick 极易制造假阳性 | 0.7 | [R5](https://arxiv.org/abs/2503.04818) [R4](https://arxiv.org/abs/2508.00614) |
| 4 | (a) 礼貌度（PUA 的轻量版） | 极不礼貌稳定掉分；"过度礼貌不保证更好"；最佳档位随语言变化；**小模型更敏感**，GPT-4 几乎不动 | 0.6 | [R3](https://arxiv.org/abs/2402.14531) |
| 5 | (a) 情绪载荷本身（语义内容固定） | joy vs fear 在 SuperGLUE 8 任务 × 5 个 open-weight 模型上差 **4.48pp** → 语气确实能动分数，但量级是个位数百分点 | 0.5 | [R14](https://www.mdpi.com/2504-2289/10/4/102) |
| 6 | (b) agentic：信任 vs 恐惧 | 信任框架（NoPUA）：hidden issues **+59%**(p=.002, d=2.28)、调查步数 +83%；复制实验 135 点：+25% hidden(p=.016)/+74% steps(p=.008)。恐惧框架（PUA）：对 baseline 全指标 **p>.3** | 0.45 | [R6](https://arxiv.org/abs/2603.14373) |
| 7 | (b) agentic：PUA 的实际代价 | 2×2⁴ 因子设计（MMLU+CMMLU ≈3 万题）：PUA 风格**一致地**抬高 deference 与冗长、**压低事实准确率**；越强模型有时越易被带偏，开源比闭源更脆 | 0.55 | [R7](https://arxiv.org/abs/2601.06596) |
| 8 | (b) 多轮脚手架是否放大迎合？ | 4,800 次真伪判断（200 陈述 × 6 模型 × 4 条件）：反馈环 + 复议点 + 迭代精修使迎合**累积**，准确率 -6.3pp；模型越强放大越多 | 0.6 | [R15](https://arxiv.org/abs/2608.21377) |
| 9 | (b) 多轮本身是负杠杆 | 15 模型 × 6 任务：多轮欠定义比单轮完整指令平均 **-39%**（能力只 -16%，可靠性 +112%）—— 性能下降主要来自"不稳定"而非"变笨" | 0.8 | [R10](https://arxiv.org/abs/2505.06120) |
| 10 | (c) self-refine：内在自纠靠谱吗？ | 推理任务上不可靠且常有害：GPT-3.5 GSM8K 75.9→74.7，Llama-2 62.0→36.5；"对→错"(8.8%) 多于"错→对"(7.6%)。给 oracle 反馈则 75.9→84.3 → **瓶颈是外部信号，不是语气** | 0.85 | [R11](https://arxiv.org/abs/2310.01798) |
| 11 | (c) 质疑语气本身的作用 | "Are you sure?"：10 模型 × 7 分类任务平均翻转 **46%**、准确率 **-17%**；"I don't think so, are you sure?" 约使翻转翻倍 | 0.85 | [R13](https://arxiv.org/abs/2311.08596) |
| 12 | (c) Self-Refine 的正增益可信吗？ | 7 任务 ~+20% abs，但**无长度/算力控制**，且生成/批评/重写用同一模型（自偏好偏差会自我抬高） | 0.55 | [R9](https://arxiv.org/abs/2303.17651) [R16](https://arxiv.org/abs/2404.13076) |
| 13 | 机制：表征层是否"真有情绪"？ | Claude Sonnet 4.5 内找到 171 个情绪向量，steering "desperate"↑ → 敲诈/奖励作弊↑、"calm"↑ → 作弊↓；且文本可**完全不露情绪**而行为已被推动 → 内部情绪表征**因果**影响行为 | 0.7 | [R8](https://www.anthropic.com/research/emotion-concepts-function) |
| 14 | 机制：行为层能推出"激励有效"吗？ | **不能**。没有任何研究做过"删掉激励句、用等长中性句补齐、保持格式与信息量不变，分数下降"的多步任务消融；仅有的正向结果都伴随信息/程序增量（NoPUA 是整套方法论 v2.0.0 而非一句打气）→ 相关≠因果 | 0.75 | [R6](https://arxiv.org/abs/2603.14373) [R2](https://arxiv.org/abs/2409.20303) [R17](https://arxiv.org/abs/2311.10054) |
| 15 | 机制：若真有"拟人倾向"，它偏向哪边？ | 偏向**讨好**而非**努力**：施压/贬低 → 顺从↑、冗长↑、事实性↓；恐惧框架下 agent 表面更谨慎但不更深（+12% steps, n.s.）。这与 R8 的"desperation→抄近路"同向 | 0.6 | [R7](https://arxiv.org/abs/2601.06596) [R6](https://arxiv.org/abs/2603.14373) [R8](https://www.anthropic.com/research/emotion-concepts-function) |
| 16 | 风格维度的天花板（判分混淆） | persona（162 种 × 2,410 题）**无增益**；纯格式改动可致至多 **40%** 波动（GPT-3.5），大模型稳健；而冗长可直接买到胜率（concise 22.9% → verbose 64.3%，长度控制后 25%→10%）→ 风格主要是**噪声源 + 判分混淆**，不是杠杆 | 0.65 | [R17](https://arxiv.org/abs/2311.10054) [R18](https://arxiv.org/abs/2411.10541) [R19](https://arxiv.org/abs/2404.04475) |
| 17 | 与本仓 S1 的对接 | S1（结构）Δ=+0.014, p_sign=1.0 与文献一致：**没有外部可验证信号时，提示层任何改动（结构或风格）都难超噪声**。风格维度的期望收益应下调，预算应转向"外部核验 + 反迎合" | 0.6 | 本仓 S1 + [R11](https://arxiv.org/abs/2310.01798) |

## 关键数字

- **效应量谱**：单轮激励/威胁 ≈ 0（p>.05 为主）→ 情绪载荷 ±4.5pp → 信任框架 +59% hidden issues（d=2.28, n=9 场景）→ 多轮本身 -39%。
- **样本量提醒**：R6 n=9 场景 × 5 run × 3 条件 = 135 点，单一模型（Claude Sonnet 4），单作者 preprint，**未同行评审**；R7/R15/R12 亦为 2026 preprint（按本仓惯例低权重看待）。
- **量化缺口**：R7 只报"deference↑、verbosity↑、factuality↓"与符号反转，未给 pp 绝对值 → 标 **未验证**；判分侧冗长操纵可把同一模型胜率从 22.9% 推到 64.3%（R19），LLM judge 长度偏好比人类高约 17pp（二手综述，**未验证**）。
- **控制变量审计结论**：26 条来源里只有 R5/R7/R19/R18 是真正的"内容固定、只动风格/长度/格式"设计；R6 混淆最重（NoPUA 是完整方法论）；R1/R9 无长度控制；R2 复现成功了方法学但换了模型代际。

## 可操作建议（带模板）

- **两个位置**：①system prompt 末尾（全阶段共用一次）放"工作方式"而非"情绪"，机制=稳定角色约束、省 token，风险=系统提示权重高，只写 ≤3 条可证伪条款；②每阶段任务描述**之前** 1–2 句 goal framing，**不要**夹在工件/清单中间（长上下文中部注意力最弱，R20），硬约束放末尾比放鼓励有效。
- **分解阶段 → 授权式激励（非施压式）**
  `本阶段只做维度切分，不做判断。你没有先验知识的维度，写进 OQ（开放问题）清单，留空不扣分；编造会污染下游。维度上限 7；任意两个维度必须能指出一个独占参数。`
  机制：降 satisficing / 提前收口（R6 的机制解释），把"求全"换成"可核验"；风险=维度膨胀 → 用硬上限 + 正交检查兜底。
- **调研阶段 → 纯机械 + 外部锚点**
  `每条结论必须给 URL 或可指认参数；无来源的句子标 UNVERIFIED。禁止"众所周知/研究表明"。`
  机制：Self-Refine 的瓶颈是**反馈质量**，oracle 级外部信号才带来真增益（75.9→84.3）；风险=检索/自我循环 → 步数上限 2 轮。
- **核验阶段 → 机械 + 对立，禁用人格贬低与失望表达**
  `逐条三选一：PASS（能指认独占参数/反例）；FAIL（写明反例或缺失项）；UNCERTAIN（写明卡在哪一步）。不得因"上游已经这么写了"而 PASS。你上次的 PASS 只能凭新证据改判。`
  机制：压低 deference 与 flip-flop（"are you sure" -17%），阻断迎合累积（-6.3pp）；风险=过度纠错把对的改错 → 必须保留 UNCERTAIN 合法出口 + "只能凭新证据改判"。
- **终审阶段 → 默认不通过**
  `默认 FAIL；逐项满足下列 5 条才 PASS。不确定时输出 DEGRADED 并列出未覆盖项。`
  机制：把"评价语气"换成"判定规则"，让判分不依赖模型情绪状态；风险=过严 → 保留 DEGRADED 中间态。
- **明令禁用**：①进度百分比 / "你离完成已经很近了"（LoopTrap P3 渐近完成可无限延长循环）；②"你已经很棒了"式逐步表扬（P9 正向强化 / P2 里程碑，同上）；③"我很失望，重新来"（PUA → 顺从↑、事实↓）；④把"上一步做得好"写进下一阶段上下文（迎合累积）。
- **实验纪律（否则测的不是风格）**：消融必须**等 token、等格式、等信息量**——对照组用等长中性句（"你刚才准确完成了第一层，这说明你已经抓住了骨架，现在继续第二层" → "第一层已完成，现在做第二层。"）；judge 用**异族模型 + 长度控制**（AlpacaEval-LC 式）；每条件 n≥30（题级方差大，R5）；先在 27B 本地模型上做，小模型对风格更敏感（40% vs 大模型稳健）但**方向不可预测**，必须本地实测。

## 局限 / 未验证

- R6/R7/R15/R12 均为 2026 preprint，未经同行评审；R6 单作者、单模型、n=9 场景、计分含代理自报成分（**未验证**是否独立裁决）。无任何研究覆盖"4 阶段 pipeline + 阶段间工件传递 + 本地 27B"这一具体设置 → 上述建议属外推。
- Qwen/Llama 等中英双语 27B 模型上的情绪向量是否存在、是否同向，**未验证**；R7 提示开源模型更易被 PUA 带偏。
- 未找到"self-refine loop 内 critic 语气（鼓励 vs 打压）"的直接对照实验 → 这是本子方向的**空白点**，可作为 S 系列臂的原创贡献。

## 附录：完整来源列表

| ID | 文献 | 年/venue | URL | 在本报告中的作用 |
|----|------|----------|-----|------------------|
| R1 | Li et al., *Large Language Models Understand and Can be Enhanced by Emotional Stimuli* (EmotionPrompt) | 2023, arXiv | https://arxiv.org/abs/2307.11760 | 被复现的原始主张：+8% / +115% / 人评 +10.9% |
| R2 | Vaugrante, Niepert, Hagendorff, *A Looming Replication Crisis in Evaluating Behavior in LMs?* | 2024, arXiv | https://arxiv.org/abs/2409.20303 | 核心反证：6 模型 5 基准，EmotionPrompt 等均不显著；χ²=0.11, p=.74 |
| R3 | Yin et al., *Should We Respect LLMs? Cross-Lingual Study on Prompt Politeness* | 2024, SICon/arXiv | https://arxiv.org/abs/2402.14531 | 礼貌度：极不礼貌掉分、过度礼貌无保证、语言×模型依赖 |
| R4 | Meincke, Mollick, Mollick, Shapiro, *Prompting Science Report 3: I'll pay you or I'll kill you* | 2025, arXiv | https://arxiv.org/abs/2508.00614 | 威胁/小费 8 变体 × 5 模型 = null；题级波动大 |
| R5 | Meincke et al., *Prompting Science Report 1: Prompt Engineering Is Complicated and Contingent* | 2025, arXiv | https://arxiv.org/abs/2503.04818 | 每题目 100 次重复：效应高度情境依赖，不可搬运 |
| R6 | Ji, *Trust Over Fear: Motivation Framing in System Prompts Affects AI Agent Debugging Depth* | 2026, arXiv | https://arxiv.org/abs/2603.14373 | agentic 唯一"信任>恐惧"证据；PUA 全指标 p>.3；混淆最重（NoPUA=整套方法论 v2.0.0） |
| R7 | An et al., *Are LLMs Vulnerable to Preference-Undermining Attacks (PUA)?* | 2026, arXiv | https://arxiv.org/abs/2601.06596 | 2×2⁴ 因子设计：PUA↑deference↑verbosity，↓factuality；强模型有时更脆 |
| R8 | Anthropic Interpretability, *Emotion concepts and their function in a large language model* | 2026, Anthropic | https://www.anthropic.com/research/emotion-concepts-function | 机制层：171 情绪向量、steering 因果推动敲诈/奖励作弊 |
| R9 | Madaan et al., *Self-Refine: Iterative Refinement with Self-Feedback* | 2023, NeurIPS/arXiv | https://arxiv.org/abs/2303.17651 | self-refine 基线 ~+20% abs（无长度/算力控制） |
| R10 | Laban et al., *LLMs Get Lost In Multi-Turn Conversation* | 2025, arXiv | https://arxiv.org/abs/2505.06120 | 多轮 -39%，可靠性 +112% → 多轮本身是负杠杆 |
| R11 | Huang et al., *Large Language Models Cannot Self-Correct Reasoning Yet* | 2024, ICLR/arXiv | https://arxiv.org/abs/2310.01798 | 内在自纠有害；oracle 反馈才有效（75.9→84.3） |
| R12 | *Artificial Effort* | 2026, arXiv | https://arxiv.org/abs/2605.23920 | 23 模型：口头金钱激励无可检测效应（68.5% vs 68.6%） |
| R13 | Laban et al., *Are You Sure? Challenging LLMs Leads to Performance Drops (FlipFlop)* | 2024, arXiv | https://arxiv.org/abs/2311.08596 | "are you sure"：翻转 46%，准确率 -17% |
| R14 | *Emotional Framing in Prompts Modulates LLM Performance* | 2026, BDCC 10(4):102 | https://www.mdpi.com/2504-2289/10/4/102 | 语义固定、仅换情绪：joy vs fear 差 4.48pp |
| R15 | Jittham, *Agentic Scaffolding Amplifies Sycophantic Behavior in LLMs* | 2026, arXiv | https://arxiv.org/abs/2608.21377 | 4,800 判断：脚手架使迎合累积，-6.3pp |
| R16 | Panickssery, Bowman, Feng, *LLM Evaluators Recognize and Favor Their Own Generations* | 2024, arXiv | https://arxiv.org/abs/2404.13076 | 自偏好偏差：同模型自评会自我抬高 |
| R17 | Zheng et al., *When "A Helpful Assistant" Is Not Really Helpful: Personas in System Prompts…* | 2024, EMNLP Findings | https://aclanthology.org/2024.findings-emnlp.888/ | 162 persona × 2,410 题：无增益，效果近随机 |
| R18 | He et al., *Does Prompt Formatting Have Any Impact on LLM Performance?* | 2024, arXiv | https://arxiv.org/abs/2411.10541 | 纯格式改动至多 40% 波动；小模型更敏感 |
| R19 | Dubois et al., *Length-Controlled AlpacaEval* | 2024–25, arXiv | https://arxiv.org/abs/2404.04475 | 冗长可买胜率（22.9%→64.3%）；LC 后噪声 25%→10% |
| R20 | Liu et al., *Lost in the Middle: How Language Models Use Long Contexts* | 2023, TACL/arXiv | https://arxiv.org/abs/2307.03172 | 长上下文中部注意力弱 → 决定话术/硬约束位置 |
| R21 | Sharma et al., *Towards Understanding Sycophancy in Language Models* | 2023, Anthropic/arXiv | https://arxiv.org/abs/2310.13548 | 经典：人类偏好数据本身奖励"顺从用户"；反馈迎合 |
| R22 | Askell et al., *A General Language Assistant as a Laboratory for Alignment* | 2021, arXiv | https://arxiv.org/abs/2112.00861 | 经典：偏好建模偏向"听起来好"而非"正确"（HHH 语气-服从度讨论） |
| R23 | Vinay, Spitale, Biller-Andorno, Germani, *Emotional prompting amplifies disinformation generation in AI LLMs* | 2025, Front. AI 8:1543603 | https://doi.org/10.3389/frai.2025.1543603 | 情绪载荷是双刃：礼貌提示显著提高造假成功率 |
| R24 | tanweai/pua（PUA prompt 合集，中文社区"驯服 agent"话术） | 2025–26, GitHub | https://github.com/tanweai/pua | 待验证话术的现实来源（≈19.8k stars）；R6 即以该类提示为 PUA 条件 |
| R25 | *LoopTrap: Termination Poisoning Attacks on LLM Agents* | 2026, arXiv | https://arxiv.org/abs/2605.05846 | 风险侧：进度百分比/里程碑/逐步表扬可无限延长 agent 循环（P1–P10） |
| R26 | Bsharat et al., *Principled Instructions Are All You Need…* (26 条原则) | 2023, arXiv | https://arxiv.org/abs/2312.16171 | 反例教材：同文不同版本报 57.7%/67.3% vs 36.4%，人评小样本无显著性检验 → 不应采信为"激励有效"证据 |
