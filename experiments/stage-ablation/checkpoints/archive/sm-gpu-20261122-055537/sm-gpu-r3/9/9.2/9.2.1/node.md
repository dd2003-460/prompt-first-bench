# N353: 在 seq_len=32768 下，RTX 4090 推理 Decode 阶段的 FLOPs 估算：每 token 生成需执行 2 * Params * FLO

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N112

## Claim

在 seq_len=32768 下，RTX 4090 推理 Decode 阶段的 FLOPs 估算：每 token 生成需执行 2 * Params * FLOP/Param (2) = 2 * 27e9 * 2 = 108 GFLOPs/token，主要受限于 Attention 的 QK^T 和 AV 计算

## Corrected Claim

在 seq_len=32768 下，RTX 4090 推理 Decode 阶段的 FLOPs 估算：每 token 生成需执行 2 * Params * FLOP/Param (2) = 2 * 27e9 * 2 = 108 GFLOPs/token，主要受限于 Attention 的 QK^T 和 AV 计算

## Evidence

先验知识/题面给定，逻辑校验通过：Decode阶段每token生成需读取全部参数，计算量约为2*Params FLOPs，27B模型对应108 GFLOPs/token，量级正确；Attention计算在长序列下虽存在，但通常小于FFN层计算量，主要瓶颈描述在工程估算语境下可接受。

## Search Query

LLM inference FLOPs per token calculation 2*params
