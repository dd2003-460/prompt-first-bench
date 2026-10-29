# T8 可解释性前沿文献调研（r51 · 纯文献，不含实验）

- **日期**：2026-10-29
- **作者**：文献调研员（arena agent）
- **任务卡**：`research/interpretability/T8-interp-research-task.md`
- **范围**：方向 1（prompt 组件消融/敏感性）、方向 2（用内部状态归因 prompt 段）、方向 3（LLM-as-judge 偏差与校准）
- **方法**：arXiv/ACL Anthology/期刊检索 + 关键条目回原文核验（标题、作者、编号、结论）。凡未回原文核验的，一律在 conf 列降档并在 §7 标注。
- **边界声明**：**本文件不跑任何实验、不改任何代码**。所有引用均为外部文献；对 pfb 仓内数据（r46/r47 的 1−cos 数值、M8 公式）只作**引用性分析**，未新增测量。

---

## 0. TL;DR（五条判定）

1. **方向 1 有成熟范式，但没有"现成工具"**。学界标准做法是「冻结基线 + 逐组件删除/替换 + 预注册指标 + 报告波动区间（spread）而非单点」。最强的方法论警告来自 FormatSpread（ICLR 2024）：语义等价的格式差异就能让准确率摆动最高 76 个点（中位约 10 点），因此**单次删除的 Δ 必须放在"格式噪声地板"之上才有意义**。→ conf 高
2. **方向 2 里，我们自研的「hidden state 余弦偏离度 top-k」不是标准 interpretability 方法，它是"表征漂移代理指标"**。标准因果归因是 **activation patching / causal tracing**（干预式，sufficiency/necessity 分开测），黑盒侧对应物是 **ContextCite**（随机消融 + 稀疏线性代理）。→ conf 高
3. **"重复造轮子"判定：部分是，部分不是。**
   - 重复的：把"偏离度排序"当作"因果重要性排序"。这条推理在文献里**没有依据**，且已知有更严格且成本可控的替代（输出空间 logprob drop / ContextCite 代理 / patching）。→ conf 高
   - 不重复的：**对"prompt 文本组件（非检索文档）"做组件级贡献归因，确实没有标准化现成工具**；PromptAnatomy 切分组件但目标是对抗鲁棒性，TokenSHAP/Shapley 是 token 级且调用成本高。缺的是**工具**，不是**原理**。→ conf 中
   - 最接近我们做法的先例存在：LAP（EMNLP 2025）证明 hidden-space 距离与最坏情况性能下降相关——**但它成立的前提是"语义等价改写"，而我们的删除操作破坏了这个前提**（详见 §2.4）。→ conf 高
4. **方向 3 我们踩的坑是"分母可变"，文献里的标准解法不是"固定 rubric"这么弱，而是"固定机会集 + 遗漏计 0 + coverage/risk 双指标 + 配对 item-level 差值"**。审计发现 pfb 现行 M8 公式 `Σ(通过权重)/Σ(全部条目权重)` 且 `未执行=权重0`，会让未执行条目**从分子分母同时消失**——这正是遗漏规避的机制。→ conf 高
5. **C3 当前方案（每配置 2 run、2 域、共 4 观测点）在文献标准下是确定性 underpowered**。Miller (2024) 的配对 + 聚类 SE + 功效公式可直接套用；n 应由最小可检测效应反推，而不是先定 run 数再解释。→ conf 高

---

## 1. 方向 1 · Prompt ablation / sensitivity 的成熟方法

### 1.1 关键工作

| # | 工作 | 链接 | 一句话结论 | conf |
|---|------|------|-----------|------|
| 1-1 | **Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design**（Sclar et al., ICLR 2024，FormatSpread） | https://arxiv.org/abs/2310.11324 | 语义等价的格式差异造成最高 76 点准确率摆动（50+ 任务平均约 10 点）；**主张报告性能区间而非单点**，并给出可在 API 模型上用的 bandit 采样算法 | **高** |
| 1-2 | **Towards Best Practices of Activation Patching in Language Models: Metrics and Methods**（Zhang & Nanda, ICLR 2024） | https://arxiv.org/abs/2309.16042 | 消融/干预的**方法学细节会改变结论**；推荐 logit difference 类连续指标、推荐对称 token 替换而非高斯噪声 | **高** |
| 1-3 | **Are All Prompt Components Value-Neutral?**（PromptAnatomy / ComPerturb, 2025） | https://arxiv.org/abs/2508.01554 | 把 prompt **自动切分为功能组件**再**逐组件扰动**，证明组件脆弱性异质；附 PPL 过滤保证扰动后文本仍自然 | **中**（预印本；但方法与我们最同构） |
| 1-4 | **Explaining LLM Decisions Using Shapley Values**（Mohammadi, 2024） | https://arxiv.org/abs/2404.01332 | 用 Shapley 值量化**每个 prompt 组件的相对贡献**；发现"token noise"——几乎无信息量的 token（空行）也能显著改变决策 | **中**（工作论文，未同行评审；结论方向与 1-1/1-2 一致） |
| 1-5 | **TokenSHAP**（Monte Carlo Shapley, 2024） | https://arxiv.org/abs/2407.10114 | 用蒙特卡洛 Shapley 做 token/片段级归因；**价值函数 = 响应与全量响应之间的 TF-IDF 余弦**（注意：它用 cosine 作价值函数，而非作重要性本身） | **中**（预印本，无顶会） |
| 1-6 | **Do LLM-Generated Skills Make Better AI Data Scientists?**（2026 预印本） | https://arxiv.org/html/2607.07504 | 7,560 runs（56 任务 × 9 配置 × 3 厂商）：**所有 p ≥ 0.396，全变体跨度仅 1.2pp**；并做了 1,512 runs 的 **token-matched 无关内容对照**——"长前缀本身"就能解释全部效应 | **低**（预印本未评审；但设计是模板级范例） |
| 1-7 | **A Prompt Sensitivity Index for LLMs**（POSIX, EMNLP 2024 Findings） | https://aclanthology.org/2024.findings-emnlp.852.pdf | 提出综合"似然/熵/语义一致性"的敏感性指数，跨任务可比；指出模板扰动与改写扰动的敏感通道不同 | **中高** |
| 1-8 | **Claude Code 的 80% 删 prompt 实践**（二手转述，Boris Cherny 访谈整理） | https://www.ai.joaoqueiros.com/blog/claude-code-cut-system-prompt-boris-cherny-ablation-playbook | 业界流程：冻结基线 → 固定 eval 集 → 先删再逐一加回，**只保留"能修复重复出现的实质失败"的指令** | **低**（二手转述，非一手论文；仅作工程佐证） |

