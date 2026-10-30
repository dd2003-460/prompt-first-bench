# 阶段 04 — 执行验证（RV3G3cdx-crossdomain-lint-coverage-expand, r150）

> 执行顺序 A1→A5。所有实跑输出可复现；cwd = repo root（样例矩阵命令在 ablation/ 下执行，脚本用 `--dir` 相对参数，无 cwd 陷阱——r149 登记项已核对：本脚本路径锚定 `Path(__file__).resolve().parents[1]`，不依赖 cwd）。

## A1 load_batch2 双检查落地 ✓

`assert-goldrank-crossdomain.py` L219-227（gold_nodes 类型检查之后、节点级循环之前）：
- **键集检查**（Y1）：`declared = pe.get("gold_nodes")` 非 None 时逐成员查 `in pe["nodes"]`，缺失者列表一次性报错 `gold_nodes members absent from nodes key set: [...]`。缺省路径零变化（实证见 A4 pos 样例 + byte-exact）。
- **prompt_version C-最小**（Y2）：`pv is None or not isinstance(pv, str) or not pv.strip()` → `'prompt_version' required (non-empty str)`。

过程注记（如实登记）：首次 Edit 误留一行占位死代码（`if ... : pass`），第二步 Edit 即删——最终落盘版本经全矩阵实跑验证无残留（若残留会在 neg-nodes-not-dict 等样例产生异常分支，实际行为全部符合预期）。

## A2 docstring 更新 ✓

- 输入 schema 节：gold_nodes 行补「显式声明时成员须 ⊆ nodes 键集（缺失 = exit 2，防判定层静默漏计）」+ 完整 fail-loud 协议指向导出候选；prompt_version 行改「r150 M2 C-最小消费：存在性 + 非空 str 机判」+ 内容级对照指向导出候选。原「换题面而未声明 = ERROR fail-loud」虚假宣称已删除（Y3 不留虚假宣称）。
- exit code 节：exit 2 行补「gold_nodes 键集缺失 / prompt_version 缺失或非空 str 违例」；新增 `--lint-only 模式` 独立行（0 = 全通过含目录不存在 SIGNAL / 2 = schema 违例；**lint 永不 exit 1**）——(d) 文档漂移闭合。

## A3 四个新负样例落盘 ✓

`batch2-lint-samples/` 新增 4 目录（各含 README.md 构造意图标注 + 所需文件子集）：

| 目录 | 构造 | 目标出口 |
|---|---|---|
| neg-json-unreadable/ | prior = 截断 JSON（L3 无闭合） | E3 unreadable |
| neg-nodes-not-dict/ | prior.nodes = list | E4 'nodes' object required |
| neg-goldnodes-badtype/ | prior.gold_nodes = str | E5 类型错 |
| neg-goldnode-not-in-nodes/ | gold_nodes 追加 N-9.9（nodes 缺席） | r150 新增键集出口 |

过程注记（负面结果声明 1）：首轮批量创建因 shell cwd 滞留 ablation/batch2-lint-samples/ 导致两处错位——mkdir 相对路径生效于错误目录 + README 循环二次拼接出嵌套 `bench/` 幽灵树。已全部清除（`rm -rf` 幽灵树 + git status 确认工作区干净后重建），最终 11 样例目录结构经 ls 逐一核验。另：neg-nodes-not-dict 首轮漏拷 hit-matrix（触发 E2 早退而非 E4），补拷后命中目标出口。

## A4 全矩阵实跑（11 样例 + E1 默认态）✓

| 样例 | exit | 末行输出 | 判定 |
|---|---|---|---|
| neg-blindtest-entry-missing-field | 2 | w3_full_ranking entry missing 'w3' | ✓ 既有零漂移 |
| neg-hitmatrix-gold-absent | 2 | hit-matrix run-b2-1: gold node N-4 absent | ✓ 既有零漂移 |
| neg-missing-prior | 2 | prior-estimates-batch2.json missing | ✓ 既有零漂移 |
| neg-nodes-missing-w1 | 2 | nodes.N-4: field 'w1' required | ✓ 既有零漂移 |
| neg-ptilde-key-absent | 2 | nodes.N-2: field 'p_tilde' required (null allowed) | ✓ 既有零漂移 |
| neg-json-unreadable | 2 | prior...unreadable: Expecting ',' delimiter: line 3 column 57 | ✓ 新 E3 |
| neg-nodes-not-dict | 2 | 'nodes' object required | ✓ 新 E4 |
| neg-goldnodes-badtype | 2 | gold_nodes must be a list of node-id strings | ✓ 新 E5 |
| neg-goldnode-not-in-nodes | 2 | gold_nodes members absent from nodes key set: ['N-9.9'] | ✓ 新键集出口 |
| pos-full | 0 | SUMMARY: lint PASS (3-file schema) | ✓ 零误伤 |
| pos-no-blindtest | 0 | SUMMARY: lint PASS (3-file schema) | ✓ 零误伤 |
| （E1 无参默认态） | 0 | [SIGNAL] blocked-on-external... | ✓ |

覆盖口径达成（Y4）：**10 个 exit 2 出口全有专属样例 + E1 默认态实跑 = 11/11 出口实证**（超任务书「8 出口全覆盖」下限，含 r150 新增的键集出口）。

## A5 byte-exact 回归 + 基线 + 冻结面 ✓

- **byte-exact**：无参调用（batch2/ 不存在态）改动前快照 vs 改动后重跑——stdout 全文 + exit 0 逐字节一致，md5 均 = `598180b0954defc64019bb5169efd64b`。**零漂移**（E1 早退路径在新检查之前返回，理论预测与实测吻合）。
- **七脚本基线**（repo root）：[0,0,0,1,0,0,0] 与 r146/r147/r149 记录逐位一致（kappa-receipt FAIL exit 1 = 已知常态项）。
- **queue-lint**：exit 0（46 行 / 3 SIGNAL 吸收登记行 / 0 FAIL）。
- **冻结面**：`git diff main --stat -- hit-matrix.json prior-estimates.json gold-tree.md runs-C0-*` = **0 行**。
- **改动面** ⊆ {assert-goldrank-crossdomain.py, batch2-lint-samples/{4 新目录}, stages/*, current-goal.md} ✓

## 负面结果声明

1. 样例批量创建 cwd 错位事故（幽灵嵌套树 + 漏拷文件）——已清除并逐一复核，未污染任何 commit（事故发生在首个样例 commit 之前）。
2. 02 S3 已修正任务书「KeyError crash」表述为「静默漏计」——本轮键集检查的拦截价值论证据此重写（防 (a) 假 FAIL/SIGNAL，而非防 crash）。

## 判定

A1-A5 全部达标，验收标准 7/7（04.5 前）。**pass → 进 04.5**。