# 阶段 02 — 现状扫描（RV3G3cdx-crossdomain-lint-coverage-expand, r150）

> 全部实跑命令可复现；cwd = repo root（r149 cwd 陷阱登记项遵守）。

## S1 — 8 个 lint 失败出口逐一实证（`--lint-only --dir <sample>`）

load_batch2 + lint_main 的失败/信号出口共 **8 个**，逐一实跑取证：

| # | 出口 | 代码位置 | 触发样例 | 实跑 exit | 实跑输出（末行） |
|---|---|---|---|---|---|
| E1 | batch2/ 目录不存在 | L193 | （无 dir / 默认态） | **0** | `[SIGNAL] lint: .../batch2 absent — 数据未落盘，无对象可校验（非错误）` |
| E2 | 文件缺失（hit-matrix/prior 缺） | L203→L209 `errs` join | neg-missing-prior | 2 | `[ERROR] lint FAIL (...): prior-estimates-batch2.json missing` |
| E3 | JSON 不可读（JSONDecodeError/OSError） | L205→L209 | **无样例** | — | 预期 `[ERROR] lint FAIL (...): <fname> unreadable: <e>` |
| E4 | nodes 非 dict / 缺 nodes 键 | L212-213 | **无样例** | — | 预期 `'nodes' object required` |
| E5 | gold_nodes 类型错（非 str list） | L216-218 | **无样例** | — | 预期 `gold_nodes must be a list of node-id strings` |
| E6 | 节点缺 w1 | L220-222 | neg-nodes-missing-w1 | 2 | `nodes.N-4: field 'w1' required` |
| E7 | 节点缺 p_tilde 键 | L223-224 | neg-ptilde-key-absent | 2 | `nodes.N-2: field 'p_tilde' required (null allowed)` |
| E8 | hit-matrix run 缺 gold 节点 | L226-229 | neg-hitmatrix-gold-absent | 2 | `hit-matrix run-b2-1: gold node N-4 absent` |
| E9 | blindtest 条目缺字段 | L231-234 | neg-blindtest-entry-missing-field | 2 | `w3_full_ranking entry missing 'w3': {...}` |

**勘误（负面结果声明 1）**：queue L23 任务书与 r147 04.5 攻击 2 均称「8 个失败出口、已覆盖 5」——按代码逐行枚举实际为 **E1-E9 共 9 个出口**（E1 是 SIGNAL exit 0 特例，严格说不是「失败出口」）。两种口径：
- 口径 A（含 E1 特例）：9 出口，已覆盖 6（E1 用默认态实跑 ✓ + E2/E6/E7/E8/E9 五样例），缺 3（E3/E4/E5）；
- 口径 B（仅 exit 2 失败出口）：**8 出口，已覆盖 5**，缺 3（E3/E4/E5）——与任务书「5/8」吻合。
本 goal 采用口径 B 命名（对齐任务书），但工件内全量记录 9 出口表防口径漂移。补 3 样例后 = 8/8 全覆盖（+E1 默认态 = 9/9 出口实证）。

## S2 — 既有 7 样例零漂移基线（改动前快照）

```
neg-blindtest-entry-missing-field  exit=2  w3_full_ranking entry missing 'w3'
neg-hitmatrix-gold-absent          exit=2  hit-matrix run-b2-1: gold node N-4 absent
neg-missing-prior                  exit=2  prior-estimates-batch2.json missing
neg-nodes-missing-w1               exit=2  nodes.N-4: field 'w1' required
neg-ptilde-key-absent              exit=2  nodes.N-2: field 'p_tilde' required (null allowed)
pos-full                           exit=0  SUMMARY: lint PASS (3-file schema)
pos-no-blindtest                   exit=0  SUMMARY: lint PASS (3-file schema)
```
样例目录结构惯例：每样例一个子目录，内含所需三件套子集（neg-missing-prior 故意缺 prior 文件；其余均带 hit-matrix，blindtest 视出口而定）。pos-full/prior 含 `"prompt_version": "DRAFT-v2-frozen"`（自由字符串，当前零消费）。

## S3 — (b) 键集检查缺口实证

