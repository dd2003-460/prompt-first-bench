# 阶段 01：目标分解 — RUBRIC-V3-FULL-AUDIT / G5 优化清单

> goal: rubric-v3-audit-g5 · 分支 ralph/rubric-v3-audit-g5 · 2026-10-30
> 上游: tasks/RUBRIC-V3-FULL-AUDIT-task-brief.md §G5 + g4-vulnerability-crosscheck.md「给 G5 的导出」+ R5.2 系列 assert-* 脚本模式

## F1 · 任务书要求与交付物定义

任务书 G5 = 「机判化候选（哪些判定能写成 assert 脚本）+ 并行化候选 + 成本估算」。G4 导出进一步约束了范围与优先级：
- 三类「部分规避」结构 → 三类优化动作：**强制机械化**（S3 降档）、**补覆盖**（S1 未到期/S4 子项）、**加固阈值**（S5 强度不足）。
- 成本估算对象必须包含 adversarial-check **12 blocker**（r111c 勘误后计数）的修复成本——G6 定稿取舍需要这个数字。
- 并行化候选的验收项 = 「有没有人真的跑过」而非「协议里写了没有」（S3 教训：纸面协议防护力为零）。

**交付物** `bench/rubric-v3/ablation/g5-optimization-list.md`，结构：
1. 机判化候选表（每条：判定内容 / 输入文件 / 断言逻辑摘要 / 现有脚本可复用性 / 实现成本 / 防住的风险引用 G4 S#）
2. 并行化候选表（每条：步骤 / 为什么可并行 / 前置条件 / 执行保真度风险 / 成本）
3. 成本估算总表（含 12 blocker 修复成本分级）
4. 负面结果声明（哪些「看起来能机判」实际不能——如语义级重判、κ 值计算本身）
5. 给 G6 的导出（哪些候选建议 G6 前落地、哪些留给后续 goal）

## F2 · 机判化候选来源盘点（仓库内已有证据）

| 来源 | 候选 | 状态 |
|------|------|------|
| G4 S3 降档 | p̃ 多源频率断言（prior-estimates.json 须记录 ≥N 独立生成源，否则拒收） | 已入队 RV3G4-prior-source-assert；本 goal 只做设计+成本，不实现 |
| G4 S3 κ 门禁 | 评分文件缺 κ 门禁回执 = FAIL | 已入队 RV3G4-kappa-receipt-assert；同上 |
| G1 先例 | assert-g1-audit.py（137 行，固定种子抽检 75/248 cell，exit 0/1 + SIGNAL 模式） | 已存在，证明该模式在本仓可运行 |
| R5.2 先例 | assert-packet-symmetry.py / assert-packet-audit.py（各 143 行，PASS/FAIL/SIGNAL 三态 + EXEMPT 哨兵） | 已存在，严格模式基线 67/0 |
| G3 验证链 | W3/W4 分数复算断言（8/8+8/8、ρ 7/7、tie 4/4、top-5 计数）——目前人工 python 一次性执行 | 可脚本化为 assert-w3w4-recompute.py |
| G2 根因层 | w2 公式层复算断言（62/62）——同样目前人工执行 | 可并入同一脚本或独立 |
| S2 同源 | gold-tree 单源检测：calc.py 引用唯一性 + gold 作者字段检查 | 低价值（已知事实），只作登记不作候选 |
| blindtest 一致性 | cross_judge_spearman 字段 vs 重算值一致断言 | 小，可并入 |

## F3 · 并行化候选盘点

| 候选 | 依据 | 关键约束 |
|------|------|----------|
| p̃ 多 LLM 盲生成（DRAFT §1-O3 原协议） | 天然 N 路并行（≥3 服务同 prompt 独立生成） | 需多 provider 通道（web-llm 当前全失效）；执行保真度是核心价值（S3 教训） |
| κ 换位双判 | 两 judge 互换角色打分，互不依赖 | 需异族 judge（R5.2-third-scorer 外部阻塞）；同族双判无家族隔离价值（finding #29） |
| 第二格实验（新域） | 与第一格完全独立 | T17 半成品不在本仓（finding #31 minor 证实）；gold 构建成本高 |
| 8 run 重跑（V0-V3 变体矩阵） | run 间独立 | finding #17 blocker：变体差异未冻结，归因不成立——**先修 DRAFT 再谈并行重跑** |
| arena 通道语义重判（RV3G1-semantic-rejudge） | 75 样本 cell 独立 | 需 arena 会话通道；样本清单已就绪 |

## F4 · 成本估算口径

- 机判脚本：按行数类比（R5.2 脚本 ~143 行 / 半天量级；assert-g1-audit 137 行）+ 输入复杂度（JSON 嵌套深度、git show 依赖）。
- 12 blocker 修复：逐条分三级——L1 文本修订（改 DRAFT 措辞/删条款，低成本）/ L2 协议重设计（需重新论证，中成本）/ L3 外部依赖（异族 judge / 新域数据 / arena 通道，高成本或不可控）。
- 明确标注哪些成本是「本轮可估」哪些是「信息边界」（如 σ_d 无先验 → n_task 反推不可估）。

## 空缺（gaps）

- G1：κ 门禁回执的格式规范不存在（DRAFT 只说「不过不开评」没定义回执长什么样）→ 机判断言需要先定义 schema，这本身是 G6 或专项 goal 的产出；本 goal 只给最小 schema 提案。
- G2：adversarial-check receipt 在 origin/rubric-v3 分支，不在 main 工作树 → 任何针对它的断言脚本都要走 git show，增加脚本复杂度（R5.2 脚本已有此先例，可行）。
- G3：「成本估算」没有统一货币单位——用「runner 回合数」还是「人时」？选 runner 回合数（本 loop 的实际资源单位），人时仅作参考换算。

## 判定

四因素齐备，候选来源全部有仓库内锚点（脚本先例 / G4 导出 / finding 编号），成本口径已定。→ 进入 02。