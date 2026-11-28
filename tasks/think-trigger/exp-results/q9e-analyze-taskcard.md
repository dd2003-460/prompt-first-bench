# 任务卡：Q9E-Analyze 分析脚本（提前备好，scan 完成后直接跑）

# origin: ai (2026-11-27 12:10, Lead 规划)
# 依赖：Q9E-Scan 执行中（pid 22941，1/15 完成，实测 ~9.5min/run → ~2.4h 完成）。本任务只写脚本+在已有 1 个 run 上测通，不跑全量分析。
# 验收：① analyze_q9e_scan.py 落盘 ② judge_v1.py 暴露 confirmed_ids（向后兼容）③ 在 q9-50-r1 上跑通出矩阵片段 ④ 单测/自测通过

## 背景（为什么做）
Q9E-Scan 跑 5 档预算（50/100/150/300/719 节点）× 3 reps = 15 runs。跑完后要出：
- **per-gate-unit 命中率矩阵**（11 gate 叶 × 5 档，跨 3 reps 聚合）
- **主端点阈值**：gate 命中率首次达 100% 的最小预算节点数
- **次端点曲线**：gate 全过 run 子集内 cost/time 叶（N-2/N-4）judge_total 随预算变化
- **阈值跨域诊断**：COS_THRESHOLD=0.70 是 gpu 域标定，Q9 域未重校——用 c_detail.sim_median 诊断
  （全档≈0=阈值过高 / 全档≈1=过低 → 按 Q9 域 sim 分布重标定，只重算 embedding 不重跑 SM）
- **P1 判决数据**：gate 是否 ~100-150 节点饱和（P1 判决本身=判断-Lead，sub 只出数据）

冻结端点定义：`experiments/stage-ablation/tasks/q9-e-experiment-design-20261124.md` L11-18（只读这节，不读全文）。

## 关键接口事实（已核，不用重查）
- `judge_v1.py`（`modules/B-pipeline-ablation/judge_v1.py`，280 行）：
  - `layer_coverage(nodes, gold_units, model, cos_threshold=COS_THRESHOLD)` → `(score, detail)`
  - **detail 不含 confirmed 集合**（只有 n_confirmed 计数）——per-gate 矩阵需要知道**哪些** unit 命中
  - `load_run_nodes(run_json)` 从 run json 取 nodes（每个 node 有 claim 字段）
  - `COS_THRESHOLD = 0.70`（L38）
  - bge-m3 模型加载：`SentenceTransformer("BAAI/bge-m3")`
- `gold-q9-units.json`（`modules/B-pipeline-ablation/data/gold-q9-units.json`）：
  - dict，keys 含 `units`（全部 21 叶）、`gate_units`（11 gate 叶）、`n_units`/`n_leaves`/`n_splits`
  - 每个 unit 有 `unit_id` + `text` 字段（layer_coverage 用这两个）
- run json（`modules/B-pipeline-ablation/data/q9-budget-scan/q9-50-r1-*.json`，已有 1 个）：
  - top keys: qid/n_nodes/n_rounds/final_state/leak_hits/rework_events/rounds/question/objective/nodes
  - `nodes` = list（budget=50 档 len=50），每 node 有 claim/depth/id
  - 文件名格式 `q9-{budget}-r{rep}-{ts}.json`，budget ∈ {50,100,150,300,719}，rep ∈ {1,2,3}

## 要做的事（3 步，按序）

### Step 1：judge_v1.py 暴露 confirmed_ids（最小改动，向后兼容）
在 `layer_coverage` 的 detail dict 里加一个 key：`"confirmed_ids": sorted(gold_units[g]["unit_id"] for g in confirmed)`。
只加这一个 key，不改任何现有逻辑/返回值/其他函数。改完 `python3 -m py_compile judge_v1.py` 过 + 跑一遍
`python3 judge_v1.py --selftest` 确认无回归（selftest 不跑 coverage 层但确认 import 链没断）。

### Step 2：写 analyze_q9e_scan.py（落 `modules/B-pipeline-ablation/analyze_q9e_scan.py`）
机械脚本，职责：
1. 读 `data/q9-budget-scan/q9-*.json`（glob，按文件名解析 budget/rep）
2. 加载 bge-m3 一次（复用，不每 run 重载）
3. 对每个 run：`load_run_nodes` → `layer_coverage(nodes, q9_units["units"], model)` → 拿 detail.confirmed_ids
4. **per-gate 矩阵**：对 11 个 gate_units，每个 gate 在每 (budget, rep) 是否 ∈ confirmed_ids → 命中率
   （budget 级 = 3 reps 平均；gate 级 = 11 个 gate 的命中比例）
5. **主端点**：gate 命中率（11 个 gate 全命中的 budget 比例）首次 = 1.0 的最小 budget；若全档 <1.0 则报 "未达 100%"
6. **次端点**：gate 全过的 run 子集内，N-2/N-4（cost/time 叶，unit_id 见 gold 文件）的命中情况 + 这些 run 的
   judge_total（调 judge_run 拿 total_score）随 budget 变化
7. **阈值诊断**：每 run 的 c_detail.sim_median 汇总；若 gate 命中率全档≈0（<0.1）或≈1（>0.9）→ 输出
   "建议按 Q9 域 sim 分布重标定 COS_THRESHOLD"（只诊断，不自动改阈值）
8. 输出 JSON 落 `data/q9-budget-scan/analysis.json`：
   ```
   {"budgets": [50,100,150,300,719],
    "gate_matrix": {gate_id: {budget: hit_rate_0_1}},
    "gate_hit_rate_by_budget": {budget: fraction_of_11_gates_hit},
    "main_endpoint": {"first_100pct_budget": int|null, "note": str},
    "secondary_endpoint": {budget: {"n_gate_full_runs": int, "judge_totals": [...]}},
    "threshold_diag": {"sim_medians": {budget: [...]}, "verdict": str},
    "n_runs_per_budget": {budget: int}}
   ```
9. 末尾 print 一行摘要（主端点值 + gate 命中率各档），供回执引用。

**约束**：脚本只读 run json + gold，不调 SM、不重跑、不写 run json。bge-m3 加载失败 → 报错退出（不 fail-open，
分析脚本没数据就没意义）。

### Step 3：在已有 1 个 run 上测通
`python3 analyze_q9e_scan.py`（此时只有 q9-50-r1 一个 run）→ 确认：
- 不崩、输出 analysis.json（n_runs_per_budget={50:1}，其他档 0）
- gate_matrix 有 11 个 gate、budget=50 有值
- 主端点报 "未达 100%"（只有 1 个 run 不可能 100% 跨档）
- print 摘要行正常
把这个输出贴进回执（证明脚本在真实数据上跑通，不是只在合成数据上）。

## 边界
- 只改 judge_v1.py（加 1 个 detail key）+ 新建 analyze_q9e_scan.py。不动 s5_state_machine.py、run json、gold 文件。
- 不跑全量分析（15 runs 没齐）——只测通 1 个 run。全量跑=scan 完成后的独立动作（Lead 触发）。
- bge-m3 模型本地已有（judge_v1 在用），不下载。

## 验收（Lead 核）
1. `git diff judge_v1.py` 只多 confirmed_ids 一个 key，无其他改动
2. `python3 -m py_compile` 两文件过
3. analysis.json 存在且结构符合上面 schema（n_runs_per_budget={50:1}）
4. 回执含 Step 3 的实际输出（gate_matrix 片段 + 摘要行）
5. commit 1 个（两文件一起）
