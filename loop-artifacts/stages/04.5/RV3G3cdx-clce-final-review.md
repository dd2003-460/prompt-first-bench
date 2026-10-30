# 阶段 04.5 — 反方复核（RV3G3cdx-crossdomain-lint-coverage-expand, r150）

> 方法：8 个独立攻击视角逐一尝试推翻「本 goal 交付达标」结论。每条 = 攻击陈述 + 证据核查 + 裁决（驳 / 成立已修 / 部分成立登记）。数字层先做独立重跑（攻击前置，见末节）。

## W1 攻击：键集检查用 `declared is not None` 判「显式声明」——若第二域数据提供方显式写出与 GOLD_DOMAIN1 完全相同的清单，行为与缺省一致；但若写成**顺序不同**的同集合，`pe.get("gold_nodes")` 非 None → 走键集检查，而 hit-matrix 侧 E8 检查用的是替换后的 `gold` 变量——两检查消费的是不是同一份数据？

**证据核查**：读代码 L214-227——`gold = pe.get("gold_nodes")`；None 时 `gold = GOLD_DOMAIN1`；键集检查用 `declared = pe.get("gold_nodes")`（原始值），E8 用 `gold`（可能已替换为默认值）。两者在 declared 非 None 时指向同一 list 对象，在 declared 为 None 时键集检查跳过、E8 用默认值——**无分叉**。顺序不同的同集合：list 相等性不影响 `in` 判断，键集检查按成员逐个查，顺序无关。**驳回**。

## W2 攻击：prompt_version 检查放在节点级 w1/p_tilde 循环**之前**——一个同时缺 prompt_version 又缺 w1 的文件只会报 prompt_version 错，修复后还要再跑一次才发现 w1 缺失。错误报告不聚合 = 对数据提供方不友好，且与 load_batch2 头部 errs join 的聚合风格不一致。

**证据核查**：属实——load_batch2 文件加载段用 `errs.append` 聚合多文件错误，但 schema 段全部是首个违例即 return（既有风格，E4-E9 同样如此）。本轮新检查沿用既有「schema 段首违例即返回」风格而非引入聚合——**风格一致性 > 单文件多错聚合**（改聚合 = 触碰既有 6 个出口的返回结构，byte-stable 面风险）。后果评估：数据提供方逐次修复的成本增加 ≤2 轮（实际样例矩阵证明每个出口独立可定位）。**部分成立登记**——多错聚合作为未来 lint 增强候选方向（不阻塞，不改）。

## W3 攻击：Y1「仅显式声明时查键集」留下漏洞——换题面且不声明 gold_nodes（D1 明令禁止的行为）仍走缺省路径零检查，静默用第一域 GOLD 清单对第二域 nodes 计数，正是 M1 想拦的场景。C-最小等于没接住 M1 的核心风险。

**证据核查**：这是 Y1/Y2 裁定的已知边界，非实现缺陷——完整拦截需要「题面版本↔gold 清单映射表」权威源，S4 实证该映射表不存在（R-10 冻结的是段落 diff 不是 gold 清单；第二域题面本身 blocked-on-external）。造映射表 = 代裁（失败降级第 1 条明令禁止）。当前处置 = 把不可机判的部分**如实降级导出候选**（A6 预登记，激活条件明确），docstring 同步删除虚假宣称（不留「fail-loud 已实现」假象）。攻击指出的风险真实存在但**在本 goal 材料边界内不可闭合**——裁定正确性在于不假装闭合。**驳回**（边界内最优解；风险已传导至候选队列）。

## W4 攻击：neg-json-unreadable 样例的截断位置（L3 column 57）依赖 CPython json 模块的具体报错文案——换 Python 版本/实现（PyPy、ujson）报错文本变化，若未来有测试断言精确文案会碎。

**证据核查**：本仓库所有 assert 脚本只断言 **exit code + 输出前缀**（[ERROR]/[SIGNAL]），无一断言 JSON 报错细节文案（grep 实证：样例 README 只记目标出口名）。且样例用途 = 人工/CI 目检 exit 2 可达性，非自动化文案回归。**驳回**。

## W5 攻击：byte-exact 回归只覆盖了 E1（目录不存在）路径——load_batch2 的其他早退路径（E2 文件缺失）在改动前后 stdout 是否一致未验证。若 A1 插入行意外改变了 errs join 顺序或 INFO 行，无参调用测不出来。

