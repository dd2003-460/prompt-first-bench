# 阶段 02 — RV3G3cdx-crossdomain-lint-coverage-expand · 现状扫描（r150）

> 全部命令仓库根执行，可复现。被扫对象 = `bench/rubric-v3/ablation/scripts/assert-goldrank-crossdomain.py`（325 行，r147 后未再改动）。

## S1 — lint 失败出口实证枚举（--lint-only --dir 实跑取证）

`load_batch2()`（L186-236）按代码顺序共有 **9 个 exit 2 出口**（含 r147 已覆盖的 5 个 + 本轮新发现的 4 个）：

| # | 出口 | 触发条件 | 错误文案 | 样例覆盖 |
|---|---|---|---|---|
| E1 | L193 | batch2/ 目录不存在 | `batch2/ directory absent` → lint 层降级 `[SIGNAL] ... exit 0`（特例） | pos（无参调用即此态） |
| E2 | L202 | hit-matrix-batch2.json 缺失 | `{fname} missing` | ❌ 缺 |
| E3 | L202 | prior-estimates-batch2.json 缺失 | 同上 | ✅ neg-missing-prior |
| E4 | L207 | 任一文件 JSON 不可读 / OSError | `{fname} unreadable: {e}` | ❌ 缺 |
| E5 | L212 | `nodes` 键缺失或非 dict | `'nodes' object required` | ❌ 缺（current-goal (a)「nodes 非 dict」） |
| E6 | L218 | gold_nodes 非 str list | `gold_nodes must be a list of node-id strings` | ❌ 缺（current-goal (a)「gold_nodes 类型错」） |
| E7 | L222 | nodes.{nid} 缺 `w1` 字段 | `field 'w1' required` | ✅ neg-nodes-missing-w1 |
| E8 | L224 | nodes.{nid} 缺 `p_tilde` 键 | `field 'p_tilde' required (null allowed)` | ✅ neg-ptilde-key-absent |
| E9 | L229 | hit-matrix run 缺 gold 节点 | `hit-matrix {rid}: gold node {nid} absent` | ✅ neg-hitmatrix-gold-absent |
| E10 | L234 | blindtest w3_full_ranking entry 缺字段 | `entry missing '{f}'` | ✅ neg-blindtest-entry-missing-field |

注：表头写 9 实际 10 行——E1 是 SIGNAL 特例非 FAIL 出口，真实 FAIL 出口 = **9 个**（E2-E10）。r147 记「5/8」的分母口径与本轮逐行枚举不一致（r147 分母可能未计 E2/E10 或合并了 E4 变体）→ 登记为数字勘误候选，本轮以代码实跑为准：**目标 = 9/9 FAIL 出口全覆盖**。

实跑基线（本轮 S1 实测，7 既有样例）：neg×5 全 exit 2 文案如上表 ✓；pos-full / pos-no-blindtest 全 exit 0 ✓。

## S2 — 「gold_nodes ⊆ prior.nodes 键集」缺口定位（current-goal (b)）

- **hit-matrix 侧已有**（L225-229）：每个 run 的 cells 必须包含全部 gold 节点，否则 E9 FAIL。
- **prior 侧缺失**：L214-218 只查 gold_nodes 的类型（str list），不查成员是否 ∈ `pe["nodes"]` 键集。
- **下游后果实证（修正 S2 初判）**：构造 gold_nodes 含 prior.nodes 不存在的键（"N-9"）且 hit-matrix cells 含 N-9 时，当前 lint = **PASS exit 0**（漏检实锤）。无 KeyError crash——`top10_gold_count`/`reachable_top10_gold_counts` 均只做 `in` 判断不做索引。真实后果 = gold 节点在 prior 权重表缺席 ⇒ 该节点不参与任何方案排序 ⇒ top-10 gold 计数系统性偏低（**静默数据缺陷，比 crash 更危险**）。
  - 注：若 N-9 同时不在 hit-matrix cells，则被既有 E9 出口拦截（hit-matrix 侧检查先行）——(b) 新检查的增量价值 = 拦「hit-matrix 有、prior.nodes 无」的半套数据形态。
