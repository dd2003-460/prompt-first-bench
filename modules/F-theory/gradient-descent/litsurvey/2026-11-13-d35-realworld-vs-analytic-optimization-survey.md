# D35 · 真实世界迭代 vs 解析先验+泛函梯度下降（文献滚雪球补缺）

- 任务书：`tasks/T53-D35-arena-task.md`
- 前序同模块 survey：`modules/F-theory/gradient-descent/litsurvey/2026-11-12-prior-art-prompt-optimization.md`（下称 **F-旧**，conf 0.78，覆盖 ~65%）
- 消费方：`tasks/T53-D35-realworld-vs-analytic-decomp.md`（S1 同构映射 / S3 文献滚雪球 / S4 实验设计）
- 本轮定位：**只补 F-旧 点名的缺口 + 做它做不了的勘误与交叉验证**，不重做它的四条结论。
- 日期：2026-11-13 · 分支 `arena/f65a5a27-prompt-first-bench`
- 检索日志（机读）：`modules/F-theory/gradient-descent/litsurvey/search-log-d35.json`
- 来源分级口径：① 本轮现取（附 URL + read_level）· ② 工作区历史（其他 agent 取过，本轮未重取）· ③ 记忆/推断（一律 `[待核验]`，不进判决主证据）

---

## 0. TL;DR（五条判决）

**判决（总）：不是 A 还是 B 的二选一，而是"B 定函数空间 + A 估计梯度 + 控制器管非平稳"的三段式；且 F-旧 的两条 gap 判断中有一条被本轮文献直接推翻。conf 0.80**

1. **Q1 判决：文献里没有"纯 A 优于纯 B"或反向的干净对照实验；2025–2026 的强证据一致指向"B 提供结构化函数空间、A 提供在线估计与选择"。GEPA 用"自然语言反思 + Pareto 前沿"同时吃到两边的收益（比 GRPO 平均 +6%，最多 +20%，rollout 少至 1/35），是当前最强的单点证据。conf 0.78**
2. **Q2 判决：可引用的失败条件是存在的，而且能拼成一个判据——非平稳带通的变差预算下界（Besbes/Gur/Zeevi 2014）、显著漂移自适应率（Suk & Kpotufe 2022 经 2407.08654 转述）、模型误差决定模型使用量的界（MBPO 1906.08253）。但没有任何定理覆盖"策略自己改变环境"的自指情形：那一档只能靠监控（HAPO 的 Drift(t)、PromptOps 的 error-triggered controller），不能靠先验保证。conf 0.72**
3. **Q4 判决：minimax / DRO 只能形式化"对指定裁判族的最坏情况保证"，不能形式化"目标函数不被 hack"——敌手空间不是紧的、也不是可枚举的。因此防 Goodhart 的可行形态是：多样性项（不可被单通道刷分）+ 裁判轮换 + 小样本人类审计，且多样性项必须与主指标**测量通道正交**。conf 0.72**
4. **Q3 判决：<20 trials 下 BO 相对随机搜索的增量主要来自先验质量而不是采集函数；本仓库应做"结构先验 + 少量定向单因子探测"，不要上 GP-BO。conf 0.66（低，本轮未取到新实证）**
5. **勘误判决：F-旧 有 3 处 arXiv ID 指向完全无关的论文（astro-ph 宇宙学 ×2、DeFi 协议 ×1），其自评"ID 已核 0.90"不成立。凡引用 F-旧 的 ID 必须先过本文 §11 勘误表。conf 0.95**

---

## 1. 问题重述与同构映射（S1 的地基）

要优化的是一个 **LLM 研究管线的"参数"**，而不是神经网络权重。参数分三层：

| 层 | 本仓库对应物 | 离散/连续 | 评估代价 |
|---|---|---|---|
| L1 分解状态机 | `experiments/stage-ablation/s5_state_machine.py::ObjectiveConfig`（gain_threshold / verify_threshold / stop_rounds / max_kids_per_parent / fbeta_beta / contribution_threshold / lambda_uncertainty / stop_std_max） | 连续+整数混合 | 一次 bench 全跑（数十题 × 多轮 LLM） |
| L2 prompt 模板 | `s5_pipeline.py` 的 P1–P4 各阶段 prompt | 文本（不可微） | 中 |
| L3 目标函数权重 | `S_alpha_corrected()` 的 α、β；本文新增的 λ/γ/δ | 连续 | 低（可回放日志重算） |

两条路线的同构（与任务书一致，此处只补充"哪里同构得不严"）：

