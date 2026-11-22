# T-PR-17 结果 — Prompt 序列消融文献滚雪球（C1-C3）

- 任务书：`experiments/stage-ablation/tasks/T-PR-17-task.md`（sha256 `3153398feb1af439f1fc4e80c3515685ee7c7834bd997a614dd2a0eb275fe405`）
- 分支 `arena/f65a5a27-prompt-first-bench` @ `585b02a` · 2026-11-22 · 中文
- 纪律执行：**7 个 arXiv ID 全部经 abs 页核对**（§检索记录逐条标 ✅）；OpenReview 2025-2026 已查（2 次，见 §检索记录 #7/#8）；否定性结论 conf ≤0.6。

## §C1 多阶段 pipeline 中「阶段顺序/编排」的效应

| 项 | 内容 |
|---|---|
| **verdict** | **部分有先例**：阶段「有/无、粒度、深度、结构搜索」都有系统研究；但**「内容固定、只置换阶段顺序」的对照实验未找到**（该否定部分 conf 0.55） |
| 反例/近邻 | ① **PIVOT 2605.11225**（arXiv 2026-05，cs.AI）：PLAN→INSPECT→EVOLVE→VERIFY 四阶段框架，**逐阶段 disable 消融**（摘录：Verify −13.3 avg 最大，Plan −11.4、Evolve −10.8、Inspect −4.2）→ "阶段可省性"有先例；但它是**删阶段**不是换顺序，且消融在自家方法内。`[数字来自 HTML 摘录，未逐行核全文]` ② **STIG 2601.09728**（arXiv 2025-12）：把 agentic workflow 的 8 个阶段压成 stage token，**8 阶段 vs 4 阶段粒度对比**（8 阶段全指标更好）→ "阶段粒度"有先例。`[粒度消融数字来自 PDF 摘录]` ③ **AFlow 2410.10762**（arXiv 2024-10，v4 2025-04）：把 workflow 表述为"LLM 节点 + 边的代码图"，用 MCTS 在结构空间搜索，均涨 5.7% → "结构（而不仅是内容）决定效果"被实证，且结构可被显式优化。④ `2509.11079`（DAAO，query-specific workflow 深度/算子分配）`[未过 abs 页，仅搜索摘录，未验证]`。⑤ **OpenReview/KDD 2025 Workshop「The Order Effect」（Guan et al.）**：输入**顺序**打乱可致最多 **13.95%** 掉点 → 顺序敏感性有 OpenReview 侧证据（但对象是上下文输入顺序，不是 pipeline 阶段顺序）。 |
| **conf** | **0.62**（"部分有先例"）；其中"无顺序置换专门研究"这一否定判断单独 **conf 0.55** |
| 对我们设计的含义 | 阶段"可省性"已被做过（PIVOT），所以**单纯"删 verify 更好/更差"不构成 novelty**；真正没被占的是：**同一中间 checkpoint + 仅改后续阶段顺序**的对照，且用**多档 depth 分**而非端任务精度验收。 |

## §C2 「固定中间状态 → 不同后续策略续跑 → 比终态」

| 项 | 内容 |
|---|---|
| **verdict** | **有先例（强同构）** |
| 反例/近邻 | ① **The Handoff Tax 2608.24358**（arXiv 2026-08，cs.AI）：**几乎就是我们想做的设计**——固定中间状态（"保留 repository 状态 W_K"），只变"跨模型边界传什么"（Raw 全轨迹 / Compact_pre / Compact_suf / Traj-drop），比**终态质量 + 成本**；结论：full-trajectory 升级只回收不到一半的质量差并付成本溢价（handoff tax），且**最优接口随方向反转**。② **PIVOT 2605.11225**：保留已验证 prefix、只重写 suffix（prefix-preserving continuation），并证明"局部修"优于全局重规划 → 续跑位置的因果性有实证。③ `2607.27937`（OVCSD，从 student-reached state 续跑 + 首个分歧点比较）`[未过 abs 页，未验证]`。 |
| **conf** | **0.80**（同构程度高）；差异点：Handoff Tax 变的是"交接接口/模型"，我们要变的是"prompt 序列"，但**实验骨架（固定状态、变后缀、比终态+成本）完全一致** |
| 对我们设计的含义 | 不能说"无人做过从中间状态续跑"。可以主张的差异：**变量换成阶段序列**（而非交接格式）、**验收换成多档 depth 分**、**同模型同接口**（排除 handoff 混淆）。Handoff Tax 的"最优接口随方向反转"是个警告：**续跑效应可能是方向依赖的，不能把所有 checkpoint 混在一起统计**。 |

## §C3 机制映射：位置/长度效应能否解释序列效应

**三条传导路径（都可引用）**
1. **位置效应**：阶段顺序变 → 中间状态块在最终 prompt 中的相对位置变 → U 型注意力偏置。`Lost in the Middle` **2307.03172**（TACL 2023）：相关信息在开头/结尾最好、**中间显著退化**；`Found in the Middle` **2406.16008**（ACL Findings 2024）：把该现象归因于**内在 U 型注意力偏置**，并用 calibration 抵消，RAG 最多 +15pp。
2. **长度效应**：阶段多少/是否省略 → 状态总 token 数变 → **即使检索完美、无干扰、证据紧贴问题，输入变长本身也让性能掉 13.9%–85%**（**2510.05381**，Findings of EMNLP 2025）。
3. **顺序效应**：单纯输入顺序置换即可致最多 13.95% 掉点（Guan et al., KDD 2025 Workshop, OpenReview 侧）。

**逐臂判定（我们的 4 臂）**

