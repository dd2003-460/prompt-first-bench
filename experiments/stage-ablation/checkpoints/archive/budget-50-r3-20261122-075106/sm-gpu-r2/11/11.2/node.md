# N120: A100 80GB PCIe 支持 BF16 精度下直接运行 Qwen3-27B（54GB权重+KV Cache），而 2×RTX 4090 总显存 48GB 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

A100 80GB PCIe 支持 BF16 精度下直接运行 Qwen3-27B（54GB权重+KV Cache），而 2×RTX 4090 总显存 48GB 仅支持 W4/INT8 精度，需对比 BF16 (A100) 与 W4 (2×4090) 的质量损失差异

## Corrected Claim

A100 80GB PCIe 支持 BF16 精度下直接运行 Qwen3-27B（54GB权重+KV Cache），而 2×RTX 4090 总显存 48GB 仅支持 W4/INT8 精度，需对比 BF16 (A100) 与 W4 (2×4090) 的质量损失差异

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB显存足以容纳Qwen3-27B的BF16权重（约54GB）及KV Cache；2×RTX 4090总显存48GB无法容纳BF16权重，必须使用W4/INT8量化，对比逻辑自洽。
