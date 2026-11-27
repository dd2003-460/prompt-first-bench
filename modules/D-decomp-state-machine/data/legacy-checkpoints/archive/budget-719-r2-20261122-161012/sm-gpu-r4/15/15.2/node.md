# N322: Decode 阶段单 Token 延迟的理论计算公式为 T_decode = (W_bytes + KV_bytes) / (Bandwidth * Utili

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N138

## Claim

Decode 阶段单 Token 延迟的理论计算公式为 T_decode = (W_bytes + KV_bytes) / (Bandwidth * Utilization)，其中 W_bytes 为量化后权重大小，KV_bytes 为当前上下文长度下的 KV Cache 占用，Bandwidth 为显存带宽。

## Corrected Claim

Decode 阶段单 Token 延迟的理论计算公式为 T_decode = (W_bytes + KV_bytes) / (Bandwidth * Utilization)，其中 W_bytes 为量化后权重大小，KV_bytes 为当前上下文长度下的 KV Cache 占用，Bandwidth 为显存带宽。

## Evidence

先验知识/题面给定，逻辑校验通过
