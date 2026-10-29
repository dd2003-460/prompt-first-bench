# 阶段 02：资料搜集与证据固化 — RUBRIC-V3-FULL-AUDIT / G5 优化清单

> goal: rubric-v3-audit-g5 · 分支 ralph/rubric-v3-audit-g5 · 2026-10-30
> web-llm 回执：`loop-artifacts/prompt-first/02-web-llm-cross-check.md`（ok=true, successful_provider_ids=[] —— 三 provider 全部 error，登录态失效；按任务书失败降级条款记录后继续本地证据提取，不阻塞）

## 仓库内证据固化

### F1 · w2 公式层独立复算验证

**方法**：对 `prior-estimates.json` 和 `judge-blindtest-r1.json` 中全部 31 节点的 `w2` 字段，用公式 `w2(p) = 1.0 if p is None else 1+min(-log2(p), log2(100))` 独立重算，逐节点比对。

**结果**：
- `prior-estimates.json`：31/31 精确匹配（浮点噪声 < 1e-9）
- `judge-blindtest-r1.json`：31/31 精确匹配（浮点噪声 < 1e-9）

**结论**：w2 公式层无计算错误，可安全作为断言脚本的校验目标。

---

### F2 · 全局权重排序构念效度指标完整矩阵

**方法**：对 5 种权重方案（W0 flat / W1 importance / W2 surprisal / W3=w1×w2 / W4=w1+w2）× 2 个 judge（orig=prior-estimates / new=judge-blindtest-r1），按节点权重降序排列 31 节点（tie-break by node id），计算：
- global top-5 gold 计数（strict gold set = {N-2.1, N-3.2.2, N-2, N-4, N-1.3}）
- global gold 平均排名（5 个 gold 节点在 31 节点排名中的 1-based 位置均值）

**结果矩阵**（id tie-break）：

| Scheme | Judge | top5_gold | goldmeanrank |
|--------|-------|-----------|--------------|
| W0     | orig  | 0/5 (degenerate) | 18.20 (degenerate) |
| W0     | new   | 0/5 (degenerate) | 18.20 (degenerate) |
| W1     | orig  | 2/5       | 11.20        |
| W1     | new   | 2/5       | 11.20        |
| W2     | orig  | 2/5       | 9.20         |
| W2     | new   | 1/5       | 10.80        |
| W3     | orig  | **3/5**   | **6.40**     |
| W3     | new   | **1/5**   | **8.60**     |
| W4     | orig  | 2/5       | 6.40         |
| W4     | new   | 2/5       | 8.60         |

注：W0 为退化情形（所有权重=1.0，完全平局），top5_gold 和 goldmeanrank 均无意义。

**交叉验证**：
- G1 C4 记录：orig W3=3/5, new W3=1/5 → ✅ 确认
- G3 表格行（gold mean rank）：W1=11.2, W2o=9.2, W3o=6.4, W4o=6.4, W2n=10.8, W3n=8.6, W4n=8.6 → ✅ 全部确认
- G3 top-10 行：W1=3, W2o=3, W3o=4, W4o=4, W2n=2, W3n=4, W4n=3 → ✅ 全部确认
- `judge-blindtest-r1.json` 存储的 `w3_full_ranking` == 重算的 new W3 权重排序（id tie-break）→ ✅ 确认
- `judge-blindtest-r1.json` 存储的 `marked_count_strict=1` == 重算的 new W3 top5_gold=1/5 → ✅ 确认

---

### F3 · Per-run 构念效度指标完整矩阵

**方法**：对每个 run（run1-run8），按 `w_v × h_v(r)` 降序排列 31 节点（tie-break by node id），计算：
- per-run top-5 gold 计数
- per-run gold 平均排名

**结果矩阵**（id tie-break）：

