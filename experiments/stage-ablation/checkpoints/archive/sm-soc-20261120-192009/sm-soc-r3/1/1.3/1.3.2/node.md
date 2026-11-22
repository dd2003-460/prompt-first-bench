# N42: 随机偏好噪声方差 σ_noise² 的量化：σ_noise² = k / (1 + standardization_index)，其中 k 为噪声强度常数，需通

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N7

## Claim

随机偏好噪声方差 σ_noise² 的量化：σ_noise² = k / (1 + standardization_index)，其中 k 为噪声强度常数，需通过实证数据拟合，通常 k ∈ [0.01, 0.05]。

## Corrected Claim

在特定随机偏好噪声模型中，σ_noise² 可建模为 k / (1 + standardization_index)，其中 k 为需通过特定实证数据拟合的噪声强度常数，其典型量级视具体应用场景而定。

## Evidence

[质询]该公式属于特定模型假设下的经验拟合参数，缺乏普适的理论推导基础，且 k 的取值范围 [0.01, 0.05] 高度依赖于具体数据集和标准化方法，作为通用量化标准缺乏广泛共识或第一性原理支持。 | source=knowledge，逻辑自洽（方差与标准化指数负相关符合直觉），但属于特定经验模型参数，无外部来源支持且非第一性原理可严格推导，依据经验事实排除条款降级。

## Search Query

noise variance standardization index empirical fitting
