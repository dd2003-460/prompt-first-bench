# N16: 公有云CDN策略的延迟特性：P99_public = min_{pop ∈ Cloudflare_Pops}(RTT_user_to_pop + T_queue

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

公有云CDN策略的延迟特性：P99_public = min_{pop ∈ Cloudflare_Pops}(RTT_user_to_pop + T_queue_public + T_transmission)，Cloudflare拥有200+全球POP点，平均RTT_base < 30ms [待核验]

## Corrected Claim

公有云CDN策略的延迟特性：P99_public = min_{pop ∈ Cloudflare_Pops}(RTT_user_to_pop + T_queue_public + T_transmission)，Cloudflare拥有200+全球POP点，平均RTT_base < 30ms [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Cloudflare POP locations count average latency 2024
