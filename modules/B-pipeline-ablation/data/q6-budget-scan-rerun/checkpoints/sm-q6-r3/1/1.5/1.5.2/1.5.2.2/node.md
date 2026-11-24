# N166: 地理分布 40/60（核心/长尾）下的混合策略P99解析：P99_hybrid ≈ w_core * P99_core + w_tail * P99_tail，

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N50

## Claim

地理分布 40/60（核心/长尾）下的混合策略P99解析：P99_hybrid ≈ w_core * P99_core + w_tail * P99_tail，其中 w_core=0.4, w_tail=0.6，假设 P99_core=250ms, P99_tail=160ms，则 P99_hybrid ≈ 0.4*250 + 0.6*160 = 196ms，此值显示长尾区域的高命中率（低P99）对整体P99有显著拉低作用，但若长尾区域P99因低命中率升至190ms（N135），则 P99_hybrid ≈ 0.4*250 + 0.6*190 = 214ms，仍优于60/40分布下的260ms，表明地理分布向长尾倾斜有利于混合策略延迟表现。

## Corrected Claim

在地理分布40/60（核心/长尾）下，混合策略的整体P99延迟需通过合并核心与长尾区域的请求延迟分布后重新计算第99百分位数得出，而非简单加权平均。若长尾区域P99因低命中率升高，整体P99将显著上升，具体数值需基于实际延迟分布数据模拟，不能仅凭子集P99线性插值。

## Evidence

[质询]该陈述存在严重的统计学逻辑谬误：P99（第99百分位数）是顺序统计量，不具备线性可加性。混合分布的P99不能通过各子分布P99的加权平均（0.4*250 + 0.6*160）直接计算得出。实际上，混合分布的P99取决于累积分布函数（CDF）的叠加，若长尾部分占比60%且其P99为160ms，整体P99通常会更接近长尾部分的尾部特征，而非简单的算术平均。此外，'60/40分布下的260ms'这一对比基准缺乏推导过程，属于无依据的经验断言。 | source=knowledge，但逻辑校验失败：P99作为分位数指标不可线性加权平均，该数学推导违背基本统计学原理，属于硬逻辑错误。

## Search Query

CDN P99 latency geographic distribution weighted average tail region
