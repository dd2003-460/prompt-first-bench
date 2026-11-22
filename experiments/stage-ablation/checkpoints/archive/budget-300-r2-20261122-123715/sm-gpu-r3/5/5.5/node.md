# N101: AMD MI300X 显存带宽为 5.3 TB/s (HBM3)，运行 Qwen3-27B BF16 (54GB) + 32K 上下文 (KV 36GB + A

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23, N24, N25

## Claim

AMD MI300X 显存带宽为 5.3 TB/s (HBM3)，运行 Qwen3-27B BF16 (54GB) + 32K 上下文 (KV 36GB + Act 5GB = 95GB)，显存充足且带宽极高，理论解码吞吐 ≈ 5300 GB/s / 95GB ≈ 55.8 tokens/s，实际效率系数 0.8 下为 44.6 tokens/s。

## Corrected Claim

AMD MI300X 显存带宽为 5.3 TB/s (HBM3)，运行 Qwen3-27B BF16 (54GB) + 32K 上下文 (KV 36GB + Act 5GB = 95GB)，显存充足且带宽极高，理论解码吞吐 ≈ 5300 GB/s / 95GB ≈ 55.8 tokens/s，实际效率系数 0.8 下为 44.6 tokens/s。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于显存占用的精确计算与容量验证，子节点2聚焦于解码吞吐公式的分母修正与理论上限验证。两者分别处理“空间（显存）”和“时间（速度）”两个不同维度，逻辑正交。父节点中的核心结论（显存充足、吞吐估算）被两个子节点分别拆解为具体的计算依据和修正逻辑，覆盖了父节点的关键论证点。）
