# N133: 显存带宽瓶颈修正：实际吞吐量公式需除以权重精度字节数，即 Throughput = Bandwidth / (Weight_Size_GB * Precisio

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

显存带宽瓶颈修正：实际吞吐量公式需除以权重精度字节数，即 Throughput = Bandwidth / (Weight_Size_GB * Precision_Bytes + Activation_GB + KV_Cache_GB)，因为带宽是字节/秒，而权重大小通常以参数量计，必须统一单位

## Corrected Claim

显存带宽瓶颈修正：实际吞吐量公式需除以权重精度字节数，即 Throughput = Bandwidth / (Weight_Size_GB * Precision_Bytes + Activation_GB + KV_Cache_GB)，因为带宽是字节/秒，而权重大小通常以参数量计，必须统一单位

## Evidence

父节点级核验未通过：非正交, 不完备（子节点与父节点存在严重逻辑矛盾且未覆盖核心内容。父节点明确定义吞吐量瓶颈为显存带宽，公式核心项为除以总数据量（权重+激活+KV Cache）。然而，子节点1引入了'通信开销'和'互联带宽'，这属于分布式/多卡场景的额外瓶颈，与父节点聚焦的单卡/本地显存带宽修正不符，且公式形式完全不同，导致概念混淆。子节点2讨论的是计算与内存的边界条件（Roofline模型），虽然相关，但并未解释父节点公式中具体的'单位统一'修正逻辑（即如何从参数量转换为字节数），且引入了新的阈值变量，偏离了父节点关于'除以权重精度字节数'这一特定修正点的主题。）
