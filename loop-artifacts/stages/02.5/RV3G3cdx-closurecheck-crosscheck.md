# 02.5 — RV3G3cdx-closure-checklist-assert · 交叉核对（独立重跑取证命令复核 02）

> goal: 收口 commit queue diff 机判门禁 · 分支 ralph/rv3g3cdx-closure-checklist-assert · 2026-10-30
> 方法：不读 02 结论列，从仓库根重新执行 git 取证，逐格比对。

## X1 — 豁免子句检测式实证

`git show 404ba7e~1:tasks/goal-queue.md | grep -c 'RV3G6-o3-claim-rejudge-evidence-audit'` = **0**（首建前不存在 ✓）。
对照：`git show c0eba3b~1:tasks/goal-queue.md | grep -c 'RV3G6-kappa-formula-adjudicate'` = **1**（既有行 ✓，走形态 1 非豁免）。
两分支区分度实证成立。✓

## X2 — 关键词集漏触发风险复核

对三个正样例 message 逐一 grep 关键词并集 {划掉, 标记完成, 核销, [ ]→[x]}：
- 404ba7e：含「queue 划掉」✓
- 9f48d94：**不含「划掉」**，含「核销轮」+「checkbox 漏翻」——命中「核销」✓（若关键词集缺「核销」则 (a) 漏触发，02 S1 已登记此风险并纳入并集）
- c0eba3b：含「queue 划掉」✓
三样例全部可被并集触发。✓

## X3 — diff 形态独立重算

`git show <h> -- tasks/goal-queue.md` 的 `^[+-] \[` 行数：404ba7e = 2 插入 0 删除（形态 2+3）✓；9f48d94 = 3 插入 1 删除（形态 1+3×2）✓；c0eba3b = 3 插入 1 删除（形态 1+3×2）✓。与 02 S2 一致。

## X4 — (c) 双向闭合可行性预检

三正样例 diff 中出现的全部 goal 短名 vs message 提及：
- 404ba7e：diff 含 evidence-audit + erratum-27；message 含两者全称 ✓
- 9f48d94：diff 含 batch2-schema-lint + queue-hygiene-sweep + crossdomain-reverify；message 含「schema-lint」「hygiene-sweep」（短名局部）+ crossdomain 全称——**(c) 的匹配规则须接受短名局部匹配**（≥8 字符前缀/子串），否则误报。02 S3 已写「短名或其前缀 ≥8 字符」，实核「batch2-schema-lint」是 message 中「schema-lint」的超串——方向反了：diff 短名比 message 词更长。修正规则：(c) 匹配 = diff 短名 ⊆ message 子串 **或** message 中存在该短名的连续子串且长度 ≥ min(8, len(短名))。「schema-lint」(11 字符) ⊂「batch2-schema-lint」✓ 可行。**本条为 02 S3 的规则修正**（04 实现按此版）。
- c0eba3b：u1k1-execution / threshold-recalibrate / kappa-formula-adjudicate 均在 message 出现 ✓

## X5 — 边界声明

- 构造性负样例（N1/N2）的临时 commit 造法在 04 定稿（临时分支 + 回滚，不污染 main）；本阶段只确认其语义定义无歧义。
- 02 S1 关键词集的最终取舍以 04 实跑为准（失败降级第 1 条：措辞多样性 → 扩集并登记）。