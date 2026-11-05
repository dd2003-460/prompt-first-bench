# 02 — RV3G3cdx-queue-hygiene-sweep · 扫描执行（收口 commit 枚举 + 逐条 queue diff + 三列对照）

> goal: queue 卫生例行扫描（近 20 轮收口 commit 的 message↔状态位一致性抽查）· 分支 ralph/rv3g3cdx-queue-hygiene-sweep · 2026-10-30
> 范围上限（current-goal 预注册）：**近 20 轮收口 commit 对应的 queue 行**，非全量历史。
> 方法：全部结论带 commit hash + `git show <h> -- tasks/goal-queue.md` 证据；当前状态位 = main@8fadb56 实读。

## S1 — 窗口定义与收口 commit 枚举

窗口 = `git log --oneline -60` 中位置 1..60（HEAD=8fadb56 起），覆盖 r126→r146 共 21 个轮次标签（r146/r145/r144/r143/r142/r141/r140/r139/r138+/r138/r137b/r137/r136b/r136/r135b/r135/r134b/r134/r133/r132c/r132b/r132/r131b/r131/r130b/r130/r129/r128/r127/r126）。

「收口 commit」判定口径（预注册）：message 含「收口」「goal-queue 收口」或为 merge 收口，且实际改动 `tasks/goal-queue.md`。枚举结果 = **15 个**（下表 A1-A15）。

排除项及理由（逐一登记，防「漏检」质疑）：
- 阶段 commit（01/02/02.5+03/04/04.5 类）：不声称 queue 动作，不在抽查对象内（其 queue 影响由对应收口 commit 覆盖）。
- `798c0b5 keepalive`：无 queue 改动（--stat 实证 0 文件触碰 queue）。
- `187b938 r132c` / `c55848f r133`：工作 commit，queue 收口分别归入 r132b(046874b) / r137b(52f70d8)。
- `0fedf42 (r130)`：prior-source 交付 commit，队列收口归入 r135b(dfed498)（核销轮先例）。
- `96a89e7 Merge r140`：merge commit，queue diff 已由 97d2adf 承载（merge 本身不改 queue——`git show 96a89e7 -- tasks/goal-queue.md` 空）。
- `2c394cf` / `3c119c2`（Merge r127/r126）：同理，queue 收口归入 6e94b4b(r128)。
- `9f48d94`(r145 阶段 02-04) / `28f0551`(r145 阶段 04.5)：r145 核销轮的阶段 commit，但**实际改动了 queue**（A3 补翻 + 候选追加 + 范围上限修订）→ 按「实际改动 queue」口径纳入抽查（A15/A16），message 对 queue 动作有明确声称，属本缺陷类的直接检验对象。

### 枚举表（15 + 2 = 17 行抽查对象）

