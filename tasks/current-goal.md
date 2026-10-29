# Goal: R5.2hard-EXEMPT-sentinel — EXEMPT 非空哨兵

> 创建：2026-10-30 · ralph loop runner（goal-queue 新导出候选，R5.2-hardening 04.5 W1）
> 依据：`loop-artifacts/stages/04.5/R5.2hard-review.md` W1 + `tasks/goal-queue.md` 候选行

## 【目标】
`r5/assert-packet-symmetry.py` 的 `EXEMPT = []` 是 r104 预留的显式豁免清单（设计预期永不为空）。风险：未来某次 run 为让断言通过而悄悄往 EXEMPT 加条目 → 严格模式被静默稀释。本 goal 加**非空哨兵**：
1. **脚本改造**：EXEMPT 非空时 stdout 输出醒目警告行（如 `WARNING [EXEMPT-NONEMPTY] N 条豁免生效中——严格模式已被部分放宽，请人工确认每条豁免的 reason 合理性`），列出全部 (prefix, reason)；**不改变 exit code 语义**（豁免命中本身仍按现有逻辑 PASS，哨兵只是可见性加固）。
2. **零行为变化验证**：EXEMPT=[] 现状下重跑必须与 r104 基线逐字一致（67 PASS / 0 FAIL，exit 0，无新增 stdout 行）。
3. **哨兵自测**：临时注入一条假豁免条目跑一次（不落盘或落盘后回滚），确认 WARNING 出现且计数正确，然后恢复 EXEMPT=[]。
4. 模板 v2 或 bench.md 补一句说明哨兵存在（防未来维护者不知道有这层保护）。

## 【阶段】
bench 度量基础设施微加固（R5.2-hardening 的 W1 收口）。前置事实已定：r104 严格模式 67/0 基线冻结；本 goal 只加可见性，不改任何可达性判定逻辑。

## 【SOP 索引】
- `sop/arena-loop-pipeline.md`（唯一 SOP 入口）
- `loop/prompt-first/00-common-review.md` + `01..04.5`（阶段定义）
- `bench/self-opt-tester/r5/assert-packet-symmetry.py`（**改造对象**，EXEMPT 定义处 L~90）
- `bench/self-opt-tester/bench.md`（W1 收口段补一句）

## 【验收标准】
1. 六阶段工件齐全于 `loop-artifacts/stages/<N>/`，文件名带前缀 `R5.2sent-*`
2. 01：哨兵设计（触发条件 / 输出格式 / exit 语义不变论证 / 自测方案）
3. 02：web-llm 强制步骤执行并留回执（预期三 provider 仍 error → 记录失败继续）
4. 02.5：风险登记（如哨兵误报面、EXEMPT 条目增长路径分析）+ 对抗核验停止理由
5. 03：每步标 owner=user/agent
6. 04：改造落盘 + 基线重跑逐字一致（67/0 exit 0）+ 假豁免注入自测留痕 + 恢复
7. 04.5：反方复核 verdict + repair_stage
8. bench.md 补一句（哨兵已就位）
9. commit + push 分支 `ralph/r5.2hard-exempt-sentinel` + ls-remote 验证

## 【失败降级】
- web-llm 三 provider 均不可用 → 记录失败回执后继续，不阻塞
- 假豁免注入自测发现基线 diff 非零 → 说明改造污染了正常路径，回滚重做（不得带病交付）