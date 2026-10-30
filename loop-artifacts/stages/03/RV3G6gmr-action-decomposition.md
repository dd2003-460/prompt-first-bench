# 阶段 03：行动分解 — RV3G6-gmr-tiebreak-prereg

> goal: gmr 主判据预注册冻结件 · 2026-10-30
> 上游：01（七节骨架 + 4 判断点）+ 02（复算结果 + AUDIT §8 偏差定位）+ 02.5（2 处修正 F1/F2）

## 行动清单

| # | 行动 | 输入 | 输出 | 验证方式 | 状态 |
|---|------|------|------|----------|------|
| A1 | 写 gmr-criterion-freeze.md §1（tie-break 规则文字化） | AUDIT §3.2 L100 + §8 规则 1/3 | 冻结件 §1 | grep「节点 ID 字典序」+ 拒绝表存在 | ✅ 完成 |
| A2 | 写 §2（阈值引用机制 + 锚点 + 门禁） | AUDIT §3.2 L100 定位声明 + G3 F3b | 冻结件 §2 | grep「threshold_top10 := RV3G3」+ 无硬编码数值 + 超几何三值 | ✅ 完成 |
| A3 | 写 §3（退出条件 checklist EC-1~EC-5） | AUDIT §3.3 L122 | 冻结件 §3 | 5 条 EC 各有触发条件+动作+机判方式；EC-3 = 4 方案 6 对（F1 已修） | ✅ 完成 |
| A4 | 写 §4（§8 byte-exact 抄录） | AUDIT-report.md L248-272 | 冻结件 §4 | python 字节比对（BEGIN/END marker 内内容 == AUDIT 原文） | ✅ 完成（BYTE-EXACT MATCH ✓） |
| A5 | 写 §4.1（复核发现：AUDIT §8 绝对值偏差） | 02 复算对比表 | 冻结件 §4.1 | 5 行对比表 + 判读段落 | ✅ 完成 |
| A6 | 写 §5（权威参考值表） | assert-gmr-recompute.py 输出 | 冻结件 §5 | 脚本 exit 0（11 PASS / 0 FAIL） | ✅ 完成 |
| A7 | 写 §6（DRAFT v2 一致性核对） | DRAFT-rubric-v3-v2.md L73/L77/L81 | 冻结件 §6 | 3 行对照表 + 「无矛盾」结论 | ✅ 完成 |
| A8 | 写 §7（冻结声明） | — | 冻结件 §7 | 5 条引用规则 + 修改流程 | ✅ 完成 |
| A9 | 写 assert-gmr-recompute.py | prior-estimates.json + judge-blindtest-r1.json | 脚本文件 | `python3 ... && echo $?` → 0 | ✅ 完成 |
| A10 | 应用 02.5 修正 F1（EC-3 7→4） | 02.5 crosscheck | 冻结件 §3 更新 | grep「4 个方案（W1/W2/W3/W4，共 6 对）」 | ✅ 完成 |
| A11 | 应用 02.5 修正 F2（§5 关键事实措辞） | 02.5 crosscheck | 冻结件 §5 更新 | grep「AUDIT 原文保留不动」 | ✅ 完成 |
| A12 | 冻结数据零修改验证 | git status | 确认 hit-matrix/prior-estimates/gold-tree/stats-*/runs-C0-* 不在变更列表 | `git status --short` 过滤 | ⏳ 待执行 |
| A13 | 04.5 反方复核 | 全部产出 | loop-artifacts/stages/04.5/ | verdict = pass | ⏳ 待执行 |
| A14 | commit + push + merge + queue 更新 | 全部文件 | main 分支更新 | ls-remote + git log | ⏳ 待执行 |

## 依赖关系

```
A1-A8, A9 → A10, A11（修正需先有文件）
A1-A11 → A12（冻结数据检查在全部写入后做）
A1-A12 → A13（04.5 审全部产出）
A13 → A14（verdict pass 才收口）
```

## 风险检查

| 风险 | 缓解 | 状态 |
|------|------|------|
| §8 byte-exact 抄录出错 | python 字节比对已做 ✓ | 已消 |
| gmr 复算公式错 | W3-orig=5.40 锚点验证 ✓ | 已消 |
| EC-3 方案数错 | 02.5 发现并修正（7→4）✓ | 已消 |
| 与 DRAFT v2 矛盾 | §6 逐行核对，无矛盾 ✓ | 已消 |
| 冻结数据被误改 | A12 git status 检查 | 待执行 |

## verdict

**pass** — 14 项行动中 11 项已完成（A1-A11），3 项待执行（A12-A14）且无阻塞依赖。进入 04。