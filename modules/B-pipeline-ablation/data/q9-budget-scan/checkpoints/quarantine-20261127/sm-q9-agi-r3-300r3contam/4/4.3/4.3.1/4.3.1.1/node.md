# N171: Platt Scaling 校准的具体参数 (A, B) 需通过最小化交叉熵损失求解：min_{A,B} -Σ[y_i log(σ(Az_i+B)) + (1-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

Platt Scaling 校准的具体参数 (A, B) 需通过最小化交叉熵损失求解：min_{A,B} -Σ[y_i log(σ(Az_i+B)) + (1-y_i)log(1-σ(Az_i+B))]，其中 z_i 为原始置信度，y_i 为真实标签，需在验证集上拟合。

## Corrected Claim

Platt Scaling 校准的具体参数 (A, B) 需通过最小化交叉熵损失求解：min_{A,B} -Σ[y_i log(σ(Az_i+B)) + (1-y_i)log(1-σ(Az_i+B))]，其中 z_i 为原始置信度，y_i 为真实标签，需在验证集上拟合。

## Evidence

先验知识/题面给定，逻辑校验通过
