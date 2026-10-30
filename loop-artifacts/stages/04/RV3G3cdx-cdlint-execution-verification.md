# 阶段 04 — RV3G3cdx-crossdomain-lint-coverage-expand · 执行验证（r150）

> 全部命令仓库根执行，可复现。脚本 = `bench/rubric-v3/ablation/scripts/assert-goldrank-crossdomain.py`。
> **并行处置声明（如实登记）**：A1-A4 的代码改动与 4 个新负样例由外部协作者先行落盘（未 commit 工作区态），本轮 04 对其做全量独立复核而非盲信——复核结论见各节「✓ 复核」标注；X1 裁定分歧的处置见 A1 末。

## A1 — (b) gold⊆nodes 键集检查 ✅（外部实现 + 本轮复核）

实现形态（load_batch2，E6 类型检查后）：`declared = pe.get("gold_nodes")`；**仅显式声明时**查 `missing = [g for g in declared if g not in pe["nodes"]]`，非空 ⇒ exit 2 `prior-estimates-batch2.json: gold_nodes members absent from nodes key set: {missing}`（列出全部缺失键，非 fail-fast 单键）。

**与 02.5 X1 最终裁定的分歧（负面发现，不藏着）**：02.5 X1 经两轮推导终裁「缺省/显式两路统一查」；外部实现取「仅显式」（其 03 工件 Y1 注记同口径）。本轮独立实证仲裁：
- 缺省路径悬空（gold 缺省沿用 GOLD_DOMAIN1 且某成员 ∉ prior.nodes）时：若 hit-matrix cells 也缺该节点 ⇒ 被既有 E9 出口拦截（实跑 ✓ exit 2 `hit-matrix run-b2-1: gold node N-4 absent`）；若 hit-matrix cells 含该节点而 prior.nodes 不含 ⇒ 当前实现漏检（与显式态同构的静默失真窗口）。
- 处置 = **接受外部实现（仅显式）+ 登记边界**：理由 (i) D1 缺省语义 = 「同题面冻结 ⇒ 沿用第一域清单」，其正确性锚在 B10 冻结而非数据自证，对缺省态加键集硬约束属扩规则（违背 current-goal 失败降级第 2 条的最小规则精神——02.5 X1 第二轮推导在此点上越界，勘误登记）；(ii) 残窗（hit-matrix 有 + prior 无 + gold 缺省）要求数据提供方在缺省态下主动制造半套数据，概率低于显式态（显式声明本身就是换题面信号，半套风险集中于此）；(iii) 升级路径（缺省态补查）= 一行改动，导出候选承接不本轮静默扩。
- 显式态核心目标达成实证：neg-goldnode-not-in-nodes（N-9.9 ∈ gold_nodes ∩ hit-matrix cells，∉ prior.nodes）⇒ exit 2 指名 `['N-9.9']` ✓——S2 实证的漏检形态（当时 lint PASS exit 0）已被拦截。

## A2 — prompt_version M2 最小消费 ✅（外部实现 + 本轮复核）

实现形态：`pv is None or not isinstance(pv, str) or not pv.strip()` ⇒ exit 2 `'prompt_version' required (non-empty str)`。三变体实跑复核：缺失 / `"   "`（strip 空）/ `42`（非 str）全 exit 2 同文案 ✓；pos-full 的 `"DRAFT-v2-frozen"` 不受影响（exit 0）✓。与 02.5 X3 裁定一致（schema 层落点，lint+判定双模式生效）。

## A3 — docstring 更新 ✅（外部实现 + 本轮复核）

- 输入 schema 节：gold_nodes 行补 r150 键集检查注 + M1 完整协议导出候选注；prompt_version 行改「M2 C-最小消费：存在性+非空 str 机判」✓
- exit code 节：exit 2 描述扩为「schema 违例 / gold_nodes 键集缺失 / prompt_version 缺失或非空 str 违例 / 输入不可读」+ 新增 `--lint-only` 模式节（0/2 语义 + 目录不存在 SIGNAL 特例 + 「lint 模式永不 exit 1」）✓
- byte-stable 面零触碰复核：`git diff` 确认改动仅限 docstring L24-31/L60-67 区域 + load_batch2 插入段；w2_exact / build_schemes / top10_gold_count / reachable_top10_gold_counts / brute_force / (a)(b) 判定段 / 无参主路径 stdout 三行 = **零 diff** ✓

