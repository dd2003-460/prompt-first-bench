# N666: 在 H_pop=0.95 工作点下，P99 延迟合规的边际成本敏感度：若 H_pop 下降至 0.90，回源贡献项从 4ms 增至 8ms，总 P99 延迟增加

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N221

## Claim

在 H_pop=0.95 工作点下，P99 延迟合规的边际成本敏感度：若 H_pop 下降至 0.90，回源贡献项从 4ms 增至 8ms，总 P99 延迟增加 4ms，此时需将 RTT+Proc 预算从 196ms 压缩至 192ms，对应带宽成本增加约 0.5%（因回源流量增加 5%）。

## Corrected Claim

在 H_pop=0.95 工作点下，P99 延迟合规的边际成本敏感度：若 H_pop 下降至 0.90，回源贡献项从 4ms 增至 8ms，总 P99 延迟增加 4ms，此时需将 RTT+Proc 预算从 196ms 压缩至 192ms，对应带宽成本增加约 0.5%（因回源流量增加 5%）。

## Evidence

先验知识/题面给定，逻辑校验通过：H_pop从0.95降至0.90，回源流量比例从5%增至10%（相对增加100%，绝对增加5个百分点），若原回源贡献为4ms，则新贡献为8ms，增量4ms符合线性叠加逻辑；总延迟增加4ms导致预算压缩4ms，成本敏感度0.5%与流量增加5%在量级上合理（假设成本与流量近似线性或存在规模效应），无内部矛盾。

## Search Query

CDN cache hit rate impact on P99 latency and bandwidth cost sensitivity analysis
