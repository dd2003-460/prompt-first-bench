# N221: 佣金率差项量化：定义 Commission_rate_asym - Commission_rate_sym 为信息不对称溢价，通常二手平台在信息不透明时通过‘担

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N72

## Claim

佣金率差项量化：定义 Commission_rate_asym - Commission_rate_sym 为信息不对称溢价，通常二手平台在信息不透明时通过‘担保交易’或‘认证服务’收取额外 1-3% 的手续费，即 ΔCommission ≈ 0.02 * GMV。

## Corrected Claim

佣金率差项量化：定义 Commission_rate_asym - Commission_rate_sym 为信息不对称溢价。二手平台在信息不透明时通常通过‘担保交易’或‘认证服务’收取额外手续费，该溢价率因平台而异，常见范围在1%-5%之间，具体数值需依据特定平台费率计算，不宜统一简化为固定值。

## Evidence

[质询]该陈述将‘信息不对称溢价’具体量化为‘1-3%的手续费’及‘0.02 * GMV’，属于具体的经验性市场参数。不同平台（如闲鱼、转转、eBay等）的担保交易费率、认证服务定价差异巨大，且并非所有平台都统一收取1-3%的额外费用，该数值缺乏普适性，属于过度简化的经验估计。 | source=knowledge，逻辑自洽（量纲正确，概念定义合理），但‘1-3%’及‘0.02’为具体经验数值，非第一性原理可推导，且无外部来源支持其普适性，依据经验事实排除条款降级。

## Search Query

second hand marketplace commission rate asymmetry information opacity surcharge
