# N57: NVFP4 精度下 Qwen3-27B 的权重存储体积基础值为 13.49 GB (26.98B * 0.5 bytes / 1e9)，但必须增加 FP4 特有

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10, N11, N12

## Claim

NVFP4 精度下 Qwen3-27B 的权重存储体积基础值为 13.49 GB (26.98B * 0.5 bytes / 1e9)，但必须增加 FP4 特有的 Block-wise Scale (FP8) 元数据开销，该开销通常使总体积增加约 6-8%（即每 16 个 FP4 参数伴随 1 个 FP8 scale 因子）

## Corrected Claim

NVFP4 精度下 Qwen3-27B 的权重存储基础体积约为 13.49 GB。由于 FP4 量化需要额外的 scale 元数据（具体开销取决于量化块大小和 scale 精度，常见实现中可能增加数个百分点的体积），实际存储体积会略高于基础值。

## Evidence

[质询]NVFP4 的具体量化方案（如 block size 是否为 16，scale 因子是否严格为 FP8 且每 16 个参数共享 1 个）属于特定实现细节，不同框架或论文中可能存在差异（例如某些实现可能使用不同的 block size 或 scale 精度），且 6-8% 的开销比例依赖于具体的 block size 假设，若无明确来源支持该特定配置，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持。基础体积计算正确（26.98B * 0.5 / 1e9 ≈ 13.49 GB）。关于 NVFP4 的元数据开销，虽然 FP4 通常需要额外的 scale 信息，但具体的 block size（16）和 scale 精度（FP8）以及由此产生的 6-8% 开销比例属于特定实现的经验参数，缺乏直接来源验证，故降级。

## Search Query

NVFP4 quantization metadata overhead block scale factor size
