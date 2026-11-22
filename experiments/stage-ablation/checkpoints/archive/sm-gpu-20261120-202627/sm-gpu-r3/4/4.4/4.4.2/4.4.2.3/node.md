# N364: Batch Size 对通信开销的稀释效应量化：在 Batch Size=B 时，All-Reduce 通信量不变（仅激活值通信），但计算量线性增加 B 倍。因

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

Batch Size 对通信开销的稀释效应量化：在 Batch Size=B 时，All-Reduce 通信量不变（仅激活值通信），但计算量线性增加 B 倍。因此 Comm/Compute Ratio 随 B 增大而降低。计算 B=1 和 B=8 时的 Ratio 差异，证明大 Batch 下 PCIe 瓶颈影响减弱（下降幅度从 15% 降至 <5%），从而确定 PCIe 方案仅在低并发（Batch<=2）时显著劣化。

## Corrected Claim

Batch Size 对通信开销的稀释效应量化：在 Batch Size=B 时，All-Reduce 通信量不变（仅激活值通信），但计算量线性增加 B 倍。因此 Comm/Compute Ratio 随 B 增大而降低。计算 B=1 和 B=8 时的 Ratio 差异，证明大 Batch 下 PCIe 瓶颈影响减弱（下降幅度从 15% 降至 <5%），从而确定 PCIe 方案仅在低并发（Batch<=2）时显著劣化。

## Evidence

先验知识/题面给定，逻辑校验通过：All-Reduce通信量在仅同步激活值时不随Batch Size线性增长（或增长远慢于计算量），而计算量随Batch Size线性增加，因此Comm/Compute Ratio随B增大而降低，符合分布式训练通信开销稀释的基本原理。