### 1.2 这一方向的"事实标准"长什么样（跨源收敛）

四个独立来源（1-1、1-2、1-6、1-8）收敛出同一套骨架，可以直接对照 C3：

1. **冻结基线 + 冻结 eval 集**，先测**噪声地板**（format/spread/A-A 重测）。
2. **一次只改一个组件**（1-2 的核心警告）；且改动要**记为精确 diff**。
3. **等长/token-matched 对照**（1-6 做得最干净：用"连贯但任务无关"的等长内容取代随机串）。
4. **指标必须是连续、单调、不易饱和的量**（1-2）；离散准确率会在阈值处放大或掩盖效应。
5. **报告区间/CI，不报单点**（1-1）。
6. **显著性 = 与噪声地板比，而不是与 0 比**（1-1 + Miller 2024）。

### 1.3 与我们现状的差距（只作事实陈述，改法见 §4）

- 我们有"冻结 diff"（C3 修正 3）和"sham 等长替换"——**方向正确，与文献一致**。
- 我们**缺"噪声地板"的显式量化**：sham 只用作"排除位置混淆"，没有被用来定义"Δ 多大才算超出噪声"。文献要求先有地板再有判据。
- 我们**报单点 M8**，未报区间。
- 我们**没有 token-matched 的"无关但连贯"对照**（sham 目前是"中性文本替换 freeze 位"，需确认是否等长且连贯）。

---

## 2. 方向 2 · 用内部状态归因 prompt 段

### 2.1 关键工作

| # | 工作 | 链接 | 一句话结论 | conf |
|---|------|------|-----------|------|
| 2-1 | **Locating and Editing Factual Associations in GPT**（ROME / causal tracing, Meng et al., NeurIPS 2022） | https://arxiv.org/abs/2202.05262 | 用**因果中介分析**：损坏输入→逐 (层, token) 恢复干净激活→量 indirect effect；定位到中层 MLP。**这是"内部状态归因"的范式来源** | **高** |
| 2-2 | **How to use and interpret activation patching**（Heimersheim & Nanda, 2024） | https://arxiv.org/abs/2404.15255 | **denoising = 充分性，noising = 必要性，二者不对称**；多数情形**优先用 patching 而非裸消融**；指标要避免离散/过锐/饱和 | **高** |
| 2-3 | **ContextCite: Attributing Model Generation to Context**（Cohen-Wang et al., NeurIPS 2024） | https://arxiv.org/abs/2409.00729 | 黑盒侧标准解：**随机消融 context 片段 → 用 LASSO 学稀疏线性代理 → 权重即归因**；32 次消融即可；评估用 top-k 的 **logprob drop** 与 Linear Datasurrogate Score | **高** |
| 2-4 | **Towards Best Practices of Activation Patching…**（Zhang & Nanda, ICLR 2024） | https://arxiv.org/abs/2309.16042 | 见 1-2；同样适用于"用内部状态做归因"的方法学下限 | **高** |
| 2-5 | **Representation Engineering**（Zou et al., 2023） | https://arxiv.org/abs/2310.01405 | 用**对比刺激对**提取"阅读向量"，再做**双向干预**（加/减）验证因果；单侧相关性不算 | **中高**（预印本，引用极广；评审意见指出其缺 OOD 与干预对照，作者已承认） |
| 2-6 | **Steering with Activation Engineering / CAA**（Turner et al., 2023） | https://arxiv.org/abs/2308.10248 | 均值差向量 + 加法干预；**同样要求双向验证** | **中** |
| 2-7 | **Probing Classifiers: Promises, Shortcomings, and Advances**（Belinkov, CL 2022） | https://arxiv.org/abs/2102.12452 | **可解码 ≠ 被使用**；探针结论只能作相对/可提取性判断，不能直接给因果 | **高** |
| 2-8 | **Probing Classifiers are Unreliable for Concept Removal and Detection**（NeurIPS 2022） | https://arxiv.org/abs/2207.04153 | 即便概念特征可 100% 线性分离，探针仍会学到非概念特征 → **基于探针的因果结论会失效** | **高** |
| 2-9 | **Tuned Lens / logit lens 路线**（Belrose et al., 2023） | https://arxiv.org/abs/2303.08112 | logit lens "常有脆性"，tuned lens 用逐 block 仿射探针更稳；**但仍是观测性方法**，作者需另做因果实验才谈"用到相同特征" | **中高** |
| 2-10 | **FormatSpread 的内部表征分析**（同 1-1 的 §5） | https://arxiv.org/abs/2310.11324 | 格式扰动的**内部表征可分性**与性能 spread 相关——"表征变化→性能变化"有先例，但作者明确是**相关性**，不是归因 | **中** |
| 2-11 | **LAP: A Latent Adversarial Framework for Prompt Robustness**（EMNLP 2025） | https://aclanthology.org/2025.emnlp-main.1595.pdf | **关键先例**：语义等价改写中，"最坏情况的 hidden-space 距离"与性能下降**相关**，并被用作 worst-case 的指示器 | **中高**（正式发表；但设定与我们的不同，见 §2.4） |

