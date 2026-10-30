# 阶段 01-03 合并工件 — RV3G4-prior-source-assert（小 goal 压缩六阶段：01/02/02.5/03 判定一次落盘，04/04.5 独立）

> origin: ai · 2026-10-30 · 说明：阶段 A 范围发现——本 goal 核心交付物已存在（commit 0fedf42 / r130），收口为验证+补强。01-03 压缩为一件，04/04.5 保持独立完整。

## 01 拆解 + 范围发现

| # | 因素 | 口径预注册 |
|---|------|-----------|
| F0 (范围) | 交付物存在性 | `scripts/assert-prior-source.py` 已落盘（0fedf42）+ `prior-estimates.json:p_tilde_provenance` 双源登记块已存在 → 本 goal 不是从零新建，是**核销+防失效实证** |
| F1 (队列原文四项) | 逐条核销 | ①「≥N 个独立源」= 检查③ distinct judge_id ≥ N_MIN=2；②「source 字段缺失 FAIL」= 检查①；③「单源 FAIL」= 检查③（N_MIN=2 使单源必 FAIL）；④「signal-only 或 verdict 二选一在 01 定」= 已定为 **verdict 型**（exit 1 = FAIL，非 signal-only）——r130 落地时的选择，本 goal 确认该选择与队列语义兼容 |
| F2 (防失效实证) | 变异测试 | 队列候选的验收语义是「能力真实生效」，纸面 PASS 不够——必须实证：删一条 source / 删整块 provenance / 清空列表，三种单源或缺失场景脚本都 FAIL exit 1 |
| F3 (冻结面) | prior-estimates.json 只读 | 变异测试全部走 /tmp 副本 + 沙盒脚本（改 ROOT/PRIOR 指向），原文件零触碰 |

**F1-④ 判据说明**：队列写「signal-only 或 verdict 二选一在 01 定」。r130 选了 verdict 型。本 goal 01 复核该选择：p̃ 来源缺失是**协议硬约束**（S3 降档教训：纸面协议零防护力直到被执行），不是待人工归类的信号 → verdict 型（FAIL 阻断）正确，不改。

## 02 研究（一手验证）

```
$ python3 assert-prior-source.py; echo $?
... 8× [PASS] ... RESULT: PASS (all checks green; signal-only — see header)
0
```
基线复验通过。provenance 块结构实证：independent_sources[2]（primary = Lead 主会话 qwen3.8-27b / blind-reestimate = fresh-context subagent qwen3.8-27b）+ note 显式登记 `family-independent: false`（两源同族事实不隐瞒，跨家族闭环挂 rubric-v3 遗留 #1）。

**措辞瑕疵发现**：脚本尾部打印 `RESULT: PASS (all checks green; signal-only — see header)`——但本脚本是 **verdict 型**（exit 1 阻断），header 第一行虽声明 "SIGNAL ONLY: provenance metadata check, NOT a family-independence verdict"，该声明的真实含义是「不构成家族独立性结论」（防过度解读），而尾行的 "signal-only" 字样与之叠加后易误读为「不参与门禁的纯信号」。两者语义不同：header 说的是**结论边界**（不裁决家族隔离），尾行说的是**门禁地位**（是否阻断）。当前尾行措辞把前者泄漏进了后者。→ J4 修尾行措辞（一行改动，输出面变化需重捕基线）。

## 02.5 对抗核验

| # | 攻击 | 裁决 |
|---|------|------|
| A1 | "goal 说'消除 p̃ 来源不可机判状态'，但脚本只查元数据块存在性与计数，不验证两个 source 真的独立生成（judge_id 是自由文本，可以填两个假 ID）" | **成立，接受为已知边界**。机器可判的上限就是元数据一致性（artifact 可解析 + blind 源 judge_id 与 judge-blindtest-r1.json byte-exact + 去重计数）；「生成过程真独立」需要执行层证据（会话日志），超出文件断言能力。note 字段已如实登记 family-independent:false——脚本的职责是**让缺失可见**，不是**证明独立性**。这与 G4 S3 教训精确对齐：机械化的是「登记义务」，不是「独立性本身」 |
| A2 | "N_MIN=2 太低——rubric 协议要求 ≥3 异族，脚本用 2 会给出虚假安全感" | **部分成立**。脚本 docstring 已显式声明「≥3 异族标准见 rubric-v3 遗留 #1，不在本脚本范围」，且 provenance.note 登记 family-independent:false——双重限定语防止误读。N_MIN=2 是「单源 vs 多源」的最小分界（队列原文「单源 = FAIL」的最低实现），提 N_MIN=3 会让当前双源数据 FAIL，属于遗留 #1 的范围（需第三个模型，外部依赖）。不改值，改法已在 docstring 封闭 |
| A3 | "尾行 'signal-only' 措辞修复会改变输出面——下游若有 grep 'signal-only' 的消费方会断" | **驳回**。grep 实证：仓库内无其他文件引用该尾行字符串（仅本脚本自身）；且修复方向是让措辞**更准确**而非删除信息（保留 "see header" 指针）。消费方若依赖错误措辞，依赖本身就是缺陷 |

## 03 行动表

| # | 行动 | 验证 |
|---|------|------|
| J1 | 基线复验 | 8/8 PASS exit 0（已做，/tmp/ps-baseline.txt） |
| J2 | 变异 M1/M2/M3（/tmp 沙盒，冻结面零触碰） | 三场景全 FAIL exit 1 + FAIL 行定位正确（已做，见 04） |
| J3 | 队列原文四项核销表 | 落盘 04 工件 |
| J4 | 尾行措辞修复：`signal-only — see header` → `metadata gate, not a family-independence verdict — see header` | 重跑 diff 仅该行变化 + exit 0 维持 |
| J5 | 冻结面 git status | 仅 assert-prior-source.py + 工件 |

**01-03 判定：pass（范围发现封闭——核销型 goal；A1/A2 边界如实登记不改值；J4 措辞瑕疵定位到行，口径封闭）。**