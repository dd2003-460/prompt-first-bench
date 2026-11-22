# N100: M3 Ultra (192GB) 运行 Qwen3-27B 的可行性分析：统一内存 192 GB 远超 BF16 需求 (65.6 GB)，可行。关键约束为带宽

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

M3 Ultra (192GB) 运行 Qwen3-27B 的可行性分析：统一内存 192 GB 远超 BF16 需求 (65.6 GB)，可行。关键约束为带宽：M3 Ultra 带宽 ~800 GB/s，低于 RTX 4090 (1008 GB/s)，Decode 速度可能较慢，但显存容量无限制，适合长上下文或多 Batch 场景。

## Corrected Claim

M3 Ultra (192GB) 运行 Qwen3-27B 的可行性分析：统一内存 192 GB 远超 BF16 需求 (65.6 GB)，可行。关键约束为带宽：M3 Ultra 带宽 ~800 GB/s，低于 RTX 4090 (1008 GB/s)，Decode 速度可能较慢，但显存容量无限制，适合长上下文或多 Batch 场景。

## Evidence

先验知识/题面给定，逻辑校验通过：M3 Ultra 192GB 统一内存确实大于 Qwen3-27B BF16 模型大小（约 54-65GB），且 M3 Ultra 带宽（~800GB/s）低于 RTX 4090（~1008GB/s）符合硬件规格常识，推理逻辑自洽。

## Search Query

Apple M3 Ultra memory bandwidth LLM inference speed