- hit-matrix 侧已有：L226-229 对每个 run 查 `nid not in cells`（gold ⊆ hit-matrix 各 run 键集）✓
- prior 侧**无**同款检查：显式 gold_nodes 声明的成员若不在 `pe["nodes"]` 键集 → load_batch2 放行 → main() 中 `build_schemes` 产出的 scheme 字典缺该 nid → `top10_gold_count` 排序后 `nid in gold` 计数时该 gold 恒不命中（静默少计，**不 crash**）；若走 reachable_top10_gold_counts 亦同。
- **修正任务书表述（负面结果声明 2）**：queue L23 称违例「会在 (a)/(b) 判定阶段 KeyError crash」——实测路径为**静默漏计而非 crash**（gold 成员缺席只使计数偏低，(a) 可能因此假 FAIL/假 SIGNAL）。危害性质不同但方向一致：都是判定层污染，提前到 lint exit 2 拦截仍成立。crash 场景仅在 gold 缺省沿用 GOLD_DOMAIN1 且第二域换题面（nodes 键集完全不同）时出现于……同样不 crash（`in` 判断天然容忍缺席）。故真实缺陷 = **静默少计**，比 crash 更隐蔽。
- D1 缺省语义边界：gold_nodes 缺省 → GOLD_DOMAIN1（第一域清单）；此时是否也查 prior.nodes 键集？查则「换题面未声明」直接 fail-loud（与 M1 联动）；不查则维持现状静默行为。**留 02.5 裁定**。

## S4 — M1/M2 权威源盘点（(c) 裁定材料）

- **M1 现状**：docstring L27-28 宣称「换题面而未声明 = ERROR fail-loud」；代码只看 gold_nodes 是否合法 list，从不与题面版本对照。
- **M2 现状**：`prompt_version` 全仓库唯一出现 = docstring L29（grep 实证：scripts/*.py 零消费，bench/rubric-v3/**/*.md 零引用该字段名）。
- **候选权威源核查**：
  1. `DRAFT-rubric-v3-v2.md` §3.2 变体矩阵冻结（R-10）：冻结的是**所有变体共用同一题面** + V0/V1/V2/V3/sham 的段落级 diff（D1/D2 行号 + 冻结 commit `61416b4`）。即 v3 实验设计内**不存在「不同题面 ↔ 不同 gold 清单」映射**——变体间题面差异是段落增删，gold 树不变。
  2. 「第二域」题面 = 新域新题面（§3.1 第二格），其 gold 需新建 → 必须显式声明 gold_nodes（D1 注释原意）。但**没有任何冻结件登记「题面 X ↔ gold 清单 Y」映射表**——第二域题面本身尚未存在（blocked-on-external）。
- **结论（预注册，待 02.5 交叉核对）**：完整 M1 fail-loud（题面内容哈希↔gold 清单对照）在当前材料下**不可机判实现**——权威源（映射表）不存在，且其创建属于第二域数据到来时的协议工作。可达的最小机判 = prompt_version 存在性 + 非空字符串检查（M2 最小消费：把「字段被声明了却无人看」变为「字段缺失/空串 = exit 2」），完整协议降级导出候选。

## S5 — (d) docstring 漂移点定位

主 docstring exit code 节（L57-59）：
```
exit code：0 = 无 FAIL（含 SIGNAL blocked-on-external / (a)(b) verdict 输出）
           1 = (a) 或 (b) FAIL
           2 = schema 违例 / 换题面无 gold_nodes 声明 / 输入不可读（ERROR fail-loud）
```
缺：`--lint-only` 模式的 exit 语义（0 = 全通过含目录不存在 SIGNAL / 2 = schema 违例；**lint 模式永不 exit 1**——不跑 (a)/(b) 判定）。lint_main 自身 docstring 已自文档化（L240-245），主节补一句即可对齐。

## S6 — byte-stable 面界定（改动纪律依据）

- 禁触碰：`w2_exact` / `build_schemes` / `top10_gold_count` / `reachable_top10_gold_counts` / `brute_force_*` / main() 的 (a)/(b) 判定逻辑 / GOLD_DOMAIN1 / S1 / T_PASS / EPS 常量。
- 允许触碰：load_batch2 schema 检查层（追加检查）、lint_main 输出层（如需）、主 docstring。
- 回归锚点：无参调用（batch2/ 不存在态）stdout 两行 `[SIGNAL] blocked-on-external...` + `[INFO] 预注册锚点...` + exit 0，须 byte-exact。

## 负面结果声明

1. 「8 失败出口」口径勘误——实际 9 出口（含 E1 SIGNAL 特例）；任务书 5/8 对应口径 B（仅 exit 2 出口），本 goal 沿用该口径并全量记录。
2. 任务书「KeyError crash」表述不实——实测为静默漏计（gold 缺席 → 计数偏低 → (a) 假 FAIL/SIGNAL 风险），比 crash 更隐蔽；拦截动机不变。