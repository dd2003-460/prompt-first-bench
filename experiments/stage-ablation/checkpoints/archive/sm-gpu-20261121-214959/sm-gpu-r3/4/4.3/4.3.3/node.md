# N95: 工作点 B3 (高成本低性/冗余)：1x H200 (141GB) 运行 BF16 Qwen3-27B (54GB) + BF16 KV Cache (12.5

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

工作点 B3 (高成本低性/冗余)：1x H200 (141GB) 运行 BF16 Qwen3-27B (54GB) + BF16 KV Cache (12.58GB) = 66.58GB < 141GB。理论 Decode 上限 ≈ 4800 GB/s / 54 GB ≈ 88.9 tokens/s。CapEx ≈ $35,000。

## Corrected Claim

工作点 B3 (高成本低性/冗余)：1x H200 (141GB) 运行 BF16 Qwen3-27B (54GB) + BF16 KV Cache (12.58GB) = 66.58GB < 141GB。理论 Decode 上限 ≈ 4800 GB/s / 54 GB ≈ 88.9 tokens/s。CapEx ≈ $35,000。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别聚焦于性能（Decode吞吐）、经济性（TCO对比）和容量/并发（Batch Size限制），维度清晰且互不重叠，完整覆盖了父节点中关于性能、成本和显存利用的关键信息。）
