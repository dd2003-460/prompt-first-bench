# 评分机制说明（逐点 overall / 罚项 / 口径 / r03 伪影）

> origin: ai · 2026-11-26 · 回答 D 两问：①「逐点 overall」是什么 ②评分具体怎么算（对不上就没分？还是分解不完整/冗余才没分？）
> 只读代码 + 数据，不跑实验（8787 被 t-repair1 占用）。所有行号为当前 HEAD 实测。

**三条评分路径先分清**（本报告核心，避免混口径）：

| 路径 | 代码 | 产出 | 用途 |
|------|------|------|------|
| A. 逐点深度分（v18 ablation-runs） | `judge_v2_depth.py::score_run` | `point_scores` + `overall` | v18/v19 状态机 run 的「total」 |
| B. 二值覆盖率（gate 指标 cov） | `s8b_pilot.judge`（s5_state_machine.py:1638 调用） | `coverage`（gold 要点逐条 0/1 的比例） | 过 gate 门限（nat 0.5801 / soc 0.898） |
| C. canonical n=90 六维总分 | `score.py::score_run` | `total`（M1-M6 加权） | S5≈0.579 / S0≈0.397 的 canonical 口径 |
| D. B-face 异族判分（T53-B12） | `t53_bface_judge.py` | 核心数字 0.5 + 口径 0.5，n=3 median | T53-B12-new3 题集验收（**异族 qwen2.5-7b @1234**，非 A/B/C 的 27B@8787） |

**judge 端点歧义澄清（一手核验）**：仓内共两个 judge 端点——**8787**（本地 proxy→27B，A/B/C 三路径共用：judge_v2_depth.py 经 ablation_harness.py:19、score.py:14 各自定义 `LLM_URL=127.0.0.1:8787`）与 **1234**（qwen2.5-7b-original，仅 D 路径 `t53_bface_judge.py:11` 使用，T53-B12 B-face 异族判分专用）。D 问的评分机制（A/B/C）全部走 8787，与 1234 无关。

D 问的「逐点 overall」= 路径 A。下面逐节。

---

## §1 逐点 overall 精确定义（路径 A）

**judge 对每个 gold 要点打什么分：0-1 连续深度分，不是 0/1 二值，也不是 0/1/2 档。**

- prompt 原文（`judge_v2_depth.py:390`）：「对每个要点，给出一个 **0.00-1.00 的连续深度分**，表示候选回答在该要点上实际达到的深度位置。」
- 每个要点在 rubric 里被拆成 K 个**深度层**（L1 浅 … LK 深），每层带权重 `w_k = k·ln(k+1) / Σ_j j·ln(j+1)`（`judge_v2_depth.py:33-41` `_w3/_w4`；亲手复算：K=3→[0.098,0.312,0.590]，K=4→[0.051,0.163,0.308,0.477]，越深层越稀有越值钱）。⚠️ 代码 docstring 标注的 K=3「[0.11,0.35,0.54]」是算错（0.693/7.049=0.098≠0.11；docstring 对 K=4 自我更正过、K=3 漏更），以 `_w3()` 实际返回值为准。
- 打分规则（prompt 392-399）：分数 = 实际达成的最高层级/总层数，**允许层间插值**（部分达成某层给该层位置的一半）；「不要只给 0、1/K、2/K 这些离散锚点」；仅提概念名无量化 ≤0.25；拿不准往低判。
- 所以单点分数是**连续的**：完全没触及=0，只达 L1=1/K，全 K 层达成=1.0，中间任意值（如 0.33、0.5、0.65）。

**overall 怎么从 point 分数聚合成一个数：跨要点等权平均（不是加权）。**

- 聚合公式原文（`judge_v2_depth.py:465`）：`overall = total / max(n_points, 1)`，其中 `total = Σ_p score_p`（462-463 累加）。
- 即 **overall = (1/N)·Σ_points score_p**，N=gold 要点数（nat=6 / soc=7 / gpu=38）。**跨要点是等权平均，要点之间不加权。**
- 「逐点加权」里的「加权」指的是**要点内部**对 K 个深度层按 k·ln(k+1) 加权（legacy 0/1 列表格式走这条，见下）；**跨要点本身是等权**。

