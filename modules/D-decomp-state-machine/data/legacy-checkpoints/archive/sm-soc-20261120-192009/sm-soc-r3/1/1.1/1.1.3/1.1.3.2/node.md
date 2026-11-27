# N127: 随机偏好噪声项 σ_noise² 的量化：定义为卖家主观定价误差的方差，假设其服从截断正态分布，标准差 σ_noise 约为内在价值标准差的 15%（即 σ_n

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N36

## Claim

随机偏好噪声项 σ_noise² 的量化：定义为卖家主观定价误差的方差，假设其服从截断正态分布，标准差 σ_noise 约为内在价值标准差的 15%（即 σ_noise ≈ 0.15 * σ_intrinsic），因此 σ_noise² ≈ 0.0225 * σ_intrinsic²；该比例需基于卖家重复挂价行为的一致性检验进行回归估计。

## Corrected Claim

随机偏好噪声项 σ_noise² 定义为卖家主观定价误差的方差，假设其服从截断正态分布。在特定模型设定中，标准差 σ_noise 可设为内在价值标准差的 15%（即 σ_noise ≈ 0.15 * σ_intrinsic，σ_noise² ≈ 0.0225 * σ_intrinsic²），但该比例需基于卖家重复挂价行为的一致性检验进行回归估计，并非固定常数。

## Evidence

[质询]该陈述中的具体数值比例（15%）及分布假设（截断正态）属于特定场景下的经验参数或模型设定，并非通用物理/数学定律，且参考来源未提供该具体数值的实证支持或理论推导，存在将特定模型假设误作普遍事实的风险。 | 逻辑推导自洽（0.15^2=0.0225），但来源[1]和[2]仅涉及噪声交易者概念或微观结构噪声定性描述，未提供σ_noise与σ_intrinsic具体比例（15%）的直接支持或实证数据，属于经验事实缺来源支持。

## Search Query

seller pricing inconsistency noise variance estimation

## Retrieval Sources

- {'url': 'https://www.docin.com/p-4239991617.html&rut=a3608b54bc849893f7ae25ce706283c89798f97fc5203258ec7172cd718f897f', 'type': 'ddg', 'title': '《资产定价II》第15讲 《金融资产定价》第15讲 SDF、行为金融与情绪量化.pdf'}
- {'url': 'https://www.quant58.com/learn/market-microstructure-noise&rut=92c146c4aced018241ba36f9e6d60750a8b0ae0984f3babce903da4976a70a3b', 'type': 'ddg', 'title': '市场微观结构噪声指标：识别虚假波动 - Quant58 AI智能量化交易平台'}
