# N289: Qwen3-27B 在 FP8 E4M3 精度下，GSM8K 数据集的最终答案准确率（Acc_FP8_GSM8K）预期为 84%-89%。准确率下降比例 ΔAc

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N121

## Claim

Qwen3-27B 在 FP8 E4M3 精度下，GSM8K 数据集的最终答案准确率（Acc_FP8_GSM8K）预期为 84%-89%。准确率下降比例 ΔAcc = (Acc_BF16 - Acc_FP8) / Acc_BF16 预期 < 1.5%。若 ΔAcc > 2%，则表明 FP8 量化对逻辑推理链路的中间状态（如思维链中的关键数值）产生了扰动，需评估是否影响实际业务场景（如数学解题助手）。

## Corrected Claim

Qwen3-27B 在 FP8 E4M3 精度下，GSM8K 数据集的最终答案准确率（Acc_FP8_GSM8K）预期为 84%-89%。准确率下降比例 ΔAcc = (Acc_BF16 - Acc_FP8) / Acc_BF16 预期 < 1.5%。若 ΔAcc > 2%，则表明 FP8 量化对逻辑推理链路的中间状态（如思维链中的关键数值）产生了扰动，需评估是否影响实际业务场景（如数学解题助手）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

FP8 quantization impact GSM8K math reasoning accuracy LLM
