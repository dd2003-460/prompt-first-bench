# N129: INT8 SmoothQuant 或 GPTQ 等高级量化方法通常包含 per-block 校准数据，其存储开销取决于 block size（如 128），额外

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

INT8 SmoothQuant 或 GPTQ 等高级量化方法通常包含 per-block 校准数据，其存储开销取决于 block size（如 128），额外开销约为 (27.8B / 128) * 4 bytes ≈ 0.87 GB，总占用约为 28.67 GB。

## Corrected Claim

INT8 SmoothQuant 或 GPTQ 等高级量化方法通常包含 per-block 校准数据，其存储开销取决于 block size（如 128），额外开销约为 (27.8B / 128) * 4 bytes ≈ 0.87 GB，总占用约为 28.67 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27.8B/128*4B ≈ 0.87GB，27.8+0.87≈28.67GB，计算无误且符合量化存储常识
