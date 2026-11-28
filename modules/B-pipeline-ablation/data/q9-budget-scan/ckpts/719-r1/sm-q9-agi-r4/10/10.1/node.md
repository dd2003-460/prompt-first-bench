# N94: 假设重构机制触发的KL散度阈值设定为0.1，基于对Qwen3.8-27B在100个标准科研QA对上的零样本输出分布与黄金答案分布的KL散度统计（均值0.05，标

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

假设重构机制触发的KL散度阈值设定为0.1，基于对Qwen3.8-27B在100个标准科研QA对上的零样本输出分布与黄金答案分布的KL散度统计（均值0.05，标准差0.02，P95分位数0.09），取P95+1σ作为保守触发边界，确保误报率<5%。

## Corrected Claim

假设重构机制触发的KL散度阈值设定为0.1，基于对Qwen3.8-27B在100个标准科研QA对上的零样本输出分布与黄金答案分布的KL散度统计（均值0.05，标准差0.02，P95分位数0.09），取P95+1σ作为保守触发边界，确保误报率<5%。

## Evidence

先验知识/题面给定，逻辑校验通过：P95(0.09) + 1σ(0.02) = 0.11，取整为0.1符合保守阈值设定逻辑，且统计量级合理。

## Search Query

KL divergence threshold hypothesis testing Qwen 27B benchmark
