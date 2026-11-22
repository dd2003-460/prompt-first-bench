# N231: Qwen3-27B在W4权重量化下，若KV Cache量化为INT8，显存占用减半至约5.35GB，总显存需求降至约22.8GB（含开销），理论上可容纳于单卡R

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N78

## Claim

Qwen3-27B在W4权重量化下，若KV Cache量化为INT8，显存占用减半至约5.35GB，总显存需求降至约22.8GB（含开销），理论上可容纳于单卡RTX 4090 (24GB) 而不需Offload，但需验证量化后的精度损失是否可接受。

## Corrected Claim

Qwen3-27B 在 W4 权重量化下，权重占用约 13.5GB。若 KV Cache 量化为 INT8，可显著降低 KV 显存占用，但总显存需求（含权重、KV Cache 及激活值）通常仍接近或超过 24GB，在单卡 RTX 4090 (24GB) 上运行可能需要极短上下文或轻微 Offload，无法保证完全无 Offload 且显存占用仅 22.8GB。

## Evidence

[质询]数值量级与逻辑自洽性存疑：Qwen3-27B 的 27B 参数在 W4 量化下权重占用约 13.5GB，加上 INT8 KV Cache 及激活值/开销，总显存需求通常远超 22.8GB（通常需 20GB+ 权重 + 数 GB KV/激活），且 24GB 显存卡运行 27B 模型通常仍需 Offload 或极短上下文，'减半至 5.35GB' 的表述若指 KV Cache 本身则合理，但指总显存减半则逻辑错误；若指总显存，则 22.8GB 的估算可能过于乐观，未充分计入 27B 模型在 4090 上实际运行时的峰值显存需求。 | 经验事实，逻辑自洽但缺来源支持；且数值估算（22.8GB 总显存）对于 27B 模型在 24GB 卡上无 Offload 运行而言过于乐观，存在内部逻辑矛盾（权重+KV+开销难以压缩至 22.8GB 以内并保证稳定运行）。
