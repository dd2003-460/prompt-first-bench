# N84: 显存余量 (Headroom) 对性能稳定性的影响量化：当剩余显存 < 5% 时，CUDA OOM (Out of Memory) 风险显著增加，可能导致推理中

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

显存余量 (Headroom) 对性能稳定性的影响量化：当剩余显存 < 5% 时，CUDA OOM (Out of Memory) 风险显著增加，可能导致推理中断。对于 24GB 卡运行 W4 (17.04 GB 需求)，余量仅 6.96 GB (29%)，安全；对于 48GB 卡运行 BF16 (59.15 GB 需求) 不可行，必须使用 INT8 (31.07 GB, 余量 16.93 GB, 35%) 或更大显存卡。

## Corrected Claim

显存余量 (Headroom) 对性能稳定性的影响量化：当剩余显存 < 5% 时，CUDA OOM (Out of Memory) 风险显著增加，可能导致推理中断。对于 24GB 卡运行 W4 (17.04 GB 需求)，余量仅 6.96 GB (29%)，安全；对于 48GB 卡运行 BF16 (59.15 GB 需求) 不可行，必须使用 INT8 (31.07 GB, 余量 16.93 GB, 35%) 或更大显存卡。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算准确（24-17.04=6.96, 6.96/24=29%; 48-59.15<0, 48-31.07=16.93, 16.93/48≈35%），且符合GPU显存管理的基本工程常识（OOM风险与剩余显存比例正相关）。
