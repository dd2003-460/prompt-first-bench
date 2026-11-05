# 04 — RV3G3cdx-batch2-schema-lint · 执行验证

> goal: batch2 schema lint 独立化 · 分支 ralph/rv3g3cdx-batch2-schema-lint · 2026-10-30
> 输入：03 A1-A5。本文件记录 A1-A4 实跑证据；A5（queue + 04.5）见收口 commit 与 stages/04.5/。

## A1 — `--lint-only [--dir]` 实现 ✅

改动面 = assert-goldrank-crossdomain.py 单文件：
- `load_batch2(base_dir=None)`：目录参数化，默认现 BATCH2 常量（无参路径零行为变化）。
- 新增 `lint_main(base_dir)`：复用同一检查链（8 个失败出口全部继承），逐文件 PASS/FAIL + 汇总行；目录不存在 → `[SIGNAL] lint: ... absent — 数据未落盘，无对象可校验（非错误）` exit 0；违例 → `[ERROR] lint FAIL (<dir>): <payload>` exit 2。
- `main()` 头部加 `--lint-only` 分支（支持 `--dir <path>` 与位置参数两种写法），其余逻辑原样。
- docstring 未动（schema 权威源保持单一）。

## A2 — 样例矩阵落盘 ✅（7 组 / 16 文件）

`bench/rubric-v3/ablation/batch2-lint-samples/`：pos-full（三文件齐）/ pos-no-blindtest（D5 变体）/ neg-missing-prior / neg-nodes-missing-w1 / neg-ptilde-key-absent / neg-hitmatrix-gold-absent / neg-blindtest-entry-missing-field。节点集 = 第一域 7 节点（含 5 gold），数值为合成占位（lint 不消费数值语义，只查结构）。

## A3 — 样例矩阵实跑 ✅（7/7 符合预期）

| 样例 | 预期 exit | 实跑 exit | 关键输出（指名道姓核验） | 判定 |
|------|----------|----------|--------------------------|------|
| pos-full | 0 | 0 | `[PASS] hit-matrix… / [PASS] prior… / [PASS] judge-blindtest…` + SUMMARY: lint PASS (3-file schema) | ✓ |
| pos-no-blindtest | 0 | 0 | `[INFO] judge-blindtest-batch2.json absent → D5 降级…（合法形态）` + SUMMARY PASS | ✓ |
| neg-missing-prior | 2 | 2 | `prior-estimates-batch2.json missing` | ✓ |
| neg-nodes-missing-w1 | 2 | 2 | `nodes.N-4: field 'w1' required` | ✓ |
| neg-ptilde-key-absent | 2 | 2 | `nodes.N-2: field 'p_tilde' required (null allowed)` | ✓ |
| neg-hitmatrix-gold-absent | 2 | 2 | `hit-matrix run-b2-1: gold node N-4 absent` | ✓ |
| neg-blindtest-entry-missing-field | 2 | 2 | `w3_full_ranking entry missing 'w3': {'node': 'N-3', …}` | ✓ |

另核「目录不存在」态：`--lint-only`（默认 dir）→ exit 0 + `[SIGNAL] lint: …/batch2 absent — 数据未落盘，无对象可校验（非错误）`——**非 crash、非误报违例**。✓

## A4 — 回归基线 ✅（byte-exact + 七脚本零漂移）

- 无参调用 vs 改动前捕获 `/tmp/cd-before.txt`：**diff = 空**（exit 0 + SIGNAL/INFO 两行逐字不变）。
- 七脚本 spot check（仓库根执行）exit=[0,0,0,1,0,0,0]，关键行与 r146 A1 表逐格一致：crossdomain SIGNAL blocked-on-external / o3-claim-list 4/4 PASS / gmr 11 PASS / kappa-receipt FAIL(1)（常态不转绿）/ rejudge SIGNAL / threshold 31 PASS / w3w4 0 mismatch。**零漂移。**

## A2b — 冻结面零修改 ✅

`git diff main --stat -- hit-matrix.json prior-estimates.json gold-tree.md runs-C0-*` = **0 行**。全量改动面 = {crossdomain 脚本, batch2-lint-samples/*, stages/{02,02.5,03}/*, current-goal.md} ⊆ B3 允许集（goal-queue.md 随收口 commit）。

## A5 — 04.5 反方复核

见 `loop-artifacts/stages/04.5/RV3G3cdx-schemalint-final-review.md`。