### 2.2 原理对比：我们的方法 vs 成熟方法

| 维度 | 我们的「最后一层 hidden state 1−cos 偏离」 | Activation patching / causal tracing | ContextCite（黑盒消融+代理） | Probing | Logit/tuned lens |
|---|---|---|---|---|---|
| 操作 | **只观测**（两次前向，各取一个向量） | **干预**（把 A 的激活写进 B 的某层某位置） | **干预输出**（删片段，看概率） | 训练分类器读表征 | 解码中间层到词表 |
| 因果强度 | **无**（相关性/代理） | 强（sufficiency/necessity 可分） | 中强（输出空间干预 + 可加性假设） | 弱（2-7/2-8 明确警告） | 弱（观测） |
| 归因粒度 | 语义段（粗） | (层, token 位)（细） | 语义段/句（与需求最贴） | 概念 | 层 × token |
| 输出量 | 一个标量距离 | logit diff / KL 的**效应量** | 每片段一个**权重** | 探针准确率 | 概率轨迹 |
| 需要什么 | 一根 5120 维向量 | 中间层 hook + clean/corrupt 对 | 只需可重复调用 | 标注数据 | 中间层 |
| 主要失效模式 | 文本改动混淆、各向异性、无标定 | OOD 破坏、指标饱和、Hydra（补偿） | 非线性交互时线性代理失真 | 探针自欺 | 早期层不可读 |
| 我们的现状（r46/r47） | ✅ 已有，但 **n=1/组件、无 CI、无地板** | ❌ 拿不到中间层（llama.cpp 需改源码） | ✅ **可做**（只需重复调用） | ⚠️ 需标注数据（M8 可作标签） | ❌ 同 patching |

### 2.3 对照判断：我们是在重复造轮子吗？

**结论：是"半重复"，而且重复的那一半恰好是最不站得住的那一半。**

**(a) 重复的部分（应当承认）**
"用模型内部量来排序哪个 prompt 段重要"这个**问题**，文献里已有成熟的问法：context attribution（2-3）、component/token attribution（1-4/1-5）、activation patching（2-1/2-2）。我们的输出形态（给每个组件一个分数并排序）与 ContextCite / Shapley 的输出形态**完全同构**，只是**打分函数换成了 1−cos**。也就是说：我们不是在发明新问题，而是在一个已有问题上换了一个**更弱**的打分函数。

**(b) 不重复的部分（确实有 gap，但不是方法学优势）**
- **对象不同**：ContextCite 归因的是"检索到的 context 文档片段"，PromptAnatomy 归因的是"prompt 的功能组件"但目标是**对抗鲁棒性**（攻击成功率），TokenSHAP 是 token 级、需大量调用。**"对 6–7 段 system/流程 prompt 做组件级贡献归因，并接一个下游质量指标"确实没有现成工具**。→ 这是工程 gap，conf 中（检索非穷尽，见 §7）。
- **约束不同**：我们的现实约束是「拿不到中间层、拿不到 logprobs、只能拿一根池化向量」。在这个约束下，1−cos 是**唯一还能算的东西**——但"唯一可算"不等于"有效"。

**(c) 我们的方法在文献坐标系里的正确定位**
它不是 activation patching 的简化版，而是 **"表征漂移代理（representation-drift proxy）"**，与 2-11（LAP）同类。定位一旦摆正，两个后果必须接受：
- 它**不能**支持"该组件对 M8 有因果贡献"这类陈述（C3 修正 5 已把措辞降级为"探索性证据"——**这一步是对的，文献支持继续降级**）；
- 它的**可信度上限**由"漂移与行为的关系"决定，而这条关系在我们这个设定下**尚未被验证过**。

**(d) 最锐利的一条批评（建议写进 C3 的风险登记）**
LAP（2-11）让"表征距离预测性能下降"成立的前提是**语义等价改写**——内容不变、只是表述变。我们的操作是**删除语义内容**，于是 1−cos 里同时混进了两个东西：
1. 被删内容的**语义量**（删得越多/越实质，漂移越大）；
2. 该组件对**下游行为**的功能贡献。

文献里没有任何结果保证这两者同向。更糟的是：**r47 的排序很可能主要反映 (1)**——candidate-freeze 是四段里最长的组件，其 0.454 的偏离是否只是"删掉的 token 最多"？这个混淆**必须先排除再谈 top-k**（可廉价检验：Spearman(偏离度, 删除 token 数)）。这是本次调研给 C3 最重要的一条结构性风险，**conf 高**（机制上确定存在；具体在我们数据上是否主导，未测，conf 低）。

