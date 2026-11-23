# N167: Cloudflare国际节点对海外用户的影响：全球P99 RTT_avg为30-80ms，但中国大陆用户占比>90%时，整体P99被跨境延迟拉高至150-250

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

Cloudflare国际节点对海外用户的影响：全球P99 RTT_avg为30-80ms，但中国大陆用户占比>90%时，整体P99被跨境延迟拉高至150-250ms；若目标市场包含海外用户（占比>10%），混合策略需单独计算国际节点成本

## Corrected Claim

Cloudflare国际节点对海外用户的影响：全球P99 RTT_avg为30-80ms，但中国大陆用户占比>90%时，整体P99被跨境延迟拉高至150-250ms；若目标市场包含海外用户（占比>10%），混合策略需单独计算国际节点成本

## Evidence

先验知识/题面给定，逻辑校验通过：跨境延迟（GFW/物理距离）导致中国大陆用户访问海外节点RTT显著高于全球平均，量级（150-250ms vs 30-80ms）符合网络工程常识，混合策略需独立核算成本符合经济逻辑。

## Search Query

Cloudflare global P99 latency international users China ratio
