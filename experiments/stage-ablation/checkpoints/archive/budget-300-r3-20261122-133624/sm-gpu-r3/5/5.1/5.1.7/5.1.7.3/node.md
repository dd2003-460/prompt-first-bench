# N353: 2× RTX 3090 方案的替代互联拓扑评估：若使用 NVLink Bridge (Ampere 支持)，带宽提升至 112.5 GB/s (双向)，通信延迟

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N118

## Claim

2× RTX 3090 方案的替代互联拓扑评估：若使用 NVLink Bridge (Ampere 支持)，带宽提升至 112.5 GB/s (双向)，通信延迟降至约 17ms/层，总通信开销约 476ms/token，吞吐降至约 2.1 tokens/s；仍远低于单卡 H100 的 64.2 tokens/s，证明 PCIe/NVLink 互联的多卡方案在 27B 模型上不具备性价比优势。

## Corrected Claim

2× RTX 3090 使用 NVLink Bridge 互联时，带宽提升至 112.5 GB/s (双向)，但具体通信延迟和吞吐需根据并行策略（如张量并行/流水线并行）重新计算，原陈述中 17ms/层延迟和 2.1 tokens/s 吞吐缺乏合理依据，无法直接证明其不具备性价比优势。

## Evidence

[质询]数值量级与物理直觉严重不符：17ms/层的通信延迟对于NVLink互联而言极高（通常应为微秒级），且476ms/token的总通信开销导致吞吐仅2.1 tokens/s，远低于单卡H100的64.2 tokens/s，这与NVLink高带宽低延迟的设计初衷及多卡并行通常提升或至少不显著降低单token延迟（在合理并行策略下）的经验事实相悖，疑似混淆了通信延迟与计算延迟，或使用了错误的并行策略假设。 | 先验知识/题面给定，逻辑校验未通过：NVLink带宽112.5GB/s合理，但17ms/层延迟及2.1 tokens/s吞吐在27B模型多卡方案中极不合理，违背基本通信/计算比例直觉。
