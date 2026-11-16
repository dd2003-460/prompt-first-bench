# T53-B12 阶段 01：目标分解

- 任务书：`tasks/B-pipeline-ablation/TASK-B12-t53-deepresearch-bench-spec.md`
- 分支：`arena/f65a5a27-prompt-first-bench` @ `f60e7f7`
- 阶段：01-goal-decomposition（只分解，不下结论）
- 必读已执行：`sop/arena-loop-pipeline.md`、`loop/00-common-review.md` … `loop/04.5-final-review.md`（注意：路径是 `loop/*.md`，不是任务书 "1-loop" 里暗示的 `loop/prompt-first/`）

## 1. 总命题

> S5 状态机在 ≥5 道 deepresearch 类题上的最终答案质量（judge 0-1）≥ 当前开源 SOTA 在同题上的分数。

拆三段：
- P1（题集）：≥5 题，其中 ≥3 题为新增，且每题可对上一个有公开分的 bench。
- P2（对标）：每题的 SOTA 分可得（公开 or 同机复跑），且与本 bench judge 口径可比。
- P3（判决）：n=3 median 下的分数差，且无泄漏（A6）、无通道静默降级。

## 2. 子问题 → 可判定化

| # | 子问题 | 成立口径 | 最小证据 |
|---|---|---|---|
| S1 | 题集够不够 | 5 题，qid 明确、题面落盘、题型覆盖多跳+检索 | 题面文件 + 表 |
| S2 | SOTA 分有没有 | 每题 ≥1 个开源系统分，带 URL + 日期 | leaderboard/论文原文 |
| S3 | 口径能不能比 | 三个尺度（0-1 / 0-100 RACE / F1）是否同尺度 | 判据文件写明 |
| S4 | 能不能跑 | 生成端 + judge 端可达 | 端点探测记录 |
| S5 | 泄漏与否 | prompt/日志/中间产物无题面原文 | grep 题面关键词 |

## 3. 预先裁定（防事后挪球门）

1. **"打赢"只用 L0（同机同 judge 复跑开源框架）判**；公开分（L1）只作量级参照，不得用于"打赢"结论。
2. **null ≠ 0**：未跑的题分数记 null，禁止当 0 参与均值/对标表述。
3. **复用题不重跑**：`gpu`、`drb-2` 直接用旧 run；但旧分若口径不符（同族 judge）须标注，不得冒充 B-face 分。
4. **公开分查不到就 `[待核验]`**，不编造。
5. **通道故障必须显式登记**（status=blocked + 证据），不得静默跳过。

## 4. AC → 机检映射

| AC | 机检 |
|---|---|
| AC1 ≥5 题（≥3 新） | 题面文件含 3 个新 qid + 报告表 5 行 |
| AC2 每题 ≥1 开源 SOTA 公开分 | 判据文件 §3 表 5 行均有 L1 分 + URL |
| AC3 judge n=3 median | run 记录含 `scores.s5_judge_n3_median` 字段（可为 null + blocked） |
| AC4a 报告 ≥5 题表 | 报告含 "五题对标表" |
| AC4b 每题 run 落盘 | 5 个 `runs-s5-sm-<qid>.json` 存在 |
| AC4c 判据文件落盘 | `sm-bench-sota-criteria.md` 存在 |
| AC5 A6 无题面原文 | 新 run 文件无 `question` 字段、无题面长句 |
| AC6 回执含 repo/branch/commit_sha | JSON 可解析 + 三字段非空 |
