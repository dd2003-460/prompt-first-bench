# T-PR-16 结果：对抗核验 novelty + 时间尺度 TCO 滚雪球

- 任务书：`tasks/T-PR-16-task.md`（sha256 `dacfc44b47fcbaf5fadc529ff6d48ce1ded7da99016cc38ad0f61a652e5e979c`）
- 分支：`arena/f65a5a27-prompt-first-bench` @ `ecd99a8`
- 日期：2026-11-21 · 中文 · 每条带 conf

## §A 对抗核验（3 条 verdict）

| # | 问题 | verdict | 反例 / 近邻（ID · venue · 一句话） | conf |
|---|---|---|---|---|
| A1 | 有没有 2024-2026 论文同时用 ≥2 约束 + 树 + 过程/深度判分？ | **部分站得住（表述过强，需改写）** | ① **OHD 2602.01969**（ICML 2026）：正交树归纳 + 行列双向**层级依赖** + 树表示 → 已含「正交+依赖+树」两约束一树，但评测是端任务 EM/LLM-eval，**无过程判分**。② **SPRING 2609.34660**（NeurIPS 2026）：**约束追踪 + 一致性 + 非冗余（压缩）** + 逐步过程奖励（"novel reasoning step"）→ 已含「多约束+过程分」，但**无 gold 树**。③ **RPTS 2511.06899**：推理树 + 逐节点加权 faithfulness → 「树+过程分」。④ **TreeReview 2506.07642**（EMNLP 2025 main）：递归问题树 + 自底向上聚合 → 「树分解」。**没有任何一篇把三者放进同一个评测协议**（gold 树 + 逐判定点打分）；但"无人组合"字面已被部分证伪——OHD 与 SPRING 各占两块，审稿人会判为"把两篇拼起来"。 | 0.62 |
| A2 | depth 作为一等指标 + 多档连续分有先例吗？ResearchRubrics 的 logical nesting 怎么打分？ | **部分站得住** | **ResearchRubrics 2511.07685**（arXiv 2025-11，2,593 rubrics）：① logical nesting **是任务级三档标注**（Shallow / Intermediate / Deep，§3.2 Table 2），**不是判分维度**；② 判分是**逐 criterion 三元**（Satisfied=1 / Partial=0.5 / Not=0，权重 [-5,5] 后加权归一，§3.4 Eq.1）→ **"非二元多档"已有先例**（三元）。所以我们的差异只剩「每判定点 3-6 档 + 深度档位化」这一档粒度；「depth 当一等指标」也有近邻（Rubrics 把 nesting 当复杂度轴、TreeReview 做树结构/深度消融）。 | 0.55 |
| A3 | 3 棵 gold 树 vs RPTS 390 棵，"差 2 量级"是否致命？有 <50 实例的顶会树评测先例吗？ | **部分站得住（量级质疑不致命，但需要论证"每例信息密度"）** | 小规模被顶会接收**有先例**：**ResearchCodeBench**（arXiv 2506.07972，**ICLR 2026**）用 **20 篇**新论文做基准；**TreeReview**（EMNLP 2025 main）用 **80 篇**（40 ICLR-2024 + 40 NeurIPS-2023，人工评测各 10 篇）。但**严格"<50 实例 + 树结构评测"的先例本轮未找到**（ResearchCodeBench 非树，TreeReview 80>50）。这些先例靠"每例极贵（专家复核/人工 review）"撑规模，pfb 的 3 棵树若不能证明同等标注强度，量级质疑会变成"数据不足"而非"篇幅问题"。 | 0.7 |

**A 段总判决**：原 novelty 声明（"无人组合"）**站不住字面**（conf 0.62 指向部分证伪），建议改写为更窄、可防的版本：
> 「已有的两两组合（OHD=约束+树、SPRING=约束+过程分、RPTS=树+过程分）都**用端任务精度或训练奖励**验收；没有工作把三者做成一个**带 gold 树与逐判定点连续分的评测协议**，并报告该协议的复现性（n=10 轮 + CI + 效应量）。我们的 novelty 在**评测协议**，不在组合本身。」
这样改后 conf 可回到 0.75，且 A3 的量级质疑可用"协议可复现性"对冲。

## §B 滚雪球（3 条结果）

