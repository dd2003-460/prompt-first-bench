# 阶段 01 — RV3G3cdx-closure-checklist-assert（补记：r148 前序会话已落盘 current-goal，本文件为工件链补全）

## 【目标】
收口 commit 的 queue diff 机判门禁：轻量 assert 脚本消费「收口 commit hash + 目标 goal 短名」，机判三项——
(a) message 含「划掉/标记完成/核销/[ ]→[x]」⇒ diff 必含对应行 `[ ]`→`[x]` 翻转；
    **豁免子句**：目标行在该 commit 之前不存在于 queue（`git show <h>~1:tasks/goal-queue.md | grep -c <短名>` = 0）
    ⇒ 「首建即 [x]」合法形态，跳过 (a)（r146 04.5 攻击 5 处置）。
(b) message 含「新导出候选/追加候选/导出候选」⇒ 每个提取出的候选短名 X 必出现在 diff 的 `+` 行中。
(c) 双向闭合：diff 中每个含 checkbox 的行变更，其 goal 短名须在 message 中有对应声称
    （匹配规则 = r148 02.5 X4 修正版：diff 短名 ⊆ message，或 message 含该短名的连续子串且长度 ≥ min(8, len(短名))）。

97d2adf 型漏翻将被 (a) 直接拦截，检测时点从事后 sweep 前移到收口当下。

## 【阶段】
01 目标分解（本文件）→ 02 现状扫描 → 02.5 交叉核对 → 03 动作分解 → 04 执行验证 → 04.5 反方复核 → 收口

## 【SOP 索引】
loop/prompt-first/01..04.5 + sop/arena-loop-pipeline.md；规则权威源 = r146 loop-artifacts/stages/02/RV3G3cdx-scan-execution.md
三列对照表 + stages/04.5 攻击 5 豁免子句。

## 【验收标准】
1. `bench/rubric-v3/ablation/scripts/assert-closure-checklist.py` 落盘，exit 三分支：0 全通过 / 1 FAIL 指名道姓 / 2 输入不可解析。
2. 正样例 PASS：真实历史收口 commit（如 r146 收口 16b063f、r147 收口 0bb55ce、r145 核销轮 9f48d94）实跑 exit 0。
3. 负样例 FAIL：构造性负样例（message 声称划掉但 checkbox 未翻转 = 97d2adf 型复刻；message 声称追加候选但 diff 无插入行）实跑 exit 1 且 FAIL 行指名道姓。
4. 冻结面零修改（hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-*）。
5. 既有断言脚本回归基线维持（七脚本 exit=[0,0,0,1,0,0,0] 语义不变）。

## 【失败降级】
- web-llm 通道不可用（登录态失效先例）→ 记录 unverified 继续，纯仓库内字符串机判不依赖外部。
- 构造负样例若与真实历史 commit 混淆 → 负样例一律在独立分支上构造并标注「构造性样例」，不进入 main 历史叙述。
- B4 预注册：本轮只交付工具，不接入任何自动门禁（接入门禁 = 未来 goal，避免改变所有后续收口行为）。