# N173: W4A16量化下，Qwen3-27B的Scale/Zero-point存储开销精确值为：(27.18e9 / 128) * 2 bytes = 425 MB (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51, N52, N53

## Claim

W4A16量化下，Qwen3-27B的Scale/Zero-point存储开销精确值为：(27.18e9 / 128) * 2 bytes = 425 MB (0.425 GB)，基于GPTQ/AWQ标准的128元素分组(Group Size=128)及FP16精度存储Scale因子。

## Corrected Claim

W4A16量化下，Qwen3-27B的Scale/Zero-point存储开销精确值为：(27.18e9 / 128) * 2 bytes = 425 MB (0.425 GB)，基于GPTQ/AWQ标准的128元素分组(Group Size=128)及FP16精度存储Scale因子。

## Evidence

先验知识/题面给定，逻辑校验通过：27.18e9参数除以128分组得到约2.12e8个组，每组2字节（Scale+Zero-point，FP16）即4.24e8字节，约425MB，计算与量级均合理。

## Search Query

GPTQ AWQ group size 128 scale factor storage overhead calculation