| # | hash | 轮次 | message 摘要（queue 相关部分） | queue diff 面 |
|---|------|------|------------------------------|--------------|
| A1 | 6e94b4b | r128 | 「RV3B1-webllm-tool-fix 标记完成 (r126+r127)」 | 1+/1- |
| A2 | 3688cda | r129 | 「RV3B1-prompt-side-freeze 标记完成 (68c2435) + receipt-per-goal 确认」 | 2+/2- |
| A3 | 5967c8e | r130b | 「R5.2audit-C4-timing-reconstruct 标记完成 (dcdd7d8) + 追加导出候选 C4-arena-export / C4-assert-hardening」 | 3+/1- |
| A4 | d17a483 | r131b | 「R5.2audit-signal-counter 标记完成 (af8e15d) + 追加导出候选 verdict-text-templatize」 | 2+/1- |
| A5 | 046874b | r132b | 「R5.2audit-C4-assert-hardening 标记完成 (8b2cc11) + 追加导出候选 docsync」 | 2+/1- |
| A6 | 5fa2508 | r134b | 「R5.2audit-verdict-text-templatize 标记完成 (6c18bc2)」 | 1+/1- |
| A7 | dfed498 | r135b | 「RV3G4-prior-source-assert 标记完成 (d5899f4, 核销轮)」 | 1+/1- |
| A8 | 19b9ffb | r136b | 「RV3G4-kappa-receipt-assert 标记完成 (26710e7) + 追加导出候选 kappa-gate-execution」 | 2+/1- |
| A9 | 52f70d8 | r137b | 「R5.2assert-suite-docsync 标记完成 (c8963c6)…本轮 = 核销验证 + 队列卫生修复」 | 1+/1- |
| A10 | 446f4cc | r138+ | 「RV3G3-goldrank-threshold-proof 标记完成 (862741b) + 新导出候选 RV3G3-threshold-crossdomain-reverify」 | 2+/1- |
| A11 | 74e3046 | r139 | 「RV3B1-jaccard-adjudicate 材料收口…queue 转『材料已备，待成璐裁定』（不划掉）」 | 1+/1- |
| A12 | 91117b8 | r141 | 「RV3G6-o3-claim-rejudge-scaffold 收口…queue 更新（RV3G6-o3-claim-rejudge 转 [~]…+ 新导出候选 RV3G6-kappa-formula-adjudicate）」 | 3+/2- |
| A13 | 404ba7e | r142 | 「RV3G6-o3-claim-rejudge-evidence-audit 收口 — queue 划掉 + 结果注记 + 新导出勘误候选 RV3G6-o3-claim-list-erratum-27」 | 2+/0- |
| A14 | 93a899b | r144 | 「RV3G6-o3-claim-list-erratum-27 收口 — 勘误备料落盘…待成璐裁定不代裁」 | 1+/1- |
| A15 | c0eba3b | r143 | 「RV3G6-kappa-formula-adjudicate 收口 — queue 划掉 + 结果注记 + 新导出候选 ×2」 | 3+/1- |
| A16 | 9f48d94 | r145 | 「…A3 queue L28 [ ]→[x] 补翻 + 核销注记 / A4 新候选 ×2：batch2-schema-lint + queue-hygiene-sweep…」 | 3+/1- |
| A17 | 28f0551 | r145 | 「…攻击 6『sweep 候选无终止条件』已修 = queue 候选补范围上限近 20 轮收口行…」 | 1+/1- |

注：A13/A14/A15 的 git 时间序为 404ba7e(r142) → 93a899b(r144) → c0eba3b(r143)，轮次标签与提交序不一致（r143/r144 两 goal 并行推进、先后交叠）——不影响逐行核对，仅登记防误读。

## S2 — 三列对照表（message 声称 / 实际 diff / 当前状态位）

每格证据 = `git show <hash> -- tasks/goal-queue.md` 提取行（前缀 `-`/`+` 为删除/插入）+ main@8fadb56 行号实读。