- **Route A ≈ model-free / policy gradient**：bench → 标量 metric → 改一处 → 重跑。同构成立在"用采样估计梯度方向"这一点；**不成立**在：① 这里的策略是确定性的参数化管线，梯度来自 1–3 次重复的噪声差分，不是 REINFORCE 的无偏估计；② LLM 的两次运行不是同分布采样（温度、缓存、检索结果都在变）。
- **Route B ≈ model-based / MBPO**：先写解析先验（哪层该宽、哪层该深、什么算"必要性"），再在函数空间里做"泛函梯度下降"（对 trace 做文本反思 → 修改结构）。同构成立在"用模型换样本"；**不成立**在：这里没有可学习的 dynamics model，先验是人类写死的结构假设 → 所谓"模型误差"其实是**先验错配**，不是拟合误差。

**这个不对称是本文全篇的支点**：MBPO 的"模型误差可控 ⇒ 多用模型"结论可以搬，但"误差可以被数据减小"这一半搬不过来——我们的先验不会因为多跑几轮 bench 自动变准，只会因为人改了它才变准。F-旧 §2 把这条记作 "policy-induced drift gap claim conf 0.70 待交叉验证"，本文 §4 给出结论。

---

## 2. Q1（最高优先级）：两条路线各自的证据强度

### 2.1 逐方法对照表（补 F-旧 §1 汇总表缺的两列）

F-旧 的表有"路线归属 / 更新信号 / Drift 感知"。本表只加它缺的两列：**是否有 held-out 泛化证据**、**是否显式处理非平稳**。

| 工作 | 路线 | 更新信号 | 显式非平稳处理 | held-out 泛化证据 | 来源级 |
|---|---|---|---|---|---|
| APE (2211.01910) | A | 候选重采样 + 分数选择 | ✗ | 部分（分 split） | ② |
| OPRO (2309.03409) | A | "meta-prompt" 读历史 top-k | ✗ | 部分 | ② |
| ProTeGi (2305.03495) | A | 文本梯度（错误归纳） | ✗ | 部分 | ② |
| DSPy/MIPROv2 (2310.03714) | B→A | 程序化模块 + 贝叶斯 opt | ✗ | ✓（train/dev 分离） | ② |
| TextGrad (2406.07496) | B | 反向文本传播 | ✗ | 弱 | ② |
| **GEPA (2507.19457)** | **A↔B** | trace 反思 + **Pareto 前沿** | 部分（Pareto 多样化防局部最优） | ✓（图 1 标注 held-out 星标） | **①** |
| **PromptOps (2611.07123)** | A + 控制器 | 5 种优化器 × 4 个运行决策 | **✓ 显式 judge drift + 触发阈值 + 冷却窗** | ✓（500-turn 流式，只用过去观测） | **①** |
| **HAPO (2601.02683)** | B（带 A 成分） | 归因 + **UCB 选编辑位置** + 漂移早停 | **✓ Drift(t)/retention + 阈值早停** | 部分（11/12 场景） | **①** |

三条新信息（F-旧 没有）：

1. **GEPA 的论点是"文本比标量奖励信息量更大"**：原文 "the interpretable nature of language often provides a much richer learning medium for LLMs, compared to policy gradients derived from sparse, scalar rewards"。这是 Route B 的最强论据，但注意它论证的是"**梯度信号形式**"，不是"先写解析结构"——GEPA 并没有先验结构，它的 Pareto 前沿是临时长出来的。**所以 GEPA 支持的是"文本梯度"，不是"解析先验"。**
2. **GEPA 的 Pareto 前沿本身就是反 Goodhart 机制**：不进化全局最优单体，而是对每个问题实例保留 top-k，迫使搜索保持实例级多样性。实测比 MIPROv2 高 +13% 聚合（MIPROv2 +5.6%）。这条可以直接搬进本仓库（见 §7）。
3. **PromptOps 明确否证"一次配置即最优"**：原文 "neither optimization algorithm choice nor update timing generalizes universally across settings"。这对"写一份解析先验然后一直用"的 Route B 是直接反证；对"跑一次 bench 就定参数"的 Route A 也是反证。**两边都被这句话打**——这正是"要控制器、不要静态最优"的文献依据。

### 2.2 Q1 判决

**判决：A 与 B 之间没有干净对照实验可引；可引的最佳单点证据（GEPA）说明"文本层面的梯度"优于"标量策略梯度"，而"解析先验"这一半要靠 PromptOps/HAPO 的非平稳证据反过来约束——结论是 B 定空间、A 定步长与停止、控制器管漂移。conf 0.78**

置信度不更高的理由：GEPA 与 PromptOps 的对照组都是各自领域（推理任务 / judge 维护）的，没有一个是"研究管线分层分解"，跨域迁移存在风险；HAPO 的 +7.21% 是对比基线平均，未给方差。

### 2.3 关于 F-旧 的 gap 判断（交叉验证结果：推翻）

