# gmr 主判据预注册冻结件

> goal: RV3G6-gmr-tiebreak-prereg · 分支 ralph/rv3g6-gmr-tiebreak-prereg · 2026-10-30
> 上游：`AUDIT-report.md` §3.2（L100）/ §3.3（L112-122）/ §8（L248-272）
> 状态：**判据冻结** — 正式实验开跑前必须引用本文件，不得另行定义 gmr 口径。

---

## 1. tie-break 规则（文字化）

### 1.1 规则定义

**预注册 tie-break = 节点 ID 字典序（ASCII 升序）。**

具体操作：当两个或多个节点的方案权重值精确相等时，按节点 ID 字符串的 ASCII 字典序排列——字典序较小的节点获得较优（较小）的 rank 编号。rank 从 0 计，越小越好。

等价表述（三选一，语义相同）：
- 「节点 ID 字典序」（AUDIT-report §3.2 L100 原文用语）
- 「落盘顺序」（= stats 文件 `sorted(nodes)` 现用规则，即 Python `sorted()` 对字符串的默认排序）
- 「id tie-break」（G5 负面结果第 3 条 / AUDIT §8 规则 1 用语）

### 1.2 为何不用其他 tie-break

| 候选 | 拒绝理由 |
|------|----------|
| 分数并列时取平均 rank（fractional/Borda） | 引入非整数 rank，破坏「rank 为整数、可逐节点报出」的可机判性；且使 gmr 变为连续量中的连续量，丧失离散可审计性 |
| 随机 tie-break | 不可复现，违反预注册原则 |
| 各方案取各自最优 tie-break | **明确禁止**（AUDIT §8 规则 3）：构成 post-hoc model selection，消除判据的事前约束力 |
| 按 gold 标记优先排序 | 循环论证：用被评估对象（gold 命中）决定排名，使 gmr 恒等于最优值 |
| 按发现时间/深度排序 | 无先验依据，引入额外自由度 |

**唯一合法操作**：跨方案比较一律在本节定义的 tie-break 下进行（AUDIT §8 规则 3 原文见 §4）。

### 1.3 适用边界

- 本规则适用于 **global 口径**（31 节点全排序）下的 gmr 计算。
- per-run 口径（单 run 内 31 节点排序）同理适用，但 per-run gmr 目前不作为过线判据（仅辅助描述）。
- W0 flat 方案下所有节点权重 = 1，全部并列 → gmr 无意义（完全平局），不适用本规则（G5 负面结果 10）。

---

## 2. 过线阈值（引用机制 + 锚点 + 门禁）

### 2.1 引用机制（不写死数值）

**gmr 本身是方案间比较指标（连续量），不作单方案裸过线判据。**（AUDIT §3.2 L100 定位声明）

pass/fail 过线功能由 **top-10 辅助口径**承担。其阈值：

```
threshold_top10 := RV3G3-goldrank-threshold-proof 产出值
```

在 RV3G3-goldrank-threshold-proof 完成并 merge 之前，**本仓库内任何文档/脚本不得将 top-10 过线阈值写为具体数值**。引用时只能写「阈值待 RV3G3 正式论证」。

### 2.2 当前锚点（超几何参考值，非定论）

基于 n=31 节点、k=5 gold、r=10 抽取的超几何分布：

| 量 | 值 | 计算 |
|----|-----|------|
| E[X] | ≈ 1.61 | k·r/n = 5×10/31 = 1.6129 |
| P(X≥4) | ≈ 2.7% | Σ_{i=4}^{5} C(5,i)·C(26,10-i) / C(31,10) = 0.027438 |
| P(X≥3) | ≈ 17.6% | 同上 i=3..5 = 0.175751 |

来源：G3 F3b（`g3-w3w4-completion.md` L51）+ 本 goal 阶段 02 独立复算（math.comb 精确值 1.6129/0.027438/0.175751）。

**这些是锚点不是结论**：它们说明 ≥4 是严判据（~2.7% 基线率），但不能替代正式论证（需考虑 gold 集非随机抽样、节点间相关性、多 judge 方差等）。

### 2.3 使用门禁