| # | hash | 目标行 | message 声称 | 实际 diff（git 证据） | 当前状态位（main@8fadb56） | 判定 |
|---|------|--------|-------------|----------------------|---------------------------|------|
| A1 | 6e94b4b | RV3B1-webllm-tool-fix | 标记完成 | `- [ ]` → `+ [x] …(r126: d8c307a + 补件 r127: 94f285b…)` | L53 `[x]` | ✓ 一致 |
| A2 | 3688cda | RV3B1-prompt-side-freeze | 标记完成 | `- [ ]` → `+ [x] …(r129: 68c2435…)` | L50 `[x]` | ✓ 一致 |
| A2' | 3688cda | RV3B1-webllm-receipt-per-goal | receipt-per-goal 确认 | `- [ ]` → `+ [x] …(r129 前置执行)…` | L52 `[x]` | ✓ 一致 |
| A3 | 5967c8e | R5.2audit-C4-timing-reconstruct | 标记完成 | `- [ ]` → `+ [x] …(r130: dcdd7d8…)` | L38 `[x]` | ✓ 一致 |
| A3' | 5967c8e | R5.2audit-C4-arena-export / C4-assert-hardening | 追加导出候选 ×2 | `+ [ ]`×2 完整条目 | L35 `[ ]` / L36 `[ ]` | ✓ 一致（C4-assert-hardening 后续被 A5 收口，见下） |
| A4 | d17a483 | R5.2audit-signal-counter | 标记完成 | `- [ ]` → `+ [x] …(r131: af8e15d…)` | L39 `[x]` | ✓ 一致 |
| A4' | d17a483 | R5.2audit-verdict-text-templatize | 追加导出候选 | `+ [ ]` 完整条目 | L33 `[x]`（后续被 A6 收口） | ✓ 一致（时序性，非异常） |
| A5 | 046874b | R5.2audit-C4-assert-hardening | 标记完成 | `- [ ]` → `+ [x] …(r132: 8b2cc11…)` | L36 `[x]` | ✓ 一致 |
| A5' | 046874b | R5.2assert-suite-docsync | 追加导出候选 docsync | `+ [ ]` 完整条目 | L32 `[x]`（后续被 A9 收口） | ✓ 一致（时序性，非异常） |
| A6 | 5fa2508 | R5.2audit-verdict-text-templatize | 标记完成 | `- [ ]` → `+ [x] …(r134: 6c18bc2…)` | L33 `[x]` | ✓ 一致 |
| A7 | dfed498 | RV3G4-prior-source-assert | 标记完成（核销轮） | `- [ ]` → `+ [x] …(r135: d5899f4…)` | L42 `[x]` | ✓ 一致 |
| A8 | 19b9ffb | RV3G4-kappa-receipt-assert | 标记完成 | `- [ ]` → `+ [x] …(r136: 26710e7…)` | L43 `[x]` | ✓ 一致 |
| A8' | 19b9ffb | RV3G4-kappa-gate-execution | 追加导出候选 | `+ [ ]` 完整条目 | L31 `[ ]`（blocked-on-external，未启动） | ✓ 一致 |
| A9 | 52f70d8 | R5.2assert-suite-docsync | 标记完成（核销+队列卫生修复） | `- [ ]` → `+ [x] …(r137: c8963c6…)` | L32 `[x]` | ✓ 一致 |
| A10 | 446f4cc | RV3G3-goldrank-threshold-proof | 标记完成 | `- [ ]` → `+ [x] …(r138+: 862741b…)` | L41 `[x]` | ✓ 一致 |
| A10' | 446f4cc | RV3G3-threshold-crossdomain-reverify | 新导出候选 | `+ [ ]` 初始条目 | L30 `[x]`（经 97d2adf 写结果注记 + 9f48d94 补翻，见 D1/D2） | ✓ 终态一致（过程异常已登记 D1） |
| A11 | 74e3046 | RV3B1-jaccard-adjudicate | 转「材料已备，待成璐裁定」（**不划掉**） | `- [ ]` → `+ [~]`（checkbox 位翻转 [ ]→[~]，正文追加材料注记） | L49 `[~]` | ✓ 一致（message 明言不划掉，[~] 即预期终态） |
| A12 | 91117b8 | RV3G6-o3-claim-rejudge | 转 [~] | `- [ ]` → `+ [~]`（正文追加骨架完成注记） | L48 `[~]` | ✓ 一致 |
| A12' | 91117b8 | RV3G6-kappa-formula-adjudicate | 新导出候选 | `+ [ ]` 完整条目 | L26 `[x]`（后续被 A15 收口） | ✓ 一致（时序性，非异常） |
| A13 | 404ba7e | RV3G6-o3-claim-rejudge-evidence-audit | queue 划掉 + 结果注记 | `+ [x]` 完整条目（首次以 [x] 形态写入，含结果注记；diff 面 2+/0-，无删除行） | L16 `[x]` | ✓ 一致（该行此前不存在于 queue，「划掉」语义 = 以 [x] 形态建档，无 checkbox 漏翻空间） |
| A13' | 404ba7e | RV3G6-o3-claim-list-erratum-27 | 新导出勘误候选 | `+ [ ]` 完整条目 | L25 `[~]`（后续被 A14 转 [~]） | ✓ 一致（时序性，非异常） |
| A14 | 93a899b | RV3G6-o3-claim-list-erratum-27 | 收口（备料落盘，**待成璐裁定不代裁**） | `- [ ]` → `+ [~]`（正文追加「材料已备，待成璐裁定…不划掉」注记） | L25 `[~]` | ✓ 一致（message 明言不代裁，[~] 即预期终态） |
| A15 | c0eba3b | RV3G6-kappa-formula-adjudicate | queue 划掉 + 结果注记 | `- [ ]` → `+ [x] …(r143: 3251510…)` | L26 `[x]` | ✓ 一致 |
| A15' | c0eba3b | RV3G6-kappa-u1k1-execution / threshold-recalibrate | 新导出候选 ×2 | `+ [ ]`×2 完整条目 | L23 `[ ]` / L24 `[ ]`（均 blocked-on-human，未启动） | ✓ 一致 |
| A16 | 9f48d94 | RV3G3-threshold-crossdomain-reverify | A3 queue L28 [ ]→[x] 补翻 + 核销注记 | `- [ ]` → `+ [x]`（正文追加「r145 核销轮补翻」注记） | L30 `[x]` | ✓ 一致（修复动作本身正确） |
| A16' | 9f48d94 | RV3G3cdx-batch2-schema-lint / queue-hygiene-sweep | A4 新候选 ×2 | `+ [ ]`×2 完整条目 | L27 `[ ]` / L28 `[ ]` | ✓ 一致（L28 = 本 goal，收口时翻 [x]） |
| A17 | 28f0551 | RV3G3cdx-queue-hygiene-sweep | 攻击 6 处置 = 候选补范围上限 | `- [ ]`（旧文案「全部 [x]/[~] 行」）→ `+ [ ]`（新文案「近 20 轮收口 commit 对应的 queue 行」） | L28 `[ ]`（文案已含范围上限） | ✓ 一致（checkbox 位不变，正文修订与 message 声称吻合） |

