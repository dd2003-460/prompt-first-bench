# 003 self-optimization-tester — goal 模板 §3.0 链路验证 + token 效率 bench

> origin: ai · 2026-10-23 · 任务卡 ≤50 行

【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00-common-review.md + 01..04.5（仓库内）。
2. 每阶段产出落盘 loop-artifacts/stages/<N>/，阶段判定 pass 才进下一阶段。
3. 完成后 commit + push（含全部 loop-artifacts/）。
4. 通道故障（403/沙箱）→ 报告 Lead，由 Lead 降级本地执行，不得静默跳过 loop。

## 目标
验证 goal 模板 §3.0 的 8 步自主探索链路能否驱动 agent 走通完整循环；在 token 效率维度建立 ≥5 指标 bench，对比 baseline。

## 执行要求
1. 按链路 8 步逐步执行并落盘 loop-artifacts/：找目标→连仓库（ls-remote 验证）→走 loop 01→04.5→交叉验证→漏洞迭代→bench→发布（push+ls-remote）。
2. bench 指标 ≥5：token 效率 / 任务书行数 / 断点通过率 / 交叉验证 conf / 迭代轮数。
3. 每步结束写 loop-state.json（当前阶段+已完成步骤）。
4. 最后产出 loop-report.md：8 步成功/失败/降级 + 卡点分析 + 对 §3.0 的改进建议。
5. arena 不可达 → 降级本地自答（conf-0.2），卡点如实记录（卡点本身是测试数据）。

## 验收
- 8 步中 ≥7 步走通，loop-artifacts/ 各阶段文件齐。
- ≥5 指标定义，加权分数 vs baseline 有数值对比。
- commit + push 后 git ls-remote HEAD 更新可验证。