| 条件 | 状态 | 效果 |
|------|------|------|
| RV3G3-goldrank-threshold-proof 完成 | ❌ 未完成（queue 中） | top-10 计数**不得**用于正式 pass/fail 判定 |
| gmr 用于方案间排序比较 | ✅ 可用 | 带 §4 限定语即可 |
| gmr 用于单方案绝对过线 | ❌ 禁止 | gmr 是相对量，无绝对过线语义 |

**一句话**：RV3G3 完成前，gmr 只做方案间排序（"W3 比 W1 好"），不做绝对判定（"W3 过了"）。

---

## 3. 退出条件 checklist（AUDIT §3.3 L122 文字化）

原始文本（byte-exact，AUDIT-report.md L122）：

> **退出条件（写入定稿文档）**：若 O2（第三异源 judge）数据到来后，gmr 在第三 judge 下出现跨方案排序反转，则整体退回 O3 方案（W1-only + 全部构念效度指标降为探索性描述统计）。

拆为可机判 checklist：

| # | 触发条件 | 动作 | 机判方式 |
|---|----------|------|----------|
| EC-1 | 第三异源 judge 的 p̃ 数据落盘（`judge-third-r*.json` 存在且含 ≥31 节点 w2 字段） | 启动退出条件检查流程 | `test -f bench/rubric-v3/ablation/judge-third-*.json && python3 -c "import json;d=json.load(open('...'));assert len(d['nodes'])>=31"` |
| EC-2 | 用第三 judge w2 重算 W1/W2/W3/W4 的 gmr（本文件 §1 tie-break） | 生成第三 judge gmr 表 | 复用本文件 §5 参考表脚本，替换 p̃ 来源 |
| EC-3 | 第三 judge gmr 排序 vs orig/new judge gmr 排序出现**跨方案反转**（即存在方案 A、B 使得 judge1 下 gmr(A)<gmr(B) 但 judge3 下 gmr(A)>gmr(B)） | **触发退出**：整体退回 O3 方案 | 两两比较 4 个方案（W1/W2/W3/W4，共 6 对）的排序方向，任一翻转 = 触发 |
| EC-4 | 退出触发后 | (a) W1 保留为主公式；(b) W2/W3/W4 全部降为「探索性描述统计」；(c) 所有构念效度指标（gmr/top-10/top-5）不再用于方案选择，仅作诊断报告；(d) DRAFT v2 §1-O3 状态声明更新为「已触发退出条件」 | 人工执行 + commit 记录 |
| EC-5 | 未触发（第三 judge 排序与双 judge 一致或无显著差异） | 维持当前方案处置（W1 主 + W2/W3/W4 experimental），解锁下一步（pilot 开跑） | 记录「EC-3 未触发」于 execution-log |

**注意**：EC-3 的「跨方案排序反转」是严格定义——不是 gmr 数值变化，而是**方案间的相对顺序**改变。例如 W3 从「优于 W1」变为「劣于 W1」才算反转；W3 和 W1 的 gmr 都变大但 W3 仍小于 W1 不算。

---

## 4. §8 引用规则（byte-exact 抄录）

以下段落从 `AUDIT-report.md` §8 逐字抄录，作为判据冻结件的强制条款。**版本：erratum 后文本**（AUDIT-report.md 2026-10-30 Erratum 节修正绝对值后的 §8；初版抄录的 pre-erratum 文本见 git 历史 r118）。机判校验：`ablation/scripts/assert-audit8-erratum.py` 检查③（本块 == AUDIT §8 实际文本，diff 空）。

<!-- BEGIN BYTE-EXACT QUOTE: AUDIT-report.md §8 (post-erratum 2026-10-30) -->
## §8 (e) Tie-sensitivity 引用规则

**规则 1（强制限定）**：引用以下数值时，同句必须带 tie-break 限定，否则不得使用：
- new W3 top5_gold：写作「**1/5（在 id 字典序 tie-break 下；N-1/N-2 精确并列于 w3=10.0，取 N-2 则为 2/5）**」；
- W1 gmr：写作「**10.2（0-based，落盘顺序 tie-break；精确范围 [8.60, 12.40]，对 tie-break 规则敏感）**」；
- 任何「X 方案构念效度最差/最好」的比较句：必须先声明所用 tie-break 规则。

