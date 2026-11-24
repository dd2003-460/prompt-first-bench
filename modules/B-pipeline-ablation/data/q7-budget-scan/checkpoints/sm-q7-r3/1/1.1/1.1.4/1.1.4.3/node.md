# N122: NVMe SSD 坏块率(BUR)对有效容量的影响：企业级 NVMe SSD 典型 BUR 为 0.1%-0.5%（即 0.001-0.005），在 500TB

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30

## Claim

NVMe SSD 坏块率(BUR)对有效容量的影响：企业级 NVMe SSD 典型 BUR 为 0.1%-0.5%（即 0.001-0.005），在 500TB 标称容量中，坏块损耗 = 500TB * 0.001~0.005 = 0.5~2.5TB；结合 RAID5 开销，总有效容量 = 500TB * (1-1/N) * (1-BUR)，当 N=8, BUR=0.005 时，有效容量 = 500 * 0.875 * 0.995 = 435.3TB，比忽略 BUR 的 437.5TB 少 2.2TB，成本分摊误差约 0.5%。

## Corrected Claim

企业级 NVMe SSD 坏块率(BUR)通常在 0.1%-0.5% 范围内（需具体厂商数据确认），在 500TB 标称容量中，坏块损耗约为 0.5~2.5TB；结合 RAID5 (N=8) 开销，当 BUR=0.005 时，有效容量约为 435.3TB，比忽略 BUR 的 437.5TB 少约 2.2TB。

## Evidence

[质询]参考来源仅讨论SSD寿命与衰减机制，未提供坏块率(BUR)的具体数值范围或容量计算公式，无法直接支持该经验参数及计算结果。 | 逻辑推导自洽（500*0.875*0.995=435.3125），但BUR 0.1%-0.5%属于经验事实，参考来源[1]主题不匹配且未覆盖该数据，依据经验事实排除条款降级。

## Search Query

enterprise NVMe SSD bad unit rate BUR specification 0.1% 0.5%

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2010096956383453604&rut=e66f32b24358a2ad592fd3ec09cee1a01d024cb1cdf7ce73beeee2917867e91c', 'type': 'ddg', 'title': '企业级 NVMe SSD 极限寿命与衰减机制深度分析报告 - 知乎'}