**单点 score 的两条取值分支**（`judge_v2_depth.py:445-461`）：
- 新格式（标量）：judge 直接给 0-1 浮点 → `score = clamp(float(raw), 0, 1)`（458）。
- legacy 格式（0/1 列表）：judge 给每层 0/1 → 先做「高层达成则低层自动达成」的前缀填充（451-453），再 `score = Σ_k w_k·v_k`（454，k·ln(k+1) 加权求和）。这就是「逐点加权」的字面来源。

> 一句话：逐点 overall = 各 gold 要点的连续深度分（0-1，越深挖分越高、层内 k·ln(k+1) 加权）的**等权平均**。

---

## §2 罚项结构（不完整 / 冗余 / 部分匹配）

**先厘清：「罚项」存在于状态机的目标函数 S_α（管节点树怎么长），不存在于 judge 评分（管答案打几分）。两者是不同环节，D 问的「冗余罚不罚」主要指前者。**

### 2.1 冗余惩罚（--beta，目标函数层，不是评分层）

- 公式原文（`s5_state_machine.py:380-395`，`S_alpha_corrected`）：
  `S = Σ_lv [lv·ln(k_lv+1) + α·k_lv·ln(lv+1)] − β·redundancy·total_nodes`
  其中 `penalty = cfg.redundancy_penalty_beta * red * len(nodes)`（394），`red = redundancy_score(nodes)`（393）。
- `redundancy_score`（349-377）= 节点对 3-gram Jaccard 相似度（`_ngram_overlap`，字符级 3-gram 集合 Jaccard）的**均值**。采样策略：**仅同层内**（同层 >20 节点时随机抽 20 两两配对，≤20 全配对）——docstring 声称「相邻层 + 同层」但代码无相邻层配对实现，实际只比同层；同层内 pair 数不截断（2026-11-11 D 指示全量算，旧 cap 200 会稀释罚项到≈0）。
- 系数 `β = redundancy_penalty_beta`，**默认 3.0**（121 行注释：full-pair mean Jaccard≈0.015 @n=117，β=3 使罚项≈5，约为 structural 的 5%；旧值 0.3 形同虚设）。
- **`--beta N` CLI 参数**（1716-1721，commit `112b03f38`）：覆盖 β。`β=0` = 纯 S_α 结构奖励、**无冗余惩罚**（复现 v13 时代行为，用于 ICL-hack 消融）；`β=3` 为当前默认。
- 含义：**冗余（拆了没用的同义/重复节点）会被罚**——罚项随「节点数 × 平均冗余度」线性增长，制造同义变体不再有利可图。罚的是**树的生长**（让模型少拆垃圾节点），不直接扣答案分。

### 2.2 分解不完整（漏要点）怎么扣分

- **评分层（judge）**：不漏要点不额外罚——漏掉的要点只是该 point 拿低分/0 分，拉低等权平均 overall。没有「漏一个要点扣 X 分」的独立罚项。漏得越多，overall 越低，是**覆盖度缺失的自然结果**，不是叠加惩罚。
- **目标函数层**：完整性无显式罚项/奖励项，由两个**信息/冗余过滤器**间接约束（一手核验调用点）：①`judge_necessary_batch`（159-216，调用点 1453）逐节点 LLM 判定是否"引入新信息"（新物理量/新约束/新可检索断言），非新信息节点被丢弃；②`marginal_gain`（145-156）用于 Q4 可压缩复杂度判据（调用点 1412：gain<0.3→子节点集合相对父节点几乎无新信息→膨胀，丢弃所有子节点）+ 记录用（1464）。**两者都是"砍冗余/膨胀"的过滤器，不是"奖励覆盖所有 gold 要点"的完整性项**——所以拆不够 → 树浅 → 综合答案覆盖少 → judge 分低，是间接的，无显式「不完整罚项」。

### 2.3 「对不上就没分」是否准确 —— **不准确，judge 给部分分**