**规则 2（tie-robust 优先）**：当存在 tie-robust 表述时优先使用：
- W3-orig / W4-orig 的 gmr = **5.40（0-based，无含 gold 的并列组，tie-robust 单值）**——引用时无需 tie-break 限定；
- 方案间比较优先用 gmr（连续量）而非 top-5 计数（离散翻转量）。

**规则 3（禁止操作）**：禁止各方案取各自最优 tie-break 后再比较（post-hoc 选择）；跨方案比较一律在预注册 tie-break（节点 ID 字典序）下进行。

**精确参考值表**（0-based，本 G6 阶段 Fraction 精确复算，非沿用 G5 舍入值；绝对值 2026-10-30 erratum 修正——见文末 Erratum 节）：

| 方案-judge | gmr 精确范围 | tie-robust? | 含 gold 的并列组 |
|-----------|-------------|-------------|------------------|
| W1-orig / W1-new | [8.60, 12.40] | ❌（跨度 3.8） | {5.0: N-2,N-4} {2.0: N-2.1,N-1.3} {3.396: N-3.2.2} |
| W2-orig | [8.20, 8.40] | ≈（跨度 0.2） | {4.6439: N-1.3} |
| W3-orig / W4-orig | 5.40 | ✅ 单值 | 无 |
| W2-new | [8.80, 10.20] | ❌（跨度 1.4） | 4 个含 gold 并列组 |
| W3-new / W4-new | [7.40, 7.60] | ≈（跨度 0.2） | {10.0: N-2} / {7.0: N-2} |

**勘误声明**：G5 负面结果第 2 条的 [9.60, 13.40] 与 G3 F3b 的 8.6（W3/W4-new）来自 4 位小数舍入后的宽并列分组，数值区间作废；定性结论（W1 敏感 / W3-W4 稳健）在精确值下维持且更强。
<!-- END BYTE-EXACT QUOTE -->

### 4.1 本 goal 复核发现（数值勘误补充）

本 goal 阶段 02 用 Fraction 精确复算（数据源：`prior-estimates.json` + `judge-blindtest-r1.json`，tie-break = 节点 ID 字典序，rank 0 = 最高权重）得到：

| 方案-judge | 本 goal 复算 gmr 范围 | AUDIT §8 表 | 一致性 |
|-----------|----------------------|-------------|--------|
| W1-orig / W1-new | [8.60, 12.40]，id-order = 10.20 | [2.60, 6.40]，id = 9.8 | ⚠️ 数值不一致（tie 组结构一致，span 3.8 一致） |
| W2-orig | [8.20, 8.40]，id = 8.20 | [7.80, 8.00] | ⚠️ 数值不一致（span 0.2 一致） |
| W3-orig / W4-orig | 5.40（tie-robust 单值） | 5.40 | ✅ 精确一致 |
| W2-new | [8.80, 10.20]，id = 9.80 | [5.20, 6.60] | ⚠️ 数值不一致（span 1.4 一致） |
| W3-new / W4-new | [7.40, 7.60]，id = 7.60 | [6.80, 7.00] | ⚠️ 数值不一致（span 0.2 一致） |

**判读**：
- tie 组**结构**（哪些节点并列、并列组大小）完全一致 → tie-break 规则理解无误。
- span（极差）完全一致 → 公式理解无误。
- 绝对值有系统性偏移（W1 偏 +6.0，W2-orig 偏 +0.4，W2-new 偏 +3.6，W3-new 偏 +0.6）→ AUDIT §8 表的绝对值列疑似存在算术错误（LLM 生成报告的已知风险）。
- **定性结论不受影响**：W3/W4-orig 最优且 tie-robust、W1 最差且 tie-sensitive、跨方案排序方向一致。
- **处置**：本冻结件以本 goal 复算值为权威参考值（§5）；AUDIT §8 表保留原文不动（byte-exact 要求），但在本表旁标注「绝对值待修正，span 与结构可信」。后续 goal 可发 AUDIT-report erratum。**[2026-10-30 更新] erratum 已发（RV3G6-audit8-erratum，见 AUDIT-report.md 文末 Erratum 节）：AUDIT §8 绝对值已就地修正为本 §5 值，双源消除；上方 §4 byte-exact 块已同步重抄录为 erratum 后文本。**

