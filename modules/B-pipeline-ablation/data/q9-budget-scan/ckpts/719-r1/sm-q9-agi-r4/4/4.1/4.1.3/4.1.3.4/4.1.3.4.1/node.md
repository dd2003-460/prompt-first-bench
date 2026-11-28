# N586: 序贯检验（Group Sequential Design）在本地推理 A/B 测试中，平均样本量 ASN 的计算公式为 ASN ≈ (Z_α + Z_β)^2 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N209

## Claim

序贯检验（Group Sequential Design）在本地推理 A/B 测试中，平均样本量 ASN 的计算公式为 ASN ≈ (Z_α + Z_β)^2 * σ^2 / δ^2 * (1 + k*log(k))，其中 k 为中期分析次数；若固定样本量 n_fixed = 100，ASN 可减少至 60-80（即 20%-40% 节约），前提是允许早期停止且 Type I error 控制在 α=0.05。

## Corrected Claim

序贯检验（Group Sequential Design）在本地推理 A/B 测试中，通过允许早期停止可在控制 Type I error (α=0.05) 的前提下减少平均样本量（ASN）。具体节约比例（如 20%-40%）取决于效应量、方差及所选的序贯边界（如 O'Brien-Fleming 或 Pocock），而非由单一通用公式 ASN ≈ (Z_α + Z_β)^2 * σ^2 / δ^2 * (1 + k*log(k)) 直接确定。

## Evidence

[质询]公式中的项 (1 + k*log(k)) 并非序贯检验（如 O'Brien-Fleming 或 Pocock 边界）计算平均样本量（ASN）的标准通用形式。标准 ASN 通常依赖于具体的边界函数和停止概率积分，而非简单的对数多项式修正。此外，'20%-40% 节约'是一个高度依赖效应量、方差和具体边界设计的经验范围，不能由该特定公式直接推导得出，且对于小样本（n=100）而言，离散效应可能导致节约比例波动极大，该陈述将特定经验结果泛化为公式推论存在逻辑跳跃。 | 先验知识/题面给定，逻辑校验发现公式形式非标准且结论推导缺乏严谨性，故降级。