- judge 对**部分匹配的要点给部分分**（连续插值，见 §1）。例如 4 层要点「给了量级和对比但没推导出数值」→ 0.65-0.75（prompt 394）；「给了公式但没代入参数」→ 该层位置一半（395）。
- 只有**完全没触及**该要点才 0 分。所以不是「对不上就没分」，而是「对到什么深度给多少分」。
- 二值口径（路径 B，`s8b_pilot.judge`，一手核验 s8b_pilot.py:157-180）才是 0/1：gold 要点逐条「覆盖/未覆盖」，**prompt 原文「覆盖=1，未覆盖或答错=0；部分覆盖按 0 计并在 reason 说明」**，`covered = sum(1 for s in scores[:n_pts] if s == 1)`、`coverage = covered/n_pts`——二值口径下连"部分覆盖"都按 0 计，是**最严格**的「对不上就没分」。r03 的 `coverage=0.133` 即 15 条 gold 要点里 2 条被覆盖（judge.scores 有 2 个 1，见 §3）。**但那是 gate 的 cov 指标，不是 D 问的逐点 overall。**
- ⚠️ **两套 gold 要点集大小不一（一手核验）**：二值 judge 用 `s8b_pilot.GOLD`（nat=6 / soc=7 / **gpu=15**），深度 judge 用 `judge_v2_depth` 内嵌 rubric（NAT=6 / SOC=7 / **GPU=38**）。nat/soc 两套点数一致，**唯 gpu 二值 15 点 vs 深度 38 点是不同大小的两套要点集**——所以 r03 的 `coverage=0.133`（2/15）与 38 点深度 `overall` 不是同一套 gold，引用 gpu 数字时必须先标是哪套。

> 一句话：冗余在**目标函数**里被罚（β·redundancy·n_nodes，默认 β=3，`--beta 0` 关掉）；分解不完整无独立罚项，漏要点只是拉低覆盖分；judge 评分**给部分分**（连续插值），「对不上就没分」只对二值 coverage 口径成立，对逐点 overall 不成立。

---

## §3 r03 伪影机理（代码分支级）

**现象**（`ablation-runs/gpu_formula_r03_judge.json`，实测）：
- `raw`（judge 原始输出）= **100 个键** `pt1..pt100`，**全部 = 0.33**（100 点全 0.33）。
- `point_scores` = **38 个键**（N-0/N-1/…/SHARED/META，当前 GPU_RUBRIC 的 38 要点），**全部 score=0.0**。
- `overall = 0.0`。而同批 r01/r02/r04/r05/r07/r08 的 raw 都是 38 键、overall 0.31-0.51。

**机理（两步，均已代码+git 证实）**：

1. **judge 输出退化（源头）**：r03 的 judge 调用返回了 100 个 `ptN` 键、值全 0.33 的退化输出。注意：**任何版本的 GPU_RUBRIC 都没有 100 个要点**（git 考古：9→15→32→38→40 键，从未 100）。所以这不是「100 个真实要点各 0.33」，而是 judge（27B@8787）对该次超长/异常输入**没按 rubric 逐点打分，而是幻觉出一个 100 键、值坍缩到 0.33 的均匀伪输出**（0.33≈1/3，像是「3 层要点只达 L1」的默认锚点被无差别套用）。真实覆盖水平≈0.33（状态机报告 §2 的判断）。

2. **聚合代码把非零 raw 变成 0（伪影固化点）**：`score_run` 聚合时按 **rubric 的 38 个要点名**去 `raw` 里取值：
   - **修复前**（commit `a8ae30551` 之前，即生成 r03 的代码）：取值逻辑是 `raw = scores_raw.get(pt_name, 0)`（旧行 433）。rubric 要点名是 `N-0/N-1/…`，而 raw 键是 `pt1..pt100` → **每个要点都取不到 → 默认 0** → 38 个 point_scores 全 0 → `overall = Σ0/38 = 0.0`。**这就是「raw 有非零 0.33 却被聚合成 0」的确切分支：键名格式不匹配 + `.get(key, 0)` 的 0 兜底。**
   - **修复后**（`a8ae30551`，2026-11-18，commit message 原文「取不到 → depth 恒 0（**r03 即此 bug 产物**）」）：加了 `pt_map` 按 rubric key 顺序建 `ptN→N-X` 映射（judge_v2_depth.py:431-441），`_lookup` 先按要点名查、再按 ptN 反查，两种格式都能取到值。修复后 r03 这种数据会被映射成 N-0/N-1/N-2 ← pt1/pt2/pt3 = 0.33（commit message 已验证）。

