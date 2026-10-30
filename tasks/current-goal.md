# Goal: RV3G6-audit8-erratum — AUDIT-report §8 参考值表绝对值勘误

> 创建：2026-10-30 · ralph loop runner（queue 队首）
> 依据：`tasks/goal-queue.md` 候选条目 + `bench/rubric-v3/gmr-criterion-freeze.md` §4.1（r118 复算发现绝对值偏差，登记「后续 goal 可发 AUDIT-report erratum」）

## 【目标】
对 `bench/rubric-v3/AUDIT-report.md` 发正式 erratum，消除与 `gmr-criterion-freeze.md` §5 权威参考值表的**双源困惑**：
1. **§8 精确参考值表（L261-271）**：基于 freeze doc §5 复算值修正绝对值——W1 [2.60,6.40]→[8.60,12.40] / W2-orig [7.80,8.00]→[8.20,8.40] / W2-new [5.20,6.60]→[8.80,10.20] / W3-new/W4-new [6.80,7.00]→[7.40,7.60]；W3-orig/W4-orig = 5.40 两源一致不动。tie 组结构列保留（freeze doc §4.1 判定结构一致）。
2. **§3.2 L109 错误结论句**：「换一个合法 tie-break，W1 的最优值（2.60, 0-based）可优于 W3-orig（5.40, 0-based）」在正确值下不成立（W1 最优 8.60 > 5.40）→ 改写为正确表述（换任何合法 tie-break，W1 最优值 8.60 仍劣于 W3-orig 的 tie-robust 单值 5.40）。
3. **同文件其他引用同一错误绝对值的位置同步修正**（防修一处留双源）：L108 范围句、L172 finding #11 区间、L252 §8 规则 1 引用模板值、L109 落盘顺序值（W1=9.8/W2=8.2/new 侧 W2=7.6/W3=W4=7.6 → 按 freeze doc §5 id-order 值 10.20/8.20/9.80/7.60 修正）。
4. **byte-exact 条款处置**：AUDIT §8 原文被 freeze doc §4 逐字抄录为判据冻结件的强制条款。本 erratum 修改 AUDIT 后，freeze doc §4 的 byte-exact 声明失效 → 同步更新 freeze doc §4（重抄录 + 标注「erratum 后版本」），保持单一事实源。
5. 新增机判断言脚本校验 AUDIT 修正后的数值与 freeze doc §5 一致（防未来再漂移）。

## 【阶段】
rubric-v3 审计链文档一致性环。纯仓库内文本修订 + 机判脚本，不改任何冻结数据（prior-estimates.json / judge-blindtest-r1.json / hit-matrix.json 只读）。工作量极小（queue 描述：改两处数值+一行措辞——实际盘点后扩为 AUDIT 5 处 + freeze doc §4 重抄录，见 01 工件）。

## 【SOP 索引】
- `sop/arena-loop-pipeline.md`（唯一 SOP 入口）
- `loop/prompt-first/00..04.5`（六阶段定义）
- `bench/rubric-v3/AUDIT-report.md`（修订对象）
- `bench/rubric-v3/gmr-criterion-freeze.md`（权威参考值源 §5 + byte-exact 条款 §4，同步更新对象）
- `bench/rubric-v3/ablation/scripts/assert-gmr-recompute.py`（既有复算脚本，erratum 数值与其 expected 表同源）

## 【验收标准】
- [ ] AUDIT-report.md 中全部 gmr 绝对值与 freeze doc §5 一致（assert 脚本机判 exit 0）
- [ ] L109 错误结论句改写为正确表述（8.60 仍劣于 5.40），且不再含「W1 可优于 W3-orig」语义
- [ ] freeze doc §4 byte-exact 块更新为 erratum 后 AUDIT §8 原文 + 状态标注（单一事实源维持）
- [ ] 新增 assert 脚本（AUDIT 数值 ↔ freeze doc §5 一致性）exit 0，含变异测试确认检查实义生效
- [ ] 定性结论零改动：W3/W4-orig 最优且 tie-robust / W1 最差且 tie-sensitive / 跨方案排序方向不变（grep 复核）
- [ ] 冻结数据零修改（git status 验证 prior-estimates/judge-blindtest/hit-matrix/stats-* 无 diff）
- [ ] 04.5 反方复核 verdict pass

## 【失败降级】
- freeze doc §4 重抄录引入新矛盾 → 以 AUDIT erratum 后文本为准重抄一次；仍不一致则登记 APPROVALS 不阻塞
- 发现 queue 描述未覆盖的其他错误数值位置 → 一并修正并登记（erratum 完整性优先于最小 diff，但每处修正必须带 freeze doc §5 或 assert-gmr-recompute.py 的 evidence）
- web-llm 回执沿用 per-goal 分文件约定（RV3B1-webllm-receipt-per-goal 候选的前置执行，避免再次覆写 batch1/o3cl 回执）