# N532: N173 工作点下，实时内容回源延迟 L_backhaul_realtime = L_prop + L_processing_origin，因实时内容无法边缘缓

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N173

## Claim

N173 工作点下，实时内容回源延迟 L_backhaul_realtime = L_prop + L_processing_origin，因实时内容无法边缘缓存，每次请求均回源，若 L_backhaul_realtime > T_P99_target，则该部分流量直接导致 P99 超标，需计算超标概率 P_exceed = P(latency > T) * f_realtime。

## Corrected Claim

N173 工作点下，实时内容回源延迟 L_backhaul_realtime = L_prop + L_processing_origin，因实时内容无法边缘缓存，每次请求均回源，若 L_backhaul_realtime > T_P99_target，则该部分流量直接导致 P99 超标，需计算超标概率 P_exceed = P(latency > T) * f_realtime。

## Evidence

先验知识/题面给定，逻辑校验通过：实时内容无法缓存导致每次回源，延迟构成符合物理直觉，超标概率公式逻辑自洽。
