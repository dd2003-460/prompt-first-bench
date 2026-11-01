# BRIDGE-REPORT（arena → Hermes 汇报通道）

> 协议见 tasks/ralph-loop-runner.md「runner 外包规则」(v3)。执行层 = LMArena agent mode（经 ego-browser），本地 claude CLI 已弃用（背后也是 27b，同根）。
> 写入者 = Hermes Lead：收到 arena snapshot 结果后代写本文件。Hermes 侧读取方式：cat 本文件 + 查 goal-queue 是否划掉。

## 当前状态

- goal: 无活跃 stage-gate goal；r185 补完 R-05 预注册报告义务（8×8 相关矩阵正式版），rubric-v3 正式实验链（RV3G6→G9）全闭环。剩余卡人项：G1b family_check（真实 IRR，需非 Qwen 凭证或 arena 模型身份披露）
- commit: main 13ac7bd（r185 收口：corr-matrix-formal-n21.json + attribution §8.5 + DRAFT 后记 + revision-log R-25 + queue 补记）
- 验收自检: 矩阵 21 个 off-diagonal 值由 judge-{1,2}-scores.json 独立复算；assert-kappa-receipt.py PASS exit 0（SIGNAL kappa=0.0 为已知边际退化假象，人工裁决不阻断）
- 结论: **R-05 ③ 报告义务在正式数据上执行完毕**——n=21 pooled 无任何 |ρ|>0.8 对，pilot {O1,O2,P4} 簇未复现（最大 ρ(O2,P4)=0.61）。R-22 选项 c 标注保留为形式合规，维度结构不变。下一可自主推进项见 goal-queue 队首扫描（C3v3-G1b-hetero-judge 可走 arena battle 通道，slim 2.5KB packet 经验已有）。
- commit: main 0aa2bf4（盲评分数+回执）/ 4fd2ef3（queue 更新）
- 验收自检: 双裁判 21 docs × 19 items 独立复算全过；Krippendorff α=0.9642
- 结论: **盲评双裁判评分核验收口完成**。agreement 0.975，α=0.9642（高一致）。弱项 O3(0.880)/O4-E2(0.523) 登记不阻塞。排名 B2>B1/B3/D3/F2>D2/F1>C2。**注意**：双判仍为同一 agent 双口径（严格度敏感性证据，非独立 IRR）。剩余：① RV3G8 归因分析立项 ② 真·异源 dual-rater（需非 Qwen API key，blocked）

## r181 收口（2026-11-02）

- **状态：盲评双裁判评分落盘 + Lead 独立核验收口**
- arena 5e17a76 cherry-pick → main 0aa2bf4：judge-{1,2}-scores.json（21 docs × 19 items，0/1/2 口径，7 NA 排除，max_score=38）
- 独立核验全过：JSON 合法 / 21 doc 两判覆盖一致 / 分值 ∈ {0,1,2} / o3_claims 长度 31×21 ✓ / total_score 复算 0 mismatch
- 一致性：agreement 389/399=0.975；Cohen κ(三档)=0 为边际退化假象（多数项双 2），改用 **Krippendorff α(interval)=0.9642**（有效指标）
- 弱项登记 2：O3-claim_coverage α=0.880、O4-E2_numeric_interval α=0.523（n=21 小样本，不阻塞）
- 排名 top8：B2(38) > B1/B3/D3/F2(37) > D2/F1(36) > C2(35.5)
- 回执：blind-eval-dual-judge-receipt.json @ main
- **注意**：此轮双判仍为同一 arena agent 双口径（非独立 IRR），定位=严格度敏感性证据（与 r180 一致）
- **下轮起点**：RV3G8-ablation-attribution 立项（归因分析：用双判分做变体间差异分解，重点看 O3/O4-E2 弱项是否影响变体排序结论的稳健性）

## r177 观察记录（2026-11-02，已被 r181 取代）

- **状态：盲评 agent 运行中，未落盘**
- 会话 01a195cb（taskSpace 904）：r176 派发已执行，agent 截至本轮检查 26 次思考 + 25 条命令，正在按 31 claim 特征 grep 全 21 份答卷并组装 0/1/2 评分（非 NA 19 项，max_score=38；O3 item 分 = 覆盖率阈值 ≥2/3→2 / ≥1/3→1 / 否则 0）
- 远端各分支暂无 `blind-eval/judge-{1,2}-scores.json`（arena 分支 tip 仍 fa59371）
- **Lead 决策：零派发**——agent 在跑时重复发消息会污染上下文；composer 显示 Stop generating = 仍在生成
- **下轮核验起点**：`git fetch origin && git ls-tree -r --name-only origin/arena/4a614e63-prompt-first-bench | grep -E "blind-eval/judge-[12]-scores"` → 落盘则 cherry-pick main + 独立核验（JSON 合法 / 21 run_id 全覆盖无重复 / 非 NA 条目有 evidence / O3 per-claim 数组长度=31）→ κ 计算（per-dimension + overall，0/1/2 原值先报）→ BRIDGE-REPORT 收口

## r183 — RV3G9 预注册统计检验执行 + attribution 勘误（2026-11-02）

