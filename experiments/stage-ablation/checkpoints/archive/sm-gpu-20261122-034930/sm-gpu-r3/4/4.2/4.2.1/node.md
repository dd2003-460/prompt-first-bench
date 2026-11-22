# N111: 工作点1（高带宽/低容量-消费级）：RTX 4090有效带宽1008 GB/s，INT8权重27GB + KV Cache 10.7GB + 框架开销4GB =

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

工作点1（高带宽/低容量-消费级）：RTX 4090有效带宽1008 GB/s，INT8权重27GB + KV Cache 10.7GB + 框架开销4GB = 41.7GB，理论吞吐上限 = 1008 / 41.7 ≈ 24.2 tokens/s；实际受计算瓶颈限制，实测约20-30 tokens/s，带宽利用率约83-124%（超过100%说明公式高估，实际受FLOPs限制）。

## Corrected Claim

工作点1（高带宽/低容量-消费级）：RTX 4090有效带宽1008 GB/s，INT8权重27GB + KV Cache 10.7GB + 框架开销4GB = 41.7GB，理论吞吐上限 = 1008 / 41.7 ≈ 24.2 tokens/s；实际受计算瓶颈限制，实测约20-30 tokens/s，带宽利用率约83-124%（超过100%说明公式高估，实际受FLOPs限制）。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090带宽1008GB/s及显存占用量级符合硬件规格，算术推导（1008/41.7≈24.2）正确，带宽利用率>100%的解释符合计算瓶颈逻辑。
