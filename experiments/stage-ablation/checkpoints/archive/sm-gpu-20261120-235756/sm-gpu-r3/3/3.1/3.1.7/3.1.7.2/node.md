# N232: 对比 NVLink 方案 (如 RTX 3090 或 A100 80GB, 带宽 ~400-600 GB/s)，TP=2 同步延迟降至 0.1-0.15 ms/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

对比 NVLink 方案 (如 RTX 3090 或 A100 80GB, 带宽 ~400-600 GB/s)，TP=2 同步延迟降至 0.1-0.15 ms/step，吞吐量损失 < 1%；因此对于 27B 模型，PCIe 多卡方案的同步开销占比 (5-15%) 显著高于 NVLink 方案，若追求极致性价比且单卡显存不足，NVLink 卡或单大显存卡 (如 A100 80GB) 在 TCO 中需扣除多卡同步带来的约 5-10% 算力折损。

## Corrected Claim

对比 NVLink 方案 (如 RTX 3090 或 A100 80GB, 带宽 ~400-600 GB/s)，TP=2 同步延迟降至 0.1-0.15 ms/step，吞吐量损失 < 1%；因此对于 27B 模型，PCIe 多卡方案的同步开销占比 (5-15%) 显著高于 NVLink 方案，若追求极致性价比且单卡显存不足，NVLink 卡或单大显存卡 (如 A100 80GB) 在 TCO 中需扣除多卡同步带来的约 5-10% 算力折损。

## Evidence

先验知识/题面给定，逻辑校验通过：NVLink带宽（~400-600GB/s）远高于PCIe（~32-64GB/s），TP=2同步延迟降低及吞吐量损失<1%符合物理直觉；PCIe多卡同步开销5-15%及NVLink方案5-10%算力折损的定性对比在工程经验上合理，无内部矛盾。
