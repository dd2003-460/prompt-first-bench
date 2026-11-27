# N76: 双RTX 4090方案中，NVLink不可用，仅通过PCIe 4.0 x16互联，KV Cache分片导致的AllReduce通信开销使得有效吞吐量仅为单卡线性

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

双RTX 4090方案中，NVLink不可用，仅通过PCIe 4.0 x16互联，KV Cache分片导致的AllReduce通信开销使得有效吞吐量仅为单卡线性扩展的60-70%（即2x4090实际吞吐约等于1.2-1.4x单卡4090），而单卡H100无此互联瓶颈，需将此效率折损纳入TCO对比。

## Corrected Claim

双RTX 4090方案中，NVLink不可用，仅通过PCIe互联（注：4090支持PCIe 5.0，非4.0），KV Cache分片导致的通信开销使得有效吞吐量显著低于线性扩展，具体效率取决于模型规模与并行策略，实测案例显示约为单卡线性扩展的60-70%（即2x4090实际吞吐约等于1.2-1.4x单卡4090），而单卡H100无此互联瓶颈，需将此效率折损纳入TCO对比。

## Evidence

[质询]陈述中关于“有效吞吐量仅为单卡线性扩展的60-70%”的具体数值缺乏通用性，该比例高度依赖于模型架构（如Transformer层数、KV Cache大小）、序列长度及具体并行策略（如是否使用ZeRO-Offload或流水线并行），并非硬件互联的固定物理常数；此外，来源[2]提到的“训练速度只提升了大约30%”（即总吞吐为1.3x，效率65%）虽在数值范围内，但属于特定场景（70B微调）的个案，不能直接推广为所有双卡4090方案的通用结论。 | 来源[1][3]直接支持“RTX 4090不支持NVLink，仅通过PCIe互联”这一硬件事实；来源[2]提供了“双卡4090跑70B模型吞吐提升约30%”的间接证据，与60-70%效率区间兼容，但该具体效率数值为经验事实且依赖具体负载，缺乏多源一致的直接定量支持，故降级。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_31220401/article/details/164531290&rut=236857488d674f8f21481a0f7b8759e188b1e9b400492cd6c086d15c6ca9247f', 'type': 'ddg', 'title': 'RTX 4090多卡互联带宽解析：PCIe 5.0与NVLink实战对比-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_29164843/article/details/165141223&rut=a53563dbd4547415c14890470be06763bb18c045d1f80750138c3b1a449141a2', 'type': 'ddg', 'title': 'RTX 4090多卡互联：PCIe 5.0与NVLink带宽之争实测解析-CSDN博客'}
- {'url': 'https://ask.csdn.net/questions/8608724&rut=16e6aeceb19631a1d8ee3001da53c81269444975a5d091cade321d0f25c11114', 'type': 'ddg', 'title': '问题：4090显卡不支持NVLink，如何实现高效多卡训练？_编程语言-CSDN问答'}