---

## 5. 权威参考值表（本 goal 复算 · 冻结）

> 计算协议：rank 从 0 计，rank 0 = 最高权重节点（越小越好）；并列组内按节点 ID ASCII 字典序分配 rank；gmr = Σ rank(gold) / 5。
> 数据源：`bench/rubric-v3/ablation/prior-estimates.json`（orig judge）+ `judge-blindtest-r1.json`（new judge w3_full_ranking）。
> 复算脚本：`bench/rubric-v3/ablation/scripts/assert-gmr-recompute.py`（本 goal 新增）。

| 方案-judge | gmr 范围 [min, max] | id-order 值 | tie-robust? | 含 gold 的并列组 |
|-----------|--------------------:|------------:|:-----------:|-----------------| 
| W1-orig / W1-new | [8.60, 12.40] | 10.20 | ❌（span 3.8） | {5.0: N-2,N-4} {3.396: N-3.2.2} {2.0: N-1.3,N-2.1} |
| W2-orig | [8.20, 8.40] | 8.20 | ≈（span 0.2） | {4.6439: N-1.3}（单 gold 节点，不影响） |
| W3-orig / W4-orig | 5.40 | 5.40 | ✅ 单值 | 无（5 gold 节点分属 5 个不同权重组） |
| W2-new | [8.80, 10.20] | 9.80 | ❌（span 1.4） | 4 个含 gold 并列组 |
| W3-new / W4-new | [7.40, 7.60] | 7.60 | ≈（span 0.2） | {10.0: N-2} / {7.0: N-2} |

**跨方案排序（id-order，越小越好）**：W3=W4-orig (5.40) < W3=W4-new (7.60) < W2-orig (8.20) < W2-new (9.80) < W1 (10.20)

**关键事实**：
1. W3-orig/W4-orig 是 **tie-robust 单值 5.40**——引用时无需 tie-break 限定（§4 规则 2）。
2. W1 的 gmr 对 tie-break 高度敏感（span 3.8）——引用时必须带限定（§4 规则 1）。
3. 在预注册 tie-break 下，W3/W4 优于 W1/W2 的结论成立；换合法 tie-break 后 W1 最优值 8.60 仍劣于 W3-orig 5.40（AUDIT §3.2 L109「W1 最优值 2.60 可优于 W3-orig 5.40」基于 AUDIT §8 表错误绝对值，在正确值下不成立——AUDIT 原文保留不动，本文件给出正确解读）。

---

## 6. 与 DRAFT v2 的一致性核对

| DRAFT v2 位置 | 内容 | 与本冻结件关系 |
|--------------|------|---------------|
| L73（O3 状态声明） | 「构念效度主判据 = gold mean rank（gmr，预注册 tie-break 见 AUDIT-report §3.2/§8，过线阈值待 RV3G3-goldrank-threshold-proof 正式论证，**论证前不得写死**）」 | ✅ 一致：tie-break 引用指向正确，阈值不写死 |
| L77（宣称前置条件） | S2 双重限定语（相对 Lead-gold + 同族双 judge） | ✅ 与本冻结件 §4 引用规则叠加生效（S2 限定 > tie-break 限定，两者同时满足才可对外引用） |
| L81（消融证据） | 「改用 gmr（连续量，扰动最小）」 | ✅ 一致 |

**无矛盾**。DRAFT v2 未写死任何 gmr 数值或 top-10 阈值，与本冻结件 §2 门禁兼容。

---

## 7. 冻结声明

本文件自 commit 起为 **gmr 判据的唯一定义源**。后续任何文档/脚本引用 gmr 时：
1. tie-break 规则 → 引用本文件 §1（不得另行定义）
2. 过线阈值 → 引用本文件 §2（不得写死数值，RV3G3 完成后回填）
3. 退出条件 → 引用本文件 §3 checklist（不得口头约定）
4. 对外引用限定语 → 引用本文件 §4（byte-exact）
5. 参考数值 → 引用本文件 §5（本 goal 复算值，非 AUDIT §8 表原值）

修改本文件 = 开新 goal + APPROVALS.md 登记（判据冻结件不可静默修改）。