| # | 问题 | 结果 | 论文 / 证据 | conf |
|---|---|---|---|---|
| B1 | 有没有把 TCO 沿**时间轴**递归拆（瞬时 vs 长期 vs 价格波动）？ | **有先例（强），"时间尺度分解 TCO"本身不新** | ① **arXiv:2509.26534** "Rearchitecting Datacenter Lifecycle for AI: A TCO-Driven Framework"：TCO=CapEx+OpEx，**按资产寿命分时间层摊销**（facility 15-30 年 / network 7-10 年 / IT 3-5 年）+ build→provisioning→operate 三阶段，含硬件换代与老化。② **arXiv:2509.07567** "Navigating Energy Doldrums"：TCO=F+E，用 2024 实时电价按**不同时间尺度采样**（周 vs 更短）判断临时关机可行性——即「价格波动 × 时间尺度」进 TCO 的正式模型。③ **arXiv:2607.07207**（2026-07）：2026-2030 情景分析，base/shortage 两条**价格分支** + 折旧传送带 + vintage breakeven。 | 0.85 |
| B2 | 有没有让 LLM **自主**产出带时间尺度的成本分解树？ | **未找到**（近邻三篇都不满足） | 近邻：**ACEM arXiv:2608.02582** 把 agentic 开发成本拆成 LLM/HITL/infra 三维 + Revision/Context factor，但是**人定的固定结构、无时间轴、非 LLM 生成**；**TCA arXiv:2609.23790** 把多 agent 成本按工作流**深度**归因（depth 1 时 memory injection 份额 0% → depth 6 时 27.6%）——**结构深度维度**的成本归因已有，但非时间维度；**BAVT arXiv:2603.12634** 树搜索带成本函数，但是推理期预算控制不是 TCO 分解。 | 0.6（否定性结论，按纪律不高于 0.6） |
| B3 | GPU 价格波动/市场周期作为 TCO 决策变量，有量化研究吗？ | **部分有先例（同行评议薄，行业分析多）** | ① **arXiv:2607.07207**：显式把 GPU 价格分 base（HBM 2028 正常化）与 shortage（涨到 2030）两支，算出 entrant/incumbent 成本差 3.2×→1.9×→3× 的路径，并给 **U 型 vintage breakeven** 曲线——即是"价格路径变→结论翻转"的量化。② 行业分析（非同行评议，仅作旁证）：Silicon Analysts 2026 GPU rental 分解给出**敏感性排序**——利用率 50%→90% 使 H100 需求溢价 $1.98→$2.85/hr（摆动 ~45% 大于任何输入价差），**折旧年限为第二杠杆**（3 年 $1.49/hr vs 5 年 $0.90/hr）。③ Intel 白皮书（PC refresh 2-5 年 + EAC/NPV）是更早的同构实践。 | 0.7 |

**B 段总判决**：**"时间尺度 × TCO 分解"不是空白，是 HPC/数据中心领域十年老题**（conf 0.85）。真正未占领的窄缝是「LLM 自主生成 + 逐节点 + 时间尺度」三合一（B2 未找到，但 TCA 已在深度维度做了同类事，空间很窄）。若在论文里主张 TCO 时间分解为 novelty，会被 2509.26534 / 2509.07567 / 2607.07207 直接打掉。

## §C 检索记录（可复现）

| # | 通道 | query / URL | 结果 |
|---|---|---|---|
| 1 | arXiv abs | `arxiv.org/abs/2602.01969` | ✅ OHD，ICML 2026（ID 正确） |
| 2 | arXiv abs | `arxiv.org/abs/2611.20755` | ✅ GPRM，PRM 四维过程评估（ID 正确） |
| 3 | arXiv abs | `arxiv.org/abs/2610.04721` | ✅ Knossos/Ariadne，19,200 图（ID 正确） |
| 4 | arXiv abs | `arxiv.org/abs/2609.34660` | ✅ SPRING，NeurIPS 2026（ID 正确） |
| 5 | arXiv abs | `arxiv.org/abs/2602.09341` | ✅ AgentAuditor（注意：系统名 AgentAuditor，不是 AgentAudit） |
| 6 | arXiv abs + html §3.2/§3.4 | `arxiv.org/abs/2511.07685`、`arxiv.org/html/2511.07685v1` chunk 2-3 | ✅ 三元判分 Eq.1 与 nesting 三档表 2 |
| 7 | web_search | `benchmark <50 expert instances accepted NeurIPS ICLR tree structure` | → TreeReview 80 (EMNLP 2025)、ResearchCodeBench 20 (ICLR 2026) |
| 8 | web_search | `total cost of ownership decomposition time horizon price volatility depreciation GPU` | → 2509.26534、2509.07567、2607.07207、Intel 白皮书 |
| 9 | web_search | `LLM agent generates cost breakdown structure decomposition tree cost estimation` | → ACEM 2608.02582、TCA 2609.23790、BAVT 2603.12634 |
| 10 | web_search | `GPU price volatility depreciation market cycle sensitivity procurement` | → 2607.07207 + Silicon Analysts / Introl / Barrack（行业） |
| 11 | arXiv API | `export.arxiv.org/api/query?id_list=…` | ❌ 连续 3 次失败（`Failed to fetch page`）；改用 abs 页逐个核 ID |

**通道故障（需 Lead 知悉，非静默跳过）**：arXiv API 的 `id_list` 批量查询在本会话不可用（3 次均失败），已降级为逐个 abs 页核验；OpenReview API / ACL Anthology 未逐条检索（时间预算），故 A1 的"OpenReview 2025-2026 全量扫描"**未完成**——这是本报告最大方法学缺口。

## 附录：未验证 / 未覆盖（如实登记）

1. **RPTS 2511.06899 本轮未复核**（沿用工作区 ② 记录：390 推理实例、逐节点加权 faithfulness）——`[未验证]`。
2. **OpenReview（ICML/NeurIPS/ICLR 2025-2026）未系统检索**：A1 的结论只覆盖 arXiv 近邻 + 1 次 web 检索，若有 OpenReview-only 的投稿（未上 arXiv）组合了三要素，本报告会漏。
3. **GPRM 2611.20755 的"四维评估"是否等价于"过程判分多档"**：摘要只说四维（look back/look ahead/self-check/goal alignment），未见档位定义 → `[未验证]`，故不计入 A1 反例。
4. **ResearchRubrics 的 logical nesting 是否参与最终分数**：§3.2 明说用于"分析模型在哪一维更弱 + 过滤子集"，未见进入 Sk 公式 → 判为"非判分维度"，conf 0.85。
5. **行业分析的数值**（Silicon Analysts / Introl / Mercatus）为博客自述、无同行评议，仅作 B3 旁证，不入主证据。
6. 本轮未检索非英文（中文/日文）TCO 文献与厂商白皮书库。