**(e) 该用哪个替代？**（按"性价比 / 因果强度"排序，具体落地见 §4）

| 优先级 | 替代方案 | 为什么 | 成本 | conf |
|---|---|---|---|---|
| **1（首选）** | **输出空间 logprob drop**（把基线输出在"删组件后的 prompt"下重算概率，量下降幅度） | 这是 2-2 推荐、2-3 用作 target 的**标准指标**；只需重复调用；**同一台 llama.cpp 上理论上可得**（`llama-server` 有 logprobs 能力，但**本仓 r41/r46 只验证过 ninfer 的 logprobs 不可用、llama.cpp 侧只验过 /embedding——需先实测确认**，conf 低） | 低 | 高（方法）/ 低（可用性） |
| **2** | **ContextCite 式随机消融 + 稀疏线性代理** | 能同时给出**片段权重 + 交互项检验**（线性假设可被检验，而非默认）；只需要黑盒调用；32 次消融量级 | 中 | 高 |
| **3** | **Activation patching（denoising）** | 若真需要"哪一层/哪个位置承载功能"才不可替代；我们现在的问法是"哪段 prompt"，粒度不匹配，且拿不到中间层 → **不推荐为此改 llama.cpp 源码** | 高 | 高（方法） |
| **4（保留但降级）** | 现有 1−cos，**仅作候选提出**，并加：多 seed、去中心/白化、sham 地板、token 数偏相关 | 在约束下聊胜于无；但必须写成"探索性排序" | 极低 | 中 |

### 2.4 为什么"1−cos 在一个原始 5120 维向量上"本身就弱（技术性，conf 中高）

- **各向异性 / 近单位余弦**：contextual 表征常挤在窄锥里，任意两句平均余弦可达 0.99 量级（Ethayarajh 2019；被 1-1、2103.15316 等反复引用）。此时 1−cos 的动态范围被压缩，**排序对预处理极度敏感**。
- **rogue dimensions**：Timkey & van Schijndel (2021) 证明 **常常只有 1–3 个维度主导 cosine/Euclidean**，且这些维度与模型行为重要性**不匹配**；"标准化后即可恢复"是可复现的修正手段。
- **massive activations / attention sink**：首 token 隐状态存在数量级跳变的极端维度（Sun et al. 2024；"When Attention Sink Emerges" ICLR 2025, https://arxiv.org/html/2410.10781v2）。我们取的是**最后一个 token**，避开了首 token，但 massive activation 会经残差传播；**未做去中心化时，cos 很可能由少数维支配**。
- 推论：**r47 的 0.454 / 0.428 / 0.421 / 0.325 这组数，其间距（0.03 量级）在同一量级的几何噪声下是脆弱的**。在没有 CI、没有多 seed、没有白化的前提下，**"0.428 vs 0.421"这种排序不能承载任何结论**（owner-tag 与 evidence-url 相差 0.007）。→ **conf 高（这是定义层面的判断）**

---

## 3. 方向 3 · LLM-as-judge 的偏差与校准

### 3.1 关键工作

| # | 工作 | 链接 | 一句话结论 | conf |
|---|------|------|-----------|------|
| 3-1 | **Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena**（Zheng et al., NeurIPS 2023） | https://arxiv.org/abs/2306.05685 | 系统化命名 position / verbosity / self-enhancement bias；强 judge 与人类一致率可 >80%；**给出缓解方案**（交换顺序等） | **高** |
| 3-2 | **LLM Evaluators Recognize and Favor Their Own Generations**（Panickssery et al., 2024） | https://arxiv.org/abs/2404.13076 | **自识别能力与自偏好强度线性相关**，且受控实验支持因果 → 换家族 judge 不是礼貌，是必需 | **高** |
| 3-3 | **Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge**（CALM, 2024） | https://arxiv.org/abs/2410.02736 | **12 类偏差 + 自动化"攻击-检测"量化**（Robustness Rate / Consistency Rate）；结论：**没有单一模型在所有偏差上占优** | **中高**（ICLR 系讨论度高；预印本起家） |
| 3-4 | **A Survey on LLM-as-a-Judge**（2024–2025，多版本） | https://arxiv.org/abs/2411.15594 | 汇总位置偏差校准（交换+平均）、报告 **Conflict Rate**（换位后不一致率）作为指标 | **中**（综述，二手） |
| 3-5 | **CheckEval: checklist-based judge**（EMNLP 2025） | https://arxiv.org/abs/2403.18771 | 把 Likert 打分拆成**二元清单**：跨模型一致性显著提升（Fleiss κ 最高约 0.72），与人评相关 +0.10；**清单是"固定条目集"，天然固定分母** | **高** |
| 3-6 | **IFEval**（Zhou et al., 2023） | https://arxiv.org/abs/2311.07911 | 固定 541 prompt、25 类可验证指令；**四项指标：instruction-level / prompt-level × strict / loose**——"分母定义"与"严格度"被显式拆开 | **高** |
| 3-7 | **Adding Error Bars to Evals**（Miller, 2024） | https://arxiv.org/abs/2411.00640 | 聚类 SE 可比朴素 SE **大 3 倍以上**；**比较两个配置必须做 item-level 配对差**；给出功效公式（δ、α、β → n） | **高**（有独立复现包 antonsoo/errorbars） |
| 3-8 | **Selective prediction / risk–coverage**（El-Yaniv & Wiener 2010 体系；综述性重构见多篇 2024–2025） | https://arxiv.org/html/2208.12084v2 （Calibrated Selective Classification，含 risk-coverage 定义） | **risk 是以"被接受的样本"为条件定义的**；必须同时报 **coverage**，否则"少做题"必然显得"更准" | **中高** |
| 3-9 | **Data contamination 综述**（Ravaut et al., TMLR 2025；Xu et al. 2024；静态→动态评测综述 2025） | https://arxiv.org/abs/2404.00699 · https://arxiv.org/abs/2502.17521 | 检测分"匹配类"（n-gram/成员推断）与"比较类"（性能异常/时序）；缓解走**动态基准/时间切分** | **中**（综述，二手为主） |

