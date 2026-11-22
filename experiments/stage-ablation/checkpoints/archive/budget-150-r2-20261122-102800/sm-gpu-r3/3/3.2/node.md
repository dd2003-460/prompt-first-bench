# N19: 工作点2（中性价比最优）：INT8精度，质量损失<2%（基于Llama-2/3量化研究，MMLU/HELMET基准下降1-3%），显存占用27GB权重+2.15

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

工作点2（中性价比最优）：INT8精度，质量损失<2%（基于Llama-2/3量化研究，MMLU/HELMET基准下降1-3%），显存占用27GB权重+2.15GB KV=29.15GB，适合A6000/L40S/RTX 4090(需多卡或offload)，推理速度tokens/s ≈ 显存带宽 / 29.15 GB = 768 GB/s / 29.15 GB ≈ 26.3 tokens/s (A6000), 864 GB/s / 29.15 GB ≈ 29.6 tokens/s (L40S)

## Corrected Claim

工作点2（中性价比最优）：INT8精度，质量损失约1-3%（基于Llama-2/3量化研究，MMLU/HELMET基准下降1-3%），显存占用约29.15GB（27GB权重+2.15GB KV），适合A6000/L40S/RTX 4090（需多卡或offload），推理速度受限于硬件带宽与计算能力，单卡实际吞吐需根据具体模型架构和batch size实测，理论带宽上限约为26-30 tokens/s（基于显存带宽估算，实际可能更低）。

## Evidence

[质询]数值量级与硬件规格存在显著矛盾：A6000显存带宽为768 GB/s，L40S为864 GB/s，但29.15GB的模型在单卡上无法达到26-30 tokens/s的推理速度（通常受限于计算而非带宽，且该速度对于29GB模型在单卡上过于乐观，通常需多卡或更高带宽）；此外，'质量损失<2%'与'MMLU下降1-3%'存在内部逻辑冲突（若基准下降1-3%，则质量损失不应严格小于2%）。 | 先验知识/题面给定，逻辑校验发现内部矛盾（质量损失与基准下降范围不一致）及硬件性能估算偏差，故降级。

## Search Query

INT8 quantization LLM quality loss MMLU HELMET benchmark 27B model inference speed
