# N263: Q_score 计算的工作点 1 (高保真/低性价比)：采用 BF16 精度。Q_score = 1.0 (定义上无损)。硬件约束：需 H100 80GB 或 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

Q_score 计算的工作点 1 (高保真/低性价比)：采用 BF16 精度。Q_score = 1.0 (定义上无损)。硬件约束：需 H100 80GB 或 2x RTX 4090 (BF16 权重 54GB + KV Cache)。此工作点仅在预算 >$25k 且业务对幻觉率极度敏感时可选，其 TCO 是其他方案的 6-10 倍，性价比最低。

## Corrected Claim

Q_score 计算的工作点 1 (高保真/低性价比)：采用 BF16 精度。Q_score = 1.0 (定义上无损)。硬件约束：需高显存GPU（如 H100 80GB 或 2x RTX 4090，以容纳 BF16 权重及 KV Cache）。此工作点仅在预算充足且业务对幻觉率极度敏感时可选，其 TCO 显著高于量化方案（通常为数倍），性价比最低。

## Evidence

[质询]硬件需求与TCO倍数属于具体工程经验数据，缺乏通用标准支持，且'6-10倍'的TCO对比基准模糊，易受具体业务负载和定价策略影响，存在口径混淆风险。 | source=knowledge，逻辑自洽（BF16精度确实无损且显存占用约为FP16/INT8的2倍，高成本符合直觉），但具体硬件配置（H100/4090）及TCO倍数（6-10x）为经验性工程估算，无来源直接支持，依据经验事实排除条款降级。
