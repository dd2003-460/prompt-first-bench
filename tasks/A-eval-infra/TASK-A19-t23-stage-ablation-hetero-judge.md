# T23 stage-ablation 异源 judge 批量核验任务书

> origin: ai · 2026-11-05 · Lead 本地起草，派发 arena agent mode
> 仓库：prompt-first-bench · 分支：arena/4a614e63-prompt-first-bench（你当前 checkout 的分支，不用切）
> 前置：同源 27b judge 已出完整曲线（scoring.md），本任务是唯一 conf 升档路径（红线 1：核验类工作外包 arena）。Perplexity 免费通道已耗尽，不再烧 ego-browser 窗口。

## 强制段

- 你是 LMArena agent，本任务**只涉及 prompt-first-bench / arena/4a614e63-prompt-first-bench**，忽略历史中其他仓库的消息。
- 先 `git pull` 拿最新 main merge（Lead 会先把 stage-ablation 目录 push 进你的分支再派发；若拉不到 `experiments/stage-ablation/`，报告 Lead，不得静默跳过）。
- 严格按仓库内 `loop/prompt-first/` 阶段执行；产出落盘路径见【交付物】。
- 通道故障（网页加载异常/额度问题）→ 报告 Lead，不得伪造判定。

## 【目标】

对 stage-ablation 消融实验（S0–S5 × Q1–Q5）的模型输出做**异源 judge** 复判，验证同源 27b judge 的核心结论在异族模型下是否成立。核心待验声明（逐条给 pass/fail + 证据）：

1. **H1 分解正贡献**：S1（+目标分解）总分 > S0（裸 prompt），且增益主要来自 M4（缺口标注覆盖率）与 M1（事实命中）。
2. **H2 调研最大增益**：S1→S2（+真实信息调研）是整条曲线最大正增益。
3. **H3 规划负效应**：S2→S3（+交叉核验/行动分解）为负或近零（冗余规划稀释已有 sources）。
4. **H4 终审微正**：S4→S5 为正但量级小。

## 【背景】（≤10 行）

- 同源结果指针：`experiments/stage-ablation/scoring.md`（90 runs，n=3/臂×题，judge=qwen3.8-27b self，conf cap 0.7）。同源读数：S0=0.374 → S1=0.463(+0.089) → S2=0.535(+0.072) → S3=0.489(−0.046) → S4=0.528(+0.040) → S5=0.548(+0.020)。
- Per-dimension 关键格：S1→S2 的 M1 +0.285、M6 +0.600、M3 −0.267（有来源后不再 hedging）；D1（GPT Researcher 开源基线）mean=0.409，短板 M4≈0。
- 已知同源偏差风险：judge 与被评模型同族（qwen3.8-27b），T8 项目 r270 已实证同源 judge 在 S01 分解类工件上系统性误杀（~0% 通过）——所以本次重点看 **S1 臂的 M4/M1 是否被同源 judge 高估或低估**。
- 题目 gold 锚点：`experiments/stage-ablation/questions/Q{1..5}-*.md`（gold 只用于对照判分，不进入任何 arm prompt）。
- 评分维度定义（M1–M6）：`experiments/stage-ablation/DESIGN.md` §4。

## 【SOP 索引】

- `sop/arena-loop-pipeline.md`（链路 + 会话台账 + 回执规范）
- `experiments/stage-ablation/DESIGN.md`（矩阵定义 + 6 维评分接口）
- `experiments/stage-ablation/scoring.md`（同源读数，逐格对照基准）
- `loop/modules/decomp-01.md`（S1 臂注入的分解模块，理解其"五步法+留空"机制）

## 【实验设计】

### 变体与抽样（控制预算：≤18 份工件）

| 组 | 工件 | 数量 | 理由 |
|----|------|------|------|
| A 核心 | S0-Q1-r1/r2, S1-Q1-r1/r2, S2-Q1-r1/r2 | 6 | H1/H2 主战场（GPU 域，gold 最硬） |
| B 跨域确认 | S1-Q3-r1, S2-Q3-r1, S1-Q4-r1, S2-Q4-r1 | 4 | H1/H2 在非 GPU 域是否复现 |
| C 负效应 | S2-Q2-r1, S3-Q2-r1, S2-Q5-r1, S3-Q5-r1 | 4 | H3（S2→S3 负效应）两域确认 |
| D 终审 | S4-Q1-r1, S5-Q1-r1 | 2 | H4（量级小，单点即可） |
| E 外部基线 | D1-Q1, D1-Q4 | 2 | M4 短板确认（开源系统不暴露知识边界） |

