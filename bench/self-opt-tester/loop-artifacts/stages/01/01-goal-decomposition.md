# 01 目标分解 — self-optimization-tester

> origin: ai · 2026-10-23 · stage 01 of 1-loop (arena-loop-pipeline §4)

## 正交子目标
1. **链路验证**：goal 模板 §3.0 的 8 步链路能否驱动自主循环（本任务主体）。
2. **token 效率 bench**：定义 ≥5 指标，对比开源方案 baseline，总加权分数高 ≥10%。
3. **发布与续接**：commit+push 验证 + 新 goal 含完整 §3.0 规则。

## 边界
- 不修改 AGENTS.md；不创建 D1-efficiency-optimization 无关目录。
- arena 无浏览器控制权 → 按降级方案本地自答（conf-0.2），卡点如实记录。

## 已知 vs 空缺
- 已知：pfb 仓库存在且绑定 arena（pfb 中转模式）；/tmp/prompt-first-bench 本地克隆存在但落后远程（本地 HEAD 6358d84 vs 远程 e92421a）。
- 空缺：开源 bench baseline 的具体选取（步骤 5 交叉验证时定）；§3.0 的改进建议（loop-report.md 汇总）。

## 原子任务表
| # | 原子任务 | 依赖 |
|---|---------|------|
| A1 | 建任务目录 + loop-state.json | — |
| A2 | 断点 A：pull 远程 → 同步 loop+pfb 任务书 → push → ls-remote 验证 | A1 |
| A3 | 任务书 003 写 + push（断点 B/C） | A2 |
| A4 | 本地执行 loop 02→04.5（降级 conf-0.2）落盘 stages/ | A3 |
| A5 | bench 指标定义 + baseline 对比 + 加权分数 | A4 |
| A6 | 发布验证 + loop-report.md + 新 goal 规则文本 | A5 |

## 判定
pass（正交、可递归、原子化完成）
