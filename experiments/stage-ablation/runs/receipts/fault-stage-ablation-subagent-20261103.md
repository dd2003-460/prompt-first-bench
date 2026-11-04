# 故障记录：stage-ablation 执行 subagent (deleg_e4e6d392)

> origin: ai · 2026-11-03T23:40+08:00

## 现象
- subagent 运行 >2h 后结束（进程消失）
- 产出：仅克隆 GPT Researcher 仓库到 runs/d1-gpt-researcher/（含其自带 evals/ 测试数据）
- 缺失：S0-S5 六臂 × 5 题 = 60 runs 全部未执行；D1 5 runs 未执行；scoring.md 未生成
- receipts/ 目录为空（无 arena 回执）

## 原因分析（待确认）
- 可能 1：subagent 在配置 GPT Researcher 环境时卡住（依赖安装/本地模型连接），超时被杀
- 可能 2：vLLM 8787 负载过高（同时跑 LoCoMo benchmark PID 37261），subagent 的 API 调用超时
- 可能 3：subagent 上下文窗口耗尽（读大量源码文件）

## 影响
- stage-ablation 核心实验（各阶段边际收益）未获得任何数据
- D1 baseline 对比未建立
- 不影响 hw-survey-flashnext bench run（独立任务，已完成）

## 处置
- [ ] 确认失败原因（查 subagent transcript）
- [ ] 降低并发：先停 LoCoMo benchmark 再重跑 stage-ablation
- [ ] 考虑拆小：先跑 S0/S5/D1 三臂 × 1 题验证管道，再扩全量