### 3.2 关于"可变分母"：文献怎么说（这是本方向最实用的部分）

**没有一篇论文直接写"删组件→核验条目变少→分数虚高"**（这是评测作弊的一个具体实例，不是独立研究课题）。但它的**两个成熟等价物**可以严格套用：

1. **Selective prediction 的 risk–coverage**（3-8）：`risk = E[loss | 被接受]`。学术界的处理是**永远同时报 coverage**，并且把"弃答"当成一个**有代价的动作**而不是"不计入"。映射到我们：**核验条目"未执行"= 弃答**，必须计入分母（记 0 分），不能从分母消失。
2. **固定条目集 + 双层指标**（3-6 IFEval、3-5 CheckEval）：分母由**任务输入预定义**（"这道题本来有 7 个该核验的机会"），而不是由**模型产出了几条**决定；再分 instruction-level（条目级）与 prompt-level（整题全过才算过）两种聚合，两者**不互相替代**。

**对 pfb 现行 M8 的具体诊断（引仓内文本，不新增实验）**：
`experiments/T8-matrix/design.md` 定义
`M8 = Σ(核验条目通过三测的权重) / Σ(全部核验条目权重)`，其中 `权重 = 通道 conf（独立 LLM 交叉 1.0 / agent 自检 0.2 / 未执行 0）`。
→ **"未执行 = 0 权重"意味着该条目在分子和分母里都贡献 0**，等价于**从统计中删除**。若删掉 evidence-url 组件后模型干脆不列核验条目，则"全部核验条目"这个集合**本身缩小**，M8 是剩下的容易条目上的比值 → **结构性偏向虚高**。这不是"实现 bug"，而是**指标定义把"遗漏"当成了"不存在"**。C3 修正 4 的方向（固定机会集 + M8-cover）是对的，本次调研补强其理论依据与具体公式（§4 R2）。

### 3.3 偏差处理对照表（文献共识 vs 我们的现状）

| 偏差 | 文献标准处理 | 我们的现状 | 缺口 |
|---|---|---|---|
| Position bias（3-1） | **双顺序各判一次再平均**；报告 Conflict Rate | C3 只提"随机排序呈现" | 未要求**双序平均**，无法量化 Conflict Rate |
| Self-preference（3-2） | judge 与生成**不同家族/不同模型**；或评审团 | 只说"独立 AI 裁决" | 未声明家族隔离；若 pipeline 与 judge 同源则结论无效 |
| Verbosity（3-1） | 长短期惩罚 / 长度归一 / 检查 score–length 相关 | 无 | **删 prompt 段 → 输出变短 → 可能被 judge 系统性扣分**，与我们要测的效应方向混淆 |
| 自识别/自偏好随能力上升（3-2） | 固定 judge 版本，报版本号，定期复核 | 无版本冻结 | judge 升级 = 指标漂移 |
| Score 噪声 vs 效应量（3-7） | 先算 SE，再做功效分析 | 每配置 2 run | **无可估 SE**（n=2 时区间几乎无意义） |
| 遗漏规避（3-8/3-6/3-5） | 固定机会集、遗漏计 0、coverage 与 risk 分报 | M8 单指标、分母随产出变 | **最致命**（见 §3.2） |
| Contamination（3-9） | 自建/动态题、时间切分、n-gram 检查 | 自建任务 → 风险较低 | 但 **judge 自身训练语料**可能覆盖我们的域，无法检验；如实标注局限 |

---

## 4. 给 C3 实验设计的 5 条具体修正建议

> 原则：每条都给「文献依据 → 具体改法 → 可验收的判据」。凡涉及 pfb 仓内文件的，注明改哪一行/哪个字段。

### R1 · 把 C1 从"证据"降为"先验"，并给它加三道地板（否则 top-k 不可用）
- **依据**：2-2（观测≠因果）、2-7/2-8（可解码≠被使用）、2-11（表征距离只在语义等价条件下被验证）、§2.4（各向异性/rogue dims）、1-1（格式噪声地板可达 10 点量级）。
- **改法**（对 `r47` 的 1−cos 流程）：
  1. **地板**：先对每个组件做 **sham 等长中性替换**，记录 1−cos 作为"文本改动地板" `d0`；只有 `d - d0` 才进排序。
  2. **长度偏相关**：报告 `Spearman(1−cos, 删除 token 数)`；若 |ρ| > 0.7，明确写"排序≈长度排序"，top-k **作废**。
  3. **几何校正 + 稳定性**：对向量做**去均值/按维标准化（z-score）后再算余弦**（Timkey & van Schijndel 的标准做法）；每组件 ≥3 seed × ≥3 域，报**均值 ± bootstrap CI**；**CI 重叠的组件视为并列**，不得用 0.007 的差值排序。
