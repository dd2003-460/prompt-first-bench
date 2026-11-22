# N264: Q_score 计算的工作点 2 (高性价比/中保真)：采用 FP8 (E4M3) 精度。Q_score 预期在 0.98-0.99 区间（基于 LLM.int

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

Q_score 计算的工作点 2 (高性价比/中保真)：采用 FP8 (E4M3) 精度。Q_score 预期在 0.98-0.99 区间（基于 LLM.int8() 或 SmoothQuant 文献，FP8 在 >7B 模型上 MMLU 损失通常 <1%）。硬件约束：需支持 FP8 Tensor Core 的 GPU (如 H100, L40S, RTX 4090 需软件模拟或特定框架支持，RTX 4090 无原生 FP8 TC，效率受限)。若使用 RTX 4090，FP8 优势减弱，需对比 INT8。

## Corrected Claim

Q_score 计算的工作点 2 (高性价比/中保真)：采用 FP8 (E4M3) 精度。Q_score 预期在 0.98-0.99 区间（基于 LLM.int8() 或 SmoothQuant 文献，FP8 在 >7B 模型上 MMLU 损失通常 <1%）。硬件约束：需支持 FP8 Tensor Core 的 GPU (如 H100, L40S, RTX 4090 需软件模拟或特定框架支持，RTX 4090 无原生 FP8 TC，效率受限)。若使用 RTX 4090，FP8 优势减弱，需对比 INT8。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8 (E4M3) 在 H100 等硬件上有原生支持，在 RTX 4090 上确实缺乏原生 Tensor Core 支持需软件模拟，且 FP8 精度损失通常小于 INT8，符合 LLM 量化领域共识。

## Search Query

Qwen3-27B FP8 quantization MMLU accuracy drop
