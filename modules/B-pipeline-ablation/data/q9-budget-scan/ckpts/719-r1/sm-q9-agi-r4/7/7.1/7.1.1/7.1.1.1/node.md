# N732: V100-SXM2 NVLink 理论峰值带宽 300 GB/s 的来源：SXM2 模块有 6 条 NVLink 连接，每条链路 4 通道 x 14 Gbps 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N271

## Claim

V100-SXM2 NVLink 理论峰值带宽 300 GB/s 的来源：SXM2 模块有 6 条 NVLink 连接，每条链路 4 通道 x 14 Gbps x 8 bytes/channel = 448 GB/s 单向？不，NVLink 3.0 每链路 25 GB/s 单向，6 链路共 150 GB/s 单向，300 GB/s 双向。All-reduce 有效带宽受限于 ring algorithm 的 2*(n-1)/n * BW_link。n=4 时，效率 2*(3)/4 = 1.5 倍于单向带宽？不，ring all-reduce 有效带宽 = BW_link * (n-1)/n * 2 (for send+receive)。若 BW_link = 150 GB/s (单向聚合)，则 All-reduce 有效带宽 ≈ 150 * 0.75 * 2 = 225 GB/s。但实际受限于 PCIe 交换和驱动开销，通常降至 60-70%，即 135-157 GB/s。

## Corrected Claim

V100-SXM2 NVLink 理论峰值带宽为 300 GB/s（双向），由 6 条 NVLink 3.0 链路组成，每条链路单向带宽 25 GB/s。All-reduce 有效带宽受 Ring 算法限制，理论上限约为单向聚合带宽的 (n-1)/n 倍（发送+接收叠加后），实际受驱动和拓扑影响通常低于理论值。

## Evidence

[质询]NVLink 3.0 单链路带宽计算存在量级错误：14 Gbps 应为 14 GT/s (Giga Transfers per second)，且 NVLink 3.0 每链路通常为 18 通道（非 4 通道），导致单链路带宽远大于 25 GB/s，进而导致总带宽和 All-reduce 有效带宽估算严重偏低。 | 先验知识/题面给定，逻辑校验发现内部数值矛盾：NVLink 3.0 单链路带宽并非 25 GB/s，而是约 20-25 GB/s 每方向（取决于具体实现，但 6 链路总带宽通常标称为 300 GB/s 双向，即 150 GB/s 单向，这与文中结论一致，但中间推导步骤 '4 通道 x 14 Gbps' 是错误的，因为 4*14*8/8 = 56 GB/s? 不，14 GT/s * 8 bits / 8 = 14 GB/s per channel. 4 channels = 56 GB/s. 文中说 25 GB/s 是错的。实际上 V100 SXM2 NVLink 3.0 每链路 18 通道，每通道 14 GT/s，单向带宽 18 * 14 / 8 = 31.5 GB/s? 不，NVLink 3.0 规格是每链路 25 GB/s 单向吗？查证：V100 SXM2 有 6 个 NVLink 3.0 端口。每个端口 18 通道。每通道 14 GT/s。单向带宽 = 18 * 14 / 8 = 31.5 GB/s? 不对，NVLink 3.0 官方数据是每链路 25 GB/s 单向？不，Tesla V100 SXM2 的 NVLink 总带宽是 300 GB/s 双向。这意味着单向 150 GB/s。6 条链路，每条 25 GB/s 单向。这与文中 'NVLink 3.0 每链路 25 GB/s 单向' 一致。但是前面的推导 '4 通道 x 14 Gbps x 8 bytes/channel' 是完全错误的单位换算和通道数。14 Gbps 是比特率，不是字节率。14 Gbps / 8 = 1.75 GB/s per channel. 4 channels = 7 GB/s. 这与 25 GB/s 不符。正确的推导应该是基于 18 通道或不同的速率定义。虽然最终结论 300 GB/s 双向是正确的（符合 V100 SXM2 规格），但中间的物理推导逻辑混乱且包含错误数值（4 通道 vs 18 通道，Gbps vs GT/s 混淆）。由于 source 为 knowledge，且核心结论（300 GB/s 双向）正确，但推导过程存在硬逻辑错误（量纲/参数错误），根据规则 '存在硬逻辑错误...才判 failed' 或 '逻辑自洽即 verified'。这里逻辑不自洽（推导错误），但结论正确。对于 knowledge 节点，若 challenge 成立且无法排除（即推导确实是错的），应降档。推导确实是错的（4通道是错的，V100 NVLink 3.0 是 18 通道/链路，或者如果是 4 通道那速率不对）。因此逻辑校验不通过（内部矛盾/推导错误），但结论本身是事实。鉴于推导错误严重，判 degraded 更合适，指出推导错误但保留正确结论。

## Search Query

V100 SXM2 NVLink 3.0 theoretical bandwidth all-reduce efficiency ring algorithm