| 臂（canonical 之外） | 主要操纵了什么 | 有多大可能只是位置/长度效应的下游 | conf |
|---|---|---|---|
| 顺序置换 | 块位置 + 排列顺序 | **很大**——这是三条路径叠加最严重的一臂 | 0.60 |
| 删 verify | 内容/证据过滤（长度小幅变） | **小**——内容变了，位置解释不了 | 0.65（认为存在真实内容效应） |
| minimal（少阶段） | 阶段数、状态总长 | **中等偏大**——长度效应可解释相当部分 | 0.55 |
| canonical（基线） | — | — | — |

**总判定：序列效应 ≈ f(内容, 长度, 位置)，三者在我们当前设计里**没有被分离**。若不控制长度与位置，"顺序置换臂"的 depth 分差异很可能主要复现的是已发表的位置/长度效应，而不是 pipeline 结构本身的因果贡献。conf 0.7**

**给实验设计的 5 条硬建议（可直接改 decomp）**
1. **长度匹配控制臂**：让各臂喂给 synthesize 的 state token 数落在同一区间（±10%），否则长度效应冒充序列效应（2510.05381）。
2. **位置旋转**：同一 state 块在 prompt 里做 头/中/尾 三位置旋转，把"位置"当随机因子而不是混淆变量（2307.03172 / 2406.16008）。
3. **null control（必做）**：不换阶段、只随机重排 state 块顺序，测出"纯位置扰动"的 depth 分波动 X；序列效应必须 **> X** 才算真。
4. **每臂 n≥5 + CI**：本文库已知合成方差（同树 coverage 0.857↔1.0），n=3 会出假阳性。
5. **checkpoint 分开统计**：Handoff Tax 显示效应随方向/状态反转，别把不同 checkpoint 的续跑结果混池。

## §检索记录（通道 + query + 结果）

| # | 通道 | query / URL | 结果 |
|---|---|---|---|
| 1 | web_search | `ablation study order of stages in multi-stage LLM pipeline workflow orchestration structure vs content` | → STIG 2601.09728、DAAO 2509.11079、PaperPilot 2607.00597、Scepsy 2604.15186 |
| 2 | web_search | `path dependence LLM agent continuation from fixed intermediate state different subsequent strategies` | → Handoff Tax 2608.24358、OVCSD 2607.27937、PIVOT 2605.11225 |
| 3 | web_search | `"context length alone" hurts LLM performance despite perfect retrieval` | → 2510.05381 |
| 4 | arXiv abs | `arxiv.org/abs/2410.10762` | ✅ AFlow（节点+边代码图，MCTS 结构搜索） |
| 5 | arXiv abs | `arxiv.org/abs/2605.11225` | ✅ PIVOT（四阶段 + 逐阶段消融） |
| 6 | arXiv abs | `arxiv.org/abs/2601.09728` | ✅ STIG（stage token，8/4 阶段粒度） |
| 7 | arXiv abs | `arxiv.org/abs/2608.24358` | ✅ Handoff Tax（固定 repository 状态，变交接接口） |
| 8 | arXiv abs | `arxiv.org/abs/2307.03172` | ✅ Lost in the Middle（TACL 2023） |
| 9 | arXiv abs | `arxiv.org/abs/2406.16008` | ✅ Found in the Middle（ACL Findings 2024） |
| 10 | arXiv abs | `arxiv.org/abs/2510.05381` | ✅ Context Length Alone Hurts（EMNLP Findings 2025） |
| 11 | **OpenReview API** | `api2.openreview.net/notes/search?term=prompt pipeline stage order&limit=10&source=forum` | ✅ 通道可用；命中 **KDD 2025 Workshop「The Order Effect」**（Guan et al.，顺序打乱最多 −13.95%）；其余为 DBLP 噪声（Order types/数据集采样论文） |
| 12 | **OpenReview API** | `api2.openreview.net/notes/search?term=path dependence continuation intermediate state agent ablation&limit=5&source=forum` | ✅ 通道可用；**无相关命中**（返回 homotopy continuation ICML2023、多智能体药物发现、dependence logic）→ 支撑 C2 在 OpenReview-only 侧无同题投稿 |

**通道登记**：arXiv API `id_list` 在上一任务连挂 3 次，本轮**未再尝试**，按要求直接走 abs 页（7/7 成功）；OpenReview API v2 **本轮可用**（2/2 成功），但**相关性排序差**（DBLP 全库索引，需人工筛）。

## §方法学缺口（不粉饰）

1. **OpenReview 只做了 2 次关键词检索**，不是 ICML/NeurIPS/ICLR 2025-2026 的**逐 venue 扫描**；API 无 venue 过滤 + 相关性差，覆盖必然不全。**C1/C2 的"未找到"仅在这 2 次检索的意义上成立**（conf ≤0.6）。
2. **未检索 ACL Anthology**（任务书允许的三通道之一），EMNLP/ACL 主会可能有 OpenReview/arXiv 都没收录的顺序消融研究。
3. **PIVOT 的逐阶段消融数字、STIG 的粒度对比**来自 HTML/PDF 摘录而非逐行核全文 → 标 `[摘录级]`，进入判决时已降权。
4. **两条 ID 未验证**（`2509.11079` DAAO、`2607.27937` OVCSD）——已在文中显式标 `[未过 abs 页]`，未进 verdict 主证据。
5. **C3 的机制映射是文献推理，不是本库实测**：我们 pipeline 的中间状态是结构化树（非平铺文档），位置效应在树状 JSON 上**是否同样 U 型，未验证**。建议用 null control（§C3 建议 3）先测这一点。