- **验收判据**：top-k 的每一段必须同时满足 (a) `d − d0 > d0 的 95% 分位`；(b) 与相邻名次 CI 不重叠。达不到就**只写"候选"，不写"锁定"**——现有 `r47` 结论中 `{candidate-freeze, owner-tag, evidence-url}` 的"双证据链独立收敛"表述应删除。

### R2 · 重写 M8：把"未执行"从分母外移回分母内，并拆成 truth / cover 两个数
- **依据**：3-8（risk 以 coverage 为条件 → 必须同报 coverage）、3-6（固定 prompt 集 + instruction/prompt 双层）、3-5（二元清单 = 固定条目集）、§3.2 的公式诊断。
- **改法**（改 `experiments/T8-matrix/design.md` §M8 口径那 2 行）：
  - **预注册"核验机会集"** `O(task)`：由**任务输入**决定（该任务书里可被核验的事实主张有 k 个），在跑 C3 之前冻结、写进 `experiments/T8-matrix/runs/design/`。
  - `M8-cover = |已执行核验 ∩ O| / |O|`（遗漏 = 0，零核验 = 0，**不得按满分**）。
  - `M8-truth = Σ_{i∈已执行∩O} 通过权重 / Σ_{i∈已执行∩O} 满权重`（**条件于已执行**）；
  - **联合判读表**：truth 升 & cover 降 → 判"遗漏规避"，不得报"质量提升"。
  - 聚合口径同时给 **item-level**（每条机会一个 0/1）与 **run-level**（全过才算过），两者分报（对齐 IFEval 的四指标思路）。
- **验收判据**：C3 报告里凡出现 M8 数字，必须同页出现 cover；只报 truth 的表格视为不合格。
- **附带**：judge 输入固定为「完整来源快照 + 执行日志 + 后续处置证据」，**rubric 与条目拆分规则在 C3 开始前冻结并 git commit 记 hash**（对应 3-6/3-5 的"条目集固定"）。

### R3 · 统计：从"2 run 比方差"改为"配对 item-level 差值 + 聚类 SE + 事前功效"
- **依据**：3-7（paired differences 方差更小、clustered SE 可大 3×、功效公式）、1-1（报告区间）。
- **改法**：
  - **分析单元 = (任务题, 核验条目)**，不是 run。每配置每题的 M8-truth 是**条目级比例的均值**，天然配对。
  - 主检验：`d_i = M8_A(i) − M8_B(i)`，**按任务块聚类**的 SE（同题多条目相关），单侧 t 或 **精确 McNemar**（二值场景）。
  - **事前功效**：先由 sham/A-A 估 `σ_d`，再按 `n ≈ 2(z_{1-α}+z_{1-β})²σ_d²/δ²` 反推题数；若预算只够 n=4 配对，**明确写"MDE ≈ X 点，小于该值的效应无法判定"**，而不是"未达显著 = 无效应"。
  - **多重比较**：3 个 B 组 → Holm（比 Bonferroni 更有功效，3-7 的复现包即用 Holm）。
- **验收判据**：报告必须含 `n`、`σ_d`、`MDE`、校正方法四项；缺任一视为未达统计标准。**当前 2 域 × 2 run 的设定应直接改写为"n 由 MDE 反推"，而不是复用 2 run。**

### R4 · 从"3 个单删"升级为"2³ 全因子 + 交互项"，并加 token-matched 无关对照
- **依据**：2-3（线性可加性是要被**检验**的假设，不是默认）、1-4/1-5（组件交互与"token noise"）、1-6（token-matched 对照把"长度效应"与"内容效应"分开）、2-2（Hydra/补偿：单删会低估）。
- **改法**：
  - top-k 恰好 3 个 → **跑 8 个组合**（全删/全留 + 6 个部分），而不是 3 个单删 + 全量。用线性模型 `M8 ~ freeze + owner + evidence` 估主效应与**三个交互项**；交互项显著 → 单删结果不可外推到 pipeline（正好回答任务卡 Part B 第 4 问）。
  - 成本：8 组 × 域数 × seed，与现方案（4 配置）同量级；若预算紧，**优先砍掉"阳性对照 A-full 重复"，改跑 (freeze×evidence) 两因素 4 组**。
  - **B-sham 重定义为 token-matched**：等长（±1% token）、结构相同、**连贯但任务无关**（不要随机串——文献明确警告随机串会引入不现实的干扰）。
- **验收判据**：报告含 8 组均值表 + 交互项 p 值与效应量；sham 与 full 的长度差 <1%。

