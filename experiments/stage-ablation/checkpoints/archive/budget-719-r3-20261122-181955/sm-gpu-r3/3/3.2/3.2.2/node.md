# N94: ITL (Inter-Token Latency) 计算公式为 ITL = 1 / Throughput_decode；在 32K 上下文下，RTX 4090 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

ITL (Inter-Token Latency) 计算公式为 ITL = 1 / Throughput_decode；在 32K 上下文下，RTX 4090 的 ITL 预计约为 1 / 11.5 ≈ 87 ms/token (理论) 至 120-150 ms/token (实测)，而 A100 80GB 的 ITL 预计约为 1 / 23.5 ≈ 42 ms/token (理论) 至 60-80 ms/token (实测)；ITL 直接决定生成阶段的流畅度。

## Corrected Claim

ITL (Inter-Token Latency) 计算公式为 ITL = 1 / Throughput_decode；在 32K 上下文下，RTX 4090 的 ITL 预计约为 1 / 11.5 ≈ 87 ms/token (理论) 至 120-150 ms/token (实测)，而 A100 80GB 的 ITL 预计约为 1 / 23.5 ≈ 42 ms/token (理论) 至 60-80 ms/token (实测)；ITL 直接决定生成阶段的流畅度。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 正交性违规：子节点2、3、4在逻辑上严重重叠，它们都是基于同一物理模型（内存带宽瓶颈）对同一公式（ITL下限）在不同硬件/量化条件下的实例化计算，而非独立的概念维度。2. 完备性缺失：父节点明确提到'实测'范围（如120-150ms），但所有子节点仅提供了'理论下限'计算，完全缺失对'实测值偏离理论值原因'（如计算延迟、PCIe传输、调度开销等）的分解，无法解释父节点中提到的实测数据。3. 冗余严重：子节点2、3、4本质上是同一个公式 `ITL_min = 1 / (Bandwidth / (Weight_Size + KV_Size))` 的三个不同参数代入案例，应合并为一个包含参数表的节点，或作为父节点的属性，而非并列子节点。）
