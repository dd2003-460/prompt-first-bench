# N33: 低层风场平均速度降低幅度 ΔV_low 的量化公式为 ΔV_low/V_surface ≈ (δ_BL,land - δ_BL,ocean)/H_ref × l

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

低层风场平均速度降低幅度 ΔV_low 的量化公式为 ΔV_low/V_surface ≈ (δ_BL,land - δ_BL,ocean)/H_ref × ln(z_ref/z_0)，其中 z_ref 为参考高度（如 10m），z_0 为粗糙长度（陆地 ~0.01-1 m，海洋 ~0.0001-0.001 m），该式表明粗糙度增加通过降低有效风廓线指数直接削减低层动能输入。

## Corrected Claim

低层风场受地表粗糙度影响，粗糙度增加（如从海洋到陆地）会导致近地面摩擦速度增大，从而降低低层风速。其定量关系通常通过风廓线公式 u(z) = (u*/κ)ln(z/z0) 描述，其中 z0 为粗糙长度，而非题目中给出的特定乘积公式。

## Evidence

[质询]公式形式存在量纲和物理机制上的可疑之处：标准风廓线公式中，粗糙度影响通常通过对数项 ln(z/z0) 体现，而非作为乘数与边界层厚度差相乘；且将边界层厚度差 (δ_BL) 直接乘以对数项来量化低层风速变化缺乏标准的边界层理论支持，可能是对相似层理论的误用或过度简化。 | source=knowledge，但公式结构不符合标准大气边界层理论（Monin-Obukhov Similarity Theory），粗糙度主要影响近地面摩擦速度和对数高度项，而非以这种乘积形式直接决定风速变化率；逻辑校验发现公式推导链条断裂，无法从第一性原理严格推出该特定形式。

## Search Query

surface roughness length effect on wind profile power law boundary layer
