# N163: 4-bit (NVFP4/W4) 精度下总显存需求 = 13.5GB (Weights) + 16GB (KV Cache: 通常保持 BF16/FP16 精度

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

4-bit (NVFP4/W4) 精度下总显存需求 = 13.5GB (Weights) + 16GB (KV Cache: 通常保持 BF16/FP16 精度以保质量，若 KV 也量化则减半) + 2GB (Overhead) ≈ 31.5GB (KV BF16) 或 23.5GB (KV 4-bit)，需 ≥31.5GB 显存

## Corrected Claim

4-bit (NVFP4/W4) 精度下总显存需求 = 13.5GB (Weights) + 16GB (KV Cache: 通常保持 BF16/FP16 精度以保质量，若 KV 也量化则减半) + 2GB (Overhead) ≈ 31.5GB (KV BF16) 或 23.5GB (KV 4-bit)，需 ≥31.5GB 显存

## Evidence

先验知识/题面给定，逻辑校验通过：13.5+16+2=31.5，13.5+8+2=23.5，数值计算自洽，符合显存估算常规逻辑。
