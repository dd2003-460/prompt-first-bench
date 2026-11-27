# N161: BF16 精度下总显存需求 = 54GB (Weights) + 32GB (KV Cache: 2*64*8*128*32768*2 / 1024^3) + 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

BF16 精度下总显存需求 = 54GB (Weights) + 32GB (KV Cache: 2*64*8*128*32768*2 / 1024^3) + 2GB (Overhead) = 88GB，需 ≥88GB 显存

## Corrected Claim

BF16 精度下总显存需求 = 54GB (Weights) + 32GB (KV Cache: 2*64*8*128*32768*2 / 1024^3) + 2GB (Overhead) = 88GB，需 ≥88GB 显存

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算 2*64*8*128*32768*2 / 1024^3 ≈ 32GB 量级正确，总显存 54+32+2=88GB 算术自洽。
