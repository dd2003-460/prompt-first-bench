# 故障记录：stage-ablation harness 未交付

> origin: ai · 2026-11-04T02:30+08:00

## 现象
- deleg_e4e6d392 task-1（harness 骨架）：status=interrupted, api_calls=1, 16s — 模型未响应即被杀
- deleg_e4e6d392 task-0（执行实验）：status=interrupted, api_calls=189, 5h46m — 只完成克隆 GPT Researcher 仓库，S0-S5 × 5题 = 60 runs 全部未执行，scoring.md 未生成
- ablation_harness.py / score.py / d1_baseline.py / test_harness.py 均不存在
- 仅存 gates.py + test_gates.py（之前 T22 产出）

## 原因分析
- task-1 失败：本地 27b 在 LoCoMo benchmark 争抢下无响应（16s 超时），subagent 无法启动
- task-0 失败：跑了 5h46m 但卡在环境配置阶段（GPT Researcher 依赖安装/Python 版本兼容），从未进入实际跑题阶段
- 根因：① vLLM 资源争抢（LoCoMo 占满）② GPT Researcher 需要 Python ≥3.10 而本机可能 3.9 ③ subagent 上下文窗口不够装下大量源码

## 影响
- stage-ablation 核心实验（各阶段边际收益 S0→S5）零数据
- D1 baseline 对比未建立（只有仓库源码，无运行结果）
- DESIGN.md §8 两条判据（每级增量符号 + S5 vs D1 总分序）无法验证

## 处置建议
1. 停掉所有 vLLM 竞争负载后再重跑
2. 先写 harness 代码（纯 stdlib，不依赖 GPT Researcher 能跑通）
3. S0/S1 臂不需要联网，可以先跑（只需 27b endpoint）
4. S2+ 臂需要 ego-browser 或 web_search — 确认通道可用再跑
5. D1 降级预案：如果 GPT Researcher 装不动，用 Open Deep Research 或 STORM 替代；三个都不行则 D1 标 N/A