F-旧 与根 `litsurvey-index.md` 跨领域缺口第 2 条都写着："**无 prior work 讨论 prompt-induced drift**"（conf 0.70，标注"待 arena 交叉验证"）。

**本轮交叉验证：该判断不成立。**

- HAPO（arXiv:2601.02683，2026-01-06）摘要即写 "current prompt optimization methods often induce **prompt drift**, where new prompts fix prior failures but impair performance on tasks the prompt previously handled successfully"，并给出可计算定义：设 t−1 轮已解集 S_{t−1}，t 轮退化集 F_t，则 Drift(t)=|F_t|/|S_{t−1}|，全局漂移取平均，超过阈值连续 S′ 轮触发保护性动作，且作为早停三个条件之一。
- PromptOps（arXiv:2611.07123，2026-11-04）把同一现象在 judge 维护场景重新命名为 "**judge drift**: a loss of agreement between a fixed judge and the intended human evaluation policy under a changing evaluation stream"，并指出 "drift can emerge solely from changes in the stream of cases being evaluated"——即**不需要模型变，评估流变就够**。
- 综述级（arXiv:2603.25681）在 §6.1 直接写："Under continual adaptation, a fixed benchmark can quickly become an unreliable target: it may be overfit through exploitation via superficial shortcuts, or simply become stale"。

**判决：F-旧 "无 prior work 讨论 prompt-induced drift" 判断被推翻（三篇独立来源，其中两篇给了可计算指标）。应当改为："2026 年起已有至少两篇工作显式定义并度量 prompt/judge drift，但都没有把它接到变差预算理论（Besbes 2014）上。" conf 0.85**

这一条对 Lead 的行动影响：**不能再用"drift 是空白"当创新点主张**。可主张的空白变成"drift 指标的预算-理论化"，这是弱得多的主张，必须重写 novelty claim。

---

## 3. Q2：可引用的失败条件与定理

### 3.1 三条可直接引用的结论

| # | 结论 | 出处 | 迁移到本仓库的含义 |
|---|---|---|---|
| T1 | 非平稳带通：变差预算 V_T 决定最小最大 regret 的量级（多项式指数形式），V_T 越大越只能用"遗忘/重启"型策略 | Besbes, Gur, Zeevi, NeurIPS 2014（**无 arXiv 版**，本轮核到 NeurIPS/MLAnthology 条目） | bench 分布变化速度决定"历史日志还能不能当证据"；不得用无限历史累积 |
| T2 | 显著漂移（significant shift）可被自适应检测，无需预知非平稳程度；Hölder/平滑环境下动态 regret ~Õ(L^{1/3}T^{2/3}) | Suk & Kpotufe 2022（AISTATS，**无 arXiv ID 可核**，经 2407.08654 的 related work 转述）② ；2407.08654 ① ；2505.18871 ① | 支持"事件触发式重分解"而非固定周期重跑：只在检测到显著变化时重置 |
| T3 | 模型误差上界决定模型可用量：悲观界太紧导致不敢用模型，用**经验估计**的模型误差可以把"短 rollout 分支"做成最优折中 | MBPO, arXiv:1906.08253（本轮核到 abs 原文）① | 解析先验只用于**短程**推理（1–2 轮重分解），超过就回真实 bench 重锚 |

**判决：T1+T2+T3 可拼成一个判据——先验可信度（短程误差小）× 非平稳速度（V_T 小）决定用 B 的比例；两者任一恶化就切回 A 并缩短记忆。conf 0.72**

### 3.2 覆盖不到的那一档（自指）

上面三条都假设"环境演化与策略无关"。本仓库不是：改 prompt/状态机会改变分解产物的分布，下一轮 bench 的观测因此**是 off-policy 的**。这一档在文献里没有定理；最接近的是：

- PromptOps 的做法：只在**过去观测**上优化（"only observations encountered so far may be accessed, never future ones"），本质是接受自指，用触发+冷却控制频率；
- HAPO 的做法：把自指后果直接度量成 retention 损失并早停；
- 综述 2603.25681 §7.1 的 "data autophagy"：迭代自产数据会降质降多样性——这是自指的**负反馈形式**，但只给了现象级描述。

**判决：自指情形的适用性只能靠"监控 + 冷却 + 周期性人类审计"保证，不能靠解析先验保证；任何声称"先验可以消除 prompt-induced drift"的说法都无文献支撑。conf 0.80**

### 3.3 与 F-旧 的两处数值口径不一致（交 Lead 复核）

1. F-旧 写 Besbes 的下界为 `Ω(√(V_T·T))`；本轮未核到公式原文，且 2407.08654/2505.18871 均以 `T^{2/3}` 型动态 regret 为基准。两者不必然矛盾（不同设定/不同项），但**不能并列引用**。标 `[待核验]`，不进判决主证据。
2. F-旧 把 "restart-on-detect" 归给 Cheung–Simchi-Levi–Zhu (1708.01799)；本轮未复查该文，按 ② 处理。

