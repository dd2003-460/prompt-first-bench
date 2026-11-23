# N316: Zipf参数α的校准值：针对视频/图片混合平台，基于实际访问日志拟合的α值通常在0.85-1.05之间；若α=1.0（标准Zipf），公式简化为 H_cache

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

Zipf参数α的校准值：针对视频/图片混合平台，基于实际访问日志拟合的α值通常在0.85-1.05之间；若α=1.0（标准Zipf），公式简化为 H_cache ≈ 1 - 1/ln(N_objects)；若α=0.9（长尾更重），H_cache对N_objects的敏感度降低。

## Corrected Claim

Zipf参数α的校准值：针对视频/图片混合平台，基于实际访问日志拟合的α值通常在0.85-1.05之间；若α=1.0（标准Zipf），公式简化为 H_cache ≈ 1 - 1/ln(N_objects)；若α=0.9（长尾更重），H_cache对N_objects的敏感度降低。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

zipf parameter alpha calibration video platform cache hit rate
