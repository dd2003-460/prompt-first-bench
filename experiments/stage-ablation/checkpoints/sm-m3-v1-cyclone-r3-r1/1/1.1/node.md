# N6: 登陆后潜热供给中断的量化损失：ΔQ_latent ≈ (1 - SSS_land/SST_ocean) × ρ × L_v × q_e，其中SST_ocean取

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

登陆后潜热供给中断的量化损失：ΔQ_latent ≈ (1 - SSS_land/SST_ocean) × ρ × L_v × q_e，其中SST_ocean取28°C(301K)，q_e为饱和比湿，L_v=2.5×10^6 J/kg，典型沿海陆地湿度比海洋低30-50%，导致单位质量空气释放潜热减少约2.0-3.5 MJ/m³，直接削减眼墙对流能量输入。

## Corrected Claim

登陆后潜热供给中断的主要原因是陆地表面缺乏液态水蒸发源，导致近地面空气比湿迅速下降。典型沿海陆地近地面比湿较海洋低30-50%，导致单位体积空气可释放的潜热减少约 2.0-3.5 MJ/m³（基于饱和比湿差值估算），从而直接削减眼墙对流能量输入。

## Evidence

[质询]公式量纲与物理机制存在严重混淆：1. 公式右侧 (1 - SSS/SST) * ρ * Lv * qe 中，SSS(盐度)与SST(温度)量纲不同，相减无物理意义；2. 潜热释放取决于水汽含量(qv)而非盐度，登陆后潜热中断是因为陆地表面蒸发源消失导致近地面空气迅速失湿，而非因为'盐度比'；3. 数值估算中 '2.0-3.5 MJ/m³' 对应的是体积潜热，但公式推导出的单位应为 J/kg 或 J/m³ 需明确密度基准，且 30-50% 的湿度降低通常导致潜热通量减少而非简单的线性比例关系，该量化公式缺乏气象学标准定义支持。 | 先验知识/题面给定，逻辑校验发现公式量纲错误（盐度与温度不可直接运算）及物理机制描述不准确（潜热中断源于蒸发源缺失而非盐度差异），故降级。

## Search Query

latent heat flux reduction landfall tropical cyclone SST specific humidity
