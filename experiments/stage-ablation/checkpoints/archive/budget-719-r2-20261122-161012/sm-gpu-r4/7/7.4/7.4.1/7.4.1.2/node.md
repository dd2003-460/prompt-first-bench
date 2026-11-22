# N659: 工作点 1 的吞吐 46.5 tokens/s 基于 FP8 精度，需确认 RTX 4090 对 FP8 推理的硬件支持：RTX 4090 (Ada Lovel

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N272

## Claim

工作点 1 的吞吐 46.5 tokens/s 基于 FP8 精度，需确认 RTX 4090 对 FP8 推理的硬件支持：RTX 4090 (Ada Lovelace) 支持 FP8 Tensor Core，但实际性能受限于驱动和推理引擎优化，实测吞吐可能比理论值低 10-20%，保守估计为 37-42 tokens/s

## Corrected Claim

工作点 1 的吞吐 46.5 tokens/s 基于 FP8 精度，需确认 RTX 4090 对 FP8 推理的硬件支持：RTX 4090 (Ada Lovelace) 支持 FP8 Tensor Core，但实际性能受限于驱动和推理引擎优化，实测吞吐可能比理论值低 10-20%，保守估计为 37-42 tokens/s

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 (Ada Lovelace) 确实支持 FP8 Tensor Core，且实际推理性能受驱动和引擎优化影响，通常低于理论峰值，10-20% 的损耗估计符合工程经验。

## Search Query

RTX 4090 FP8 inference performance Qwen3-27B vLLM benchmark
