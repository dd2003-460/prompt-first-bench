# N138: 2× RTX 4090 部署 vLLM 时，由于缺乏 NVLink，张量并行 (TP=2) 的通信开销占比从单卡方案的 ~0% 上升至 ~15-20% (基于 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N45, N46, N47

## Claim

2× RTX 4090 部署 vLLM 时，由于缺乏 NVLink，张量并行 (TP=2) 的通信开销占比从单卡方案的 ~0% 上升至 ~15-20% (基于 batch_size=1, seq_len=32K 估算)，导致实际吞吐量 (tokens/s) 相比理论带宽上限下降 15-20%。

## Corrected Claim

2× RTX 4090 部署 vLLM 时，由于缺乏 NVLink，张量并行 (TP=2) 的通信开销相比单卡方案显著上升（在长序列、小 batch 场景下估算约为 10-20%），导致实际吞吐量相比理论带宽上限出现明显下降。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 648)
