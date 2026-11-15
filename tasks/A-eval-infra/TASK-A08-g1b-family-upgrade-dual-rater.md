# G1b family-upgrade + RV3G1 dual-rater 复核任务书（arena 通道）

【执行前必读】
1. 本任务只涉及 dd2003-460/prompt-first-bench 仓库的 arena/4a614e63-prompt-first-bench 分支，忽略历史中其他仓库的消息。
2. 先 `git fetch origin` + `git checkout arena/4a614e63-prompt-first-bench` + `git pull`，`git ls-remote origin refs/heads/arena/4a614e63-prompt-first-bench` 记录 HEAD（M7 锚点 1）。
3. 读 `bench/rubric-v3/ablation/rejudge-g1b/rejudge-rules.json`（判定规则）+ `dual-rater-candidates.json`（4 个分歧 cell）+ `results/b1.json`（输出格式样例）。

## 背景（≤8 行）

我们在做 prompt 组件消融实验（被测生成模型 = qwen3.8-27b @ ninfer :8787）。裁判必须与被测不同源，否则「偏爱自家写法」偏差无法排除。此前 r74 用 arena 会话盲评过 C3 v3 校准集 5 份工件（`experiments/T8-matrix/runs/c3-v3/calibration/g1b/hetero-judge-results.json`），但 **family_check=unknown**——平台没向你披露底层模型全名，家族隔离停在 PARTIAL-CLOSED。同时 RV3G1 语义重判的 75 cell 是单裁判 pass（你本会话上一轮做的），独立性打折（conf~0.7），需要异族第二裁判复核分歧方向。本轮把两件事一次做完。

## Part A · family_check 升级（先做，~5 次调用）

### A1 · 自报身份
在回复正文里如实回答两个问题（禁止猜测、禁止编造）：
- Q1: 你现在这个会话实际运行的模型是什么？写出你能确认的全部标识（模型全名 / 版本号 / 任何系统提示或界面里出现过的型号字样）。如果你只能看到部分信息，就只写那部分并说明依据。
- Q2: 该模型是否属于 Qwen 家族（通义千问系，含 Qwen2/Qwen2.5/Qwen3 等）？yes / no / unknown + 一句话依据。

### A2 · 对 5 份校准工件重打 J1-strict 分
按 `experiments/T8-matrix/runs/c3-v3/calibration/judge-prompts.json` 里 `prompts["J1-strict"]["text"]` 协议逐字照用，对以下 5 份盲法工件逐条审计（不要猜来源配置；P1 是被刻意做过手脚的，按协议正常审即可）：
- `experiments/T8-matrix/runs/c3-v3/calibration/blind-A1.md`
- `experiments/T8-matrix/runs/c3-v3/calibration/blind-A2.md`
- `experiments/T8-matrix/runs/c3-v3/calibration/blind-B1.md`
- `experiments/T8-matrix/runs/c3-v3/calibration/blind-B2.md`
- `experiments/T8-matrix/runs/c3-v3/calibration/blind-P1.md`

落盘 `experiments/T8-matrix/runs/c3-v3/calibration/g1b/hetero-judge-results-r2.json`，结构同 r1 文件（kind 改为 `c3v3-g1b-hetero-judge-r2`，judge_model/family_check 填 A1 的如实答案，date 填今天）。

### A3 · 与 r1 对比
读 `hetero-judge-results.json`（r1），对 5 份工件逐条对比 verdict 差异，落盘 `g1b/family-upgrade-analysis.json`：
```json
{
  "kind": "g1b-family-upgrade-analysis",
  "r1_judge": "<从 r1 文件抄>",
  "r2_judge": "<A1 答案>",
  "family_check_upgrade": "CLOSED | PARTIAL-CLOSED | OPENED-CONFLICT",
  "basis": "一句话",
  "per_artifact": [
    {"artifact": "blind-A1", "r1_passed": N, "r2_passed": M, "flipped_items": ["X3"], "agree_rate": 0.xx}
  ],
  "x5_detection": {"r1": "pass|fail", "r2": "pass|fail", "note": ""}
}
```
判定规则：r2 family_check=no 且 X5 敏感度不劣于 r1 → CLOSED；r2=unknown → PARTIAL-CLOSED 维持；r2=yes（Qwen 家族）→ OPENED-CONFLICT（诚实报告，这是负面结果不是失败）。