---

## 4. Q4：防 Goodhart 能否被形式化

### 4.1 能形式化的部分

DRO 框架（Rahimian & Mehrotra, arXiv:1908.05659，Open J. Math. Optim. 3 (2022) art.4）① 提供标准形态：

```
min_θ  sup_{Q ∈ 𝒰(P̂)}  E_Q[ L(θ) ]
```

把"裁判分布"当 ambiguity set 𝒰，可以形式化：
- 换裁判版本/换 judge 模型 = 换 Q；
- "同一裁判族内最坏情况不崩" = minimax over judge set，可写成有限集上的 max（本仓库就是有限的：rubric-v3.3 judge 族 × 温度 × 采样数）。

这一层是**可证明的**，而且和已有的多裁判集成/轮换实践对得上（F-旧 §4 已收）。

### 4.2 不能形式化的部分（三条，缺一不可）

1. **敌手空间不可枚举**：hack 是"人类没想到的捷径"，不是一个可参数化的分布族；𝒰 建不出来，minimax 就退化成"对已想到的几种坏法取最坏"。
2. **目标函数本身是文本**：本仓库的"目标"是一段 rubric/instructions（见 `modules/C-objective-goodhart/litsurvey/text-objective-goodhart-survey.md`，T-PR-15 结论 conf 0.7–0.8），文本的语义边界无法被精确约束 → 存在"合法但非本意"的解读空间，形式化只能约束数值层。
3. **优化压力与时序耦合**：越多轮优化，越接近 proxy 的边界（2603.25681 §7.3 "optimization-driven failures: training-time optimization against proxy rewards distorts model behavior"）；静态 minimax 不含"优化轮数"这个维度。

### 4.3 可行的折中：正交多样性项

**判决：防 Goodhart 不能被形式化成保证，只能被形式化成"上界 + 正交惩罚"；实践上正确的形态是让多样性项与主指标在不同测量通道上取值，使单通道刷分无法同时推高两者。conf 0.72**

具体形式（本文提案，直接落在 S5 现有代码上）：

```
J_t(θ) = S_α(θ) + λ·Div_t(θ) − β·Red(θ) − γ·Drift_t(θ) − δ·Cost(θ)
```

- `S_α(θ)`：现成，`s5_state_machine.py::S_alpha_corrected()`，= Σₙ[n·ln(kₙ) + α·kₙ·ln(n)] − β·redundancy·total_nodes。
- `Div_t`：**探索多样性**，本文新增。= w₁·H(每层分支度分布)/log K + w₂·(独立 edge-type 覆盖率，来自 `classify_edge` 的 edge taxonomy) + w₃·(不同来源域数 / 节点数，来自 `NodeRecord.retrieval_sources`)。
  - 关键性质：三项分别落在**结构通道、语义通道、证据通道**，与主指标（judge 分数）不同通道 → 刷分要在三个通道同时做功。
- `Red`：现成冗余罚（β=3.0，2026-11-11 已标定，罚项≈structural 5%）。
- `Drift_t`：HAPO 式 retention 损失（本文 §2.3），*新增*，现有代码完全没有。
- `Cost`：token × rollout 数，定标到同一量纲后 δ 取小值（仅用于防"无限搜索"）。

**为什么这不是单指标 Goodhart 陷阱**：
(a) `Div_t` 不是 S_α 的单调函数（S_α 奖励深宽结构，Div 奖励**分布均匀**——把 5 个子节点全挂在同一维度下，S_α 涨、Div 不涨）；
(b) 三项来自不同测量通道，无法用同一种"造同义变体"手段同时提升（这正是 β 罚当初要解决的问题，F-旧未意识到它只堵了一半）；
(c) `Drift_t` 是**跨轮**测量，单轮内怎么改都动不了它。

---

## 5. Q3（最低优先级）：<20 trials 下的预算分配

F-旧 §3 已给"grid 不可行 / random 是强 baseline / BO 在有结构时占优"。本轮**没有取到新实证**，只做两条口径加固：

1. PromptOps 的成本-误差前沿（Fig.2，23 个配置 × 2 个 judge backend × 3 次重复）是**筛选研究（screening），不是定序**——原文自述 "we use this experiment as a screening study rather than to establish a definitive ranking"。这与本仓库"n=3 重复不足以定参"的经验一致，**支持"低 trials 只做筛选、不做最优化"**。
2. 22 个配置里非支配点从便宜的 TPE(L)/Rubric 一直到 GEPA(S)→TPE(S) 复合管线 → **没有单一最优**，与 §2.1 的 PromptOps 结论互证。

