# Goal: R5.2audit-C4-assert-hardening — assert-c4-timing.py 健壮性小修

> 创建：2026-10-30 · ralph loop runner（r130 04.5 W2/W3 导出的立即续项）
> 依据：`tasks/goal-queue.md` 候选「R5.2audit-C4-assert-hardening」+ `stages/04.5/R5.2audit-C4-adversarial-review.md` W2/W3

## 【目标】
1. **W3**：WS_RUN2 路径缺失时显式 FAIL 路径（当前 FileNotFoundError 崩溃≈FAIL 但非显式机判输出）——目录不存在 → check FAIL + 跳过后续枚举 + exit 1。
2. **W2**：秒级时间戳解析支持——epoch() 从「截前 12 位数字 strptime %Y%m%d%H%M」改为按实际位数分派（12 位=分钟级 / 14 位=秒级），防未来带秒转录件丢精度。

## 【阶段】
r130 登记的极小健壮性修复。单文件改动 + 基线回归 + 变异测试。

## 【SOP 索引】
- `loop/prompt-first/01..04.5`；对象 `bench/self-opt-tester/r5/assert-c4-timing.py`

## 【验收标准】
- [ ] 正常路径实跑输出与 r130 基线**逐字一致**（SIGNAL not-reconstructable，exit 0）——零行为漂移
- [ ] WS 缺失场景：指向不存在目录的副本运行 → 显式 `FAIL run2 目录存在` + exit 1（非 traceback）
- [ ] 秒级解析：注入 `2026-10-24T00:34:00` 与 `2026-10-24T00:48:00` 两锚 → 跨度 840s 正确（分钟级/秒级同值）
- [ ] 冻结面零触碰

## 【失败降级】
- 改后基线漂移 → 回滚重做
- web-llm 不可用 → unverified 降级（机械改动边际贡献 ≈ 0）