- **结论修正（负面发现）**：(b) 检查的动机从「防 KeyError crash」（current-goal 原文）修正为「防 gold 引用悬空导致计数静默失真」——拦截价值成立且更高；current-goal 与后续 04.5 攻击面引用 crash 叙事的措辞须同步更正。
- 检查插入点裁定材料：应在 L218 类型检查之后、L219 per-node 循环之前（先验 gold 合法再逐节点查，错误报告顺序稳定）。

## S3 — prompt_version 消费面盘点（M2）

- 全脚本 grep `prompt_version`：仅 docstring L29 一处声明，**零代码消费**（与 r147 M2 登记一致，本轮复核确认）。
- 权威源现状：
  - DRAFT-rubric-v3-v2.md §3.2（L178-201）冻结的是**段落级 diff**（D1/D2 行号 + 冻结 commit 61416b4 文件快照），**不是完整题面文本**，更不是「版本名 ↔ gold_nodes 清单」映射；
  - `ablation/prompt-V0.txt`（42 行）是第一域 V0 题面实体文件，存在且可读；
  - revision-log-batch1.md 回填状态节：冻结语义 = 收口 commit 文件快照（取回方式 `git show 61416b4:...`）。
- **推导结论（供 02.5 裁定）**：「题面版本↔gold_nodes 映射」的权威源**在当前冻结件内不存在**——变体矩阵冻结的是 diff 不是 gold 清单，且六变体共用同一基础题面（B10 规则 L180），gold_nodes 差异只可能在「换题面」（跨域）场景出现，而跨域题面文本本身尚未有任何落盘件。⇒ 完整 fail-loud（对照题面内容判换题面）在本轮不可机判实现，触发 current-goal 失败降级第 1 条路径。

## S4 — M1/M2/M3 登记原文取证（r147 stages/02 S4 表）

- **M1**（换题面未声明 gold_nodes = ERROR fail-loud，docstring L27-28）：代码只看 gold_nodes 是否合法 list，不与题面版本对照 → 登记不擅自扩规则。
- **M2**（prompt_version 字段，L29）：无任何检查消费它 → 同 M1 口径。
- **M3**（hit-matrix h∈{0,1}/evidence 类型，L19）：设计内非缺陷（协议不消费 h 值）→ 不改。
- r147 02.5 补记：prior.nodes.{parent_id,w2,parent_share} 无存在性检查且零消费（并入 M1 处置口径）。

## S5 — byte-stable 面边界（改动禁区确认）

- 禁触：`w2_exact`（L76-81）、`build_schemes`（L84-97）、`top10_gold_count`（L100-103）、`reachable_top10_gold_counts`（L106-162）、`(a)/(b)` 判定段（L295-317）、无参主路径 stdout（L281-284 三行）。
- 可动：`load_batch2` schema 检查链（追加检查）、`lint_main`（新增 PASS 行）、主 docstring（exit code 节 + M1/M2 状态更新）。
- 无参调用当前 stdout 基线已捕获（/tmp/noarg.txt，exit 0，2 行：SIGNAL blocked-on-external + INFO 预注册锚点）——batch2/ 目录不存在态，(b) 新检查在该路径不可达 ⇒ **byte-exact 回归天然成立**（前提：不动 L278-285 任何一行）。

## S6 — 开放问题（转 02.5）

- X1：(b) 检查对 D1 缺省路径（gold_nodes 缺省沿用 GOLD_DOMAIN1）是否适用？→ 预判：仅显式声明时检查（current-goal 失败降级第 2 条已预注册此最小规则）。
- X2：(b) 违例出口编号与文案格式（对齐 E 系列风格 `prior: gold node {nid} not in nodes keys`）。
- X3：M1 降级落地形态——prompt_version「存在性 + 字符串非空」检查放 load_batch2（schema 层）还是 lint_main？若放 load_batch2 则判定模式也生效（byte-exact 不受影响因 batch2/ 不存在态不可达，但未来数据到来时判定模式行为改变——需 docstring 预注册）。
- X4：「题面版本↔gold_nodes 映射」权威源缺失的处置——导出候选（建映射登记表）vs APPROVALS（需成璐裁定映射归属）？预判：前者（纯仓库内新建件不需裁定，裁定的是「谁有权改映射」属流程问题）。