**判决：<20 trials 下应做"结构先验 + 定向单因子探测"，把 BO 降级为可选；预算分配建议 4:8:4:3（基线 / 单因子 / 交互 / held-out 复核）。conf 0.66**

low conf 的理由：本轮零新增实证，纯由上一轮工作区历史 + 两项口径推断；`[待核验]` 项：Hyperband/ASHA 在小预算下的收益本轮未核。

---

## 6. 非平稳性三档分类（本仓库可直接用）

| 档 | 定义 | 本仓库实例 | 该用什么 |
|---|---|---|---|
| N1 外生漂移 | 评估流变，策略不变 | DRB 题库版本变化、题面 phrasing 变体（`T0T1T2-phrasing-gradient.md`） | PromptOps 式触发 + 冷却；保留"过去观测"日志 |
| N2 内生漂移（自指） | 策略改变导致分布变 | 改 `max_kids_per_parent` → 分解树形态变 → 后续所有观测都是 off-policy；v17 blowup 是极端形态（`research/v17-hier-decomposition-blowup.md`） | HAPO 式 retention 监控 + 周期性重分解；不可用先验保证 |
| N3 评估器漂移 | 裁判/rubric 版本变 | RACE 相对评分漂移（T53C X1 已记录）、rubric-v3.1 修复 | **先固定版本再比较**；跨 bench 排名一律作废 |

**判决：三档必须分开治理，混在一起会出现"以为在调参、其实在追着裁判版本跑"的假收敛。conf 0.75**

---

## 7. A vs B vs 结合：结合的具体形式（本任务的核心交付）

### 7.1 一句话

**用 B 写出函数空间与短程动力学（结构 + 哪些参数单调、哪些交互），用 A 在这个低维空间里做少量真实测量，用控制器（PromptOps）决定何时重新测量，用 drift 监控（HAPO）决定何时扔掉历史重写先验。**

### 7.2 具体架构（四段 + 两条回路）

```
                    ┌──────────────────────────────┐
                    │ P0 写先验 (Route B, 人写)      │
                    │  - 定 θ 维度与单调方向假设    │
                    │  - 定 J 的项结构 (S_α/Div/…)  │
                    └──────────────┬───────────────┘
                                   │ 结构假设 h
                    ┌──────────────▼───────────────┐
                    │ P1 短程"模型内"推演 (B)       │  支路长度 k ≤ 2 轮重分解
                    │  - 在日志上做反事实回放        │  (= MBPO 的 short rollout)
                    │  - 文本反思产生候选改动 (GEPA) │
                    │  - Pareto 保留实例级 top-k     │
                    └──────────────┬───────────────┘
                                   │ 候选 Δθ（≤8 个）
                    ┌──────────────▼───────────────┐
                    │ P2 真实测量 (Route A)         │  只测候选，不测网格
                    │  - bench 重跑，n≥3 重复        │
                    │  - 记录 ΔJ 与方差              │
                    └──────────────┬───────────────┘
                                   │ 实测
                    ┌──────────────▼───────────────┐
                    │ P3 控制器 (PromptOps)         │
                    │  - trigger: 窗内 ΔJ ≤ −τ 触发 │
                    │  - cooldown: w 轮内不再触发    │
                    │  - 预算守卫: cost > 上限即停   │
                    └──────────────┬───────────────┘
                          ┌────────┴─────────┐
                   Drift ≤ κ │                  │ Drift > κ 或 先验连续 2 次失准
                          ▼                  ▼
                    回到 P1            回到 P0（重分解/重写先验）
```

两条回路对应文献的两条结论：
- **内回路（P1↔P2↔P1）= MBPO**：短程用模型、长程回真实数据。MBPO 的依据是"经验模型误差"可估；我们的对应物是**回放误差**：用日志回放预测 ΔJ，与实跑 ΔJ 的偏差就是"先验错配度"（可直接算，见 §7.4）。
- **外回路（P3 → P0）= PromptOps 的 trigger + HAPO 的 drift early-stop**：先验失准不是靠"调得更细"解决，而是靠**降级重写**。

### 7.3 落成公式（与现有代码逐字段对齐）

```
θ* = argmax_θ  J_t(θ),  J_t = S_α(θ) + λ·Div_t(θ) − β·Red(θ) − γ·Drift_t(θ) − δ·Cost(θ)

S_α      ← s5_state_machine.py::S_alpha_corrected()            （现成，不改）
Red      ← redundancy_score() × cfg.redundancy_penalty_beta    （现成，β=3.0）
Div_t    ← w₁H(k)/log K + w₂·edge_type_coverage + w₃·src_domains/n   （新增）
Drift_t  ← 1 − |re-run(θ_prev) 仍判为 verified 的节点| / |verified(θ_prev)| （新增，HAPO 口径）
Cost     ← tokens + c·rollouts                                  （新增，仅守卫）
```

