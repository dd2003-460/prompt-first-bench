# T41: Gold 分解树复现 — 泛化测试 (Q1 + Q3)

【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00..04.5
2. 每阶段产出落盘 loop-artifacts/stages/<N>/
3. 完成后 commit + push
4. 通道故障 → 报告 Lead 降级，不得静默跳过

## 任务

为以下两个问题各构建一棵**定量分解树**。每个叶子的数值必须来自真实 web 搜索。

### Q1: GPU 选型
见 experiments/stage-ablation/questions/Q1-gpu-selection.md

### Q3: LLM API 供应商选择
见 experiments/stage-ablation/questions/Q3-api-provider.md

## 要求（同 T40）

- 根节点：可排序标量 + 公式
- 正交维度 3-5 个
- 深度≥3，节点≥15
- 每叶子有数值+来源+敏感性
- 交叉验证表
- 缺口清单
- 最终结论

## 输出

分别写入：
- loop-artifacts/stages/04/Q1-execution-log.md
- loop-artifacts/stages/04/Q3-execution-log.md
