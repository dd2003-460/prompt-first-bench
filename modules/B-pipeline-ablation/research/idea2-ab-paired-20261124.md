# origin: ai
# idea2 (checkpoint-as-cache) A/B 配对统计 — 2026-11-24

## 0. 口径声明 (来自 plan-layered L2-4)

- B 臂 `--resume` 从 checkpoint `experiments/stage-ablation/checkpoints/archive/budget-150-r1-20261122-093447/sm-gpu-r2`
  (122 节点固定前缀: L1=6 + L2=28 + L3=88) 续跑; A 臂从头跑。runner: `experiments/stage-ablation/idea2_runner.sh`。
- **B 臂的正确解读 = ① wall time 节省 + ② 前缀一致性** (B 的前 122 节点 vs checkpoint 是否逐字/语义一致)。
  质量分数 (judge/metacog) 只作旁证, 不作主结论。
- **预算口径勘误 (本轮新发现, 重要)**: 本批 6 个 run 跑于 2026-11-22 22:13–11-23 03:24, 早于
  `max_nodes` 逐轮硬钳制修复 (commit `47a8543cd`, 2026-11-23 13:44, "K7 干净预算轴")。
  因此 `--max-nodes 150` 实际未生效为硬顶: realized 节点数 A 臂 316/394/435, B 臂 401/411/402
  (来源: 各 run json `n_nodes` 字段 + stdout `DONE` 行)。
  → 任务背景中 "B 臂只有 28 个新节点" 的假设在本批数据上不成立 (B 臂实际新增 279/289/280 节点)。
  质量对比的不公平性比预期更强, 旁证定位不变; wall time 与前缀一致性两轴不受此影响。

## 1. Wall time 配对 (3 对)

来源: 各 `.stdout` 首尾时间戳独立复算, 与 `data/idea2/idea2-run.log` 的 `wall_s` 行逐一对账, 6/6 完全一致。

| rep | A (s) | B (s) | diff A−B (s) | B 相对 A 节省 |
|-----|-------|-------|--------------|----------------|
| r1  | 2865  | 3077  | −212         | −7.4% (B 更慢) |
| r2  | 3427  | 3026  | +401         | +11.7% |
| r3  | 3947  | 2359  | +1588        | +40.2% |

- 配对差 (A−B): **mean = +592.3 s, sd = 915.1 s (n=3)**; A 均值 3413.0 s, B 均值 2820.7 s。
- B 相对 A 平均节省 **17.4%** (592.3/3413.0)。
- 显著性: paired t(2 df) = 1.121, 远低于双侧 p<0.05 所需 |t|>4.303 → **n=3 下节省不显著**, 且 r1 为负。
- 注意: 两臂节点规模不同 (A 316–435 vs B 401–411, B 反而更多), 且 run 串行、A 在前 B 在后
  (vLLM 负载/温度漂移可能影响), wall time 差不能干净归因于 resume 本身。

## 2. 前缀一致性 (B 前 122 节点 vs checkpoint sm-gpu-r2)

方法: 逐节点按 id 对齐 (B 前 122 节点 id 集合 == checkpoint 122 节点 id 集合, 3/3 完全一致, 无缺失/多余),
对 12 个字段 (id/claim/level/source/status/corrected_claim/rework_count/parent_ids/edge_type/search_query/
retrieval_sources/objective) 逐字比对; `evidence` 字段单独统计 (见下)。
脚本: `scratch/idea2_prefix_compare.py`, 结果: `scratch/idea2-prefix-result.json`。

| rep | id 集合一致 | claim 逐字一致 | 全字段逐字一致 | 漂移节点数 |
|-----|-------------|----------------|----------------|------------|
| B-r1 | ✅ 122/122 | **122/122** | 92/122 | 30 |
| B-r2 | ✅ 122/122 | **122/122** | 88/122 | 34 |
| B-r3 | ✅ 122/122 | **122/122** | 90/122 | 32 |

**漂移全部集中在两个运行时字段, 内容字段零漂移:**

| rep | edge_type 漂移 (B→ckpt) | status 漂移 (B→ckpt) |
|-----|--------------------------|------------------------|
| B-r1 | 24 (19× quotient→cartesian, 5× cartesian→quotient) | 6 (5× pending→verified, 1× pending→degraded) |
| B-r2 | 21 (15→, 6←) | 15 (10× pending→verified, 3× pending→degraded, 1× verified→degraded, 1× verified→pending) |
| B-r3 | 19 (14→, 5←) | 18 (15× pending→verified, 2× pending→degraded, 1× verified→pending) |

漂移样例 (前 5, B-r1): N46/N129 edge_type (quotient vs cartesian); N48/N49 status (pending vs verified); N126 (pending vs degraded)。

**漂移归因 (内容核心保真, 运行时标注字段漂移):**
1. **claim / corrected_claim / level / parent_ids / source 全部 122/122 逐字一致 (3/3 run)** — 节点内容核心零漂移。
2. `evidence` (核验文本) 有漂移: B-r1 95/122, B-r2 87/122, B-r3 86/122 — resume 后重核验会重写核验文本 (LLM 生成, 非确定)。
3. `edge_type` 由 LLM 现场分类 (`classify_edge`, commit `af99f9bba`/`9e897167c`, 2026-11-12),
   非确定性: 同一 claim 重分类会翻 cartesian↔quotient。checkpoint 里 112 cartesian / 10 quotient,
   B 臂重分类后比例接近 A 臂全量风格 (234/82) → 漂移方向是"重分类"而非"内容变化"。
