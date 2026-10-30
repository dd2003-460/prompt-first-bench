# Goal: RV3G3cdx-m4-independent-source-ops — M4「独立源」口径操作化定义（r152）

> 创建：2026-10-30 · ralph loop runner（队列自找 fallback——goal-queue.md 全部 13 个未完成行均外部阻塞/待成璐裁定，按协议阶段 A 第 1 步扫 bench/self-opt-tester/bench.md「已知缺陷（进 R5）」清单，选产投比最高的未解决项）
> 依据：bench.md L75 缺陷 #2「M4『独立源』口径仍依赖裁决者主观——需操作化定义（如：不同 provider 且不同 prompt 模板的回执对）」。实证基础已齐备：两打分器（DeepSeek r4 / Claude Code r5.1）对 3 run 的 M4 判分 basis 原文逐条引用了各自的主观口径（`r4/independent-scoring-deepseek.json` L28 / `r5/scoring-claude-r1.json` M4 basis ×3）；evidence-packet-template-v2.md P6 已有 `independent_sources[{claim,source,conf,nature}]` + `channel_status` 字段但**无判定规则**——「给足源清单让打分器自己判，不代判」正是缺陷本体。本 goal = 把两个打分器的实际判分逻辑提炼为可机判的操作化定义，并用 packet v2 既有数据做回测验证。纯仓库内文本+脚本工作，零外部依赖。

## 【目标】
三件事，范围边界明确（打分器侧的实际执行切换不在本轮——那需要下一轮 run 才有新数据）：
- **(a) 操作化定义落盘**：`bench/rubric-v3/m4-independent-source-definition.md`——从两打分器 basis 原文反向工程出判定规则：(i) 「独立源」的可判据（provider 维度 / 通道维度 / 读取方式维度的区分表，含「同源双读」「上轮回执转录」「单通道 web_search 多 URL」三个反例类——全部有先例原文锚点）；(ii) conf 标注与独立源计数的关系（≥2 独立源的计数规则）；(iii) 降级态处理（`channel_status` 非可达时 M4 上限语义）。每条规则标注证据来源（scoring json file:line / packet template file:line）；
- **(b) 机判规格预注册**：在定义文档中写明 assert 脚本的未来收紧规格（P6 `independent_sources` 条目级校验：nature 枚举合法性 / 同一 source 字符串去重计数 / ≥2 独立源判定函数签名），但**本轮不改任何现有脚本**（assert-packet-audit.py 等十五脚本零改动禁区——与 r151 契约 §3 同构的分层纪律）；
- **(c) 回测验证**：用 packet v2 既有 `independent_sources` 数据（run1×2 / run2×6 / run3×2 共 10 条）对新定义做回测——按新规则重新计数每 run 独立源数，与两打分器实际判分方向对账（不要求分数一致，要求**判低分的理由类别**被新规则覆盖）；对账结果如实登记（含 mismatch 若有）。

## 【阶段】
00 预检 → 01 分解（本文件）→ 02 现状扫描（两打分器 M4 basis 全文取证 + packet v2 P6 全字段枚举 + 缺陷 #2 上下文链）→ 02.5 交叉核对（定义条款逐条与 basis 原文互验 + 回测口径裁定）→ 03 动作分解 → 04 执行验证（定义文档落盘 + 回测实跑 + 十五脚本零漂移回归）→ 04.5 反方复核 → 收口（queue 更新 + merge main）

## 【SOP 索引】
- `tasks/ralph-loop-runner.md` 阶段 B/C
- 证据源（只读）：`bench/self-opt-tester/bench.md`（缺陷清单 + r3→r4 变化解释）/ `bench/self-opt-tester/r4/independent-scoring-deepseek.json` / `bench/self-opt-tester/r5/scoring-claude-r1.json` / `bench/self-opt-tester/r5/evidence-packet-template-v2.md`（P6 节）/ `bench/self-opt-tester/r5/evidence-packet-r4-v2.json`（回测数据）
- 参照先例：`tasks/queue-format-contract.md`（条款带证据来源 + 升级路径预注册 + 矛盾登记原则的结构范式）/ `gmr-criterion-freeze.md`（冻结件七节结构）

## 【验收标准】
- [ ] `bench/rubric-v3/m4-independent-source-definition.md` 落盘，每条判定规则带证据来源（file:line），覆盖 (i)(ii)(iii) 三类
- [ ] 定义含机判升级路径章节（规格写明，现有脚本本轮零改动）
- [ ] 回测记录落盘（10 条 independent_sources 逐条按新规则分类 + 每 run 独立源计数 + 与两打分器判分方向对账表）
- [ ] 十五 assert 脚本基线零漂移（exit code 序列与 main 一致）；冻结面（hit-matrix.json / prior-estimates.json / gold-tree.md）零修改
- [ ] 04.5 verdict pass；queue 更新（追加本 goal `[x]` 收口行 + 结果注记 + 新候选 ≥1【建议：m4-assert-lint 机判落地候选，激活条件 = 下一轮 run 产出新 packet】）

## 【失败降级】
- 若两打分器 basis 揭示的口径互相矛盾（如同一形态一个计入一个不计入）→ 按「多数派 + 最新轮次」（r151 契约 §5 原则）裁定并如实登记矛盾项，不强行统一历史判分
- 若回测发现新规则无法覆盖某打分器判低分理由（规则不完备）→ 如实登记缺口 + 该理由类别标「待下轮 run 新数据再裁定」，不硬造规则凑覆盖
- 若 P6 字段不足以支撑某条判定规则（如缺 provider 字段）→ 定义中标注「当前 packet schema 不可机判，需 schema 扩展」，导出 schema 扩展候选而非本轮改 schema