# N267: 工作点 C (高成本低性/可行且质量最优)：RTX 4090 单卡 + CPU Offload (BF16)。权重部分驻留 RAM，显存仅存 KV Cache 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N119

## Claim

工作点 C (高成本低性/可行且质量最优)：RTX 4090 单卡 + CPU Offload (BF16)。权重部分驻留 RAM，显存仅存 KV Cache 和热点层。显存占用 < 24GB，可行。但 Decode 吞吐量受限于 PCIe 4.0 带宽 (64 GB/s) 和 RAM 带宽 (100 GB/s)，预计吞吐量 < 5 tok/s，延迟 > 200ms/token，严重超出交互式对话阈值 (100ms/token)，仅适用于离线批处理。

## Corrected Claim

工作点 C (高成本低性/可行且质量最优)：RTX 4090 单卡 + CPU Offload (BF16)。权重部分驻留 RAM，显存仅存 KV Cache 和热点层。显存占用 < 24GB，可行。但 Decode 吞吐量受限于 PCIe 4.0 带宽 (64 GB/s) 和 RAM 带宽 (100 GB/s)，预计吞吐量 < 5 tok/s，延迟 > 200ms/token，严重超出交互式对话阈值 (100ms/token)，仅适用于离线批处理。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存24GB，BF16下大模型权重无法全驻留，Offload至RAM受限于PCIe 4.0带宽（~64GB/s）及内存带宽，导致Decode阶段吞吐量极低（<5 tok/s）且延迟高，符合物理直觉与工程经验。
