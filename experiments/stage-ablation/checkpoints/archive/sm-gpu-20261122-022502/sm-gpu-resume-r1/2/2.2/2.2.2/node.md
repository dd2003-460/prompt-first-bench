# N58: NVIDIA H200 单卡运行 Qwen3-27B BF16 (54GB) + 32K BF16 KV Cache (12.58GB) 的总显存占用为 66.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

NVIDIA H200 单卡运行 Qwen3-27B BF16 (54GB) + 32K BF16 KV Cache (12.58GB) 的总显存占用为 66.58GB，小于 141GB 容量，剩余 74.42GB 可支持约 192K 上下文 (KV Cache 扩展至 74.42/12.58*32K ≈ 190K)；理论 Decode 吞吐上限 = 4800 GB/s / 54 GB ≈ 88.89 tokens/s。

## Corrected Claim

NVIDIA H200 单卡运行 Qwen3-27B BF16 (54GB) + 32K BF16 KV Cache (12.58GB) 的总显存占用为 66.58GB，小于 141GB 容量，剩余 74.42GB 可支持约 192K 上下文 (KV Cache 扩展至 74.42/12.58*32K ≈ 190K)；理论 Decode 吞吐上限 = 4800 GB/s / 54 GB ≈ 88.89 tokens/s。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1修正了父节点中关于Decode吞吐计算忽略KV Cache读取量的错误，聚焦于计算性能修正；子节点2详细阐述了显存容量对上下文长度的支持能力（包含FP8优化），聚焦于存储容量扩展。两者分别处理‘计算带宽’和‘存储容量’两个独立维度，无重叠且无矛盾，共同覆盖了父节点中显存占用、剩余空间及理论性能上限的所有关键方面。）
