# N130: AMD RX 7900 XTX 在 Qwen3-27B 推理中的有效性价比折损：尽管其硬件成本 ($950) 仅为 RTX 4090 ($1700) 的 56%

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N47

## Claim

AMD RX 7900 XTX 在 Qwen3-27B 推理中的有效性价比折损：尽管其硬件成本 ($950) 仅为 RTX 4090 ($1700) 的 56%，但由于 ROCm 生态对 LLM 推理的支持滞后（FlashAttention 内核缺失、量化支持不完整），实际吞吐量通常仅为同显存 NVIDIA 卡的 50%-70%，导致其有效单位 token 成本反而高于 NVIDIA 卡，故在‘性能/美元’维度上不占优。

## Corrected Claim

AMD RX 7900 XTX 在 Qwen3-27B 推理中，由于 ROCm 生态对 LLM 推理的支持（如 FlashAttention 内核、量化支持）相对滞后，其实际吞吐量通常低于同显存 NVIDIA 卡，导致在‘性能/美元’维度上可能不占优。

## Evidence

[质询]具体数值（50%-70%吞吐量、$950/$1700价格）属于随时间波动的经验事实，且ROCm生态支持状况动态变化，缺乏实时数据支撑，存在过时或偏差风险。 | 先验知识/题面给定，逻辑校验通过：AMD ROCm在LLM推理优化上确实长期落后于CUDA，导致同等硬件下效率较低，符合技术常识；但因无外部来源验证具体数值，依据经验事实排除条款降级。