**为什么只有 r03 中招**：其余 rep 的 judge 正常输出 38 个 `N-X` 键（与 rubric 同名），`.get(pt_name)` 直接命中，不走 0 兜底；只有 r03 的 judge 退化成了 `ptN` 格式 + 100 键，撞上修复前的格式盲区。

**定性**：r03 的 `overall=0.0` 是**聚合伪影，不是真实 0 分**。真实覆盖≈0.33（raw 均值），应从均值统计剔除（状态机报告已剔，6 有效）。注：该文件 mtime 为 2026-11-26 00:47（晚于 11-18 修复），但其内容是**修复前代码**产生的数据（git 里自 `b0fb66a29`(11-19) 起未变过），mtime 只是文件被 checkpoint/复制刷新，不代表用新代码重判过——**它至今仍是坏数据，未重判**。

**全仓伪影扫描（2026-11-26 补验，全量重扫修正）**：对 `experiments/stage-ablation/` 全部含 `point_scores`+`overall` 结构的 judge 文件跑伪影检测器（raw 非零点>0 且 point_scores 全 0 / raw 键数≠ps 键数），共 **15 个文件 / 237 个 score_run 对象**，**仅 r03 一个 ARTIFACT**。分布：`ablation-runs/gpu_formula_r01-r08`（7 个 gpu 对象，r03 伪影，r01 .395/r02 .351/r04 .509/r05 .395/r07 .402/r08 .310 均 raw/ps 键数一致）+ `runs-prod/judge-v2-{S0,A3,A4}-{nat,soc}` 与 `runs-prod-s3/judge-v2-S3-{nat,soc}`（230 个 nat 6 点 / soc 7 点对象，raw/ps 键数全一致、零伪影）。**「r03 唯一伪影」经全仓 237 对象扫描确认，非仅 gpu_formula 系列内成立。**

**独立复现（2026-11-26 二次核验）**：用独立脚本（递归遍历全仓 .json，兼容顶层 dict/list/嵌套三种结构）重跑同一检测器，**精确复现 237 对象 / 15 文件 / 1 伪影（r03）**，分布 7 gpu + 230 prod（S0-nat 20 / 其余各 30），key-mismatch 对象仅 r03 一个。注：首版检测器漏了顶层 list 结构（runs-prod 文件是 list 非 dict）只数出 7 对象，修正后与报告 237 一致——**237 这一关键统计声明经独立脚本一手复现坐实**。

**离线重判复算（2026-11-26，不调 LLM，纯本地）**：用当前 HEAD 的 ptN→N-X 映射 + 聚合逻辑对 r03 已有 raw 复算，38 个要点全映射到 0.33 → **overall = 0.33**（印证"真实覆盖≈0.33"）。对 7 个 gpu rep 均值的影响：剔除 r03（6 有效）= **0.3934**（与状态机报告 §2 记的 0.393 一致）；含重判 r03(=0.33) 的 7-rep = 0.3844，**Δ 仅 -0.0091**——**剔除 r03 不扭曲结论**，重判与否均值几乎不变，"剔除"是稳健选择。

> 一句话：r03 伪影 = judge 退化成「100 个 ptN 键全 0.33」+ 修复前聚合代码按 `N-X` 要点名 `.get(...,0)` 取不到值全落 0 兜底 → 非零 raw 被聚合成 overall=0.0；`a8ae30551` 加 ptN→N-X 映射已修，但 r03 数据本身未重判。

---

## §4 两套口径对照表（canonical n=90 总分 vs v18 逐点 overall）