4. `status` 在 resume 后被重新核验 (verified/degraded/pending 翻转), 属运行时状态, 非节点内容。

**结论: 缓存语义在内容层成立** — 前 122 节点的 claim 文本、层级、父子结构、source 逐字保真 (122/122 × 3 run);
不逐字的是三个 LLM 重新生成/重判定的字段 (evidence 核验文本、edge_type 重分类、status 重核验),
属缓存的"语义一致、标注重算"模式, 不是内容漂移。

## 3. 双轴评分 (旁证, 不作主结论)

口径: `judge_v1.judge_run` 默认 gold = gpu 域 (`gold-gpu-units.json`, 36 units; `judge_v1.py` L34 `GOLD_UNITS`,
`gold_units=None` 时 `load_gold("gpu")`), 与已有 `data/idea2/idea2-scores.json` 一致 (本轮重算 6/6 与旧值完全吻合,
含 cov 2026-11-23 修复后的去重口径)。评分脚本: `scratch/idea2_rescore.py`, 结果: `scratch/idea2-rescore.json`。
参考代码: `experiments/stage-ablation/q7_budget_scan_queue.sh` L39-60 PYEOF 段 (该段用 q7 gold, 此处按 gpu 域改回默认)。

| arm-rep | n_nodes | judge total | depth | cov | metacog total | gap | hg | post |
|---------|---------|-------------|-------|-----|----------------|-----|------|------|
| A-r1 | 316 | 0.5944 | 0.800 | 0.3889 | 0.2365 | 0.0633 | 0.9302 | 0.4000 |
| A-r2 | 394 | 0.5806 | 0.800 | 0.3611 | 0.1502 | 0.0660 | 0.8632 | 0.1333 |
| A-r3 | 435 | 0.5944 | 0.800 | 0.3889 | 0.1145 | 0.0690 | 0.9811 | 0.0000 |
| B-r1 | 401 | 0.5111 | 0.800 | 0.2222 | 0.2461 | 0.1397 | 0.9366 | 0.2500 |
| B-r2 | 411 | 0.5250 | 0.800 | 0.2500 | 0.2174 | 0.1436 | 0.8827 | 0.0952 |
| B-r3 | 402 | 0.5250 | 0.800 | 0.2500 | 0.2628 | 0.0995 | 0.9767 | 0.4000 |

- judge total: A 均值 0.5898 vs B 均值 0.5204 (差 −0.0694, B 更低); depth 两臂全 0.800 (饱和, 无区分度);
  差距全在 cov (A 0.3611–0.3889 vs B 0.2222–0.2500)。
- metacog total: A 均值 0.1671 vs B 均值 0.2421 (B 略高); gap B 更高 (0.0995–0.1436 vs 0.0633–0.0690)。
- **旁证解读**: B 臂 cov 更低与其前 122 节点被冻结、新增节点 (279–289) 挤占预算有关, 但本批 max_nodes 未硬钳制
  (见 §0 勘误), 两臂 realized 规模接近 (B 甚至更多), 故 cov 差不能简单归因于"新预算只有 28 节点"。
  质量分仅作旁证, 主结论看 §1/§2。

## 4. 结论

1. **Wall time**: B 臂平均省 592.3 s (17.4%), 但 n=3 下不显著 (t=1.121, 2df), r1 反而慢 212 s;
   且两臂节点规模/串行时序混杂, 本批数据**不足以支持 "checkpoint-as-cache 带来可靠 wall time 收益"**。
2. **前缀一致性**: 内容核心 (claim/层级/父子/source) 122/122 逐字一致 × 3 run, **缓存语义在内容层成立**;
   evidence/edge_type/status 三个 LLM 重生成字段有漂移 (标注重算, 非内容漂移)。
3. **预算口径勘误**: 本批跑于硬钳制修复 (`47a8543cd`) 之前, "--max-nodes 150 / B 臂仅 28 新节点" 假设不成立;
   若要在干净预算轴上重测 wall time 收益, 需在 `47a8543cd` 之后的代码上重跑本实验。

## 5. 数据来源

| 数字 | 来源文件 |
|------|----------|
| wall_s (6 run) | `modules/B-pipeline-ablation/data/idea2/idea2-run.log` + 各 `.stdout` 首尾时间戳 (独立复算, 6/6 一致) |
| n_nodes | 各 run json `n_nodes` 字段 + stdout `DONE` 行 |
| 前缀比对 | `data/idea2/idea2-B-r{1,2,3}-*.json` vs `experiments/stage-ablation/checkpoints/archive/budget-150-r1-20261122-093447/sm-gpu-r2/**/node.json` |
| judge/metacog | 本轮重算 (`scratch/idea2_rescore.py`), 与 `data/idea2/idea2-scores.json` 逐值吻合 |
| 硬钳制修复时点 | git `47a8543cd` (2026-11-23 13:44); idea2 批跑时段 2026-11-22 22:13 → 11-23 03:24 (`idea2-run.log`) |