| Scheme | Judge | per-run top5_gold (max) | per-run goldmeanrank (mean of 8 runs) |
|--------|-------|-------------------------|---------------------------------------|
| W0     | orig  | 0                       | 19.12                                 |
| W0     | new   | 0                       | 19.12                                 |
| W1     | orig  | 2                       | 17.23                                 |
| W1     | new   | 2                       | 17.23                                 |
| W2     | orig  | 2                       | 17.32                                 |
| W2     | new   | 2                       | 17.35                                 |
| W3     | orig  | 2                       | 17.05                                 |
| W3     | new   | 2                       | 17.15                                 |
| W4     | orig  | 2                       | 17.05                                 |
| W4     | new   | 2                       | 17.15                                 |

**关键发现**：per-run 口径下，无任何 run 在任何方案下达 ≥3 gold 标记（max=2）。这与 G1 的"per-run top-5 口径下无任何 run 过线"结论一致。

---

### F4 · Tie-sensitivity 分析

**方法**：对每种 scheme×judge 组合，检查权重排序中是否存在平局（ties），以及平局是否跨越 top-5 或 top-10 边界。若跨越，则 top5_gold 或 goldmeanrank 的值依赖于 tie-breaking 规则。

**结果**：

#### Global weight-only ranking ties

| Scheme | Judge | Ties at top-5 boundary | Ties at top-10 boundary | top5_gold range | goldmeanrank range |
|--------|-------|------------------------|-------------------------|-----------------|--------------------|
| W1     | orig  | No                     | Yes (w=2.972, pos 10-11) | [2,2] (fixed)   | [9.60, 13.40]      |
| W1     | new   | No                     | Yes (w=2.972, pos 10-11) | [2,2] (fixed)   | [9.60, 13.40]      |
| W2     | orig  | No                     | No                      | [2,2] (fixed)   | [9.20, 9.40]       |
| W2     | new   | Yes (w=3.3219, pos 5-6)| Yes (w=2.737, pos 9-12) | [1,1] (fixed)   | [9.80, 11.20]      |
| W3     | orig  | No                     | No                      | [3,3] (fixed)   | [6.40, 6.40]       |
| W3     | new   | Yes (w=10.0, pos 5-6)  | No                      | [1,2]           | [8.40, 8.60]       |
| W4     | orig  | No                     | No                      | [2,2] (fixed)   | [6.40, 6.40]       |
| W4     | new   | No                     | No                      | [2,2] (fixed)   | [8.40, 8.60]       |

**关键发现**：
1. **new W3 的 top5_gold 是 tie-sensitive 的**：N-1 和 N-2 在 rank 5-6 处平局（w=10.0），N-2 是 gold 节点。若 N-2 排在 N-1 前面，top5_gold=2/5；若 N-1 排在前面，top5_gold=1/5。当前 id tie-break 给出 1/5（N-1 < N-2 alphabetically），但这不是唯一可能的值。
2. **W1 的 goldmeanrank 高度 tie-sensitive**：[9.60, 13.40] 的范围意味着 W1 的构念效度评估严重依赖于 tie-breaking 规则。
3. **W3/W4 在 orig judge 下无 ties**：这些指标是确定的，不依赖 tie-breaking。

#### Per-run ranking ties

Per-run 口径下，W0 和 W1 存在显著的 tie-sensitivity（由于 h 值为 0/1 整数，w1×h 产生大量平局），而 W2/W3/W4 的 per-run top5_gold 在所有 8 个 run 中都是固定的（不受 tie-breaking 影响）。

---

### F5 · 超几何基线参考

**参数**：n=31 节点，k=5 gold 节点，r=5（top-5 窗口大小）

**计算**：
- E[X] = k×r/n = 5×5/31 ≈ 0.806
- P(X≥3) = Σ_{x=3}^{5} C(5,x)×C(26,5-x) / C(31,5) ≈ 1.99%

**含义**：在随机排序下，top-5 中期望只有 ~0.8 个 gold 节点，P(≥3)≈2% 属于极小概率事件。因此 orig W3 的 3/5 是显著高于随机的信号，而 new W3 的 1/5 接近随机水平。

---

## 机判化候选可行性证据

### C1 · p̃ 多源频率断言（RV3G4-prior-source-assert）

