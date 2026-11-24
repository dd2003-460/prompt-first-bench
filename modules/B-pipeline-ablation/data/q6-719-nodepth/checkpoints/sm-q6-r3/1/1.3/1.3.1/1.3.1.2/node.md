# N222: 在 T=150ms 阈值下，若 H_pop=0.90 且回源延迟 P99(T_origin_fetch_self)=120ms，则 (1-H_pop)*P99(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

在 T=150ms 阈值下，若 H_pop=0.90 且回源延迟 P99(T_origin_fetch_self)=120ms，则 (1-H_pop)*P99(T_origin_fetch_self) = 12ms，该工作点下回源延迟贡献占比显著，需确保 RTT+Proc 之和 < 138ms 才能合规

## Corrected Claim

在 T=150ms 阈值下，若 H_pop=0.90 且回源延迟 P99(T_origin_fetch_self)=120ms，则 (1-H_pop)*P99(T_origin_fetch_self) = 12ms，该工作点下回源延迟贡献占比显著，需确保 RTT+Proc 之和 < 138ms 才能合规

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 (1-0.90)*120ms = 12ms 正确；剩余预算 150ms - 12ms = 138ms 推导正确；逻辑自洽且数值量级合理。
