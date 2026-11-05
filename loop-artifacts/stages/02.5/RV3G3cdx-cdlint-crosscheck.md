# 阶段 02.5 — RV3G3cdx-crossdomain-lint-coverage-expand · 交叉核对与裁定（r150）

> 输入：stages/02/RV3G3cdx-cdlint-scan.md S1-S6。本文件 = (b)/(c) 判定语义权威源，脚本 docstring 须 byte-stable 引用本节。

## X1 — (b) 键集检查对 D1 缺省路径的适用性

**裁定：仅显式声明 gold_nodes 时检查；缺省沿用 GOLD_DOMAIN1 路径不查。**

依据：(i) current-goal 失败降级第 2 条已预注册此最小规则；(ii) 缺省路径的语义是「同题面冻结 ⇒ 沿用第一域清单」，其正确性由 B10 变体矩阵冻结保证而非数据自证——对缺省态查 prior.nodes 键集会把「batch2 prior 必须包含第一域全部 5 个 gold 节点」变成隐式硬约束，超出 schema 声明面（prior 可以合法地只含子集节点 + 缺省 gold？不——若 gold 缺省且 nodes 缺 gold 成员，下游同样静默失真……但此形态被 E9 hit-matrix 侧检查覆盖：hit-matrix 必须含全部 gold 节点，而 build_schemes 用 prior.nodes 合成权重，gold∉nodes 仍漏检）。
**复核后修正裁定**：缺省路径同样存在悬空风险且 E9 不兜底（E9 只查 hit-matrix 侧）。但缺省态下「哪些键必须在 prior.nodes」的答案 = GOLD_DOMAIN1 常量，检查逻辑与显式态完全同构（只是 gold 来源不同）。⇒ **最终裁定：两路都查**（gold 解析完成后统一 `for nid in gold: if nid not in pe["nodes"]`），因为检查对象是解析后的 gold 变量，代码零分叉；byte-exact 不受影响（无参路径 batch2/ 不存在不可达）。current-goal 失败降级第 2 条的「仅显式」预判被本轮实证推翻——降级条款是防冲突预案，实际无冲突（D1 缺省语义 = 「沿用清单」，清单成员自然应在权重表内，检查不与任何声明语义矛盾）。此推翻如实登记。

## X2 — (b) 出口文案与位置

**裁定**：插入点 = load_batch2 L218（gold_nodes 类型检查）之后、L219 per-node w1/p_tilde 循环之前。文案对齐 E 系列风格：
`prior-estimates-batch2.json: gold node {nid} absent from 'nodes' keys`（逐缺失键报告，首个即 return——与既有检查链 fail-fast 风格一致）。
位置理由：先确认 gold 本身是合法 list（E6 先行），再查成员归属；在 per-node 循环前报告可避免「w1 缺失 + gold 悬空」双错时报告顺序随 dict 迭代序漂移。

## X3 — M2 prompt_version 最小消费落点

**裁定：放 load_batch2 schema 层（非 lint_main）。**

检查内容（M2 最小消费，fail-loud 不扩判）：
- `prompt_version` 键缺失 ⇒ exit 2 `prior-estimates-batch2.json: field 'prompt_version' required`
- 值非 str 或 strip 后为空 ⇒ exit 2 `prompt_version must be a non-empty string`

落点理由：(i) schema 层检查在 lint 与判定两模式同时生效——这正是 M2「零消费」缺陷的修复方向（判定模式才是主消费者）；(ii) byte-exact 回归不受影响（无参路径 batch2/ 不存在态不可达，已 S5 确认）；(iii) 未来 batch2 数据到来时判定模式立即获得该防线，无需二次改动。
**docstring 预注册义务**：主 docstring 输入 schema 节 L29 从「题面版本标识（对照用）」更新为「题面版本标识——schema 层强制存在 + 非空字符串（M2 最小消费，r150）；内容级对照（换题面 fail-loud）未实现，见 M1」。

## X4 — M1 完整 fail-loud 处置

**裁定：降级登记 + 导出候选（走 current-goal 失败降级第 1 条路径），不写 APPROVALS。**

