# 阶段 02：信息研究（仓库内既有实现精读）— RV3G3-threshold-crossdomain-reverify

> 事实源全部只读；本 goal 无外部事实主张，无网络需求。所有引用带文件+行号/JSON path。

## R1 · 复算协议提取（骨架必须逐字对齐的权威实现）

**来源**：`ablation/scripts/assert-goldrank-threshold.py` L60-107 + `assert-gmr-recompute.py` L13-45

| 协议要素 | 权威定义 | 出处 |
|---------|---------|------|
| GOLD 集合 | `["N-2.1", "N-3.2.2", "N-2", "N-4", "N-1.3"]`（5 节点） | assert-gmr-recompute.py L13；goldrank-threshold-proof.md L31 声明同一清单 |
| w2_exact(p) | `p is None → F(1)`；否则 `F(min(-log2(F(p)), log2(1/EPS))).limit_denominator(10**6) + 1`，EPS=0.01 | assert-goldrank-threshold.py L38-42 |
| 七方案合成 | W1=`w1`；W2-orig=`w2_exact(p_tilde)`；W3-orig=`w1×w2_exact`；W4-orig=`w1+w2_exact`；new 侧从 blindtest `w3_full_ranking[]` 取 `{node, w1, w2, w3}`，W2-new=`w2`、W3-new=`w3`、W4-new=`w1+w2` | assert-goldrank-threshold.py L90-99 |
| top-10 计数 | `sorted(ws.items(), key=(-float(w), nid))[:10]` 中 ∈ GOLD 的个数（tie-break = 节点 ID ASCII 字典序） | assert-goldrank-threshold.py L101-104 |
| gmr | rank 0-based，并列组内按 order_fn 排序；`gmr = Σ rank(gold)/5` | assert-gmr-recompute.py L31-39 |
| tie 枚举（gmr 版） | 三 order_fn：lo=gold 优先 / hi=gold 靠后 / mid=纯字典序 | assert-gmr-recompute.py L41-43 |

**关键发现 K-R1**：第一域 tie-sensitivity 结论（proof L57「全量合法 tie-break 置换枚举验证」）在既有脚本中**没有落盘为可复用函数**——assert-gmr-recompute.py 只做三 order_fn 极值（对 gmr 是精确 min/max，因 gmr 是 gold ranks 之和且 gold 相对顺序唯一影响极值），而 **top-10 计数的「全量置换枚举」逻辑不存在于任何既有脚本**。本 goal 骨架必须新写该枚举器（见 03 A2）。

## R2 · 「全量合法 tie-break 置换」的可计算化

**问题**：权重并列组 G₁..Gₘ（组大小 s₁..sₘ），合法 tie-break = 各组内部任意排列，总数 Π sᵢ! —— 全量枚举在组大时爆炸。

**可计算化引理**（骨架采用）：top-10 计数只依赖「切线两侧各有哪些 gold」。设按 (−weight, id) 排序后的名次序列，cut 位于第 10/11 位之间。则：
- 计数变化只可能来自**跨越 cut 的并列组**（即存在成员分列 rank≤10 与 rank≥11 的同权组）；
- 不跨 cut 的组无论怎么排，其成员在 top-10 内的数量不变；
- 单个跨 cut 组（大小 s，其中 g 个 gold，x 个当前在 top-10 内）在 top-10 内可取的 gold 数 = `[max(0, g − (s − x)), min(g, 10 − (in_top10_non_gold))]` 区间内的整数（取决于该组多少成员被排进前 10）。

**多组交互**：多个跨 cut 组共享 10 席预算时，计数可达集合 = 各组可选 gold 数的背包式组合。骨架用**动态规划**求可达计数集合（状态 = 已用席位，转移 = 每组可选 gold 数 × 非 gold 占用），复杂度 O(m × 10²)，无枚举爆炸。单组情形退化为闭式区间。

