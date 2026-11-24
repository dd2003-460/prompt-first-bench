# N221: 在 T=200ms 阈值下，若 H_pop=0.95 且回源延迟 P99(T_origin_fetch_self)=80ms，则 (1-H_pop)*P99(T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

在 T=200ms 阈值下，若 H_pop=0.95 且回源延迟 P99(T_origin_fetch_self)=80ms，则 (1-H_pop)*P99(T_origin_fetch_self) = 4ms，该工作点下回源延迟贡献占比 < 3%，P99_self 主要受 RTT 主导

## Corrected Claim

在 T=200ms 阈值下，若 H_pop=0.95 且回源延迟 P99(T_origin_fetch_self)=80ms，则 (1-H_pop)*P99(T_origin_fetch_self) = 4ms，该工作点下回源延迟贡献占比 < 3%，P99_self 主要受 RTT 主导

## Evidence

先验知识/题面给定，逻辑校验通过：计算 (1-0.95)*80ms = 4ms 正确；4ms 占 200ms 阈值的 2% (<3%)，且 4ms 远小于典型 RTT 量级，结论自洽。