依据（S3 推导链）：完整 fail-loud 需要「题面版本↔gold_nodes 映射」权威源；现有冻结件（DRAFT v2 §3.2 冻结 diff + revision-log 冻结 commit 快照）**不含**该映射——六变体共用同一基础题面（B10），gold 差异只可能出现在跨域换题面场景，而跨域题面文本无任何落盘件。⇒ 内容级对照在当前仓库内**无机判可实现的对象**。
处置分解：
- 本轮落地：X3 的 M2 最小消费（存在性 + 非空）——把 prompt_version 从「纯注释字段」变为「有机器检查的字段」，M1/M2 的「登记了没人接」状态终结；
- 导出候选（新 goal）：「batch2 题面↔gold_nodes 映射登记表」——新建 `bench/rubric-v3/ablation/batch2-prompt-gold-map.json`（或 md）承载 {prompt_version: {prompt_file, gold_nodes, freeze_ref}}，届时 fail-loud = 对照表查表 + 不一致 exit 2。建表动作纯仓库内不需成璐裁定（裁定的是流程归属，属候选 goal 内部事项）。
- M1 原登记项（r147）状态更新：「登记不擅自扩规则」→「部分承接：M2 最小消费已落地；完整 fail-loud 导出候选 <name>」。

## X5 — 样例矩阵目标口径（勘误 r147「5/8」）

**裁定：以 S1 代码实跑枚举为准 = 9 个 FAIL 出口（E2-E10），目标 9/9 全覆盖。**
r147「5/8」分母口径无法从现存工件复原（r147 stages 文档未留出口编号表）——登记为数字勘误（负面结果），不追溯修改 r147 工件（历史工件不改写原则），在本 goal 收口注记中说明口径切换原因。
新增负样例 ×4（持久落盘 `batch2-lint-samples/`，命名沿用 neg-* 先例）：
- `neg-hitmatrix-missing/` → E2
- `neg-unreadable-json/` → E4（prior 文件写 `{broken`）
- `neg-nodes-not-dict/` → E5
- `neg-gold-not-list/` → E6
- `neg-gold-dangling-in-prior/` → (b) 新出口（N-9 ∈ hit-matrix cells ∩ gold_nodes，∉ prior.nodes——S2 实证的漏检形态）
合计 5 新增；既有 5 neg 零改动（零漂移验证对象）。pos-full / pos-no-blindtest 零改动。

## X6 — docstring lint 模式节（d）内容定稿

主 docstring exit code 节（L57-59）改写为：
```
exit code：0 = 无 FAIL（含 SIGNAL blocked-on-external / (a)(b) verdict 输出）
           1 = (a) 或 (b) FAIL
           2 = schema 违例 / 换题面无 gold_nodes 声明 / 输入不可读（ERROR fail-loud）

--lint-only [--dir DIR] 模式（r147 交付，r150 补本节）：纯 schema 校验不跑 (a)/(b)。
  exit 0 = 全通过；特例：目录不存在 = [SIGNAL]「数据未落盘」exit 0（非错误）；
  blindtest 缺失 = [INFO] D5 降级提示 exit 0。exit 2 = schema 违例（含 r150 新增：
  gold_nodes 成员 ⊄ prior.nodes 键集 / prompt_version 缺失或非非空字符串）。
  供数据提供方落盘前自验；判定模式（无 --lint-only）行为不变。
```
另：输入 schema 节 L26-29 gold_nodes/prompt_version 行同步更新（见 X3/X4）。

## 终局判定语义（docstring 抄录源）

1. load_batch2 检查链新序（r150 加粗项）：文件存在性(E2/E3) → JSON 可读(E4) → nodes 为 dict(E5) → gold_nodes 为 str list(E6) → **【新】gold 成员 ⊆ nodes 键集** → per-node w1/p_tilde(E7/E8) → **【新】prompt_version 存在 + 非空 str** → hit-matrix gold 覆盖(E9) → blindtest entry 字段(E10)。
   - 注：prompt_version 检查放 per-node 循环后（X3 落点微调：与 gold 键集检查同为「顶层字段」类，集中放置；顺序不影响 byte-exact，因该路径当前不可达）。
2. (b) 键集检查对缺省/显式两路统一生效（X1 最终裁定）。
3. M1 完整 fail-loud 未实现（权威源缺失，X4）；M2 最小消费已实现（X3）。