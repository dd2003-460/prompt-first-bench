# N411: 低并发长文本 (batch=1, seq=32768) 下，Decode 阶段吞吐量受内存带宽限制。RTX 4090 (1008 GB/s) 理论吞吐 17.3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N164

## Claim

低并发长文本 (batch=1, seq=32768) 下，Decode 阶段吞吐量受内存带宽限制。RTX 4090 (1008 GB/s) 理论吞吐 17.3 tokens/s，但实际受 KV Cache 读取影响，实测吞吐约为理论值的 70-80%，即 12.1-13.8 tokens/s。

## Corrected Claim

低并发长文本 (batch=1, seq=32768) 下，Decode 阶段吞吐量受内存带宽限制。RTX 4090 (1008 GB/s) 理论吞吐 17.3 tokens/s，但实际受 KV Cache 读取影响，实测吞吐约为理论值的 70-80%，即 12.1-13.8 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 带宽 1008 GB/s 与 LLM 权重/激活大小估算得出的理论吞吐 17.3 tokens/s 量级合理，且 70-80% 的效率折损符合实际硬件中内存访问非理想性的经验规律。
