# N77: 平台佣金收入损失 ΔR_platform 的计算公式定义为：ΔR_platform = (1 - Retention_Sellers) * GMV_Baseli

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

平台佣金收入损失 ΔR_platform 的计算公式定义为：ΔR_platform = (1 - Retention_Sellers) * GMV_Baseline * Commission_Rate，其中 Retention_Sellers 为干预后高溢价卖家留存率，GMV_Baseline 为干预前月 GMV，Commission_Rate 为平台平均抽成比例（通常 3%-5%）。

## Corrected Claim

平台佣金收入损失 ΔR_platform 的计算公式定义为：ΔR_platform = (1 - Retention_Sellers) * GMV_Baseline * Commission_Rate，其中 Retention_Sellers 为干预后高溢价卖家留存率，GMV_Baseline 为干预前月 GMV，Commission_Rate 为平台平均抽成比例（通常 3%-5%）。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同参数（Retention_Sellers, Commission_Rate）下的具体数值实例，而非独立的逻辑分支或概念维度，因此存在严重冗余。此外，父节点定义的是一个通用计算公式，而子节点仅提供了两个特定假设场景（高/低风险），未覆盖公式本身的通用推导逻辑、变量定义边界或中间计算步骤，导致在概念分解上不完备。）
