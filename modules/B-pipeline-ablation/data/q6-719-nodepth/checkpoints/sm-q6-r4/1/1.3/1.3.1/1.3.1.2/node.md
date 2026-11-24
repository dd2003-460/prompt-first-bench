# N222: 在 T=150ms 阈值下，若 H_pop=0.90 且回源延迟 P99(T_origin_fetch_self)=120ms，则 (1-H_pop)*P99(

- **status**: pending
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

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 788)
