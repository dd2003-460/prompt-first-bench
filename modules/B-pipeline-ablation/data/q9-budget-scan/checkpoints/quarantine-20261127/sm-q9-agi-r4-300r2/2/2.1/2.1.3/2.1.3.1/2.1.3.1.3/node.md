# N301: 指数衰减模型 Follow_Rate(L) = 1 - α * exp(-β * (L - L_0)) 假设衰减是单调且平滑的，但在 RoPE 外推或量化误差累

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N121

## Claim

指数衰减模型 Follow_Rate(L) = 1 - α * exp(-β * (L - L_0)) 假设衰减是单调且平滑的，但在 RoPE 外推或量化误差累积场景下，实际衰减可能呈现阶梯状或非线性突变；需引入修正项 ε_noise 表示量化/位置编码引起的额外随机波动，修正后模型为 Follow_Rate(L) = 1 - α * exp(-β * (L - L_0)) - ε_noise，其中 ε_noise 需通过多次采样方差估计。

## Corrected Claim

指数衰减模型 Follow_Rate(L) = 1 - α * exp(-β * (L - L_0)) 假设衰减是单调且平滑的，但在 RoPE 外推或量化误差累积场景下，实际衰减可能呈现阶梯状或非线性突变；需引入修正项 ε_noise 表示量化/位置编码引起的额外随机波动，修正后模型为 Follow_Rate(L) = 1 - α * exp(-β * (L - L_0)) - ε_noise，其中 ε_noise 需通过多次采样方差估计。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

non-linear instruction following decay noise quantization error long context