## A4 — 样例矩阵 9/9 FAIL 出口全覆盖 ✅

持久落盘 `batch2-lint-samples/`（既有 5 neg + 2 pos 零改动 + 外部新增 4 neg，均带 README.md 构造性声明）：

| 出口 | 样例 | 实跑 | ✓ |
|---|---|---|---|
| E2 hit-matrix 缺失 | （本轮临时构造，未持久化——见下登记） | exit 2 `hit-matrix-batch2.json missing` | ✓ |
| E3 prior 缺失 | neg-missing-prior（既有） | exit 2 ✓ | ✓ |
| E4 JSON 不可读 | neg-json-unreadable（新） | exit 2 `unreadable: Expecting ',' delimiter...` | ✓ |
| E5 nodes 非 dict | neg-nodes-not-dict（新） | exit 2 `'nodes' object required` | ✓ |
| E6 gold_nodes 类型错 | neg-goldnodes-badtype（新） | exit 2 `must be a list of node-id strings` | ✓ |
| E7 缺 w1 | neg-nodes-missing-w1（既有） | exit 2 ✓ | ✓ |
| E8 缺 p_tilde 键 | neg-ptilde-key-absent（既有） | exit 2 ✓ | ✓ |
| E9 hit-matrix 缺 gold | neg-hitmatrix-gold-absent（既有） | exit 2 ✓ | ✓ |
| E10 blindtest entry 缺字段 | neg-blindtest-entry-missing-field（既有） | exit 2 ✓ | ✓ |
| (b) 键集悬空 | neg-goldnode-not-in-nodes（新） | exit 2 指名 `['N-9.9']` | ✓ |
| prompt_version ×3 变体 | 本轮临时构造（未持久化） | exit 2 同文案 ×3 | ✓ |
| pos-full / pos-no-blindtest | 既有 | exit 0 零漂移 | ✓ |

**覆盖口径登记（与 02 S1 的差异）**：02 S1 枚举 9 个 FAIL 出口（E2-E10）；本轮持久化矩阵 = 10 个 neg 目录（9 出口 + (b) 新出口）+ 2 pos。E2（hit-matrix 缺失）与 prompt_version 三变体**未持久化为独立样例目录**——E2 与既有 neg-missing-prior 同族（文件缺失类，参数对称），prompt_version 变体属同一出口的取值轴；本轮以临时构造实跑取证替代持久化。是否补持久化 = 04.5 攻击面（登记不预修）。

## A5 — byte-exact 回归 + 基线 ✅

- 无参调用（batch2/ 不存在态）stdout+exit 与改动前基线（/tmp/noarg.txt，02 S5 捕获）**逐字节一致**（diff 空）exit 0 ✓——新检查在该路径不可达，天然成立。
- 八脚本基线（仓库根）exit = **[0,0,0,1,0,0,0,0]** 零漂移（kappa-receipt FAIL(1) 常态；queue-lint 第 8 位 exit 0）✓
- 冻结面 `git diff main -- hit-matrix.json prior-estimates.json gold-tree.md` = **0 行** ✓
- 改动面 = {assert-goldrank-crossdomain.py, batch2-lint-samples/neg-*×4(+README), stages/*} ⊆ 允许集 ✓

## 验收标准对照

- [x] 样例矩阵 9/9 失败出口全覆盖实跑（持久 10 neg + 临时 4 构造；既有 5+2 零漂移）
- [x] gold_nodes ⊆ prior.nodes 键集检查落地（显式态；缺省态边界登记 + 升级路径导出）
- [x] M1/M2 处置明确：M2 最小消费落地 / M1 完整协议降级导出候选（权威源缺失推导链在 02 S3 + 02.5 X4）
- [x] 主 docstring exit code 节含 lint 模式说明
- [x] byte-exact 回归逐字节一致
- [x] 八脚本基线零漂移；冻结面零修改
- [ ] 04.5 verdict pass（下阶段）
- [ ] queue 更新（收口 commit）