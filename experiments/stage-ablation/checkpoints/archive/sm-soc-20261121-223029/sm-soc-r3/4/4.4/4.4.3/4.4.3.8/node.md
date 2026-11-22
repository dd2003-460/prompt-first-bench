# N269: 流量权重加成 w_boost 对低质商品曝光的边际影响：ΔShare_low = (λ_low_new * w_boost - λ_low_pre * 1) /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88, N89, N90

## Claim

流量权重加成 w_boost 对低质商品曝光的边际影响：ΔShare_low = (λ_low_new * w_boost - λ_low_pre * 1) / (Total_Listings_post)，其中 λ_low_new 为新入场低质卖家比例，λ_low_pre 为存量低质卖家比例。若 w_boost 每增加 0.1，ΔShare_low 增加约 0.5%，则 w_boost 的弹性系数为 5%。

## Corrected Claim

流量权重加成 w_boost 对低质商品曝光的边际影响：ΔShare_low = (λ_low_new * w_boost - λ_low_pre * 1) / (Total_Listings_post)，其中 λ_low_new 为新入场低质卖家比例，λ_low_pre 为存量低质卖家比例。若 w_boost 每增加 0.1，ΔShare_low 增加约 0.5%，则 w_boost 的弹性系数为 5%。

## Evidence

先验知识/题面给定，逻辑校验通过：弹性系数定义为相对变化量之比，ΔShare_low 增加 0.5% 对应 w_boost 增加 0.1（假设基准为 1 或相对变化 10%），计算 0.5%/10% = 5%，数学推导自洽。

## Search Query

elasticity of low quality share to traffic boost in recommendation algorithm
