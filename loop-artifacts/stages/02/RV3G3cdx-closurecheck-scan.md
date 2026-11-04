# 02 — RV3G3cdx-closure-checklist-assert · 现状扫描

> goal: 收口 commit 的 queue diff 机判门禁 · 分支 ralph/rv3g3cdx-closure-checklist-assert · 2026-10-30
> 方法：盘点历史收口 commit 的 message 措辞模式 + queue diff 形态，确定关键词集与解析规则。

## S1 — message 措辞模式（近 20 轮收口 commit 实读）

| 动作 | 实际措辞样本 | 关键词集（预注册） |
|------|-------------|-------------------|
| 划掉/完成声称 | 「queue 划掉」（404ba7e/c0eba3b）、「核销轮…checkbox 漏翻」（9f48d94）、「收口 — queue L28 [ ]→[x]」（16b063f） | `划掉` / `标记完成` / `核销` / `[ ]→[x]` / `[x]`（出现在「L\d+」语境）——取并集，任一命中即触发 (a) |
| 追加候选声称 | 「新导出候选 X」「追加候选 X」「导出候选 ×N 见下」 | `新导出候选` / `追加候选` / `导出候选` —— 触发 (b)，X = 紧随其后的短名（`RV\w[\w-]*` 或 `R5\.\w[\w.-]*` 正则提取） |

**措辞多样性风险实证**：9f48d94 的 message 不含「划掉」二字（用「核销轮…补翻」表述）——若关键词集只有「划掉」会漏触发 (a)。处置：关键词集取上表并集；仍为纯字符串匹配（失败降级第 1 条口径）。

## S2 — queue diff 形态枚举（git show 实跑）

三种合法形态（全部有真实实例）：
1. **既有行翻转**：`- [ ] <goal>…` + `+ [x] <goal>…`（同行改写，c0eba3b/9f48d94/16b063f）
2. **首建即 [x]**：仅 `+ [x] <goal>…`，无对应 `-` 行，且该 goal 在 `<h>~1` 版本中不存在（404ba7e evidence-audit 行——豁免子句对象）
3. **候选追加**：`+ [ ] <new-goal> | …`（新行，状态位 `[ ]`，404ba7e erratum-27 / c0eba3b u1k1+recalibrate / 9f48d94 schema-lint+sweep）

注意形态 2 与形态 3 在 diff 层面都是「纯插入行」，区分靠**状态位**（`[x]` vs `[ ]`）+ **是否为目标 goal 本身**。

## S3 — 三项检查的机判规则定稿（供 03/04 实现）

- **(a)** 触发 = message 含划掉类关键词；通过条件 = diff 中存在目标 goal 行的 `[ ]`→`[x]` 翻转（形态 1）**或** 豁免（`git show <h>~1:tasks/goal-queue.md | grep -c <短名>` = 0 且 diff 含 `+ [x] <短名>` 行，形态 2）。两者皆否 → FAIL(a)。
- **(b)** 触发 = message 含追加类关键词；对每个提取出的候选短名 X：diff 的 `+` 行中含 X ⇒ PASS，否则 FAIL(b,X)。
- **(c)** 双向闭合：diff 中每个含 checkbox 的行变更（`^[+-] \[[ x~]\]`），其 goal 短名必须出现在 message 中（短名或其前缀 ≥8 字符）。防「diff 动了某行但 message 只字未提」。
- exit 2 态：commit hash 无效 / `git show <h> -- tasks/goal-queue.md` 无 diff（非 queue 收口 commit）。

## S4 — 正/负样例选择（供 04 实跑）

- 正样例 ×3：**404ba7e**（形态 2 豁免 + 形态 3 追加）、**9f48d94**（形态 1 翻转 + 形态 3 双追加 + message 无「划掉」字样走「核销」关键词）、**c0eba3b**（形态 1 + 形态 3 双追加，message 含「queue 划掉」）。
- 负样例 ×2（构造性，临时 commit 不入 main）：N1 = message 声称「划掉」但 diff 无翻转（97d2adf 型复刻）；N2 = message 声称「追加候选 XXX-nonexistent」但 diff 无该行。构造方式 = 在临时分支造两个合成 commit 后回滚（不污染 main 历史）。
- 异常态 ×2：不存在 hash → exit 2；选一个无 queue diff 的 commit（如 d626088 阶段 commit）→ exit 2。