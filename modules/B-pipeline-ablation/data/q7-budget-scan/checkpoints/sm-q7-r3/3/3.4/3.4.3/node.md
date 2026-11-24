# N70: 工作点C（RTO=4h, HDD+SSD分层）：SSD层故障恢复快（T_rebuild < 1h），HDD层故障恢复慢（T_rebuild > 24h）；加权平

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

工作点C（RTO=4h, HDD+SSD分层）：SSD层故障恢复快（T_rebuild < 1h），HDD层故障恢复慢（T_rebuild > 24h）；加权平均RTO代价取决于故障概率分布，假设SSD故障概率 10%，HDD 90%，C_rto = 0.1×0 + 0.9×(24-4)h×¥5000/h = ¥90,000

## Corrected Claim

工作点C（RTO=4h, HDD+SSD分层）：SSD层故障恢复快（T_rebuild < 1h），HDD层故障恢复慢（T_rebuild > 24h）；加权平均RTO代价取决于故障概率分布，假设SSD故障概率 10%，HDD 90%，C_rto = 0.1×0 + 0.9×(24-4)h×¥5000/h = ¥90,000

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 776)
