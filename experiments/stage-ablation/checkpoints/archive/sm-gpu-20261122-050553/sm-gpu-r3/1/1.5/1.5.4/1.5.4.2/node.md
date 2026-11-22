# N173: CPU 内存中转 (No P2P) 下的通信带宽瓶颈量化：当 PCIe P2P 禁用时，跨卡数据传输路径为 GPU0 -> CPU RAM -> GPU1，受限

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N53

## Claim

CPU 内存中转 (No P2P) 下的通信带宽瓶颈量化：当 PCIe P2P 禁用时，跨卡数据传输路径为 GPU0 -> CPU RAM -> GPU1，受限于内存控制器带宽和 PCIe 通道共享；在典型消费级 CPU (如 i9-14900K) 上，双通道 DDR5-6000 带宽约 98 GB/s，但 PCIe 4.0 x16 仅 32 GB/s，因此瓶颈在 PCIe 侧；实测显示，No P2P 情况下，TP=2 的 All-Reduce 操作延迟比 P2P 启用时高 3-5 倍，导致 Qwen3-27B 的解码速度从 ~40 tokens/s (P2P) 降至 ~20-25 tokens/s (No P2P)，这一性能差距使得 2x4090 在 No P2P 环境下的性价比远低于 1x5090 (单卡无通信开销)。

## Corrected Claim

当 PCIe P2P 禁用时，跨卡数据传输路径为 GPU0 -> CPU RAM -> GPU1，受限于内存控制器带宽和 PCIe 通道共享；在典型消费级 CPU 上，PCIe 4.0 x16 带宽（约 32 GB/s）通常低于双通道 DDR5 内存带宽，因此瓶颈在 PCIe 侧。No P2P 情况下，TP=2 的 All-Reduce 操作延迟显著高于 P2P 启用时，导致多卡解码速度大幅下降，使得 2x4090 在 No P2P 环境下的性价比可能低于单卡高性能 GPU（如 1x5090）。

## Evidence

[质询]该陈述包含大量具体的经验性数值（如 i9-14900K 的 DDR5 带宽、PCIe 4.0 带宽、Qwen3-27B 在特定硬件配置下的具体解码速度 tokens/s 及性能倍数），这些属于硬件规格和实测性能数据，无法从第一性原理推导，且参考来源为空，无法验证具体数值的准确性。 | 经验事实，逻辑自洽但缺来源支持。虽然 PCIe 4.0 x16 带宽（~32GB/s）低于双通道 DDR5-6000 带宽（~98GB/s）导致瓶颈在 PCIe 侧的逻辑成立，且 No P2P 路径确实会增加延迟，但具体的 tokens/s 数值和 3-5 倍延迟差距缺乏外部证据支持。

## Search Query

PCIe P2P disabled multi-GPU inference throughput drop RTX 4090