**θ 的搜索只用 8 个参数**（ObjectiveConfig 里已存在），不要搜索 prompt 全文——这是"B 定空间"的实际含义：把无限维文本空间压到 8 维 + 有限个文本候选。

### 7.4 先验错配度的可计算定义（本仓库独有优势）

日志里已有每节点 `retrieval_sources`、`contribution`、`edge_type`。因此：

```
ε_prior = mean | ΔĴ_replay(θ) − ΔJ_measured(θ) | / std(ΔJ_measured)
```

- ε_prior < 1：先验可用，P1 可以多推几步（k 可到 2）；
- ε_prior ≥ 1：先验不比噪声准，退化为纯 A（k=0），只在真实 bench 上做单因子探测。

这比 MBPO 的"模型误差"更容易算，而且**不需要 dynamics model**——因为日志就是模型。

### 7.5 与本仓库 S5 现有设计的差异（对标 `experiments/stage-ablation/`）

| 项 | 现状（S5） | D35 建议 | 依据 |
|---|---|---|---|
| 目标函数 | S_α − β·Red（结构 + 反冗余） | + λ·Div − γ·Drift | §4.3、§2.3 |
| 停止判据 | `stop_criterion=necessary` + `stop_std_max` 方差守卫 | 保留，但方差守卫**不能**替代 drift 守卫（前者防采样噪声，后者防分布变化） | PromptOps/HAPO |
| 重分解触发 | 无（人工改配置重跑） | 事件触发：窗内 ΔJ ≤ −τ 且超过冷却 w | T2、PromptOps |
| 历史利用 | 全量日志 | 变差预算 → 截断窗口（V_T 大则窗口短） | T1 |
| 探索 | 冗余罚（只反塌缩，不促探索） | Div 项（促探索） | §4.3 |
| 参数搜索 | 人工扫参 | 8 维 + 单因子 4:8:4:3 预算 | §5 |

**判决（结合的具体形式）：B 的产物是"8 维参数空间 + J 的项结构 + 短程回放器"，A 的产物是"每个候选的实测 ΔJ 与方差"，控制器决定两者的切换频率；三者缺一，要么退化成无先验的随机搜索，要么退化成不可验证的先验教条。conf 0.79**

---

## 8. 反方复核（≥3 条质询与回应）

**反方复核 1：GEPA 的 35× 样本效率是在 6 个 benchmark 上、对 GRPO 24k rollouts 比的；本仓库 bench 只有几十题、没有 verifier 训练集，"文本梯度"会不会直接退化成过拟合 dev set？**
回应：会。GEPA 原文只报 held-out 星标，没有报 held-out 的方差；而 PromptOps 明确记录 "recovery after recalibration rather than invariance"、且 "adaptation can cause specialization"。所以本仓库必须把 **test 集冻结 + 每轮只允许一次改动**，否则文本梯度就是在背题。此质疑使 Q1 conf 从 0.85 降到 0.78。

**反方复核 2：你说"没有任何定理覆盖自指情形"，但 prompt 改变环境本质上就是"环境 = 策略的函数"，这类问题在 RL 里叫 non-stationary MDP / adversarial MDP，也许已有界，只是你没搜到。**
回应：承认检索不完整。本轮只覆盖了 bandit 侧（T1/T2）与 model-based 侧（T3），**没有系统检索 adversarial MDP / endogenous dynamics**。该方向 `[待核验]`，本轮不给判决，标为缺口。这不改变"本仓库现在不能用定理保证"的实践结论。

**反方复核 3：多样性项 Div 本身就是一个可被优化的代理，模型会学会"造多样性"而不是"探索"。这不过是把 Goodhart 从主指标挪到 Div 上。**
回应：部分成立，这是本文最弱的一环。缓解三点：(a) Div 三项跨通道（结构/语义/证据），造假的成本高于收益；(b) Div 只在**未访问**子空间上计算（novelty 而非 count），重复造同类不算；(c) Div 的权重 λ 由人固定、不参与搜索（冻结 λ 是防"优化 Div"的关键）。但必须承认：**λ 固定意味着 J 不是完全自动的**，本方案的定位是"人在回路的结构化搜索"，不是"自动发现目标函数"。

**反方复核 4（自加）：你说的 3 处 ID 错误，会不会是你 fetch 到了错误的 arXiv 页面？**
回应：三处都是 arxiv.org/abs 的标题/分类原文：2101.05574 = astro-ph "cosmic distance duality"；1403.3919 = astro-ph "relic gravitational waves"；2202.06384 = cs.GT "FairTraDEX"。三者与 RL/bandit 无关，且 D35 同时独立核到 MBPO 正确 ID = 1906.08253（arxiv abs 原文，Janner/Fu/Zhang/Levine）。误抓三篇无关论文且恰好都被同一份 survey 引用，概率极低。

