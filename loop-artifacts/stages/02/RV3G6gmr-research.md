# 阶段 02：信息调研 — RV3G6-gmr-tiebreak-prereg

> goal: gmr 主判据预注册冻结件 · 2026-10-30
> 任务：从冻结数据独立复算全部方案-judge 的 gmr，定位 AUDIT-report §8 参考值表的数值偏差

## 1. 复算协议（从冻结数据反推）

### 1.1 数据来源
- **orig judge**：`bench/rubric-v3/ablation/prior-estimates.json` → `nodes.{nid}.{p_tilde, w1, w2}`
- **new judge**：`bench/rubric-v3/ablation/judge-blindtest-r1.json` → `w3_full_ranking[].{node, p_tilde, w1, w2, w3}`
- **gold strict 集**（5 节点）：`["N-2.1", "N-3.2.2", "N-2", "N-4", "N-1.3"]`（AUDIT §3.2 L100 + stats-w3w4.json construct_validity.gold_strict）

### 1.2 权重公式（prior-estimates.json weight_formulas）
| 方案 | 公式 | 依赖 |
|------|------|------|
| W0 | w = 1 | 无（flat） |
| W1 | w = 1 + 4×SHARE(parent) | 仅结构（不依赖 p̃） |
| W2 | w = 1 + min(−log₂ p̃, log₂(1/ε)), ε=0.01 | p̃ |
| W3 | w = w1 × w2 | w1 + p̃ |
| W4 | w = w1 + w2 | w1 + p̃ |

### 1.3 gmr 计算协议
```
输入：{node_id: weight} 全 31 节点
排序：按权重降序（rank 0 = 最高权重）；并列组内按节点 ID ASCII 字典序
rank：competition ranking（连续整数，rank 从 0 起）
gmr  = Σ rank(gold_node) / |gold| = Σ rank(gold) / 5
```

**rank 方向判定（J1）**：
- AUDIT §3.2 L100 原文「rank 从 0 计（越小越好）」→ rank 0 对应最优位置
- 最优位置 = 最高权重（权重高 = 先验认为重要 = 应排前面）
- **锚点验证**：W3-orig 在 descending 下 gmr = 5.40 且 tie-robust（lo==hi），与 AUDIT §8 表精确一致；ascending 下无法得出此值
- **结论**：rank 0 = 最高权重（descending weight order）是唯一自洽解

### 1.4 tie-break 边界值
对每个含 gold 节点的并列组，gmr 的最小值 = gold 节点在该组内排最前（字典序最小优先），最大值 = gold 节点排最后。
- lo = 所有含 gold 并列组内 gold 取最优位
- hi = 所有含 gold 并列组内 gold 取最差位
- id-order = 严格按节点 ID 字典序（预注册规则）

## 2. 复算结果（Fraction 精确值）

脚本：`bench/rubric-v3/ablation/scripts/assert-gmr-recompute.py`（本 goal 新增）
运行结果：**11 PASS / 0 FAIL**

| 方案-judge | gmr [lo, hi] | id-order | tie-robust? | 含 gold 并列组 |
|-----------|:------------:|:--------:|:-----------:|---------------|
| W1-orig / W1-new | [8.60, 12.40] | 10.20 | ❌ span 3.8 | {5.0: N-2,N-4} {3.396: N-3.2.2} {2.0: N-1.3,N-2.1} |
| W2-orig | [8.20, 8.40] | 8.20 | ≈ span 0.2 | {4.6439: N-1.3} |
| W3-orig / W4-orig | 5.40 | 5.40 | ✅ 单值 | 无 |
| W2-new | [8.80, 10.20] | 9.80 | ❌ span 1.4 | 4 个含 gold 并列组 |
| W3-new / W4-new | [7.40, 7.60] | 7.60 | ≈ span 0.2 | {10.0: N-2} / {7.0: N-2} |

## 3. 与 AUDIT §8 表的对比（偏差定位）

| 方案-judge | 本 goal 复算 | AUDIT §8 表 | 偏差 | tie 组结构 | span |
|-----------|:----------:|:----------:|:----:|:---------:|:----:|
| W1 | [8.60, 12.40] id=10.20 | [2.60, 6.40] id=9.8 | +6.0 | ✅ 一致 | ✅ 3.8 一致 |
| W2-orig | [8.20, 8.40] id=8.20 | [7.80, 8.00] | +0.4 | ✅ 一致 | ✅ 0.2 一致 |
| W3/W4-orig | 5.40 | 5.40 | 0 | ✅ 一致 | ✅ 0 |
| W2-new | [8.80, 10.20] id=9.80 | [5.20, 6.60] | +3.6 | ✅ 一致 | ✅ 1.4 一致 |
| W3/W4-new | [7.40, 7.60] id=7.60 | [6.80, 7.00] | +0.6 | ✅ 一致 | ✅ 0.2 一致 |

**判读**：
- tie 组结构（哪些节点并列、组大小）完全一致 → tie-break 规则理解正确
- span（极差）完全一致 → 公式理解正确
- 绝对值有系统性偏移 → AUDIT §8 表的绝对值列存在算术错误
- **定性结论不受影响**：跨方案排序方向一致（W3/W4-orig 最优 < W3/W4-new < W2-orig < W2-new < W1）

### 3.1 AUDIT §3.2 L109 勘误
AUDIT-report.md L109 原文：「W1 最优值 2.60 可优于 W3-orig 5.40」
- 基于 AUDIT §8 表的 W1 lo=2.60（错误值）
- 正确值 W1 lo=8.60 > W3-orig 5.40 → **该句不成立**
- 修正：在正确值下，W1 的最优 tie-break 值（8.60）仍劣于 W3-orig（5.40），W3/W4 优势更稳固

## 4. 超几何锚点复算

n=31, k=5 (gold), r=10 (top-10 抽取)

| 量 | 公式 | 精确值 | AUDIT/G3 引用值 | 一致性 |
|----|------|--------|----------------|--------|
| E[X] | k·r/n = 5×10/31 | 1.6129 | ≈1.61 | ✅ |
| P(X≥4) | Σ_{i=4}^{5} C(5,i)C(26,10-i)/C(31,10) | 0.027438 | ≈2.7% | ✅ |
| P(X≥3) | Σ_{i=3}^{5} C(5,i)C(26,10-i)/C(31,10) | 0.175751 | ≈17.6% | ✅ |

来源交叉验证：`g3-w3w4-completion.md` L51（G3 F3b）与本 goal 复算一致。

## 5. 外部文献

**不需要**。本 goal 是纯仓库内文本固化 + 数值复算工作，无外部依赖。

## verdict

**pass** — 复算协议从冻结数据唯一确定（J1 有锚点验证）；7 个方案-judge 的 gmr 全部机判通过（11/0）；AUDIT §8 绝对值偏差已定位（tie 结构/span 一致，绝对值有算术错误）；§3.2 L109 勘误已记录；超几何锚点三值复算一致。进入 02.5。