| 维度 | canonical n=90 总分（路径 C） | v18 逐点 overall（路径 A） |
|------|------------------------------|---------------------------|
| 代码 | `score.py::score_run` | `judge_v2_depth.py::score_run` |
| 聚合公式 | `total = Σ_k scores[M_k]·weights[M_k]`（score.py:307），六维加权：M1 0.25 / M2 0.20 / M3 0.15 / M4 0.20 / M5 0.10 / M6 0.10（232 行；Q5 时 M1 减半 0.125 后重归一，233/302-305） | `overall = Σ_points score_p / N_points`（judge_v2_depth.py:465），跨要点等权平均 |
| **聚合公式是否同一个** | **否，完全不同的两套公式**：C 是「六维质量分 × 固定权重」，A 是「gold 要点深度分等权平均」。C 不逐 gold 要点打分（M1 按断言 match 率、M4 按缺口覆盖），A 逐 gold 要点打连续深度分 | 同左 |
| 单点分档 | M1/M4 是 judge 断言级 match 率（matched/total_decidable），M2/M3/M5/M6 是 gates.py 规则分 | 每要点 0-1 连续深度分（层内 k·ln(k+1) 加权） |
| 题集 | **Q1-Q5**（questions/Q1-gpu-h100 … Q5-methodology，gold/ 目录 5 份） | v18 状态机题：**nat / soc / gpu**（+ q6/q7/q8 新题），rubric 在 judge_v2_depth.py 内嵌（NAT_RUBRIC 6 点 / SOC_RUBRIC 7 点 / GPU_RUBRIC 38 点） |
| **题集是否同一批** | **不是同一批**。canonical Q1-Q5 与 v18 nat/soc/gpu 是不同题面（nat/soc/gpu 来自 T53 新题域，Q1-Q5 来自 r1 + t17-generalization）。唯一重叠嫌疑：Q1-gpu-h100（GPU 规格）vs v18 gpu 题（GPU TCO/roofline）——同域不同题面，gold 要点集不同，不能当同题 | 同左 |
| judge | 同源 27B @8787，temp=0（RESCORE-V3-NOTES：确定性已验证；score.py:14 `LLM_URL=127.0.0.1:8787`、:23 temperature=0 一手核验） | 同源 27B @8787（ablation_harness.py:19 `LLM_URL=127.0.0.1:8787`），temp=0 |
| **数据足迹（2026-11-26 全仓扫描）** | scoring.md 91 数据行（一手统计：仅 S0 31/S1 30/S5 30 三臂 × Q1-Q5 × r1-r6，**不含 S2/S3/S4**）；canonical n=90 基准（S0-S5 全 6 臂 × Q1-Q5 × r1-r3=90）是另一批数据（scoring-v3-gatefixed.md），scoring.md 是其子集+扩展 rep，两者不可混用 | **不止 v18 状态机**：`ablation-runs/gpu_formula_*`（v18 状态机，7 rep）+ `runs-prod/judge-v2-{S0,A3,A4}-{nat,soc}`、`runs-prod-s3/judge-v2-S3-{nat,soc}`（S0/A3/A4/S3 臂 × nat/soc × r1-r30，共 230 对象）——同一 `score_run` 口径横跨多个实验批次 |
| 基准值 | S5≈0.579 / S0≈0.397（scoring-v3-gatefixed.md，n=90，S0-S5×Q1-Q5×r1-r3） | v18 gpu mean 0.393（7 rep 剔 r03 后 6 有效）；nat gate 0.5801 / soc 0.898（二值 cov 口径，非 A） |
| 可比性 | 状态机报告 §2 已标注：**跨行比较只看方向，绝对值不可直接比**；要与 0.579 可比须在「同一 judge + 同一题集（canonical n=90 口径）」下重判（状态机报告 §4 第 5 条待办） | 同左 |

**附带第三条口径（gate 的 cov）**：`s8b_pilot.judge` 二值覆盖（gold 要点逐条 0/1 → coverage），nat gate 0.5801 / soc gate 0.898 用的是它，**既不是 A 也不是 C**，三套口径并存，引用数字时必须先标口径。