---

## 9. 对本仓库的可执行结论（给 `tasks/T53-D35-realworld-vs-analytic-decomp.md` S4 用）

1. **不要再把 "drift 无人研究" 当创新点**（§2.3，conf 0.85）。改写为"drift 的预算-理论化 + 自指档的处理"。
2. **目标函数立刻加 Div 与 Drift 两项**（§7.3），Div 的 λ 冻结不参与搜索。
3. **实验设计**：8 维参数、4:8:4:3 预算、每轮一次改动、test 冻结、n≥3 重复、报告 ΔJ 与 std。
4. **必测的对照**：① 纯 A（随机单因子）；② B-only（先验给定不做实测）；③ 本文结合式（回放预筛 + 实测）。指标除 J 外必须报 Div 与 Drift，否则无法区分"真提升"与"追着裁判跑"。
5. **先修 ΔJ 的噪声底**：`stop_std_max=0.06` 是 P5 回标值；任何小于该噪声的"提升"不得宣称。

---

## 10. 与 `litsurvey-index.md` 的关系

本轮只更新根索引 `F-theory/gradient-descent` 一行（第 15 行）。**未修改 F-旧 文件本身**（保留其作为历史工件），但 F-旧 的 3 处 ID 错误与 1 处 gap 判断已在本文件 §11 / §2.3 给出勘误，引用前必须先看勘误表。

---

## 11. 附录 B：F-旧 arXiv ID 勘误表（**引用前必读**）

| F-旧 中的写法 | 实际指向 | 正确处理 | 本轮证据级 |
|---|---|---|---|
| PlaNet = 1811.04551 | 未核（本轮未取） | 保留 `[待核验]` | ② |
| MBPO = **2101.05574** | ❌ astro-ph，Qin/Melia/Zhang "Test of the cosmic distance duality relation" | **改 1906.08253**（Janner, Fu, Zhang, Levine, NeurIPS 2019） | ① arxiv abs 原文 |
| Besbes et al. 2014 = **1403.3919** | ❌ astro-ph，Zhao/Cheng/Huang "Hint of relic gravitational waves" | Besbes/Gur/Zeevi **无 arXiv 版**；引 NeurIPS 2014 pp.199–207（MLAnthology 条目） | ① |
| Suk & Kpotufe 2022 = **2202.06384** | ❌ cs.GT，FairTraDEX（DEX 协议） | 该文本轮未定位到 arXiv ID；引 AISTATS 2022，或经 2407.08654 转述 | ①（证伪 2202.06384）/ ②（正确定位） |
| AdaPrompt = `[待核验]` | ✅ 有 ID：**2202.04824** | Chen, Liu, Dong, Wang, Zhu, Zeng, Zhang, "AdaPrompt: Adaptive model training for prompt-based NLP" | ①（两个独立参考文献列表一致） |
| Metelli 2018 OPE variance | 未核 | 保留 ② | ② |
| Cheung–Simchi-Levi–Zhu 1708.01799 | 未核 | 保留 ② | ② |

**判决：F-旧 的"arXiv ID 已核（0.90）"自评不成立——3/7 被本轮核到的 ID 指向无关论文。凡下游引用 F-旧 的任何 ID，必须先过本表。conf 0.95**

---

## 12. 附录 A：来源分级表（本轮全部引用）

