# P4 口径召回修复设计（治 nat gold 要点 5：树有 verified 节点但 P4 没引用）

> origin: ai · 2026-11-26 18:45 · 设计任务（只读+提案，不改代码）。任务卡是唯一指令来源。

## 背景（sub 不需再查）

- nat 失败模式已重判（见 `experiments/stage-ablation/nat-failure-mode-20261126.md` 顶部更正 + `obj-inject-probe-20261126.md` §5，commit `3ba1ef39f`/`ad962650e`）：原"b 型维度盲区"诊断被宽口径重测推翻（full run 老化命中 98，非 0）。
- **真失败点 = P4 综合丢失**（gold 要点 5）：full run 树里 N247（L4, verified）原文含「u=1%/天 → 每个对象平均每 100 天被替换一次新内容」+ 推导公式，N17/N262 提供 1-exp(-λT_res) 与数值范围——树信息量足够。但 P4 综合答案（`runs-s5-sm-nat-synth.json`）用 T_res≈1.5 天口径、引用 [N182,N193,N260]/[N74,N192]，**N247 未引用、全文「100 天」=0 命中** → P4 没选这个口径，答案丢了 100 天量级。
- 目标：设计**最小**的 P4 口径召回修复，让综合答案覆盖树内已 verified 的关键数值口径（尤其 1/λ=100 天这类量级），不漏掉树里已推导出来的数。

## 要回答的设计问题（decomp，先拆后查）

1. **P4 综合代码在哪、怎么选节点**：定位 s5_pipeline.py 里 P4/synthesis 阶段（grep `P4\|synth\|synthesize\|final_answer\|P4_SYNTH` 等），读懂它如何从 278 节点里挑出被引用的节点（是 top-k by score？by level？by relevance？全量塞 prompt？）。
2. **N247 为什么没被选中**：对照 N247 的 status/score/level 和被引用的 N182/N193/N260，找出选择机制里丢掉 N247 的具体原因（score 低？层级太深被截断？relevance 没匹配到问题词？）。
3. **最小改法**：给 1-2 个候选修复（优先 prompt 级、改动最小），例如：
   - 候选 A：P4 prompt 增加「口径覆盖检查」——把树内 verified 节点的关键数值口径（量级/常数/公式）列成清单注入 prompt，要求答案对每个口径要么采用要么显式说明为何不用。
   - 候选 B：P4 前加一步「口径召回」——从 verified 节点抽取数值口径（regex 抓 常数+单位/量级），强制纳入综合上下文。
   - 选改动最小、不破坏现有 P4 行为的那个，说清为什么。
4. **验证方案**：怎么确认修复有效（最小探针：重跑 nat P4 综合，看答案是否出现 100 天口径 / 引用 N247；调用量上限）。

## 数据源（只读）

- `experiments/stage-ablation/s5_pipeline.py`（P4 综合逻辑）
- `experiments/stage-ablation/s5_state_machine.py`（若 P4 在 SM 里）
- `experiments/stage-ablation/runs-s5-sm-nat.json`（full run 树，N247/N17/N262 等节点）
- `experiments/stage-ablation/runs-s5-sm-nat-synth.json`（P4 综合答案 + 引用节点）
- `experiments/stage-ablation/nat-failure-mode-20261126.md`（要点 5 证据，§6）

## 执行步骤

1. 写脚本到 `/Users/a1-6/.hermes/cache/scratch/p4_recall_diagnose.py`：解析 runs-s5-sm-nat.json 提取 N247/N17/N262/N182/N193/N260 的 {id, level, status, score, claim 前 120 字}；解析 synth.json 提取答案引用节点列表 + 全文「100 天」「N247」命中 → 写 `/Users/a1-6/.hermes/cache/scratch/p4_recall_diagnose.json`
2. read s5_pipeline.py 的 P4 综合段（grep 定位，~150 行），读懂节点选择机制
3. 对照 diagnose.json + P4 代码，定位 N247 丢失的具体原因（一行结论）
4. 写设计提案 `experiments/stage-ablation/p4-recall-fix-20261126.md`（≤70 行）：§1 节点选择机制（P4 怎么挑节点，引代码行号）/ §2 N247 丢失原因（一行+证据）/ §3 候选修复 A/B（各 ≤15 行，改哪几行/加什么 prompt）/ §4 推荐（一行，选哪个+为什么最小）/ §5 验证方案（最小探针+调用量上限）
5. `git add experiments/stage-ablation/p4-recall-fix-20261126.md && git commit -m 'design(stage-ablation): P4 口径召回修复设计(治 nat gold 要点5, N247 未引用)'`，**不 push**

## 验收

- p4_recall_diagnose.json 存在（含 6 节点字段 + 答案引用列表）
- 设计提案 §1-§5 齐全，§4 推荐明确（A/B 二选一）
- commit hash
- summary ≤6 行：P4 节点选择机制一行 + N247 丢失原因一行 + 推荐修复一行 + 验证方案一行 + commit hash

## 边界

- **只读 + 写提案一个文件 + scratch 脚本/JSON**；不改 s5_pipeline.py / s5_state_machine.py（设计阶段不动代码）；不跑 LLM；不 push；不 stash/checkout/切分支
- 提案是给 Lead 决策用的，不是直接实施——改代码是下一步（Lead 看过方案再派）
