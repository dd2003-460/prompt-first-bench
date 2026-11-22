# N42: Qwen3-27B 在 INT8 精度下，推理所需的总硬性显存需求为 47.48 GB，由 27 GB 权重显存与 20.48 GB KV Cache 显存相加

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Qwen3-27B 在 INT8 精度下，推理所需的总硬性显存需求为 47.48 GB，由 27 GB 权重显存与 20.48 GB KV Cache 显存相加得出，需额外预留约 2-5 GB 用于激活值缓冲和框架开销。

## Corrected Claim

Qwen3-27B 在 INT8 精度下，推理所需的总硬性显存需求为 47.48 GB，由 27 GB 权重显存与 20.48 GB KV Cache 显存相加得出，需额外预留约 2-5 GB 用于激活值缓冲和框架开销。

## Evidence

父节点级核验未通过：不完备（父节点明确指出总显存由'27 GB 权重显存'和'20.48 GB KV Cache'两部分相加得出，但子节点仅解释了 KV Cache 的计算过程，完全缺失了权重显存（27 GB）的来源解释（例如：27B 参数 * 1 byte/INT8 = 27 GB），导致分解未覆盖父节点的所有关键方面。）
