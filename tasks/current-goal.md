# Goal: R5.2audit-signal-counter — assert-packet-audit.py 汇总行 SIGNAL 计数变量化

> 创建：2026-10-30 · ralph loop runner（queue 候选区下一个纯仓库内项）
> 依据：`tasks/goal-queue.md` 候选条目「R5.2audit-signal-counter」+ r105 04.5 R6/W1 登记（汇总行 "+ 1 SIGNAL(C12)" 硬编码，未来加第二个 signal 时汇总行会撒谎）

## 【目标】
把 `bench/self-opt-tester/r5/assert-packet-audit.py` 汇总行的硬编码 `+ 1 SIGNAL(C12)` 改为 **signal 计数变量**：新增 `signals` 列表，C12 三个分支各 append 一条信号记录，汇总行输出 `+ {len(signals)} SIGNAL(C12[,{未来项}])`。防未来加第二个 signal 时汇总行与实际信号数脱节。

## 【阶段】
r105 04.5 登记的极小健壮性修复。单文件改动 + 基线回归验证。

## 【SOP 索引】
- `loop/prompt-first/01..04.5` + `sop/arena-loop-pipeline.md`
- 对象：`bench/self-opt-tester/r5/assert-packet-audit.py` L133 汇总行 + C12 信号段（L116-131）

## 【验收标准】
- [ ] 汇总行改用 `len(signals)` 变量；当前实跑输出与改前**逐字一致**（16 PASS / 0 FAIL / 1 SKIP + 1 SIGNAL(C12)）——零行为漂移
- [ ] 变异测试：临时注入第二条假 signal（/tmp 副本），确认汇总行变 `+ 2 SIGNAL(...)` 后删除
- [ ] exit code 语义不变（signal-only 不参与 exit code）
- [ ] 冻结面零触碰（仅该脚本 + stage 工件 + queue）

## 【失败降级】
- 改后输出与基线不一致 → 回滚重做，不放宽基线
- web-llm 不可用 → unverified 降级（纯机械改动，边际贡献 ≈ 0）