**现状**：`prior-estimates.json` 的节点字段仅包含 `parent_id`, `p_tilde`, `reason`, `w2`, `parent_share`, `w1`——**无 source/provenance 字段**。顶层元数据有 `source_baseline_commit: '8ee73de'` 但这是 git commit hash，不是 p̃ 生成源的标识。

**断言逻辑**：
- 检查 `prior-estimates.json` 是否存在 `p_tilde_sources` 或类似字段
- 若缺失或单源 → FAIL
- 若存在且 ≥N 个独立源 → PASS

**实现成本**：~50-80 行 Python（参考 R5.2 assert-* 模式），需定义 schema（G1 gap：κ 门禁回执格式不存在，同理 p̃ source 格式也不存在）。

**防住的风险**：G4 S3 降档（纸面协议 vs 实际执行落差）

---

### C2 · κ 门禁回执断言（RV3G4-kappa-receipt-assert）

**现状**：DRAFT-rubric-v3.md line 15 规定"judge 校准门禁沿用 C3 v3 的 R5（换位双判 + κ≥0.6 + 长度去偏），评分前不过门禁不开评"，但**无回执文件存在**。`TASK-ablation.md` 中 grep κ/kappa/0.6 返回空。

**断言逻辑**：
- 检查评分目录是否存在 `kappa-receipt.json` 或类似文件
- 若缺失 → FAIL
- 若存在，检查 schema（gate_passed: bool, kappa_value: float, method: str, date: str, judges: [str, str]）
- 若 gate_passed=false 或 kappa_value<0.6 → SIGNAL（警告但不 fail，因为可能是历史数据）

**实现成本**：~60-100 行 Python，需先定义最小 schema（G1 gap）。

**防住的风险**：G4 S3 κ 门禁 unverified 状态

---

### C3 · W3/W4 分数复算断言（assert-w3w4-recompute.py）

**现状**：G3 已完成人工 python 一次性验证（W3/W4 分数 8/8+8/8、ρ 7/7、tie 4/4、top-5 计数全通过），但未脚本化。

**断言逻辑**：
- 加载 `hit-matrix.json`, `prior-estimates.json`, `judge-blindtest-r1.json`
- 对每个 run×scheme 组合，重算 O3 = Σ w_v·h_v / Σ w_v
- 与 `stats-w3w4.json` 存储值比对（容差 1e-4）
- 重算 Spearman ρ(W3, W4) 并与存储值比对
- 重算 top-5 gold 计数并与存储值比对

**实现成本**：~150-200 行 Python（参考 assert-g1-audit.py 的 137 行结构 + spearman 实现）。

**防住的风险**：防止未来数据更新时引入计算错误

---

### C4 · w2 公式层断言

**现状**：本阶段已验证 31/31 精确匹配，可安全脚本化。

**断言逻辑**：
- 加载 `prior-estimates.json` 和 `judge-blindtest-r1.json`
- 对每个节点，用公式重算 w2 并与存储值比对（容差 1e-9）
- 任一 mismatch → FAIL

**实现成本**：~50-70 行 Python（简单循环 + 公式）。

**防住的风险**：防止公式实现变更时引入错误

---

### C5 · blindtest cross_judge_spearman 一致性断言

**现状**：`judge-blindtest-r1.json` 存储了 `cross_judge_spearman` 字段（含 `p_tilde_rho_n30_excl_root`, `threshold`, `stable`, `verdict`, `run_ranking_rho_w3` 等 7 个子字段）。

**断言逻辑**：
- 从 `prior-estimates.json` 和 `judge-blindtest-r1.json` 提取 p̃ 值
- 重算 Spearman ρ（排除 root 节点，n=30）
- 与存储值比对（容差 1e-4）

**实现成本**：~80-120 行 Python（需实现 spearman 或复用 C3 的实现）。

**防住的风险**：防止统计量计算错误

---

## 并行化候选可行性证据

### P1 · p̃ 多 LLM 盲生成

**依据**：DRAFT §1-O3 原协议要求"≥3 个 LLM 服务相同 prompt 盲生成分解树，按语义类统计出现频率，p̃=(k+0.5)/(N+1) 平滑"。

