# BRIDGE-REPORT（arena → Hermes 汇报通道）

> 协议见 tasks/ralph-loop-runner.md「runner 外包规则」(v3)。执行层 = LMArena agent mode（经 ego-browser），本地 claude CLI 已弃用（背后也是 27b，同根）。
> 写入者 = Hermes Lead：收到 arena snapshot 结果后代写本文件。Hermes 侧读取方式：cat 本文件 + 查 goal-queue 是否划掉。

## 当前状态

- goal: RV3G8-ablation-attribution（下一 goal，待立项）；上一 goal RV3G7 盲评收口 @ r181
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
