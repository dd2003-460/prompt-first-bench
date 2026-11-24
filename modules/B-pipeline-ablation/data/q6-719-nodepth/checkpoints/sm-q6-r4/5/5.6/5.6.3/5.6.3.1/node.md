# N477: 公有云CDN规模折扣实际执行条件：Q_total > 50TB/月 时，基础折扣 D_base = 0.6，但若叠加年付承诺（12个月）可再降 10%，最终 D

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N155

## Claim

公有云CDN规模折扣实际执行条件：Q_total > 50TB/月 时，基础折扣 D_base = 0.6，但若叠加年付承诺（12个月）可再降 10%，最终 D_final = 0.54；若仅月付则维持 D_final = 0.6。

## Corrected Claim

公有云CDN通常提供基于流量规模（如月流量超过一定阈值）和付费周期（如年付承诺）的阶梯折扣，具体折扣率（如基础折扣0.6，年付再降10%）因厂商和合同条款而异，需参考具体服务商的最新报价单。

## Evidence

[质询]具体数值（50TB阈值、0.6基础折扣、10%年付优惠）属于特定云厂商的商业定价策略，不同厂商（如阿里云、AWS、Cloudflare）差异巨大，且随时间动态调整，无法作为通用事实成立。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该事实为具体商业参数，非第一性原理可推导）。

## Search Query

Alibaba Cloud CDN annual commitment discount tier 50TB monthly