## S3 — 缺陷实例锚点复核（97d2adf，预期 = 已修复项出现在表中）

`git show 97d2adf -- tasks/goal-queue.md` = **2 insertions / 1 deletion**（--stat 实证）：
- 插入 L23 新候选 `RV3G3-batch2-arrival-closure`（完整条目）；
- 原 crossdomain 行改写：追加完整**结果**注记（A3/M0/M1-M4/SIGNAL 常态/冻结面/04.5/N3 全量）；
- **行首 checkbox 仍 `[ ]`**（`git show 97d2adf:tasks/goal-queue.md` L23 实证 `- [ ] RV3G3-threshold-crossdomain-reverify (2026-10-30, r140: f8c096b, …)`）。

message 声称「queue 划掉」vs 实际未翻 = **D1 型缺陷（message↔状态位矛盾）**，跨 r141-r144 四轮无人发现（r141 91117b8 / r142 404ba7e / r144 93a899b / r143 c0eba3b 四 commit 的 queue diff 均未触碰该行——S2 各行 diff 实证）。**r145/9f48d94 已修复**（A16 行：[ ]→[x] + 核销注记），当前 main L30 = `[x]`。✅ 按 current-goal 预注册，作为「已修复项」出现于对照表。

## S4 — 异常清单

| 编号 | 类型 | 对象 | 状态 |
|------|------|------|------|
| D1 | message↔状态位矛盾（漏翻） | 97d2adf / RV3G3-threshold-crossdomain-reverify | **已修复**（r145/9f48d94，A16 行实证） |
| D2 | 同 D1 的下游效应：r141-r144 四轮未察觉 | 同上 | 随 D1 修复闭环；复发路径封死 = 本 goal（S2 全量对照 + 04 回归 spot check） |

**零新增未修复异常。** 17 行抽查对象（15 收口 commit + 2 个 r145 阶段 commit）中，除 D1（已修复）外全部 ✓ 一致。

## S5 — 负面结果声明

无漏检方向遗漏需声明。两点如实登记（非异常）：
1. A13（404ba7e）的「queue 划掉」针对的是**首次建档即 [x]** 的行：`git show 404ba7e~1:tasks/goal-queue.md | grep -c evidence-audit` = **0**（该行在收口 commit 之前不存在于 queue，系 r142 轮内新导出并直接以 `[x]` 形态建档），故不存在可漏翻的 checkbox 位；message 措辞与实际动作语义兼容。
2. A11/A14 两个 `[~]` 行的 message 均明言「不划掉」——[~] 是设计内终态（待成璐裁定），不计为异常。