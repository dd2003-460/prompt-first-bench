# 03 — RV3G3cdx-closure-checklist-assert · 动作分解

> goal: 收口 commit queue diff 机判门禁 · 分支 ralph/rv3g3cdx-closure-checklist-assert · 2026-10-30
> 输入：02（关键词集 + 三形态 + 规则定稿）+ 02.5（X4 修正 (c) 匹配规则为子串双向）。

## 判定

规则零新增设计（全部机械化自 r146 02 表 + 攻击 5 豁免子句），直接实现。唯一设计增量 = 02.5 X4 的 (c) 子串匹配修正（已预注册于 02.5，非临时扩规则）。

## 行动分解

| # | 动作 | 对象 | 可验证产物 |
|---|------|------|-----------|
| A1 | 实现 assert-closure-checklist.py `<hash> <short-name>`：解析 message + queue diff，执行 (a)/(b)/(c)，exit 0/1/2 三分支 | bench/rubric-v3/ablation/scripts/assert-closure-checklist.py（新文件） | 源码 |
| A2 | 正样例实跑 ×3（404ba7e / 9f48d94 / c0eba3b）→ exit 0；豁免分支与翻转分支分别命中实证 | 三个真实 commit | 04 表 |
| A3 | 负样例构造 ×2（临时分支合成 commit：N1 漏翻型 / N2 虚报追加型）→ exit 1 指名道姓；跑完回滚不留痕 | 临时分支 tmp/closurecheck-neg-samples | 04 表 + `git branch -D` 清理证据 |
| A4 | 异常态 ×2（不存在 hash / 无 queue diff 的 commit d626088）→ exit 2 | — | 04 表 |
| A5 | 回归基线七脚本 spot check vs r147 A4 表 + 冻结面 0 行 diff + queue 收口 + 04.5 | 全仓 | 04 表 + verdict pass |

## 预注册边界（04.5 消费）

- B1：纯字符串机判，不做语义理解；关键词集 = 02 S1 并集 {划掉, 标记完成, 核销, [ ]→[x]}，(b) 触发词 = {新导出候选, 追加候选, 导出候选}。
- B2：(c) 匹配规则 = 02.5 X4 修正版（diff 短名 ⊆ message 或 message 含其 ≥min(8,len) 连续子串）。
- B3：改动面 ⊆ {新脚本, stages/*, current-goal.md, goal-queue.md}；临时负样例 commit 只存在于被删除的临时分支，main 历史零污染。
- B4：本脚本是**工具**不是**门禁接入**——本轮不修改任何现有流程使其强制调用（接入义务登记为候选，防超范围）。