### R5 · Judge 校准做成"前置门禁"，而不是事后说明
- **依据**：3-1/3-2/3-3/3-4/3-7。
- **改法**（在 C3 前跑一个 ~20–30 例的小校准集，成本极低）：
  1. **换位双判**：每对配置判 A|B 与 B|A，取平均并报 **Conflict Rate**（换位后翻转率）；>10% 视为 judge 不可用于该对比。
  2. **家族隔离**：judge 与 pipeline 生成模型**必须不同家族**；声明版本号并冻结（3-2）。
  3. **CALM 式扰动**：注入 verbosity（加长但不加信息）、authority（加伪造引用）、refinement-aware（"这是修订版"）三类扰动，测 **Robustness Rate**；若 judge 在 authority 扰动下明显加分 → 我们的 evidence-url 组件效应将与其混淆。
  4. **人工金标 + κ**：≥30 例人工双标，报 Cohen's κ；**κ < 0.6 或评分误差区间与 δ 同量级 → 先修 rubric，不进确认性实验**。
  5. **长度混杂检查**：报 `corr(输出长度, judge 分)`；删 prompt 段会缩短输出，必须确认这不是分数变化的主因。
- **验收判据**：一张校准表（Conflict Rate / Robustness Rate / κ / 长度相关），四项全过才允许开 C3 主实验。

---

## 5. 对任务卡三个"特别要查"问题的直接回答

**Q1：activation patching / causal tracing 是不是比"hidden state 余弦偏离度"更标准的因果归因手段？**
是。它们是**干预式**：patching 在 (层, 位置) 上替换激活并量输出变化，能分 sufficiency（denoising）/ necessity（noising）；causal tracing 是它在事实回忆任务上的特化（损坏主语 → 逐点恢复 → indirect effect）。我们的方法**不干预任何内部量**，只比较两个输入各自的末层池化向量，因此在因果阶梯上低于 patching，也低于"黑盒删片段 + 量输出概率"的 ContextCite。→ **conf 高**

**Q2：我们的"表征偏离度排序"在方法论上站不站得住？**
分三层回答：
- 作为**探索性候选生成器**：勉强站得住，但**必须先过三道地板**（sham 地板、长度偏相关、几何校正 + CI），且**不能称为"锁定"**。→ conf 高
- 作为**因果证据**：站不住。理由：观测非干预（2-2）、可观测≠被使用（2-7/2-8）、我们的删除操作破坏了 LAP 的语义等价前提（2-11 + §2.3d）。→ conf 高
- 作为**"双证据链独立收敛"**：不成立。C1 与 L1 共享同一批任务/模板/域（C3 修正 5 已识别此点），且 C1 的信号可能主要来自文本长度差异，故两条链**不是独立的**。→ conf 中高

**Q3：固定分母 / 覆盖率指标是不是已有共识做法？**
是，但文献里的名字不叫"固定分母"，而是 **(a) 固定条目集/清单**（IFEval、CheckEval）+ **(b) risk 必须与 coverage 同报**（selective prediction）+ **(c) 遗漏/弃答计为失败而非剔除**。三者独立来源给出同一方向。→ conf 高（方法共识）/ conf 中（是否有"prompt 消融专用"的现成协议 → 未找到）

---

## 6. 三条最容易犯、但文献已明确否定的推断（自查清单）

1. ❌"删了组件 M8 不变 → 组件无效" → 补偿/Hydra 与"可替代"必须区分（2-2、3-7 的等效性检验框架）。**C3 修正 1 已改对。**
2. ❌"Δ 超过基线重测方差 → 显著" → A−B 的方差 ≠ A 自身方差；必须配对（3-7）。**C3 修正 2 已改对，但改成"配对"后仍需功效计算，目前缺。**
3. ❌"表征偏离大 → 该组件对 M8 重要" → 需先排除长度/文本改动混淆（§2.3d）。**目前 C3 尚未处理，是本轮新增的必改项。**

---

## 7. 低 conf / 未找到 / 检索瓶颈（如实登记）

| 项 | 状态 | 说明 |
|---|---|---|
| "prompt 组件级消融已有现成工具/框架" | **未找到** | 检索到的是**方法论**（FormatSpread 有代码、ContextCite 有代码、TokenSHAP 有代码），但没有"给 7 段 prompt 自动做组件消融 + 显著性检验"的开箱工具。**不敢断言不存在**，只能说本轮渠道内未找到 → conf 中 |
| ContextCite 打败"semantic similarity"基线 | **conf 低** | 来自二手评述（Lacuna/月光摘要），**未读原论文表格**。若要用这条来论证"cosine 类方法已被证伪"，必须先读原文 §4。**本文件未把它当作核心论据。** |
| llama.cpp `llama-server` 是否暴露可用 logprobs | **conf 低（未实测）** | 仓内 r41 只测了 **ninfer** 的 logprobs/embeddings（均不可用），r46 只测了 llama.cpp 的 `/embedding`。**"改用 logprob drop"这条建议的可行性未经验证**，需一次 10 分钟的端点探测（本任务不跑实验，故只登记）。 |
| r47 的 1−cos 数值是否主要由长度/rogue dims 驱动 | **conf 低（未测）** | §2.3d 只证明**机制上存在该风险**，未在数据上验证。这正是 R1 要做的三件事。 |
| 2026 年 arXiv 预印本（2601.22025 / 2607.07504 / 2606.07237 等） | **conf 低** | 未经同行评审，且本文件只引用了它们的**设计模式**（token-matched 对照、四条件消融），未引用其数值结论。 |
| "Claude Code 删 80% prompt" | **conf 低** | 二手访谈整理，非一手论文；仅作工程界佐证，不作为方法学依据。 |
| 中文语料 / 工业界内部消融协议 | **未检索** | 本轮只覆盖英文 arXiv/ACL/期刊。中文社区与厂商内部实践（如各家 prompt 优化 SOP）未覆盖 → 明确的信息搜集缺口。 |
| "12 类偏差"在不同 judge 上的一致性 | **conf 中** | CALM 的结论是"没有单一模型在所有偏差上占优"，但我们**没有**在本地候选 judge 上实测 → 迁移性存疑。 |

