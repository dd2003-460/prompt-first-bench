# N332: 量化平台流量倾斜效应：高挂价商品（$P > 1.15 \cdot C_{ref}$）相对于标准价商品的首页曝光量 $E_{high}$ 与标准曝光量 $E_{s

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N116

## Claim

量化平台流量倾斜效应：高挂价商品（$P > 1.15 \cdot C_{ref}$）相对于标准价商品的首页曝光量 $E_{high}$ 与标准曝光量 $E_{std}$ 的比值 $R_{exposure} = E_{high} / E_{std}$，需通过平台日志数据计算该比值，若 $R_{exposure} > 1.2$ 则支持平台驱动假说。

## Corrected Claim

量化平台流量倾斜效应：高挂价商品相对于标准价商品的首页曝光量比值 R_exposure = E_high / E_std，需通过平台日志数据计算该比值。若 R_exposure 显著大于 1（具体阈值需根据平台实证数据确定，例如 > 1.2），则支持平台驱动假说。

## Evidence

[质询]该陈述包含具体的经验性阈值（1.15倍参考价、1.2倍曝光比），这些数值并非第一性原理可推导，而是依赖于特定平台的算法机制和实证数据。由于缺乏来源支持，无法确认这些具体数值是否准确反映了真实平台的流量倾斜效应，存在将假设性参数当作既定事实的风险。 | 经验事实，逻辑自洽但缺来源支持。该陈述定义了基于平台日志数据的验证方法，逻辑结构完整，但具体阈值（1.15, 1.2）属于经验参数，无外部来源直接支持或验证其准确性。

## Search Query

e-commerce platform algorithm bias high price listing exposure ratio empirical data