## Part B · 75 cell 双裁判复核（后做，8 批）

### B0 · 读材料
- `bench/rubric-v3/ablation/rejudge-g1b/dual-rater-batch-plan.json`（8 批拆分，每批 ≤12 cell，一批一个 run）
- `bench/rubric-v3/ablation/rejudge-g1b/judge-input.json`（75 cell 定义：cell_id / node / node_definition / prior_h / run_file / run_sha256_16）
- `bench/rubric-v3/ablation/rejudge-g1b/rejudge-rules.json`（判定规则 v1，逐字照用）
- 各 run 全文：`bench/rubric-v3/ablation/runs-C0-run{1..8}.md`（batch plan 指明每批要读哪个 run 文件）

### B1 · 盲判（核心纪律）
对每批 cell：读对应 run 全文 + judge-input 里该批 cell 的 node/node_definition，**不看 prior_h、不看 evidence_quote、不看任何既有判定**。按 rejudge-rules.json 的 decision_rule 判 h∈{0,1} + evidence_quote（h=1 时 run 原文逐字片段 ≤60 字符，h=0 时 none）。不确定时保守判 h=0。

### B2 · 落盘（每批一个文件，共 8 个）
`bench/rubric-v3/ablation/rejudge-g1b/dual-rater/dr-b{1..8}.json`：
```json
{
  "batch": "dr-b1",
  "source": "arena agent mode session <你的会话ID> (dual-rater second pass)",
  "observed_at": "<ISO 时间>",
  "judge_model": "<A1 自报的模型标识>",
  "run_files_read": ["bench/rubric-v3/ablation/runs-C0-run1.md"],
  "judgments": [
    {"cell_id": "run1/N-1", "h": 1, "evidence_quote": "逐字片段"}
  ]
}
```
每批 ≤12 cell，发完一批落盘一批再下一批（防上下文漂移）。

### B3 · 汇总分析
全部 8 批完成后，Lead 侧会合并计算（你不用算 κ），但你需落盘 `dual-rater/dr-summary.json`：
```json
{
  "kind": "dual-rater-summary",
  "total_cells": 75,
  "completed_batches": ["dr-b1", ...],
  "flip_candidates": [
    {"cell_id": "...", "first_pass_h": 0, "second_pass_h": 1, "first_reason": "", "second_evidence": ""}
  ],
  "divergence_count": N,
  "notes": ""
}
```
flip_candidates 从 `rejudge-rejudge-local.json`（第一裁判 pass，路径 `bench/rubric-v3/ablation/rejudge-g1b/rejudge-results-local.json`）对照得出——只列 h 值不同的 cell，附双方依据。

## 提交与回执

1. 全部文件 commit + push 到 `arena/4a614e63-prompt-first-bench`（你有该分支权限；若 push 被拒走 PR，PR 描述注明 base 分支）。push 后 `git ls-remote origin refs/heads/arena/4a614e63-prompt-first-bench` 记录新 sha（M7 锚点 2）。
2. 回执（写入回复正文，必须含全部字段）：
   - repo URL + branch + commit_sha
   - Part A：Q1 模型标识 + Q2 family_check 答案 + family_check_upgrade 结论
   - Part A：5 工件 × 2 判 agree_rate + X5 检测对比
   - Part B：8 批完成数 + flip cell 数 + 最严重分歧 3 例（cell_id + 双方理由）
   - 异常清单（packet 缺失 / run 文件 sha 不符 / 截断等，没有就写"无"）

## 硬约束
- 盲判纪律：Part B 判定时不得参考 prior_h / 第一裁判结果 / hit-matrix，直到 B3 汇总阶段才允许对照。
- 模型身份如实自报，禁止编造；不知道就写 unknown + 依据。
- 不碰 main 分支，只写 arena/4a614e63-prompt-first-bench。
- 冻结件零触碰：`rejudge-rules.json` / `judge-input.json` / `dual-rater-candidates.json` / `results/*.json` 只读不改。
- 完成后回执必须含 repo URL + branch + commit_sha（核验指纹）。