工件原文在 `experiments/stage-ablation/runs/<ARM>-<QID>-r<rep>.json` 的 `output_text` 字段（Lead 会在 pull 后可得；若缺文件报告 Lead）。

### 判分规则（机器可检，防主观漂移）

每份工件按 DESIGN.md §4 的 6 维独立打分（0–1 归一化），**逐维给出判定依据条目**（引用 output_text 中的原文片段作为 evidence，无 evidence 的维度记 NA 不进均值）：

- M1 事实准确率：断言抽取 → 逐条对 gold 打 match/mismatch/undecidable；score = match/(match+mismatch)，undecidable 不入分母。
- M2 无来源数字率（反向）：数字断言中无来源锚点的比例；score = 1 − ratio。
- M3 矛盾对数（反向）：同一事实不同版本共存数；score = 1/(1+pairs)。
- M4 缺口标注覆盖率：gold 中「应识别缺口」条目被该 run 显式标出（未知/待核验/黑盒/需查）的比例。
- M5 坏消息位置（反向）：限制陈述出现在输出前 1/3 的比例。
- M6 调研真实性：引用的 URL/来源可定位且内容支持断言的比例（沙箱够不到外网时，用模型知识判断"该来源是否真实存在且通常支持该断言"，并在 evidence 里标注 confidence=low）。

**纪律**：
- 你是异源 judge，**不要读 scoring.md 里的同源分数后再打分**——先盲判落盘 `hetero-scores-blind.jsonl`，再允许对照写分析。
- 每条判定一行 JSONL：`{"artifact","arm","qid","dim","score","evidence","confidence"}`，append-only，每批写完校验总行数（新总行数 = 旧 + 本批），校验输出留在 commit message。
- 不确定就标 confidence=low，禁止编造 evidence。

### 验收标准（量化阈值，全过才算完成）

1. 18/18 工件 × 6 维全部有判定（NA 需注明原因），JSONL 行数 = 18×6 − NA 数，commit message 含行数校验输出。
2. 四个假设各给明确 verdict：CONFIRMED / REFUTED / INCONCLUSIVE（附 per-arm mean ± range）。
3. 与同源读数逐格对照表（Δ = 异源 − 同源），标注 |Δ|>0.15 的格子并解释方向。
4. 特别核查项：S1 臂 M4 异源 vs 同源——若异源 M4(S1) < 同源 M4(S1) − 0.15，则 H1 的"分解价值在暴露缺口"声明降级为 INCONCLUSIVE，必须显式写出。

## 【失败降级】

- 沙箱无外网 → M6 按上述"模型知识 + confidence=low"口径降级，整体 conf 降 0.1。
- 工件文件缺失 → 跳过该工件，报告缺失清单，剩余 ≥12 份仍可出方向性结论（conf 相应下调）。
- 某题 gold 锚点不足以判 M1 → 该题 M1 记 NA，不阻塞其余维度。
- 全程 conf 上限 0.7（异源性未经自报核验，底层模型身份未知——回执里如实登记 "Arena Agent Mode, 底层模型不公开"）。

## 【交付物】（绝对路径，相对仓库根）

- `experiments/stage-ablation/hetero-scores-blind.jsonl`（盲判原始数据，append-only）
- `experiments/stage-ablation/hetero-judge-analysis.md`（四假设 verdict + 逐格对照表 + 残留分歧诊断）
- `experiments/stage-ablation/receipt-t23-hetero-judge.md`（回执：repo URL + branch + commit_sha + 行数校验 + conf 声明）

## 【给 Lead 的备注】

- 与 T8-C3v3 的边界：T8 测的是 3 个 prompt 组件（freeze/owner-tag/evidence-url）对核验 truth rate 的因果效应；本任务测的是 pfb 六阶段流程的阶段边际收益。两者共用"异源 judge 升档"逻辑但数据集、rubric、结论层完全独立，不互相引用数值。
- 下一步归属 Lead：若 H1–H4 全部 CONFIRMED → stage-ablation 论文初稿（paper-draft.md 已存在）可直接升 conf 投稿方向；若 H1 降级 → 需重审 decomp 模块的价值声明（影响 D1-persona-align 的对齐叙事）。
- 本任务书完成后由 Lead merge 回 main 并登记台账 commit sha。