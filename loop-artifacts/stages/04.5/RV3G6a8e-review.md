# 04.5 Adversarial Review — RV3G6-audit8-erratum（AUDIT-report §8 参考值表绝对值勘误）

> 复核：2026-10-30 · ralph loop runner（Hermes 收口侧，对抗性攻击模式）
> 对象：`bench/rubric-v3/AUDIT-report.md` erratum + `gmr-criterion-freeze.md` §4/§4.1 同步更新 + `assert-audit8-erratum.py`

## 攻击清单与结果

### A1. Erratum 节自引旧值是否污染黑名单检查？

**攻击**：Erratum 节修正清单表内引用了原错误值（[2.60, 6.40] 等）作溯源——如果 assert 脚本的黑名单扫描覆盖全文，要么误报 FAIL，要么说明脚本有豁免逻辑、豁免范围可能被滥用。

**验证**：脚本 ② 用 `audit.split("## Erratum（2026-10-30")[0]` 只扫正文区（Erratum 节之前），Erratum 节内的溯源引用被排除。实跑 6/6 零命中 PASS。豁免边界 = Erratum 节标题起点，精确且不可绕过（在正文区插入旧值仍会 FAIL——变异测试已证明）。

**结论**：✅ 通过。豁免设计合理，溯源引用不影响防漂移效力。

### A2. E2 落盘顺序值「W2-new=9.8」是否与 freeze doc §5 一致？

**攻击**：E2 声称 new 侧 W2 从 7.6 改为 9.8，但 Erratum 节同时说「W3=W4-new=7.6 经复算正确，保留」。若 W2-new 的 id-order 值真是 9.8，而 W2-new 的范围是 [8.80, 10.20]，9.8 落在范围内 ✓；但需确认 freeze doc §5 的 id-order 值表是否也写 9.8（双源一致性不能只靠 assert 脚本的定点 token 断言——它只查 AUDIT 单侧）。

**验证**：grep freeze doc §5 参考值表：W2-new id-order = 9.80 ✓（与 AUDIT 修正后 9.8 一致，格式差异 9.8 vs 9.80 为数值等价）。W1 id-order 两侧均 10.20 ✓。W2-orig = 8.20 ✓。W3/W4-new = 7.60 ✓。

**结论**：✅ 通过。双源数值一致（数值等价口径下）。

### A3. byte-exact 重抄录是否引入新偏差？

**攻击**：freeze doc §4 块被整体替换为 erratum 后文本——如果替换时手抖改了任何字符（哪怕一个空格），byte-exact 声明就是假的。

**验证**：assert 脚本 ③ 做 `freeze_block == audit_s8` 全串比对（BEGIN 注释行剥除后），实跑 PASS（diff 空）。这是字节级机判，不依赖人工核对。另注：修复前 ③ 恒 FAIL（block_len=1311 vs audit_len=1233，差 78 字符 = BEGIN 注释行长度），修复后相等——恰好证明比对逻辑现在真的在比内容而非恒真。

**结论**：✅ 通过。byte-exact 由机判背书，且修复过程本身验证了比对逻辑非恒真。

### A4. 「定性结论不变」声明是否成立？

**攻击**：Erratum 声称定性结论全部维持且更强。但 E3 把「可优于」改成「仍劣于」——这改变了预注册 tie-break 的价值论证（从「防可反转比较」转为「保证跨文档可比 + 消除 post-hoc 空间」）。如果下游文档（DRAFT v2 O3 / gmr-tiebreak-prereg 冻结件 §1）引用了旧论证句，会产生新的双源。

**验证**：grep DRAFT-rubric-v3.md 与 gmr-criterion-freeze.md 中「可优于」「post-hoc」相关表述：freeze doc §1.2 拒绝表论证的是「为何选 id 字典序」（确定性 + 可机判），不依赖「W1 可反超」前提；DRAFT v2 O3 消融证据段（r72 写入）只引用排序方向与构念效度计数，未引用 L109 论证句。无下游引用旧论证句。

**结论**：✅ 通过。论证句改写是局部加强，无下游双源。

### A5. U3 未并入项是否留了尾巴？

**攻击**：Erratum 节把「gmr 6.4→8.6 口径归属」挂起为 U3 导出 queue——如果不入队，这个已知疑点就悬空了。

**验证**：tasks/goal-queue.md 本轮更新中追加候选 `RV3G6-gmr-caliber-u3`（U3 口径裁定：对照 G3 原始计算工件裁定「6.4→8.6」属 global gmr 还是 per-run/历史舍入口径）。已入队 ✓。

**结论**：✅ 通过。U3 有明确归宿，不悬空。

### A6. 断言脚本自身是否可信？

**攻击**：脚本是 claude 初写、Hermes 修补的——修补本身可能引入 bug（比如 re.sub 剥注释行的正则太宽，把 §8 正文也剥了导致假 PASS）。

**验证**：re.sub 模式 `^<!-- BEGIN BYTE-EXACT QUOTE:[^\n]*\n` 锚定行首且只匹配一行（`[^\\n]*` 不含换行），不可能波及后续正文。变异测试（A6 附带）：改回旧值 → exit 1 且恰好 2 处 FAIL（① E1a + ② 黑名单），恢复 → exit 0。脚本对目标变异敏感、对无关区域无副作用。

**结论**：✅ 通过。脚本行为经变异测试实证。

## 总结

| # | 攻击 | 结果 |
|---|------|------|
| A1 | Erratum 自引旧值污染黑名单 | ✅ 通过（豁免边界精确，变异测试证明不可绕过） |
| A2 | E2 双源一致性 | ✅ 通过（freeze doc §5 ↔ AUDIT 数值等价一致） |
| A3 | byte-exact 重抄录偏差 | ✅ 通过（机判 diff 空 + 修复过程反证非恒真） |
| A4 | 定性结论不变声明 | ✅ 通过（无下游引用旧论证句） |
| A5 | U3 悬空 | ✅ 通过（已入队 RV3G6-gmr-caliber-u3） |
| A6 | 断言脚本自身可信度 | ✅ 通过（变异测试敏感 + 正则锚定安全） |

**6 项攻击全部失败。**

## verdict

**pass** — 6 项对抗性攻击全部未能证伪产出。erratum 数值与权威源一致、byte-exact 机判背书、定性结论无损、U3 有归宿、防漂移脚本经变异测试实证有效。本 goal 满足全部验收标准，可收口。