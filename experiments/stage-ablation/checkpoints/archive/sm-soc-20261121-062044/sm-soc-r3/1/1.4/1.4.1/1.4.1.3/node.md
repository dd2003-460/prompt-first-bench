# N115: 市场流动性对 P_willing_high 的弹性系数 ε_liq：定义为 P_willing_high 对平台月活跃买家数 (MAU_buyer) 的弹性，实

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N36

## Claim

市场流动性对 P_willing_high 的弹性系数 ε_liq：定义为 P_willing_high 对平台月活跃买家数 (MAU_buyer) 的弹性，实证估计 ε_liq ≈ 0.3，即 MAU 增加 10%，P_willing_high 增加 3%。若流动性下降导致 P_willing_high < 5%，则高挂价策略失效。

## Corrected Claim

市场流动性对 P_willing_high 存在正向弹性关系（ε_liq > 0），即 MAU 增加会提升 P_willing_high。具体弹性系数及策略失效阈值需依据特定市场实证数据确定，当前缺乏可靠来源支持 ε_liq ≈ 0.3 及 5% 阈值的具体数值。

## Evidence

[质询]该陈述包含具体的实证估计值（ε_liq ≈ 0.3）和特定的阈值条件（P_willing_high < 5%），属于经验事实。在缺乏任何参考来源支持的情况下，无法验证该弹性系数的具体数值是否准确，也无法确认5%的阈值是否为行业公认标准或特定模型设定。 | 经验事实，逻辑自洽但缺来源支持。弹性系数为正符合经济学直觉（流动性增加通常提升买家支付意愿），但具体数值0.3及阈值5%无外部证据佐证。

## Search Query

market liquidity elasticity buyer willingness to pay used goods platform