---

## 8. 参考清单（按方向，全部含链接）

**方向 1**
1. Sclar et al., *Quantifying LMs' Sensitivity to Spurious Features in Prompt Design*, ICLR 2024 — https://arxiv.org/abs/2310.11324
2. Zhang & Nanda, *Towards Best Practices of Activation Patching*, ICLR 2024 — https://arxiv.org/abs/2309.16042
3. Zheng et al., *Are All Prompt Components Value-Neutral? (PromptAnatomy/ComPerturb)*, 2025 — https://arxiv.org/abs/2508.01554
4. Mohammadi, *Explaining LLM Decisions Using Shapley Values*, 2024 — https://arxiv.org/abs/2404.01332
5. Kargupta et al., *TokenSHAP*, 2024 — https://arxiv.org/abs/2407.10114
6. *Do LLM-Generated Skills Make Better AI Data Scientists?* 2026 预印本 — https://arxiv.org/html/2607.07504
7. *A Prompt Sensitivity Index for LLMs (POSIX)*, EMNLP 2024 Findings — https://aclanthology.org/2024.findings-emnlp.852.pdf
8. Cherny 访谈整理（二手）— https://www.ai.joaoqueiros.com/blog/claude-code-cut-system-prompt-boris-cherny-ablation-playbook

**方向 2**
9. Meng et al., *Locating and Editing Factual Associations in GPT (ROME/causal tracing)*, NeurIPS 2022 — https://arxiv.org/abs/2202.05262
10. Heimersheim & Nanda, *How to use and interpret activation patching*, 2024 — https://arxiv.org/abs/2404.15255
11. Cohen-Wang et al., *ContextCite*, NeurIPS 2024 — https://arxiv.org/abs/2409.00729（博客版：https://gradientscience.org/contextcite/）
12. Zou et al., *Representation Engineering*, 2023 — https://arxiv.org/abs/2310.01405
13. Turner et al., *Steering with Activation Engineering*, 2023 — https://arxiv.org/abs/2308.10248
14. Belinkov, *Probing Classifiers: Promises, Shortcomings, and Advances*, CL 2022 — https://arxiv.org/abs/2102.12452
15. Kumar et al., *Probing Classifiers are Unreliable for Concept Removal and Detection*, NeurIPS 2022 — https://arxiv.org/abs/2207.04153
16. Belrose et al., *Tuned Lens*, 2023 — https://arxiv.org/abs/2303.08112
17. Fu & Barez, *LAP: A Latent Adversarial Framework for Prompt Robustness*, EMNLP 2025 — https://aclanthology.org/2025.emnlp-main.1595.pdf
18. Timkey & van Schijndel, *All Bark and No Bite: Rogue Dimensions…*, EMNLP 2021 — 见 https://scite.ai/reports/all-bark-and-no-bite-mOPWmvL1
19. Su et al., *Whitening Sentence Representations*, 2021 — https://arxiv.org/abs/2103.15316
20. *When Attention Sink Emerges in Language Models*, ICLR 2025 — https://arxiv.org/html/2410.10781v2
21. Kornblith et al., *Similarity of Neural Network Representations Revisited (CKA)*, ICML 2019（表征相似度的方法学基准；本轮未回原文核验，仅作方法名引用）— conf 中

**方向 3**
22. Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*, NeurIPS 2023 — https://arxiv.org/abs/2306.05685
23. Panickssery et al., *LLM Evaluators Recognize and Favor Their Own Generations*, 2024 — https://arxiv.org/abs/2404.13076
24. Ye et al., *Justice or Prejudice? (CALM)*, 2024 — https://arxiv.org/abs/2410.02736（项目页 https://llm-judge-bias.github.io/）
25. Gu et al., *A Survey on LLM-as-a-Judge*, 2024 — https://arxiv.org/abs/2411.15594
26. Lee et al., *CheckEval*, EMNLP 2025 — https://arxiv.org/abs/2403.18771
27. Zhou et al., *IFEval*, 2023 — https://arxiv.org/abs/2311.07911
28. Miller, *Adding Error Bars to Evals*, 2024 — https://arxiv.org/abs/2411.00640（复现包 https://github.com/antonsoo/errorbars）
29. *Calibrated Selective Classification*（risk–coverage 定义）— https://arxiv.org/html/2208.12084v2
30. Ravaut et al., *Contamination Detection Survey*, TMLR 2025 — https://arxiv.org/abs/2404.00699
31. *Benchmarking LLMs Under Data Contamination: Static to Dynamic*, 2025 — https://arxiv.org/abs/2502.17521

---

## 9. 一句话结论

**我们造的不是轮子的形状，是轮子的替代品**：问题（哪个 prompt 段重要）是老的，工具（1−cos 末层漂移）是新但更弱的；文献给出的标准答案是"干预 + 连续指标 + 配对统计 + 固定分母 + 校准过的 judge"。**C3 不需要推翻，但必须做三件事**：把 C1 降级并加地板（R1）、把 M8 的遗漏计回分母（R2）、把 n 由 MDE 反推（R3）——这三条不做，C3 跑出来的任何"显著"都无法在文献标准下站住。