**证据核查**：A1 插入点位于 L218 之后——**所有早退路径（E1 L193 / E2 L209）都在插入点之前返回**，代码上不可能被影响；E2 实跑输出（neg-missing-prior）与 02 S2 基线快照逐字一致（`prior-estimates-batch2.json missing`，A4 表 ✓）。其余路径（E4-E9 + 新增）本就无「改动前」stdout 可比（新行为），以 03 预期表为准全中。**驳回**（结构性论证 + E2 实测双证）。

## W6 攻击：docstring 说「lint 模式永不 exit 1」，但 lint_main 复用 load_batch2——若未来有人往 load_batch2 加 (a)/(b) 判定逻辑，lint 会开始 exit 1 而 docstring 失实。文档承诺了实现不保证的性质。

**证据核查**：lint_main 自身 docstring（L240-245）已写明「纯 schema 校验（不跑 (a)/(b) 判定）」——主 docstring 的「永不 exit 1」是对**当前实现**的描述，与 lint_main 自文档化一致。防未来漂移的机制 = 本仓库既有的「改动须 byte-exact 回归 + 04.5 复核」流程（r147/r149 同款纪律），非靠一句 docstring 承诺。**驳回**（描述性文档，非契约性承诺；流程兜底存在）。

## W7 攻击：四个新样例的 hit-matrix 全部复制自 neg-nodes-missing-w1——若该文件的 hit-matrix 本身含隐性 schema 问题（如某 run 缺字段），新样例可能在到达目标出口前先触发别的检查，覆盖口径虚高。

**证据核查**：逐一核对触发链——neg-json-unreadable 死于文件解析（L205，先于一切 schema 检查）✓；neg-nodes-not-dict 死于 L212（nodes 类型，先于 gold/节点级）✓；neg-goldnodes-badtype 死于 L217（gold 类型，先于键集/节点级）✓；neg-goldnode-not-in-nodes 需 hit-matrix 合法才能走到……**等等**——键集检查（L219-223）在 hit-matrix 检查（L231+）**之前**，所以即使 hit-matrix 有问题也先报键集错。且 pos-full 用同一 hit-matrix 结构通过全链（exit 0），证明该 hit-matrix 无隐性问题。**驳回**（检查顺序 + pos-full 正对照双证）。

## W8 攻击：任务书要求「(c) M1/M2 裁定承接」，本轮只落地了 M2 最小消费，M1 被整体推给导出候选——「承接」变成「转手」，验收标准第 3 条（不留没人接状态）是否真的满足？

**证据核查**：验收标准原文 = 「M1/M2 处置有明确裁决（实现 or 降级登记），docstring 同步更新，不留『登记了但没人接』状态」。本轮：M1 有明确裁决（C-完整否决，理由 = 权威源不存在，02.5 X2 方案对照表落盘）+ docstring 如实化（虚假宣称删除）+ 导出候选带激活条件（第二域题面落盘）+ 与 RV3G3-batch2-arrival-closure 联动标注。「没人接」状态的判据 = 无裁决/无去向——两者皆无。**驳回**（按验收标准字面满足；「承接」≠「必须实现」，current-goal 失败降级第 1 条预先授权了此路径）。

## 数字层独立重跑（攻击前置）

```
$ for d in batch2-lint-samples/*/; do --lint-only --dir $d; done   # 11 样例
neg×9 全 exit 2（末行与 04 A4 表逐格一致）/ pos×2 全 exit 0
$ python3 scripts/assert-goldrank-crossdomain.py                    # E1
exit=0，md5=598180b0954defc64019bb5169efd64b（与 04 A5 基线一致）
$ 七脚本基线（repo root）= [0,0,0,1,0,0,0]；queue-lint exit 0
```
零 mismatch。

## 汇总

| # | 攻击 | 裁决 |
|---|---|---|
| W1 | 键集/E8 数据源分叉 | 驳（同一对象 + 顺序无关） |
| W2 | 错误报告不聚合 | **部分成立登记**（多错聚合 = 未来 lint 增强候选） |
| W3 | Y1 留 M1 核心风险敞口 | 驳（材料边界内不可闭合，已如实传导候选） |
| W4 | JSON 报错文案跨实现脆弱 | 驳（无文案断言消费方） |
| W5 | byte-exact 只覆盖 E1 | 驳（插入点在全部早退之后 + E2 实测） |
| W6 | 「永不 exit 1」文档承诺超实现保证 | 驳（描述性 + 流程兜底） |
| W7 | 共享 hit-matrix 隐性污染 | 驳（检查顺序 + pos-full 正对照） |
| W8 | M1「承接」变「转手」 | 驳（按验收标准字面满足，降级路径预授权） |

**verdict：pass**（8 攻击 7 驳 / 1 部分成立登记【W2 多错聚合候选】）。无未处置 blocker。