**前置条件**：
- 需多 provider 通道（web-llm 当前全失效——本阶段 02 再次确认）
- 需 arena 会话通道或本地多模型部署

**执行保真度风险**：S3 教训表明"纸面协议防护力为零"——即使协议写了 ≥3 LLM，如果实际只跑了 1 个，风险状态不变。验收项必须是"有没有人真的跑过"而非"协议里写了没有"。

**成本**：高（外部依赖不可控）

---

### P2 · κ 换位双判

**依据**：DRAFT 规定"换位双判 + κ≥0.6"作为评分门禁。

**前置条件**：
- 需异族 judge（R5.2-third-scorer 外部阻塞）
- 同族双判无家族隔离价值（adversarial-check finding #29）

**执行保真度风险**：同上，需实际执行而非纸面协议。

**成本**：高（外部依赖）

---

### P3 · 第二格实验（新域）

**依据**：DRAFT §3.1 要求"第二格选『gold 需新建的域』并验证可构建性"。

**前置条件**：
- T17 半成品不在本仓（adversarial-check finding #31 minor 证实）
- 需构建新域 gold 树（成本高）

**执行保真度风险**：跨域可比性无机制（G4 S4 判定），即使做了第二格，分数对齐方法也未定义。

**成本**：极高（gold 构建 + 分数对齐设计）

---

### P4 · 8 run 重跑（V0-V3 变体矩阵）

**依据**：DRAFT §3 实验设计定义了 V0-baseline / V1 / V2 / V3 四个变体。

**前置条件**：
- **BLOCKED by adversarial-check finding #17 (blocker)**：变体差异未冻结，归因不成立。必须先修 DRAFT 再谈并行重跑。

**执行保真度风险**：若变体定义不清，重跑结果无法归因。

**成本**：高（需先完成 DRAFT 修订）

---

### P5 · arena 通道语义重判（RV3G1-semantic-rejudge）

**依据**：G1 已落盘 75 样本 cell 清单（`bench/rubric-v3/ablation/scripts/g1-sample-cells.json`），覆盖 h=0 漏判方向。

**前置条件**：
- 需 arena 会话通道

**执行保真度风险**：低（样本清单已就绪，只需执行）

**成本**：中（arena 通道可用时）

---

## 负面结果声明

1. **W0 构念效度指标退化**：flat 权重下所有节点权重相等，global top5_gold 和 goldmeanrank 均无意义（完全平局）。这不是"计算错误"而是"指标不适用"——W0 作为 baseline 的价值在于 run 排序（O3 分数），不在于节点级构念效度。

2. **W1 构念效度高度 tie-sensitive**：goldmeanrank 范围 [9.60, 13.40] 意味着 W1 的"构念效度差"这一结论部分依赖于 tie-breaking 规则。若采用不同 tie-break，W1 的 goldmeanrank 可能改善到 9.6（接近 W2 的 9.2）。这削弱了"W1 构念效度最差"的绝对性表述。

3. **new W3 top5_gold tie-sensitive**：当前报告的 1/5 依赖于 id tie-break（N-1 < N-2）。若采用其他 tie-break 规则，值可能为 2/5。这意味着"new W3 否决构念效度"的结论需要带"在 id tie-break 下"的限定语，或者改用 tie-robust 指标（如 goldmeanrank，其范围 [8.40, 8.60] 更窄）。

4. **Per-run 口径下无 run 过线**：所有 scheme×judge 组合的 per-run top5_gold max=2，无一达 ≥3。这与 global 口径（orig W3=3/5）形成对比，说明"过线"与否强烈依赖于聚合口径（global vs per-run）。

---

## 仍未解决

- κ 门禁回执 schema 不存在（G1 gap）——C2 断言需要先定义 schema，这本身是 G6 或专项 goal 的产出。
- p̃ source 字段格式不存在（G1 gap）——C1 断言需要先定义 schema。
- 异族 judge 不可用（R5.2-third-scorer 外部阻塞）——P1/P2 并行化候选本轮不可执行。
- DRAFT 变体矩阵未冻结（finding #17 blocker）——P4 并行化候选 BLOCKED。