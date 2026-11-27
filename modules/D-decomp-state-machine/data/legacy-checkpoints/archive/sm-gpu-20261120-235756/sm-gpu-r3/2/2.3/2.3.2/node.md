# N62: 在 BF16 精度、32K 上下文、单流推理下，RTX 4090 的理论 TPOT ≈ (6.6 GB + 4 GB) / 1008 GB/s ≈ 10.5 m

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

在 BF16 精度、32K 上下文、单流推理下，RTX 4090 的理论 TPOT ≈ (6.6 GB + 4 GB) / 1008 GB/s ≈ 10.5 ms/token (约 95 tokens/s)，A100 80GB ≈ (6.6 GB + 4 GB) / 2039 GB/s ≈ 5.2 ms/token (约 192 tokens/s)，RTX 5090 ≈ (6.6 GB + 4 GB) / 1792 GB/s ≈ 5.9 ms/token (约 169 tokens/s)，显示带宽差异直接导致吞吐差异。

## Corrected Claim

在 BF16 精度、32K 上下文、单流推理下，RTX 4090 的理论 TPOT ≈ (6.6 GB + 4 GB) / 1008 GB/s ≈ 10.5 ms/token (约 95 tokens/s)，A100 80GB ≈ (6.6 GB + 4 GB) / 2039 GB/s ≈ 5.2 ms/token (约 192 tokens/s)，RTX 5090 ≈ (6.6 GB + 4 GB) / 1792 GB/s ≈ 5.9 ms/token (约 169 tokens/s)，显示带宽差异直接导致吞吐差异。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点2和子节点3在核心论点上高度重复（均指出RTX 5090/4090在BF16 32K下显存不足导致方案不可行），且子节点1忽略了显存可行性这一关键约束，仅讨论带宽理论值，与子节点2/3的“不可行”结论存在逻辑上的不协调（虽非直接矛盾，但缺乏统一前提）。此外，三个子节点中关于显存溢出的描述存在冗余。）

## Search Query

Qwen3-27B inference benchmark RTX 4090 A100 H100 tokens per second
