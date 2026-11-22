# N53: PCIe P2P (Peer-to-Peer) 通信在消费级主板上的支持度受限，许多主板 BIOS 默认禁用 P2P 或存在稳定性问题，导致跨卡数据传输需经过 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

PCIe P2P (Peer-to-Peer) 通信在消费级主板上的支持度受限，许多主板 BIOS 默认禁用 P2P 或存在稳定性问题，导致跨卡数据传输需经过 CPU 内存中转，带宽降至 PCIe 3.0 x4 水平 (4 GB/s) 或更低，使通信开销增加 8 倍，需在部署前验证主板和 CPU 的 P2P 支持情况。

## Corrected Claim

PCIe P2P (Peer-to-Peer) 通信在消费级主板上的支持度可能受限，部分主板 BIOS 可能默认禁用 P2P 或存在稳定性问题，导致跨卡数据传输需经过 CPU 内存中转，带宽可能显著降低，需在部署前验证主板和 CPU 的 P2P 支持情况。

## Evidence

[质询]该陈述包含具体的经验性硬件行为描述（如“许多主板默认禁用”、“带宽降至4GB/s”、“开销增加8倍”），这些属于特定硬件配置下的经验事实，无法从第一性原理严格推导，且缺乏来源支持其普遍性和具体数值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

PCIe P2P peer-to-peer support consumer motherboard LLM inference stability
