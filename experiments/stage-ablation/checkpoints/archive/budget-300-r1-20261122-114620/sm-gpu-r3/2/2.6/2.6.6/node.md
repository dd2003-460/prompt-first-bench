# N84: KV Cache 对 Decode 吞吐的边际影响：每增加 1K tokens 上下文，KV Cache 增加约 0.05GB (基于 N7 公式修正)，导致 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

KV Cache 对 Decode 吞吐的边际影响：每增加 1K tokens 上下文，KV Cache 增加约 0.05GB (基于 N7 公式修正)，导致 RTX 4090 的 Decode 吞吐下降约 0.1% (0.05/54.05)，影响可忽略；但在 32K 上下文下，KV 占用约 1.6GB，总带宽需求增加 3%，吞吐下降约 3%

## Corrected Claim

KV Cache 对 Decode 吞吐的边际影响：每增加 1K tokens 上下文，KV Cache 增加约 0.05GB (基于 N7 公式修正)，导致 RTX 4090 的 Decode 吞吐下降约 0.1% (0.05/54.05)，影响可忽略；但在 32K 上下文下，KV 占用约 1.6GB，总带宽需求增加 3%，吞吐下降约 3%

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别从公式定义/参数修正、带宽占比计算、显存容量限制三个不同维度展开，逻辑清晰且无重叠。它们共同修正了父节点中关于数值估算（0.05GB vs 0.0268GB）和归因错误（带宽瓶颈 vs 容量限制）的问题，覆盖了父节点提及的所有关键方面（KV大小、带宽影响、具体场景分析）。）
