# T35 Goal（goal 落库等效物）

> 本环境无 `create_goal` 工具，按任务书规定本文件即 goal 落库等效物。
> 格式遵循 `agents/goal-template.md` §1 五字段。
> 绑定任务：T35「S8 嵌入式验证 + 数字一致性修复建议」。
> 执行通道：**本地降级**（本任务不做 arena 外包），按 `pfb/sop/arena-loop-pipeline.md` §0：loop 六阶段不豁免，conf 标 0.2。

## 【目标】

复核 pfb stage-ablation 主结果的数字一致性并产出「文件+行号+旧值+正确值」修正清单（不直接改已有文件）；实验验证把 claim 级验证规则**嵌入 S7 既有节点、保持单次生成**能否在保住 M6 引用能力的同时，用单次生成拿到接近 S7V 的 M1。

## 【阶段】

pfb / experiments/stage-ablation，T30–T32 工具链（S7T/S7F/S7V）已完成、paper v2.0 已成稿之后的 **T35 一次性优化迭代**。
四段对应 1-loop：调研与交叉验证（02/02.5）→ 实验（04）→ 迭代优化判定（04.5 前半）→ 反方复核（04.5）。
产出 FINAL.md 后立即结束，不自行创建新 goal、不开新任务。

## 【SOP 索引】

- `agents/goal-template.md` §1 五字段 / §2 1-loop 六阶段 / §3 质量原则 / §4 量化验收
- `pfb/sop/arena-loop-pipeline.md` §0 优先级（降级：本地执行、loop 不豁免、conf 0.2）、§3.1 judge 同族标注条款（`qwen3.8-27b ×1, non-IRR`）
- `pfb/experiments/stage-ablation/ablation_harness.py`、`score.py`、`score_m7.py`（复用现有 harness 与评分口径，不另造评分标准）
- `pfb/experiments/stage-ablation/paper-draft.md` §3.2 臂定义 / §4.1 主表 / §4.2 per-question / §5.1 T30–T32（只读取证，不改）
- `README.md`、`tasks/T30,T31,T32-*.md`（只读取证，不改）

## 【验收标准】

1. 6 个交付文件（`goal.md`/`01-research.md`/`02-experiment.md`/`03-iteration.md`/`04-review.md`/`FINAL.md`）全部存在且非空；`goal.md` 含 §1 全部五个字段标题。
2. 数字一致性审计列出 ≥3 处带「文件+行号+旧值+正确值」的不一致；run 对账给出 S7T/S7F/S7V 各有效 run 数（目标 15/15/15）。
3. 实验至少完成 4 个 pilot run（Q1+Q4 × 2 reps）或明确记录端点降级原因；每个 run 有可复核的原始指标（M1/M4/M6/total）。
4. per-question 对比表包含 S7 / S7V / S8E 三臂在 pilot 题目上的 total 与 M1。
5. 从原始 JSON / 评分输出独立复算的 mismatch 数明确写出（目标 0）；≥2 个反驳角度各有 verdict（成立/不成立/无法判定）。
6. 迭代轮数 ≤2、实验总 run 数 ≤19、未 push、未改任何已有文件、未读写 `~/.hermes/.stage-gate/`、未创建 goal/PAUSE/HALT/INBOX、未触发 hook。

## 【失败降级】

- **端点降级**：`:8787` 单 run >120s 或不可用 → 立即停止扩展，如实记录为降级（conf 0.2），不空转重试；pilot 不足 4 则写明原因，验收 3 按降级计。
- **实验降级**：pilot 无正向信号（total 或 M1 至少一题 ≥ S7V 且无任何题掉 >0.1）→ 不扩到 15 runs，直接写否定结论 + 适用边界，禁止包装成提升。
- **提交降级**：`git status` 出现他人改动 → 跳过 `git commit`，在 FINAL.md 说明。
- **口径降级**：judge 为同族单 judge（27B 自评，非独立 IRR）；`score.py` 实为 6 维口径，与 paper 7 维 rubric 的 total 不可直接比较，冲突时以「同一 score.py 口径本地重算」为准并显式标注。
- 注：goaltemp §3 写「complete 后 commit + push」，本任务书硬性禁止 push，以任务书为准，仅 `git add` + `git commit`。
