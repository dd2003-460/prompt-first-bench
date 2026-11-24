# N110: 故障对缓存命中率 H(t) 的冲击：单 POP 故障导致其本地缓存失效，该 POP 承载的 10% 流量全部回源，H_effective 从稳态 85% 降至 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

故障对缓存命中率 H(t) 的冲击：单 POP 故障导致其本地缓存失效，该 POP 承载的 10% 流量全部回源，H_effective 从稳态 85% 降至 76.5%（85%×90% + 0%×10%）；回源率从 15% 升至 23.5%，回源带宽成本增加 56.7%，同时回源延迟从 20ms 升至 80ms，P99 延迟额外增加 60ms×23.5% = 14.1ms（加权平均）。

## Corrected Claim

故障对缓存命中率 H(t) 的冲击：单 POP 故障导致其本地缓存失效，该 POP 承载的 10% 流量全部回源，H_effective 从稳态 85% 降至 76.5%（85%×90% + 0%×10%）；回源率从 15% 升至 23.5%，回源带宽成本增加 56.7%，同时回源延迟从 20ms 升至 80ms，P99 延迟额外增加 60ms×23.5% = 14.1ms（加权平均）。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 10 column 5 (char 739)