**⚠️ 「rubric v3」命名碰撞（2026-11-26 一手核验）**：`bench/rubric-v3/` 目录（DRAFT-rubric-v3.md / v2 / v3.1-s01-fix）是**第三套 rubric 体系**——「outcome + process 双层 pipeline 评分标准」（O1 候选集覆盖度 / O2 矛盾挖掘深度，0/1/2 三档，设计原则第 1 条明文「outcome 和 process 分开报，不合成总分」），**不是本报告的逐点 gold 深度 rubric**（后者内嵌 `judge_v2_depth.py`，NAT 6 / SOC 7 / GPU 38 点，0-1 连续深度分）。另有 `bench/rubric-v3/ablation/gold-Q6~Q10.md`（Q6 CDN / Q7 存储 / Q8 eval-benchmark / Q9 VLM / Q10 RLHF 五道新题 gold 树，属 pipeline rubric 的消融材料，与 Q1-Q5 AI/ML 域无重叠）。引用「rubric v3」时必须先区分三套：① pipeline 级 outcome+process 草案（`bench/rubric-v3/DRAFT-*`）② 逐点深度 rubric（`judge_v2_depth.py` 内嵌）③ 二值 gold（`s8b_pilot.GOLD`）。

**⚠️ 同名"v3"两批数字并存（2026-11-26 一手核验，引用前必看）**：`research/` 下有两个都叫"v3"的文件，数字差很大，**不可混引**：
- `scoring-v3-gatefixed.md`（2026-11-05，**n=90**，S0-S5 全 6 臂 × Q1-Q5 × r1-r3）：S0=0.397 / S1=0.526 / S5=0.579 —— **本报告引用的 canonical 基准即此批**。
- `RESCORE-V3-NOTES.md`（2026-11-06，**61 runs**，主臂仅 S0/S1/S5 三臂 × Q1-Q5 × r1-r3=45 + 次臂 16）：S0=0.615 / S1=0.630 / S5=0.805 —— 数字显著更高。
- 差异根源（RESCORE-V3-NOTES 自述）：judge 从 v2→v3 改为 **full gold text（去掉 [:6000] 截断）+ type-aware assertion 抽取** + Q4 token-equivalent 修复。同一 27B@8787/temp=0，但 judge prompt 版本不同 → 分数系统性抬高（S5 0.579→0.805）。
- 另有 `scoring-v4-m2m5fixed.md`（2026-11-05，v4 M2/M5 口径修正）：S0=0.4894 / S5=0.7061，其"与 v3 对比"节记 v3 S0=0.3973/S1=0.5259，**与 gatefixed 的 0.397/0.526 互证**（坐实 gatefixed 数字）。
- **结论**：引用"canonical S5≈0.579/S0≈0.397"必须指明是 **gatefixed（11-05, n=90, 6 臂, judge 截断版）**；若用 RESCORE-V3（11-06, 3 主臂, judge full-gold 版）则是 0.805/0.615。两套都叫"v3"但 judge prompt 版本 + 臂数 + run 数都不同，绝对值不可互换。

---

## §5 对 D 问题的直接回答（每问一行）

1. **「逐点 overall」是什么**：judge 对每个 gold 要点打 0-1 **连续深度分**（要点内按深度层 k·ln(k+1) 加权、层间可插值），overall = 各要点分**等权平均**（`judge_v2_depth.py:465`）——不是 0/1 二值，也不是 0/1/2 档。
2. **评分具体怎么算，对不上就没分吗**：不是——judge 对部分匹配的要点**给部分分**（对到什么深度给多少分）；漏要点无独立罚项，只是覆盖缺失拉低平均分；「对不上就没分」只在二值 coverage 口径（gate 的 cov）下成立。
3. **冗余罚不罚**：罚，但在**目标函数层不在评分层**——`S_α = 结构项 − β·redundancy·n_nodes`（`s5_state_machine.py:394`），默认 β=3，`--beta 0` 可关（复现 v13 无惩罚行为）；罚的是拆垃圾节点，不直接扣答案分。
4. **r03 为什么 0 分**：judge 退化成 100 个 ptN 键全 0.33 + 修复前聚合代码按 N-X 要点名 `.get(...,0)` 全落 0 兜底 → 伪影 0.0；离线重判复算真实 overall=0.33，剔除与否 7-rep 均值仅差 -0.009（0.3934 vs 0.3844），剔除稳健；`a8ae30551` 已修代码，r03 数据未重判。
5. **两套口径**：canonical n=90 总分（六维加权，Q1-Q5）与 v18 逐点 overall（要点等权平均，nat/soc/gpu）**公式不同、题集不同**，绝对值不可直接比，只比方向。

