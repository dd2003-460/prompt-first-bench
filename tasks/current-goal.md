# Goal: R5.2audit-verdict-text-templatize — assert-packet-audit.py VERDICT 段硬编码事实快照处置

> 创建：2026-10-30 · ralph loop runner（r131 04.5 W2 导出的立即续项）
> 依据：`tasks/goal-queue.md` 候选「R5.2audit-verdict-text-templatize」+ `stages/04.5/R5.2audit-sigcnt-adversarial-review.md` W2

## 【目标】
消除 `assert-packet-audit.py` L144-148 VERDICT 段的同构缺陷：'8 confirmed / 3 mismatch / 1 unverified / 1 形式性' 是**硬编码事实快照**——若未来新增断言，汇总行（已动态化，r131）会更新但 VERDICT 段不会，产生与汇总行矛盾的静默撒谎。二选一处置：**动态生成**（从 check 调用记录推导文字）或 **注释标记**（显式声明"新增断言须同步本段"）。选动态生成——与 r131 signal-counter 同一防撒谎方向，彻底消除残余耦合。

## 【阶段】
单文件小改 + 基线回归（正常路径输出逐字一致）+ 变异测试（注入新断言 → VERDICT 段计数联动）。

## 【SOP 索引】
- `loop/prompt-first/01..04.5`；对象 `bench/self-opt-tester/r5/assert-packet-audit.py`

## 【验收标准】
- [ ] 正常路径实跑输出与当前基线**逐字一致**（16 PASS / 0 FAIL / 1 SKIP + 1 SIGNAL(C12)，exit 0，VERDICT 段文字不变）——零行为漂移
- [ ] VERDICT 段四个数字（confirmed/mismatch/unverified/形式性）改为从 check 调用记录动态推导，不再硬编码
- [ ] 变异测试：注入一条新 confirmed 断言（如 C99）→ VERDICT 段 '9 条 confirmed' 联动变化（证明动态生效），同时汇总行 '17 PASS' 联动
- [ ] 冻结面零触碰（仅 assert-packet-audit.py 一个文件改动）

## 【失败降级】
- 动态化后基线文字漂移（措辞不完全等价）→ 调整模板使输出逐字还原，不放宽"逐字一致"标准
- web-llm 不可用 → unverified 降级（机械改动边际贡献 ≈ 0，与 r131/r132 同判据）