# N30: 条件性推荐前置条件：(1) 电力预算：总功耗 (W) * 24h * 365d * 电价 ($/kWh) ≤ 年度电力预算；(2) 散热环境：房间/机柜散热能力

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

条件性推荐前置条件：(1) 电力预算：总功耗 (W) * 24h * 365d * 电价 ($/kWh) ≤ 年度电力预算；(2) 散热环境：房间/机柜散热能力 (W) ≥ 总TDP * 1.2；(3) 软件栈选择：CUDA (NVIDIA) vs ROCm (AMD) vs CPU-only，影响可用GPU和性能；(4) 模型微调需求：若需微调，需额外显存 (梯度+优化器状态)，推荐显存≥2x推理需求；(5) 并发需求：单用户 vs 多用户，影响KV Cache大小和batch size。

## Corrected Claim

条件性推荐前置条件：(1) 电力预算：总功耗 (W) * 24h * 365d * 电价 ($/kWh) ≤ 年度电力预算；(2) 散热环境：房间/机柜散热能力 (W) ≥ 总TDP * 1.2；(3) 软件栈选择：CUDA (NVIDIA) vs ROCm (AMD) vs CPU-only，影响可用GPU和性能；(4) 模型微调需求：若需微调，需额外显存 (梯度+优化器状态)，推荐显存≥2x推理需求；(5) 并发需求：单用户 vs 多用户，影响KV Cache大小和batch size。

## Evidence

先验知识/题面给定，逻辑校验通过
