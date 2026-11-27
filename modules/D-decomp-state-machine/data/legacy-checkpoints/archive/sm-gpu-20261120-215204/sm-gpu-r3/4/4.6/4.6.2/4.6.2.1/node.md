# N313: 工作点 A (高 MFU ~60%)：使用 TensorRT-LLM 且启用 FlashAttention-2 与 PagedAttention 优化时，RTX

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N111

## Claim

工作点 A (高 MFU ~60%)：使用 TensorRT-LLM 且启用 FlashAttention-2 与 PagedAttention 优化时，RTX 4090 在 BF16 预填充阶段的 MFU 可达 55-65%，主要受限于 Tensor Core 利用率和内存带宽同步

## Corrected Claim

工作点 A (高 MFU)：使用 TensorRT-LLM 且启用 FlashAttention-2 与 PagedAttention 优化时，RTX 4090 在 BF16 预填充阶段的 MFU 可能达到较高水平（具体数值需实测验证，通常受限于 Tensor Core 利用率及内存带宽瓶颈，55-65% 为乐观估计值）。

## Evidence

[质询]数值量级存疑：RTX 4090 作为消费级显卡，其内存带宽（~1TB/s）与计算能力（~80 TFLOPS BF16）的比值较低，在预填充（Prefill）阶段通常受限于计算而非内存带宽同步；且 55-65% 的 MFU 对于消费级硬件在复杂优化下属于极高值，缺乏公开基准数据支持，可能混淆了理论峰值与实际可达 MFU，或高估了消费级卡在大模型推理中的效率上限。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体数值区间属于特定硬件配置下的经验性能指标，无法从第一性原理严格推导，需外部基准数据佐证）

## Search Query

TensorRT-LLM RTX 4090 BF16 prefill MFU benchmark FlashAttention-2