**验证锚点**（骨架自测必须复现的第一域事实，proof L57）：
- W3-orig/W4-orig：无任何并列组 → 可达集合 {4}（tie-robust）
- W3-new：并列组 {10.0: N-1,N-2} 在 rank 0-1、{3.725: …} 在 rank 20+，均不跨 cut → 可达集合 {4}
- W2-new：跨 cut 组 {2.737: N-1.1.2, N-1.3.1, N-2.1, N-5.3}（4 节点含 2 gold… 注：N-1.3.1/N-2.1 中仅 N-2.1 ∈ GOLD）→ 可达集合 [2,3]（proof L57 原文「可取 [2, 3]」）

⚠️ 待 04 现场核对：W2-new 跨 cut 组的 gold 成员构成需从数据实算确认（上行为预判，以 04 变异测试实测为准）。

## R3 · r136 schema 预注册模式（骨架结构模板）

**来源**：`ablation/scripts/assert-kappa-receipt.py` L1-40

模式四要素：① docstring 内嵌最小 schema（每字段带注释与理由）；② 三分支判定（缺失→FAIL exit 1 / schema 违例→FAIL / 数值边界→SIGNAL exit 0）；③ 派生量禁双写（gate_passed 类字段不设，现场计算）；④ 常态 FAIL/SIGNAL 是预期行为（回执不存在时不伪造转绿）。

**本 goal 适配**：第二域数据不存在 = 「回执缺失」同构 → 常态 **SIGNAL blocked-on-external + exit 0**（区别于 kappa-receipt 的 FAIL exit 1——本 goal 的「缺数据」不是违规而是等待外部，语义更近 signal-only 的 assert-prior-source.py；此选择登记为设计决策 D4，04.5 复核对象）。

## R4 · L4.2 条件 (a)(b) 的机判映射

**来源**：`bench/rubric-v3/goldrank-threshold-proof.md` L83

- **(a) t=4 过线集合跨域稳定** → 第二域各方案 top-10 gold 计数 ≥4 的方案集合 S₂，与第一域 S₁={W3-orig, W4-orig, W3-new} 对照。判定语义（01 D3）：S₂==S₁ → PASS；|S₂|==|S₁| 但成员不同 → SIGNAL（人工裁决）；否则 FAIL。
  - ⚠️ 口径注意：第一域 S₁ 含 new-judge 侧方案。第二域若只有 orig judge，可比集应限定 orig 侧 {W3-orig, W4-orig}——**D5 设计决策**：脚本按输入 JSON 实际含哪些方案做「同方案名对照」，不强行要求 7 方案齐全（缺 = 该方案不参与对照并登记）。
- **(b) tie-sensitivity 审计** → 对第二域每个过线方案跑 R2 可达计数集合：过线方案的所有合法 tie-break 下计数恒 ≥4 → tie-robust；存在 <4 的可达值 → tie-sensitive（FAIL，除非降级路径）。全部过线方案 tie-robust → (b) PASS。

## R5 · 空缺核验结果

| 01 空缺 | 02 核验 |
|---------|--------|
| K1 第二域 hit-matrix | 确认不存在（`find bench -name "*batch2*"` 零命中）→ 外部阻塞维持 |
| K2 gold 集合沿用 | 题面冻结依据确认：变体矩阵六变体同题面（DRAFT v2 batch1 冻结，revision-log R-10）→ D1 默认沿用成立；换题面必须显式 gold_nodes 声明 |
| K3 双侧对称 | blindtest `w3_full_ranking` schema 确认 `{node, p_tilde, w1, w2, w3}`（judge-blindtest-r1.json 首元素实证）→ 第二域 new 侧 JSON 可直接镜像该 schema |
| K4 量化判据 | R4 已给出三分支；无新增空缺 |

## 负面结果声明

- N1：第一域「全量置换枚举」验证（proof L57）**无落盘代码**，其结论目前只有文档记载——本 goal 的 DP 枚举器是对该结论的首次可复现化（附带价值：可对第一域重跑回归）。
- N2：hit-matrix.json 在本 goal 复算协议中**未被消费**（top-10 计数走 prior-estimates + blindtest 权重，与第一域脚本一致）——queue 条目「消费第二域 hit-matrix」表述修正为：hit-matrix 是第二域数据的组成部分（h 值供未来 claim 级判据），但 (a)/(b) 两条件的复算协议与第一域相同，只需权重侧输入。此修正登记入 04 工件。