**分支**: `ralph/rv3g9-formal-stats-execution` → main `0481ed4`

### 做了什么
按 DRAFT v2 §3.3 (R-11) 预注册方案，对盲评双裁判数据跑完整统计检验：
- **28 项配对置换检验**（4 主对比 × 7 维度，10⁴ sign-flips）+ Holm-Bonferroni 全族校正
- 敏感性：Wilcoxon（多组 |d|=0 不适用，已记录）
- 效应量 dz、MDE 反推样本量

### 结果
- **0/28 维度检验、0/4 复合总分检验 Holm 后显著**（最小原始 p=0.2528）
- n=3 下置换检验分辨率上限 ~p≈0.25——结构性 underpowered，非效应不存在
- MDE 反推：总分对比需 n≥8，O1 单维需 n≥139
- 方向性结论全部复算确认：V1-full > V1-align > V0 排序、D2 边际 +5.06 超噪声带、P4-E2 二分机制、O1 主通道

### 发现并修正的归因报告错误（4 处）
| # | 位置 | 原值 | 实际值 | 影响 |
|---|------|------|--------|------|
| DISC-1 | §3 D1 净效应 | ≈+0.12（组均值口径） | B−F=+2.67（干净配对） | 中——定性不变，数值差 22× |
| DISC-2 | §4 V0 O1 | 1.67/6 | 1.67/6 ✓ 无误 | 无 |
| DISC-3 | §4 O1 区间 | 3.67–6.0 | 4.0–6.0（下界=C 组均值） | 低 |
| DISC-4 | §3 F 组 SD | 2.88 | pool 6 值=2.88 / merged 3 值=3.21 | 低——口径差异 |

### 产出文件
- `bench/rubric-v3/ablation/formal-matrix/formal-stats-results.json`（完整统计回执）
- `attribution-analysis.md` 勘误 4 处 + 新增 §8 统计检验段
- `DRAFT-rubric-v3-v2.md` §3.1 第三步同步勘误

### 下一步
补 run 至 n≥8（MDE 要求）才能出正式显著性结论；当前证据级别 = 方向性 + 效应量 + sham 对照结构。

## r185 — R-05 报告义务执行：正式矩阵 8×8 相关矩阵（2026-11-02）

### 做了什么
补上预注册漏项：R-05 ③「正式报告必须附 8×8 维度间相关矩阵」在正式矩阵收口后从未执行。对 judge-{1,2}-scores.json（21 run × 双判）做 judge-merged per-run 维度分 Spearman 全表（NA 7 项剔除，P2 维全 NA 不入矩阵），落盘 `ablation/formal-matrix/corr-matrix-formal-n21.json` + attribution-analysis.md §8.5 + DRAFT v2 L198 裁定段 r185 后记 + revision-log R-25。

### 结果
**无任何 |ρ|>0.8 对。** pilot（n=9）实测簇 {O1,O2,P4}（ρ(O2,P4)=1.0、ρ(O1,O2)=ρ(O1,P4)=0.854）在 n=21 下未复现——最大 ρ(O2,P4)=0.608/0.617（J1/J2）。pilot 小样本 rank 相关被噪声放大；次级观察 ρ(P3,P4)=0.68 未过阈值。

### 含义
① R-22 选项 c（分开报+共线风险标注）的标注在正式数据下无触发条件，保留为预注册形式合规义务；② 维度结构按分开报执行不受影响，确认性主维 O3+O1 不变；③ 权重表/n_pairs 公式/检验族零 diff。

### 下一步
卡人项不变：G1b family_check（真实 IRR，需非 Qwen 凭证或 arena 模型身份披露）/ erratum 类候裁项。下一可自主推进项见 goal-queue 队首扫描。

## r184 — V0.1 hit-matrix 重算收口（2026-11-02）

**分支**: `ralph/v0.1-hit-matrix-recompute` → main `fd07453`

### 做了什么
发现旧 hit-matrix 的 98 条 evidence quote 有 97 条在 V0.1 文本中不存在（V0.1 移除了题面中的 cache-ratio，run 措辞全变）。按 o3-claim-list 盲判协议重判 248 cell。

### 结果
- 总分 98→77（-21），加权分 260→181（-79）
- 分解：题面效应（N-5.3/N-3.1 结构性归零）占 64%，判据收紧占 36%
- O3 mean: 0.312→0.229；Spearman ρ=0.619（top-1 翻转 run6→run8，bottom-2 不变）
- Jaccard mean: 0.572→0.477（区分度提升）
- 有效对比维度 31→29（N-5.3/N-3.1 在 V0.1 下无区分力）

### 产出文件
- `hit-matrix.json`（V0.1 版）+ `hit-matrix-v0-pre.json`（旧版保留）
- `receipt-v0.1-hit-matrix-r184.md`（完整回执：flip 明细 + prior 交叉核对 + 加权分 + O3 + Jaccard）

### 下游影响
- formal-stats-results.json / blind-eval judge scores：不受影响（独立评分通道）
- coverage-rescan-h1.json：需在新文本上重跑（pending，不阻塞）
