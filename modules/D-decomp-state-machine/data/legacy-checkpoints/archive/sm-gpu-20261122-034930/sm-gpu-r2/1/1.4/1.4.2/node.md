# N56: KV Cache 精度对齐修正：N10/N16 中 KV Cache 按 FP16 (2 bytes) 计算为 10.7GB。若模型权重为 INT8，KV Ca

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10, N11, N12

## Claim

KV Cache 精度对齐修正：N10/N16 中 KV Cache 按 FP16 (2 bytes) 计算为 10.7GB。若模型权重为 INT8，KV Cache 通常也量化为 INT8 (1 byte)，此时 KV Cache 降至 5.35GB，总显存需求降至 27+5.35+4 = 36.35GB，这将改变单卡可行性阈值（36.35GB < 40GB，使 A100 40GB 在 INT8 下可行）。

## Corrected Claim

KV Cache 精度对齐修正：N10/N16 中 KV Cache 按 FP16 (2 bytes) 计算为 10.7GB。若模型权重为 INT8，KV Cache 通常也量化为 INT8 (1 byte)，此时 KV Cache 降至 5.35GB，总显存需求降至 27+5.35+4 = 36.35GB，这将改变单卡可行性阈值（36.35GB < 40GB，使 A100 40GB 在 INT8 下可行）。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 大小与精度线性相关，FP16(2B)到INT8(1B)减半，10.7GB/2=5.35GB，总显存27+5.35+4=36.35GB，计算无误且符合工程常识。
