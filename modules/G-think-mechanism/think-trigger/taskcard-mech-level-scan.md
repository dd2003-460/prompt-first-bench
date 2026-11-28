# 任务卡: 机制级微架构内容扫描 (三要素判据)

## 背景 (自包含, 不需读其他文件)
Q9 budget-scan 10 个 run 共 1198 节点 (L1=57/L2=260/L3=586/L4=295)。此前用关键词扫描判"微架构内容"被判据坏掉: 命中的全是规格级 (带宽多少/容量多少/支不支持某指令), 不是机制级。D 定义的"微架构" = 访存+计算的每一步, 参数变化→影响什么→影响多大。本任务用 LLM 按三要素判据重扫全部 1198 节点, 回答: 机制级内容有多少, 分布在哪些深度, 样例是什么。

## 输入
10 个 run JSON: `/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/B-pipeline-ablation/data/q9-budget-scan/q9-{50,100,150,300}-r{1,2,3}-*.json` (300 只有 r1)。
每个节点字段: `id`, `claim`, `evidence`, `status`, `level`。只判 `claim` 文本。

## 判据 (三要素, 全有 = 机制级)
1. **参数变化**: claim 含具体参数/配置的变化或对比 (如 L2 cache 8MB vs 96MB、指令周期、带宽、占用率、batch size、量化位宽的具体数值对比或取值)
2. **影响机制**: 说明因果机制 — 该参数如何影响访存/计算/流水线 (why/how, 不是只说"会影响性能")
3. **影响量**: 量化结果 — 影响多大 (数值估计、百分比、公式推导出的量)

判定分档:
- `mech` = 三要素全有
- `spec` = 只有规格值罗列 (①可能有, ②③缺)
- `other` = 与微架构/访存/计算效率无关 (如流程/调度/成本/工具链)
注意: ②"影响机制"要求真正的因果解释 ("因为 L2 命中率下降导致 HBM 访问次数增加, 带宽利用率从 X 降到 Y"), 不是泛泛的"会影响"。③"影响量"可以是公式推导 (如 27B×2B/4=13.5GB 这类算术) 或数值估计。

## 方法
- 写脚本 `/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/B-pipeline-ablation/research/q9_mech_level_scan.py`
- LLM endpoint: `http://127.0.0.1:8787/v1/chat/completions`, `model=qwen3.8-27b`, `temperature=0`
- 每批 8 个节点送 LLM, 严格 JSON 输出: `{"<node_id>": ["mech"|"spec"|"other"], ...}` (每节点一个标签; 如需细分三要素可加 `"e": [b,b,b]` 字段, 可选)
- 失败重试 3 次; 全部批次完成后聚合
- **产出 JSON 必须由脚本生成写盘**, 不要手打数据进输出流

## 产出
1. 脚本 `research/q9_mech_level_scan.py`
2. 结果 `data/q9-budget-scan/mech-level-scan-20261127.json`, 结构:
   - `counts_by_level`: {L1: {total, mech, spec, other}, ...}
   - `counts_by_run`: {run_tag: {total, mech, spec, other}, ...}
   - `mech_samples`: 机制级节点样例 ≤30 条, 每条 {run, id, level, claim_excerpt≤80字}
   - `spec_samples`: 规格级样例 ≤10 条 (同上结构)
   - `conclusion`: 1 行结论
3. 1 个 commit: `feat(research): 机制级微架构扫描 (三要素判据) 1198 节点`

## 验收
- JSON 存在且 `counts_by_level` 各级 total 之和 = 1198
- 样例可回溯: 抽 3 条 mech_samples 在原 json 里 grep 得到相同 id+claim 片段
- **judge 一致率**: 读校准集 `data/q9-budget-scan/judge-calib-set-20261127.json` (Lead 手工标注 16 条边界样例, 含 mech/spec/other 三档), 对你的判定算一致率 (exact match + 混淆矩阵), 写进结果 JSON 的 `calibration` 字段。一致率 <75% 时结论里必须声明 "judge 松紧未校准, 绝对值不可信, 仅跨档相对值可用"
- commit 存在 (`git log --oneline -1`)
- 汇报: 1 行数字 (mech/spec/other 总数 + 按深度分布) + 一致率 + JSON 路径 + commit hash

## 边界
- 不修状态机、不改 10 个 run json、不重跑 SM、不改 decomposition.md
- 只新增: 脚本 + 结果 JSON + 1 commit
