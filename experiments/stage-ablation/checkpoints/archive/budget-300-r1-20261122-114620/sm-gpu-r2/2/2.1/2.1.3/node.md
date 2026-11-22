# N56: AMD RX 7900 XTX (24GB) 推理性能基准：ROCm 5.7 环境下 Qwen3-27B INT8 吞吐 15 tokens/s (batch=

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

AMD RX 7900 XTX (24GB) 推理性能基准：ROCm 5.7 环境下 Qwen3-27B INT8 吞吐 15 tokens/s (batch=1)，比 NVIDIA 同价位卡低 40%；主要瓶颈在 ROCm 对 FlashAttention-2 的支持不完整，需使用 SDPA 后端导致 20% 额外延迟

## Corrected Claim

AMD RX 7900 XTX (24GB) 在 ROCm 环境下运行 Qwen3-27B INT8 推理时，性能通常低于同价位 NVIDIA 显卡，主要受限于 ROCm 生态对特定注意力机制优化（如 FlashAttention-2）的支持程度及后端选择。

## Evidence

[质询]具体数值（15 tokens/s, 40%差距, 20%延迟）属于高度依赖具体硬件批次、驱动版本及测试脚本的经验数据，缺乏通用性；且ROCm 5.7对FlashAttention-2的支持状态随时间快速变化，该具体瓶颈描述可能已过时或仅适用于特定非官方构建。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体基准数值及瓶颈归因）

## Search Query

RX 7900 XTX ROCm Qwen3-27B inference benchmark FlashAttention
