# N221: LRU 缓存命中率 60% 的敏感性分析：命中率 H 对有效 QPS 的提升公式为 QPS_eff = QPS_limit / (1 - H * (1 - T_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63, N64, N65

## Claim

LRU 缓存命中率 60% 的敏感性分析：命中率 H 对有效 QPS 的提升公式为 QPS_eff = QPS_limit / (1 - H * (1 - T_cache/T_req))。当 T_cache << T_req 时，QPS_eff ≈ 1/(1-H)。若 H 从 60% 降至 40%（因 TTL=24h 过短或查询多样性高），QPS_eff 从 2.5 req/s 降至 1.67 req/s，导致检索队列积压，T_retrieval 从 800ms 上升至 2.4s。

## Corrected Claim

LRU 缓存命中率 60% 的敏感性分析：命中率 H 对有效 QPS 的提升公式为 QPS_eff = QPS_limit / (1 - H * (1 - T_cache/T_req))。当 T_cache << T_req 时，QPS_eff ≈ 1/(1-H)。若 H 从 60% 降至 40%（因 TTL=24h 过短或查询多样性高），QPS_eff 从 2.5 req/s 降至 1.67 req/s，导致检索队列积压，T_retrieval 从 800ms 上升至 2.4s。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合排队论基本逻辑，数值计算（1/(1-0.6)=2.5, 1/(1-0.4)=1.67）准确，量级合理。
