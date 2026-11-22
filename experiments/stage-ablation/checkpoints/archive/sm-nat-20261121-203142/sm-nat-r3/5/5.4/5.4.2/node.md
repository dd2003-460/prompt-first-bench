# N73: 真实 CDN 运维案例中的折损系数：在 u=0.01/day 的基准场景下，主流 CDN（如 Cloudflare, Akamai）报告的 LRU 有效命中率相

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

真实 CDN 运维案例中的折损系数：在 u=0.01/day 的基准场景下，主流 CDN（如 Cloudflare, Akamai）报告的 LRU 有效命中率相对静态命中率的折损系数 δ 实际值范围为 0.98-0.995，即折损 0.5%-2%，该数值来源于厂商公开的技术白皮书或运维报告，需区分不同对象大小分布下的差异 [待核验]

## Corrected Claim

在真实CDN运维中，LRU有效命中率相对静态命中率存在一定折损，具体折损系数δ取决于对象大小分布与缓存策略，通常认为折损幅度较小（如1%-2%量级），但具体数值需依据特定场景的实测数据确定，缺乏统一的公开基准值。

## Evidence

[质询]该陈述声称具体数值范围（0.98-0.995）来源于厂商公开的技术白皮书或运维报告，但主流CDN厂商（如Cloudflare, Akamai）极少在公开文档中披露如此具体的内部LRU折损系数统计值，且该数值高度依赖于对象大小分布、缓存策略及流量特征，缺乏公开可查的直接证据支持其作为通用基准。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且该具体数值属于未公开的内部运维指标，无法从第一性原理推导，亦无外部来源直接证实）。

## Search Query

CDN LRU cache hit rate reduction object update rate 1% per day real world case study
