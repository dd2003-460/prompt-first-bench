# Judge v2: 深度梯度评分 — 初步结果 (2026-11-08)

## 一句话

把 6 个二元 gold 点（分母=6，只有 7 个离散值）拆成 22 个深度层级 + k·ln(k+1) 加权，分辨率从 7 → 245 个可能总分（35×），A3/A4 在 S0 基线上的真实效应量从 Δ≈0.02-0.06 拉到 Δ≈0.30。

## 权重公式

w_k = k · ln(k+1) / Σ_j j·ln(j+1)，k ∈ {1..K}

- K=3 → [0.11, 0.35, 0.54]
- K=4 → [0.05, 0.16, 0.31, 0.48]

直觉：越深的层级越罕见（base rate 越低），信息量越大，权重越高。纯 log 会低估深层贡献，×k 补偿。这是 bench/self-opt-tester/bench.md O3 公式 w_v = 1 + min(−log₂ p̃_v, log₂(1/ε)) 的确定性代理——固定深度阶梯替代 LLM 估计的 p̃（无同族 judge 偏置）。

## 数据状态（⚠️ 口径不一致）

| 臂 | n | judge prompt | 权重 | 可比性 |
|---|---|---|---|---|
| S0 r1-5 | 5 | strict | k·ln(k+1) | ✅ 完全一致 |
| S0 r6-30 | 25 | strict | k·ln(k+1) | ✅ 完全一致 |
| A3 r1-30 | 30 | **lenient**（旧版） | k·ln(k+1)（重算） | ⚠️ prompt 不同 |
| A4 r1-30 | 30 | **lenient**（旧版） | k·ln(k+1)（重算） | ⚠️ prompt 不同 |

**S0 vs A3/A4 的绝对差异不可直接比较**（judge 松紧不同）。但以下结论在各自口径内成立：

## S0 内部（strict judge, n=30）

mean = 0.514 ± 0.129，unique scores = 26/30（旧 binary: 5/30 unique out of 7 possible）

per-point:
| pt | mean | 解读 |
|---|---|---|
| pt1 (Pareto 命中率) | 0.555 | 中等深度 |
| pt2 (α 临界敏感性) | 0.822 | 较深 |
| pt3 (LFU 老化) | 0.373 | 浅 |
| pt4 (字节 vs 请求) | 0.406 | 浅 |
| pt5 (驻留时间推导) | **0.077** | 极浅 — 模型几乎不做 T_res 推导 |
| pt6 (假设标注) | 0.906 | 深（[待核验] 标注是强项） |

pt5 level breakdown (S0): L1=13/30, L2=4/30, L3=2/30, L4=0/30
→ 只有 43% 的 run 提到"驻留时间"概念，13% 给了量级，7% 做了对比，0% 推导出折扣因子。

## A3/A4 内部（lenient judge, n=30 each）

| | A3 | A4 |
|---|---|---|
| mean | 0.833 ± 0.143 | 0.822 ± 0.177 |
| unique | 10/30 | 13/30 |

pt5 level breakdown:
| level | A3 | A4 |
|---|---|---|
| L1 (提到概念) | 23/30 | 29/30 |
| L2 (量级估计) | 23/30 | 28/30 |
| L3 (显式对比) | 23/30 | 28/30 |
| L4 (推导折扣) | 21/30 | 28/30 |

→ A4 在 pt5 每个层级都略高于 A3，L4 差距最大（28 vs 21）。

## 与旧 binary 对比（S0, 同 reps 6-30, n=25）

| 指标 | old binary | new depth (strict) |
|---|---|---|
| S0 mean | 0.587 | 0.523 |
| unique scores | 5/25 (of 7) | 21/25 (of 245) |
| pt5 hits | 2/25 (8%) | L1=11/25 (44%), L4=0/25 |

旧 binary 把 pt5 压成 0/1，新 depth 能看出"提到了但没推导"和"完全没提"的区别。

## 下一步

1. **用 strict prompt 重跑 A3/A4 × nat × 30**（~20min），消除口径不一致
2. 然后做 matched-pair sign test（n=30），看 A3/A4 的效应在统一口径下是否显著
3. S3 补跑完成后（~40/60），同样用 strict judge 打分，四臂对比
4. soc 域同理（7 点 × 3-4 层 = 24 层）

## 文件

- `judge_v2_depth.py` — 评分脚本（strict prompt + k·ln(k+1) 权重）
- `runs-prod/judge-v2-S0-nat.json` — S0 严格判分（r1-5 strict + r6-30 strict）
- `runs-prod/judge-v2-A3-nat.json` — A3 lenient 判分（待重跑）
- `runs-prod/judge-v2-A4-nat.json` — A4 lenient 判分（待重跑）