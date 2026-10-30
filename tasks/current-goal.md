# Goal: R5.2audit-C4-timing-reconstruct — C4 "14m27s" 数值化机判

> 创建：2026-10-30 · ralph loop runner（queue 候选区队首可执行项；R5.2-third-scorer 因需 arena 通道/第三本地模型标记 blocked-on-external 跳过）
> 依据：`tasks/goal-queue.md` 候选条目 + `r5/packet-audit-r4-v1.md` C4 行（verdict=unverified, X5）+ `stages/02.5/R5.2audit-cross-check.md` X5 节

## 【目标】
C4 "14m27s" 由人工预判升级为**机判信号**：
1. **A1**：机判脚本 `bench/self-opt-tester/r5/assert-c4-timing.py`——对 `$WS/run2/` 全部文件做 ISO 时间戳全量枚举，判定是否存在 ≥2 个逐事件时间戳：有 → 差值区间 vs 867s 比对输出 SIGNAL(reconstructable)；无 → SIGNAL(not-reconstructable) + 列出唯一可用时间戳证明单点无法定界
2. **A2**：X5 状态更新落盘 `loop-artifacts/stages/02.5/R5.2audit-C4-cross-check.md`（预判「不可重建」→ 机判实证结论）
3. **A3**：`packet-audit-r4-v1.md` C4 行补机判引用（同 r105 C12 处置方式，verdict 不翻转——禁升级 confirmed）
4. **A4**：04 执行日志 + 04.5 反方复核

## 【阶段】
R5.2-audit 02.5 A4 导出项。纯仓库内只读消费 WS 转录件 + 新增一个 assert 脚本与 stage 工件。工作量小。

## 【SOP 索引】
- `loop/prompt-first/01..04.5` + `sop/arena-loop-pipeline.md`
- 模式参考：`r5/assert-packet-audit.py`（signal-only、不参与 exit code、冻结分不动）
- 证据源（只读）：`$WS/run2/`（7 文件），WS = `/Users/a1-6/Desktop/workspace/projects/AI-计算科学/D1-efficiency-optimization/tasks/self-optimization-tester/loop-artifacts/stages/04.5/r3`

## 【验收标准】
- [ ] assert-c4-timing.py 落盘可重放，exit 0，输出含 C4 SIGNAL 二态之一 + 时间戳枚举清单
- [ ] SIGNAL 语义正确（口径预注册于 01：逐事件时间戳 = 同一 run 内 ≥2 个不同时刻的 ISO 时间戳；executed_at 单点不算）
- [ ] X5 状态更新落盘 02.5 工件；packet-audit-r4-v1.md C4 行补机判引用
- [ ] 冻结数据零修改（git status 验证 pfb 仓内仅新增/预期改动文件）
- [ ] 04.5 反方复核 verdict pass

## 【失败降级】
- WS 路径不可达 → 登记边界，goal 标记 blocked-on-external 跳过取下一个
- 发现意外存在 ≥2 时间戳 → 走 reconstructable 分支如实比对，不预设结论
- web-llm 通道不可用 → unverified 降级（本 goal 证据链仓库内闭合，边际贡献 ≈ 0）