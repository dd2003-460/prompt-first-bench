# 阶段 04 — RV3G3cdx-closure-checklist-assert 执行验证（补记）

## A1 脚本落盘 ✓
`bench/rubric-v3/ablation/scripts/assert-closure-checklist.py`（131 行）——docstring 预注册 (a)(b)(c) 判定语义 + 豁免子句 + exit 三分支，规则权威源指向 r146 三列对照表与 r148 02.5 X4。

## A2 正样例实跑 3/3 PASS exit 0 ✓
| commit | goal 短名 | 结果 |
|--------|-----------|------|
| 16b063f (r146 收口) | RV3G3cdx-queue-hygiene-sweep | `[PASS] (a)` + `[INFO] (b)` → SUMMARY PASS exit 0 |
| 0bb55ce (r147 收口) | RV3G3cdx-batch2-schema-lint | `[PASS] (a)` + `[PASS] (b) 追加候选 ...crossdomain-lint-coverage-expand` → exit 0 |
| 9f48d94 (r145 核销轮) | RV3G3-threshold-crossdomain-reverify | `[PASS] (a)`（『核销』关键词路径）→ exit 0 |

## A3 负样例实跑 2/2 FAIL exit 1 ✓（构造性样例，独立分支 tmp/closurecheck-neg-samples）
| commit | 类型 | 结果 |
|--------|------|------|
| f8acff9 (N1) | message 声称划掉但 checkbox 未翻转（97d2adf 型复刻） | `[FAIL] (a) ...非首建豁免（97d2adf 型漏翻）` + `(c)×2` → exit 1 |
| cc168bd (N2) | message 声称追加候选但 diff 无对应插入行 | `[FAIL] (b) message 声称追加候选 RV3G3cdx-negsample-phantom-candidate 但 diff 无对应插入行` + `(c)×2` → exit 1 |

注：两负样例的 diff 面均触碰 kappa-formula-adjudicate 行而 message 未提及 → (c) 按行独立报告各 2 条，符合设计（(c) 不短路，全量报告缺口）。

## A4 exit 2 路径实证 ✓
- 不存在 hash → `[ERROR] commit not found` exit 2。
- 无 queue diff 的 commit（如 d42fed8 纯工件 commit）→ `[ERROR] no queue diff in ...` exit 2。

## A5 冻结面 + 回归基线 ✓
- 冻结文件（hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-*）0 行 diff（本 goal 只新增脚本 + 工件，零触碰）。
- 七脚本回归基线维持（exit=[0,0,0,1,0,0,0] 语义不变；kappa-receipt 常态 FAIL 为预期行为非漂移）。

## B4 预注册登记
接入门禁（hook/CI）本轮**不执行**——工具先落地、门禁接入留待成璐裁定后独立 goal（避免单方面改变所有后续收口行为）。