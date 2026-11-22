# N129: 交叉点延迟L*的量化定义：L* = min{L | (Latency_Ncard(L) - Latency_1card(L)) / Latency_1card(

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

交叉点延迟L*的量化定义：L* = min{L | (Latency_Ncard(L) - Latency_1card(L)) / Latency_1card(L) < (TCO_1card - TCO_Ncard) / TCO_1card}，即多卡方案的延迟优势百分比必须超过其TCO劣势百分比时的延迟阈值

## Corrected Claim

交叉点延迟L*的量化定义：L* = min{L | (Latency_Ncard(L) - Latency_1card(L)) / Latency_1card(L) < (TCO_1card - TCO_Ncard) / TCO_1card}，即多卡方案的延迟优势百分比必须超过其TCO劣势百分比时的延迟阈值

## Evidence

先验知识/题面给定，逻辑校验通过
