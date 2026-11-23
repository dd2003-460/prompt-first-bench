# DreamCoder / LILO / STITCH 撞车调研 + 应用映射（2026-11-23）
# origin: ai · D 2026-11-23 指令："调研这个文献然后看看和我们什么撞车以及可以如何应用"
# 来源①：arXiv API 本轮实查（https 通道）+ 本地 lit 覆盖检查（local-first 四步走完）

## 文献地图（arXiv 实查，conf 0.9）

| 系统 | 出处 | 结构 | 分工 |
|---|---|---|---|
| DreamCoder | 2006.08381 (2020, Ellis/Wong/Nye/…/Tenenbaum) | wake-sleep 交替：①语言扩展（新符号抽象）②神经引导网络在想象+重放问题上训练 | 神经网络引导搜索，符号语言存抽象；重发现函数式编程/向量代数/牛顿库仑定律 |
| LILO | 2310.19791 (ICLR 2024, Grand/Wong/Bowers/Olausson/Liu/Tenenbaum/Andreas) | 迭代：LLM 综合 → STITCH 压缩（找最优 lambda 抽象）→ AutoDoc（自然语言命名+docstring） | **LLM 负责带领域先验的搜索，符号系统 STITCH 负责压缩**；三个 benchmark（字符串编辑/场景推理/图形组合）超 DreamCoder |
| STITCH | **2211.16605** (2022-11, Bowers/Olausson/Wong/Grand/Tenenbaum/Ellis/Solar-Lezama, "Top-Down Synthesis for Library Learning") — 2026-11-24 从 LILO 参考文献定位（LILO 引用 "Bowers et al., 2023"） | corpus-guided top-down synthesis：从 DSL 原语出发构建抽象，中间抽象的**语法模式匹配**剪枝搜索空间，导向最大化捕获语料共享结构的抽象 | 压缩器本体；比 DreamCoder 演绎式库学习**快 3-4 个数量级、省 2 个数量级内存**，质量（compressivity）相当或更好；可扩展到数百复杂程序；**对早停鲁棒**（early stopping 仍可 scale） |
| Solomonoff/AIT | 经典（Li & Vitányi） | 归纳 = 偏好低 Kolmogorov 复杂度的贝叶斯推理 | 理论根基；D 11-07 note 已有（compression-unified-view，含 MDL/2509.22445） |

## 撞车判决（逐层）

1. **"搜索求解 + 共用抽象重构进库"的结构** → **撞车**（DreamCoder 2020 / LILO 2024，conf 0.95）。不是新结构。
2. **"LLM 搜索（带先验）+ 符号系统压缩"的分工** → **撞车**（LILO/STITCH 原话，conf 0.95）。
3. **理论根基（Solomonoff/MDL）** → **撞车且 D 已有**（compression-unified-view-2026-11-07.md，D 11-07 独立走到 + AI 补 MDL/ALBI/2601.00086 脚手架，conf 0.9）。
4. **把这套循环用在开放 research（非固定文法 program synthesis）** → **未见先例**（conf 0.6，查询覆盖有限）：
   - `library learning × research agent` → 空
   - `reusable knowledge × program synthesis × research` → 空
   - `DreamCoder × research` → 只有 ARA 基准（固定文法）
   - **差异点**：DreamCoder/LILO 有固定基语言+文法+验证器（程序跑不跑得通例子）；开放 research 没有验证器、没有固定文法——"压缩对象"是研究树/claim，"验证"是 judge/证据。这个 gap 是真实的但需要 arena 交叉核验（查询词可能没覆盖到）。
5. **与本地工作的同构**：S5 状态机 = "搜索求解"半边（decompose LLM + research_hook + marginal_gain J_decomp + rework/verify）；**缺的是"重构进库"半边**——P1 实测 rep 间 claim 重叠仅 4.7%（0.85 阈值）= 每个 run 独立重新发现相同 claim，正是 DreamCoder/LILO 用库学习消掉的浪费。gold 树/ rubric 是静态人工库，不是从系统自身 run 长出来的。

## 应用映射（research-agi-budget goal，按性价比排序）

### A. 跨 run claim 库（最便宜，现有数据+设施直接测）
- 机制：把历史 run 的 verified claim（带 source）建成库；decompose LLM 搜索前注入 top-k 相关库条目（= DreamCoder 语言扩展的 analog）。
- 可检验预测：①CACHE-HIT 率升（claim 收敛到库条目 → cache key 命中）②同预算 coverage 升（省掉重新发现）③rep 方差降（**注意方向**：库是故意耦合 rep 的共享先验，与当前重跑批的 rep 独立性实验相反 → 必须独立臂，不能改重跑批）。
- 设施：P1 重叠梯度 + Q6 gold coverage 都是现成测量。

### B. 状态机内压缩步（STITCH analog）
- 机制：每轮结束后对当前树做符号压缩——跨分支找近重复 claim（cos≥0.85），合并为单个抽象节点，更新 parent。
- 直接攻击"46-unit 分辨率饱和"：合并近重复叶子 = 提高有效覆盖分辨率。
- 设施：marginal_gain 已有 embedding，复用。

### C. AutoDoc analog（库条目的适用条件）
- LILO 实证：AutoDoc 提升下游性能（综合器能"解读并部署"学到的抽象）。
- 映射：库条目晋升时生成自然语言命名 + **适用条件 docstring**（何时该用/何时误用）——没有适用条件的库条目会被误应用，这是 research 域比 code 域更危险的失败模式。

### D. 理论框架（论文用）
- 库条目值得加 ⟺ 未来期望描述长度降幅（少重新发现）> 条目自身成本（记忆+误用风险）。
- = MDL 检验 = D 的"奥卡姆=先证必要再引入"的形式化。接 D1-generalization 压缩/泛化实证线。

### E. 与当前 goal 的直接连接（⑤ gold 骨架）
- **库 = "小预算→压缩细节"的机制本体**：库养得好，150 节点 run 能覆盖 300 节点 run 的覆盖（库供给本该消耗节点的重新发现）。
- **库质量是预算 Pareto 前沿的隐藏因子** → Q9 gold 骨架的"记忆轴"（5 因子之一）目前在工作区是空的（盘点无实现）——DreamCoder/LILO 给记忆轴提供了具体机制。这是 ⑤ 的直接输入。

## 边界与待核验
- ~~STITCH 独立论文未定位~~ → **已定位：2211.16605**（2026-11-24，LILO 参考文献 "Bowers et al., 2023" 对应 "Top-Down Synthesis for Library Learning"；arXiv API 实查摘要确认 "We present an implementation of the approach in a tool called Stitch"）。
- **STITCH 算法细节对应用 B 的启示**（2211.16605 摘要，conf 0.9）：①从原语**自底向上**构建抽象（不是全局找重复）②中间抽象做**语法模式匹配**剪枝 ③**对早停鲁棒**——映射到 research 域：claim 库可以从已验证 claim 增量构建，每轮跑不完就早停，不用等全树收敛。
- "gap 真实" conf 0.6：arXiv 查询覆盖有限，下一步走 arena 交叉核验（红线 1：调研核验外包）。
- 应用 A/B/C 是设计不是实验；最便宜的第一个实验 = A（Q6 上 2 臂 × 300 预算，复用现有 harness）。
- arXiv API 本轮用 http://export.arxiv.org 实际有返回（与 11-21 记录的"返回空"不一致，可能不稳定；后续统一走 https）。
