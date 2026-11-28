# N188: A/B 测试标定的具体实验设计：选取 20 个典型任务（10 个复杂数值模拟 + 10 个文献综述），每个任务运行 5 次（共 100 次推理），记录首次通过率

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

A/B 测试标定的具体实验设计：选取 20 个典型任务（10 个复杂数值模拟 + 10 个文献综述），每个任务运行 5 次（共 100 次推理），记录首次通过率 (First-Pass Success Rate, FPSR)；P_fail_local = 1 - (Σ FPSR_i / N_trials)，其中 N_trials=100；同时记录每次失败的错误类型分布以修正 N103 的错误占比权重。

## Corrected Claim

A/B 测试标定的具体实验设计：选取 20 个典型任务（10 个复杂数值模拟 + 10 个文献综述），每个任务运行 5 次（共 100 次推理），记录首次通过率 (First-Pass Success Rate, FPSR)；P_fail_local = 1 - (Σ FPSR_i / N_trials)，其中 N_trials=100；同时记录每次失败的错误类型分布以修正 N103 的错误占比权重。

## Evidence

先验知识/题面给定，逻辑校验通过：实验设计样本量（20任务*5次=100次）与公式中N_trials=100一致，FPSR定义及P_fail_local计算逻辑自洽，符合A/B测试标定常规做法。