| # | 来源 | URL | 级 | read_level | 用在 |
|---|---|---|---|---|---|
| 1 | PromptOps: Iterative Prompt Optimization for LLM-as-a-Judge (2611.07123) | https://arxiv.org/html/2611.07123 | ① | full（§1–§4.2，11 chunks 中的 0/3） | Q1/Q2/§6/§7 |
| 2 | HAPO: Hierarchical Attribution Prompt Optimization (2601.02683) | https://arxiv.org/html/2601.02683 | ① | partial（abstract + intro + related + §method 摘录） | Q1/§2.3/§4.3 |
| 3 | GEPA: Reflective Prompt Evolution (2507.19457) | https://arxiv.org/html/2507.19457 | ① | partial（abstract + §1） | Q1/§4.3 |
| 4 | MBPO: When to Trust Your Model (1906.08253) | https://arxiv.org/abs/1906.08253 | ① | abstract + 摘录 | Q2 T3/§7.2 |
| 5 | Besbes, Gur, Zeevi, Non-stationary MAB (NeurIPS 2014) | https://mlanthology.org/neurips/2014/besbes2014neurips-stochastic/ | ① | abstract | Q2 T1 |
| 6 | Adaptive Smooth Non-Stationary Bandits (2407.08654) | https://arxiv.org/abs/2407.08654 | ① | abstract + related 摘录 | Q2 T2 |
| 7 | Non-Stationary Lipschitz Bandits (2505.18871) | https://arxiv.org/pdf/2505.18871v1 | ① | partial（摘录） | Q2 T2 |
| 8 | Self-Improvement of LLMs: Technical Overview (2603.25681) | https://arxiv.org/html/2603.25681v3 | ① | partial（§4/§6/§7 摘录） | Q1/Q4/§2.3 |
| 9 | DRO: A Review (1908.05659) | https://arxiv.org/abs/1908.05659 | ① | abstract | Q4 |
| 10 | AdaPrompt (2202.04824) | https://arxiv.org/pdf/2205.05638v2（他文参考文献） | ① | ID 级（内容未读） | §11 勘误 |
| 11 | 反证材料：2101.05574 实为 astro-ph | https://arxiv.org/abs/2101.05574 | ① | abstract | §11 勘误 |
| 12 | 反证材料：1403.3919 实为 astro-ph | https://arxiv.org/abs/1403.3919 | ① | abstract | §11 勘误 |
| 13 | 反证材料：2202.06384 实为 FairTraDEX | https://arxiv.org/abs/2202.06384 | ① | abstract | §11 勘误 |
| 14 | OPRO (2309.03409) | — | ② | 工作区历史 | §2.1 |
| 15 | APE (2211.01910) | — | ② | 工作区历史 | §2.1 |
| 16 | ProTeGi (2305.03495) | — | ② | 工作区历史 | §2.1 |
| 17 | DSPy/MIPROv2 (2310.03714) | — | ② | 工作区历史 | §2.1 |
| 18 | TextGrad (2406.07496) | — | ② | 工作区历史 | §2.1 |
| 19 | EvoPrompt / PromptBreeder / PromptAgent | — | ② | 工作区历史 | §2.1 |
| 20 | PlaNet (1811.04551) | — | ② | 工作区历史 | §11 |
| 21 | Suk & Kpotufe 2022 (AISTATS) | — | ② | 经 2407.08654 转述 | Q2 T2 |
| 22 | Cheung–Simchi-Levi–Zhu (1708.01799) | — | ② | 工作区历史 | §3.3 |
| 23 | Metelli 2018 OPE variance | — | ② | 工作区历史 | §11 |
| 24 | T-PR-15 文本目标函数 survey（本仓库） | modules/C-objective-goodhart/litsurvey/text-objective-goodhart-survey.md | ② | 工作区历史 | Q4/§4.2 |
| 25 | Skalse et al. 2210.10760（hackability） | — | ② | 工作区历史（T-PR-15 已判 conf 0.75） | Q4 |
| 26 | F-旧 survey（本模块） | modules/F-theory/gradient-descent/litsurvey/2026-11-12-prior-art-prompt-optimization.md | ② | 工作区历史 | 全篇基线 |

统计：**① 本轮现取 13 条**（其中 read_level ≥ abstract 的 12 条，12 条中有 7 条读到摘要以外的正文），**② 工作区历史 13 条**，合计 26 条 ≥ 20；③ 记忆级一律未进判决。

---

## 13. 附录 C：未找到 / 未核验（如实记录，conf ≤ 0.3）

| 项 | 尝试的查询 | 结论 |
|---|---|---|
| adversarial MDP / endogenous dynamics 下"策略改变环境"的 regret 界 | 未检索（本轮时间预算用在 Q1/Q2/Q4） | **未找到**；不构成否定性证据，仅"本轮未覆盖"，conf 0.2 |
| Suk & Kpotufe 2022 的 arXiv ID | 检索 "Suk Kpotufe Adaptive Nonstationary Bandits arXiv id" | **未找到**（只有转述）；标 `[待核验]`，conf 0.3 |
| Besbes 2014 的精确指数与 F-旧 `Ω(√(V_T·T))` 口径 | 未逐字核到公式 | **未核验**，conf 0.3，不进判决 |
| Hyperband/ASHA 在小预算（<20 trials）的实测收益 | 未检索 | **未找到**，conf 0.2 |
| prompt drift 的"预算-理论化"（把 Drift(t) 接进 V_T） | 检索 drift + variation budget | **未找到**任何工作做这件事。按"搜了没找到"纪律只能给 conf 0.3；即使日后被证实为真空白，也需 Lead 二次交叉验证后才能作为行动前提 |
| planning / world model 在文本策略空间的直接应用 | 未检索 | **未找到**，conf 0.2 |

---

## 14. 一句话总结

**解析先验负责"别在无限文本空间里瞎搜"，真实迭代负责"别相信自己没验过的先验"，控制器负责"别用过期历史"，多样性项负责"别被自己写的指标骗"——四件事各司其职，任何一件被省掉，路线选择就变成教条选择。**
