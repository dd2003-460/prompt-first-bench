# N249: KV Cache 量化对单 token 显存占用的修正系数：在 FP8 精度下，单 token KV Cache 占用为 BF16 的 50%（即 128 KB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

KV Cache 量化对单 token 显存占用的修正系数：在 FP8 精度下，单 token KV Cache 占用为 BF16 的 50%（即 128 KB/token）；在 INT8 下同样为 50%；在 INT4 下为 25%（64 KB/token），但需评估低精度 KV Cache 对长上下文注意力分数精度的影响阈值。

## Corrected Claim

KV Cache 量化对单 token 显存占用的修正系数：在 FP8 精度下，单 token KV Cache 占用为 BF16 的 50%（即 128 KB/token）；在 INT8 下同样为 50%；在 INT4 下为 25%（64 KB/token），但需评估低精度 KV Cache 对长上下文注意力分数精度的影响阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8/INT8均为8位精度，BF16为16位精度，故显存占用减半（50%）；INT4为4位精度，故显存占用为四分之一（25%）。数值量级与精度位宽比例完全自洽。
