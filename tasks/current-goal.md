# Goal: RV3G3-threshold-crossdomain-reverify 核销轮（r145）

> 创建：2026-10-30 · ralph loop runner（queue 消费——队列卫生修复 + 核销验证，纯仓库内工作）
> 依据：`RV3G3-threshold-crossdomain-reverify` 的全部交付物已在 r140（f8c096b，经 96a89e7 合入 main）完成——assert-goldrank-crossdomain.py 骨架落盘（schema 预注册 + DP tie 可达枚举器）+ A3 第一域回归锚点 18/18 + M0 fuzz 50/50 + M1-M4 变异全过 + 冻结面零修改 + 04.5 verdict pass。r140 收口 commit 97d2adf 的 message 声称「queue 划掉 + 结果注记」且确实写入了完整 **结果** 注记，但 checkbox 仍为 `[ ]`（未划掉）。本轮 = 补核销（`[ ]`→`[x]`）+ 验证增量。
> 先例：r137 R5.2assert-suite-docsync 核销轮（r133/c55848f 已交付未收口 → r137 补收口 + 行为实证，零代码改动）、r135 RV3G4-prior-source-assert 核销轮。

## 【目标】
queue L28 `- [ ]` → `- [x]` + 日期 + 核销注记（事实链一句话：r140 已交付、97d2adf 漏翻 checkbox），附 ≥3 项实跑验证增量；追加新导出候选 ≥1。

## 【阶段】
01（本文件）→ 02 事实链核验（git 证据：f8c096b 交付清单 / 97d2adf queue diff / 当前 checkbox 状态）→ 02.5 交叉核对（基线对照表 + 输出 byte-exact 捕获）→ 03 动作分解 → 04 执行验证（checkbox 翻转 + 回归实跑留痕）→ 04.5 反方复核 → 收口（queue 更新 + merge main）

## 【SOP 索引】
- `tasks/ralph-loop-runner.md` 阶段 B/C（六阶段不可跳过；核销轮的 02/02.5 = 事实链与基线对照，非信息研究）
- 先例工件：r137 docsync / r135 prior-source 核销轮（loop-artifacts/stages/*）
- 被核销对象（只读）：`bench/rubric-v3/ablation/scripts/assert-goldrank-crossdomain.py`（r140 落盘）/ `loop-artifacts/stages/04/RV3G3cd-execution-log.md` / `loop-artifacts/stages/04.5/RV3G3cd-review.md`

## 【验收标准】
- [ ] queue L28 `- [ ]` → `- [x]` + 日期 + 核销注记
- [ ] 验证增量 ≥3 项全部实跑留痕：(a) assert-goldrank-crossdomain.py 从仓库根实跑 = SIGNAL blocked-on-external exit 0（byte-exact 输出捕获）；(b) 冻结面（hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-*）git diff main = 0 行；(c) 回归基线对照（assert-o3-claim-list 4/4 · assert-gmr-recompute 11 PASS · assert-kappa-receipt FAIL exit 1 常态 · assert-o3-claim-rejudge SIGNAL exit 0 · assert-goldrank-threshold 31 PASS · assert-w3w4-recompute SIGNAL exit 0）
- [ ] 新导出候选 ≥1（追加到 queue 底部）
- [ ] 冻结件零修改（git status 仅 loop-artifacts + tasks/goal-queue.md + 本文件）
- [ ] 04.5 verdict pass

## 【失败降级】
- 若实跑输出与 r140 预注册语义（SIGNAL blocked-on-external exit 0）不一致 → 停止核销，如实登记为基线漂移，不翻 checkbox，导出排查候选
- 若发现 r140 交付物有缺失（脚本不存在 / docstring 缺 D1-D5 判定语义段）→ 同上，降级为「交付物完整性审计」goal