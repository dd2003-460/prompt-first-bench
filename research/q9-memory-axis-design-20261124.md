# Q9 gold 骨架 · 记忆轴机制设计（DreamCoder/LILO 映射）
# origin: ai · 2026-11-24 · 应用映射 E 的具体化
# 上游: research/dreamcoder-lilo-stitch-collision-20261123.md (应用 A-E)
# 下游: q9-gold-skeleton-arena-taskcard.md 任务卡 A 背景段（D 确认题面后注入）
# 状态: 设计非实验；最便宜第一实验 = 跨 run claim 库 2 臂（Q6 150 档复用 harness）

## 问题：记忆轴为什么是空的

Q9 题面 5 因子之一"记忆轴（跨 session 状态保持）"目前只有一句话定义，
gold 骨架建定时 arena 会拿这句话去调研——但没有机制锚点，调研会发散
（跨 session 状态保持可以是 RAG、可以是 checkpoint、可以是库）。
DreamCoder/LILO 给出一个有先例、可测量、且直接服务排序键的机制。

## 机制：跨 run claim 库（DreamCoder 语言扩展 + LILO 库学习的 research 域 analog）

### 结构（三组件，对应 LILO 的 synthesize/compress/document 分工）
1. **库本体**：历史 run 的 verified claim（status=verified 且 evidence 非空），
   每条 = {claim, source, question_id, budget, rep, verified_at}。
   从现有 83-run 语料 + 重跑批直接抽取，零新增成本。
2. **注入（synthesize 半边）**：decompose LLM 搜索前，按 question 相似度
   注入 top-k 相关库条目（k=5 起步，[待标定]）。= DreamCoder 的
   "语言扩展"（新符号抽象供搜索用）的 analog。
3. **压缩（STITCH 半边）**：库条目晋升时做近重复合并（cos≥0.85 的
   claim 合并为单条抽象条目），防止库膨胀稀释注入质量。
   STITCH 算法细节（2211.16605）：自底向上从原语构建 + 语法模式匹配剪枝
   + 对早停鲁棒 → research 域映射：库从 verified claim 增量构建，
   每轮跑不完就早停，不等全树收敛。
4. **适用条件 docstring（AutoDoc 半边）**：库条目晋升时生成自然语言
   命名 + 适用条件（何时该用/何时误用）。LILO 实证 AutoDoc 提升下游性能；
   research 域误用比 code 域更危险（错误 claim 注入 → 污染整棵研究树）。

### 为什么直接服务排序键（单位预算闭环成功率 post_acc）
- 库命中 → 省掉"重新发现"消耗的检索节点 → 同 150 预算下更多节点
  用于新 claim → coverage 升。
- 库条目带 verified 状态 + source → 注入后 verify 成功率高 → post_acc 升。
- 可检验预测（2 臂对照，Q6 150 档，复用现有 harness）：
  ① cov 升（库供给本该消耗节点的重新发现）
  ② post_acc 升（verified claim 注入）
  ③ 检索节点占比降（省掉的重新发现）
  ④ rep 方差降（**注意方向**：库是故意耦合 rep 的共享先验，
     与重跑批 rep 独立性实验相反 → 必须独立臂，不能改重跑批）

### 与 P1 实测的连接（为什么这不是空想）
P1 阈值梯度验证（2026-11-23 23:48，goal state 记录）：原批 300 档 r1×r2 claim 重叠
0.95:0.0 / 0.90:0.3 / **0.85:4.7** / 0.80:15.7 / 0.75:32.7%（平滑无尖峰）
= 95.3% 的 claim 每个 run 独立重新发现 = DreamCoder/LILO 用库学习消掉的浪费。
库机制直接攻击这个浪费。

## gold 骨架里的落点（任务卡 A 背景段注入内容）

记忆轴因子下的 3-6 子节点（arena 调研后定稿，以下是机制锚点非结论）：
- [记忆轴] 跨 run claim 库：verified claim 抽取 → 相似度注入 top-k → 省重新发现节点 | 测量口径: 库命中时 cov/post_acc vs 无库基线 | 来源: DreamCoder 2006.08381 + LILO 2310.19791 + STITCH 2211.16605 | conf 0.7（机制有先例，research 域 gap conf 0.6 待 arena 核验）
- [记忆轴] 库条目压缩：近重复合并（cos≥0.85）防库膨胀 | 测量口径: 库大小 vs 注入质量 | 来源: STITCH 2211.16605 | conf 0.7
- [记忆轴] 库条目适用条件 docstring：何时该用/何时误用 | 测量口径: 误用率（注入后 verify 失败占比） | 来源: LILO AutoDoc 2310.19791 | conf 0.6
- [记忆轴] 库质量 × 预算 Pareto：库养得好 → 小预算覆盖大预算覆盖 | 测量口径: 150 节点+库 vs 300 节点无库的 cov 对照 | 来源: 本设计推导 | conf 0.5 [待实验]

## 边界
- 这是设计不是实验；第一实验 = 2 臂 × 150 节点（Q6 harness 复用），
  按 D 11-23 纪律排 workshop 里程碑后。
- gap 判断（开放 research 域无先例）conf 0.6，派发 arena 时作为
  交叉验证项（任务卡 B 独立核验）。
- 库机制与"rep 独立性"方向相反：库臂必须独立于重跑批，
  不能改重跑批的 Q6_REP 设置。
