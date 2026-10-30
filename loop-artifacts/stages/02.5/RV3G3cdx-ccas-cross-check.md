# 阶段 02.5 — RV3G3cdx-closure-checklist-assert 交叉核对（补记）

## X1 豁免检测式 0/1 实证
`git show <h>~1:tasks/goal-queue.md | grep -c <短名>`：
- 既有行翻转 commit（16b063f）→ cnt ≥ 1 → 非首建，走 (a) 翻转判定。
- 首建即 [x] 形态（404ba7e 先例）→ cnt = 0 且 plus 含 `+ [x] <name>` → 豁免命中。
- 注意：grep 管道必须 shell=True 执行——列表形式传 `|` 会被 git 当字面路径参数（exit 128），脚本内已注释。

## X2 9f48d94『核销』关键词漏触发风险复核
9f48d94 message 无「划掉」字样，仅「核销」。若 FLIP_KW 只含「划掉」则该 commit 的 (a) 不触发 → 漏检。
处置：FLIP_KW 取并集含「核销」；实跑 9f48d94 + RV3G3-threshold-crossdomain-reverify → `[PASS] (a)` exit 0，确认覆盖。

## X3 构造负样例与真实历史的隔离
N1/N2 在独立分支 tmp/closurecheck-neg-samples 上构造（基于 main 的 queue 快照做反向编辑），commit message 显式标注「构造性负样例」。
它们**不是** r148 的真实收口 commit——r148 真实收口 = 本 goal 收口轮在 main 上的 queue 划掉 commit。
隔离目的：负样例进 main 历史会污染后续 sweep 的「message↔状态位一致性」抽查窗口（sweep 按收口 commit 枚举）。

## X4 (c) 匹配规则修正（双向子串）
初版 (c) 只判 `dname in msg`：message 用局部短称（如「schema-lint」指代「batch2-schema-lint」）时误报 FAIL。
修正为双向：`dname == name or name in dname or dname in msg`，或 message 中存在长度 ≥ min(8, len(dname)) 的连续子串命中 dname。
实跑验证：0bb55ce（message 含完整短名）PASS；短称场景由正则 `[\w][\w.-]{7,}` 提取候选片段兜底。

## X5 数字层独立重算
正样例 3/3 PASS exit 0（16b063f / 0bb55ce / 9f48d94）；负样例 2/2 FAIL exit 1（f8acff9 (a)+(c)×2 / cc168bd (b)+(c)×2）；
exit 2 路径：不存在 commit / 无 queue diff 的 commit（如 d42fed8 纯工件 commit）实测 exit 2。全部分支可达。