# 04 — RV3G3-threshold-crossdomain-reverify 核销轮 · 执行验证

> goal: queue 队列卫生修复 + 核销验证 · 分支 ralph/rv3g3-threshold-crossdomain-reverify-close · 2026-10-30
> 输入：03 动作表 A1-A5。本文件 = A1-A5 逐项验收记录。全部实跑从仓库根执行（脚本用 CWD 相对路径）。

## A1 — 回归基线实跑 ✅（7/7 与 X3 预期一致）

| 脚本 | exit | 关键输出 | X3 预期 | 判定 |
|------|------|----------|---------|------|
| assert-goldrank-crossdomain.py | 0 | `[SIGNAL] blocked-on-external: batch2 data absent (等 batch2 数据落盘 bench/rubric-v3/ablation/batch2/ 后零改动接入)` + `[INFO] 预注册锚点: S1=['W3-new', 'W3-orig', 'W4-orig'], T_PASS=4, GOLD_DOMAIN1=['N-2.1', 'N-3.2.2', 'N-2', 'N-4', 'N-1.3']` | 同左 | ✅ 逐字一致 |
| assert-o3-claim-list.py | 0 | `=== 4/4 检查组 PASS · 0 明细项 FAIL ===` | 同左 | ✅ |
| assert-gmr-recompute.py | 0 | `=== 11 PASS / 0 FAIL ===` | 同左 | ✅ |
| assert-kappa-receipt.py | 1 | `RESULT: FAIL (1 checks failed)` | 同左（常态——kappa-receipt.json 不存在，不伪造转绿） | ✅ |
| assert-o3-claim-rejudge.py | 0 | `[SIGNAL] blocked-on-external: rejudge-results.json absent (…)` | 同左 | ✅ |
| assert-goldrank-threshold.py | 0 | `SUMMARY: 31 PASS / 0 FAIL` | 同左 | ✅ |
| assert-w3w4-recompute.py | 0 | `SIGNAL: W0-W4 × 8 run 合计 0 mismatch` | 同左 | ✅ |

失败降级触发条件（crossdomain 输出偏离预注册语义）**未触发**。

## A2 — crossdomain 输出 byte-exact 复核 ✅

`od -c` 全量捕获：stdout 恰两行，第二行以 `]\n` 结尾（offset 0000377），无 stderr 混入、无尾随空白。与 X3 第一行及 02 阶段首次实跑逐字节相等（同一脚本同一输入面，两次独立运行输出稳定）。

## A3 — queue L28 checkbox 翻转 ✅

`tasks/goal-queue.md` L28：`- [ ]` → `- [x]`，注记头扩为 `(2026-10-30, r140: f8c096b, ralph/rv3g3-threshold-crossdomain-reverify；r145 核销轮补翻——97d2adf 收口 message 声称「queue 划掉」但 checkbox 漏翻，本轮补核销 + 基线复验零漂移)`。**结果** 注记主体零改动（diff 面 = 该行前缀一处替换）。A4 新候选两条追加于 kappa-formula-adjudicate 条目之后（新导出候选区）：RV3G3cdx-batch2-schema-lint + RV3G3cdx-queue-hygiene-sweep。

## A4 — 新导出候选 ✅（2 条 ≥ 1）

见上。两条均纯仓库内可执行、带产投比依据与工作量估算。

## A5 — 冻结面终验 ✅

`git diff main --stat`（十件冻结文件：hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-run1..8.md）= **0 行**。
全仓改动面 = `tasks/current-goal.md`（重写为本 goal）+ `tasks/goal-queue.md`（L28 翻转 + 2 候选追加）+ `loop-artifacts/stages/{02,02.5,03}/RV3G3cdx-*`（新增）+ 本文件（新增）。**无任何冻结件/脚本/既有 queue 行状态位被触碰**（batch2-arrival-closure 保持 `[ ]` 不变）。✅

## 验收标准对照（current-goal【验收标准】逐项）

- [x] queue L28 翻转 + 日期 + 核销注记（A3）
- [x] 验证增量 ≥3 项实跑留痕：(a) crossdomain SIGNAL exit 0 byte-exact（A1/A2）；(b) 冻结面 0 行 diff（A5）；(c) 七脚本回归基线全一致（A1）
- [x] 新导出候选 ≥1（A4：2 条）
- [x] 冻结件零修改（A5）
- [ ] 04.5 verdict pass（下一阶段）