---

## 附录：证据索引

- 聚合公式：`experiments/stage-ablation/judge_v2_depth.py:408-467`（score_run）、`:33-41`（`_w3/_w4` k·ln(k+1) 权重，K=3 实际 [0.098,0.312,0.590]）、`:388-404`（judge prompt 原文）
- 六维总分：`experiments/stage-ablation/score.py:232-233,267,307`
- 冗余罚项：`experiments/stage-ablation/s5_state_machine.py:121,349-395,1716-1721`；`--beta` commit `112b03f38`
- 完整性过滤器：`marginal_gain` s5_state_machine.py:145-156（调用点 1412 Q4 判据 gain<0.3 丢弃 / 1464 记录）、`judge_necessary_batch` :159-216（调用点 1453）——均为砍冗余/膨胀，非完整性奖励
- 二值 cov 口径：`experiments/stage-ablation/s8b_pilot.py:157-180`（judge，GOLD[gpu]=15 点 vs 深度 GPU_RUBRIC=38 点）；r03 coverage=0.133 出自 `ablation-runs/gpu_formula_r03.json`（非 _judge.json）
- r03 数据：`ablation-runs/gpu_formula_r03_judge.json`（raw 100 键全 0.33 / point_scores 38 键全 0 / overall 0.0）；修复 commit `a8ae30551`（message 点名 r03）
- 口径标注：`state-machine-status-20261126.md` §2（口径标注，line 20）/ §4（下一步，第 5 条口径统一待办；该文件仅 §1-§4 无 §5）；canonical 基准 `modules/A-eval-infra/research/scoring-v3-gatefixed.md`
- judge 端点：`ablation_harness.py:19`（127.0.0.1:8787，本地 proxy→27B）+ `score.py:14`（同 8787，temp=0）+ `t53_bface_judge.py:11`（localhost:1234，qwen2.5-7b 异族 B-face 专用）；本次未调用任何端点
- canonical 数据足迹：`modules/A-eval-infra/research/scoring.md`（91 数据行，仅 S0/S1/S5 三臂 × Q1-Q5 × r1-r6）
- 「rubric v3」命名碰撞：`bench/rubric-v3/DRAFT-rubric-v3.md`（pipeline outcome+process 双层草案，0/1/2 三档，「分开报不合成总分」）≠ 逐点深度 rubric（`judge_v2_depth.py` 内嵌）≠ 二值 gold（`s8b_pilot.GOLD`）；`bench/rubric-v3/ablation/gold-Q6~Q10.md` 五道新题 gold 树（CDN/存储/eval-benchmark/VLM/RLHF）
- **独立复算脚本**：`experiments/stage-ablation/verify-scoring-20261126.py`（`python3 verify-scoring-20261126.py`，只读不调 LLM，24 项断言全 PASS：「rubric v3」命名碰撞(bench/rubric-v3/=pipeline outcome+process 双层草案 0/1/2 三档≠逐点深度 rubric≠二值 gold，Q6-Q10 五道新题 gold 树)、canonical 六维权重 M1.25/M2.20/M3.15/M4.20/M5.10/M6.10 + Q5 M1 减半重归一、双 v3 陷阱数字 gatefixed S0=0.397/S5=0.579 vs RESCORE-V3 S0=0.615/S5=0.805（一手解析两源文件非转录）、_w3/_w4 权重、GPU/NAT/SOC rubric 键数 38/6/7、r03 raw 100 键全 0.33 + 存储 overall=0.0 伪影 + 当前 HEAD 逻辑重判=0.33、7 gpu rep 均值剔 r03=0.3934/含重判=0.3844/Δ=-0.0091、全仓 237 对象/15 文件/仅 r03 一个伪影）
