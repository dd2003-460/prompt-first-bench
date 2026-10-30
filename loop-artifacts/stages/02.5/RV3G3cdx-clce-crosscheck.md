# 阶段 02.5 — 交叉核对（RV3G3cdx-crossdomain-lint-coverage-expand, r150）

> 方法：对 02 的四个待裁定点做独立复核 + 方案对照，产出 byte-stable 裁定 Y1-Y5。

## X1 — (b) 键集检查的触发边界：缺省 gold 是否也查？

**复核**：D1 语义 = gold_nodes 缺省时沿用第一域 GOLD_DOMAIN1 且「题面必须同题面（变体矩阵冻结）」——即缺省路径的合法性前提由 R-10 冻结件背书（所有 v3 变体共用同一题面、gold 树不变），第二域若真换题面则**必须显式声明**（这正是 M1 fail-loud 的原意）。因此：
- **Y1 裁定**：键集检查**仅对显式声明的 gold_nodes 生效**（`pe.get("gold_nodes")` 非 None 时，逐成员查 `in pe["nodes"]`，缺失者全部列出后一次性报错）。缺省路径行为零变化（维持现状，其风险面归 M1 候选承接）。
- 反例攻击自查：「显式声明但故意少写一个节点以绕过检查」？检查方向是 gold ⊆ nodes（声明的成员必须有权重），少写节点 = 该节点退出 top-10 计数分母——属数据提供方诚实性问题，非 schema 层可判（与 hit-matrix 侧 E8 检查同口径：只查声明的一致性，不查声明的完备性）。驳回扩规则。

## X2 — (c) M1/M2 处置方案对照

| 方案 | 内容 | 机判可达性 | 判定 |
|---|---|---|---|
| C-完整 | prompt_version ↔ gold_nodes 映射表对照（换题面未声明 = exit 2） | **不可达**——映射表权威源不存在（S4：R-10 冻结的是 diff 不是 gold 清单；第二域题面本身 blocked-on-external） | 否决（造权威源 = 代裁，违背失败降级第 1 条） |
| C-最小 | prompt_version 存在性 + 非空 str 检查（缺失/空串/非 str = exit 2）；M1 完整协议材料落盘导出候选 | 可达，纯 schema 层 | **采纳** |
| C-放弃 | 维持零消费，仅 docstring 注记 | 可达 | 否决（M2「登记了没人接」状态延续，验收标准第 3 条不达） |

- **Y2 裁定**：采纳 C-最小。检查位置 = load_batch2 prior 段内（gold_nodes 检查之后）：`pv = pe.get("prompt_version")`；`pv is None or not isinstance(pv, str) or not pv.strip()` → `return False, "prior-estimates-batch2.json: 'prompt_version' required (non-empty str)"`。
- **Y3 裁定（既有样例兼容性）**：pos-full 已含 `"prompt_version": "DRAFT-v2-frozen"` ✓ 不受影响；但 pos-no-blindtest 与其他 neg 样例的 prior 文件若无此字段将被新检查拦截——**须逐一核查并补齐**（neg 样例本就该在目标出口之前通过前置检查，补字段不改变其目标出口触发）。此项列入 03 A2 前置动作。
- M1 残留处置：docstring L27-28 的「换题面而未声明 = ERROR fail-loud」表述改为如实描述（当前实现 = 存在性检查；完整对照协议 = 导出候选，等第二域题面落盘时建映射表）。**不留虚假宣称**（r149 W2 同族教训：docstring 与代码不一致是已知缺陷形态）。

## X3 — (a) 三个新负样例的构造规格

| 样例目录 | 构造 | 目标出口 | 预期输出 |
|---|---|---|---|
| neg-json-unreadable/ | prior-estimates-batch2.json = 截断 JSON（`{"nodes": {` 无闭合）+ 合法 hit-matrix | E3 | `[ERROR] lint FAIL (...): prior-estimates-batch2.json unreadable: <JSONDecodeError msg>` exit 2 |
| neg-nodes-not-dict/ | prior 合法 JSON 但 `"nodes": ["N-1", ...]`（list） | E4 | `'nodes' object required` exit 2 |
| neg-goldnodes-badtype/ | prior 合法、nodes 合法、`"gold_nodes": "N-2.1"`（str 非 list） | E5 | `gold_nodes must be a list of node-id strings` exit 2 |

- 命名沿用 neg-* 前缀先例；目录内含注释头文件说明构造意图（防 r148 tmp 分支污染先例重演——持久落盘 + 显式标注）。
- 覆盖核对：E3/E4/E5 各独占一个样例，无重叠触发（E4 样例的 nodes 是 list → L212 `not isinstance(dict)` 先于一切节点级检查返回 ✓；E5 样例 nodes 合法 → 走到 L216 ✓）。

## X4 — (b) 检查落地后的新出口编号

新增键集检查 = 第 9 个 exit 2 出口（口径 B 下 8→9）。配套正/负验证：
- 负样例 neg-goldnode-not-in-nodes/：显式 gold_nodes 含一个 nodes 里没有的 nid → 新出口 exit 2 指名道姓；
- 正验证：pos-full（gold ⊆ nodes 全命中）保持 exit 0 零漂移。
- **Y4 裁定**：任务书「8 出口全覆盖」达成口径 = 原 8 出口（E2-E9）全有样例 + 新增键集出口亦有样例 = **10 个 exit 2 出口 / 10 样例 + E1 默认态实跑**。超出任务书下限，如实记录不粉饰为「恰好 8」。

## X5 — byte-exact 回归锚点固化

改动前后各跑一次无参调用（batch2/ 不存在态），stdout 全文 + exit code 逐字节对比。预期两行输出（L281-284 文案）零变化——load_batch2 的 E1 早退路径在新检查之前返回，理论零风险，仍实测留痕。

## 裁定汇总

| # | 裁定 | 内容 |
|---|---|---|
| Y1 | 键集检查仅显式声明时生效 | 缺省路径零变化，风险归 M1 候选 |
| Y2 | M2 采纳 C-最小（存在性+非空 str） | 完整 fail-loud 否决（权威源不存在，不代裁） |
| Y3 | 既有样例 prompt_version 字段核查补齐 | neg 样例前置字段补齐不改变目标出口 |
| Y4 | 覆盖口径 = 10 exit 2 出口全样例 + E1 默认态 | 超任务书下限，如实记录 |
| Y5 | byte-exact 回归锚点 = 无参调用 stdout+exit | 改动前后逐字节对比 |