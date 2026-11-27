# N413: 修正 N160 结论：RTX 5090 单卡 INT8 在 32K 上下文下因显存溢出（需 ~33GB > 32GB）不可行；RTX 6000 Ada 单卡 I

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N160

## Claim

修正 N160 结论：RTX 5090 单卡 INT8 在 32K 上下文下因显存溢出（需 ~33GB > 32GB）不可行；RTX 6000 Ada 单卡 INT8 可行（需 ~33GB < 48GB），但其带宽 960 GB/s 低于 4090 的 1008 GB/s，Decode 速度约为 4090 的 95%。

## Corrected Claim

修正 N160 结论：RTX 5090 单卡 INT8 在 32K 上下文下因显存溢出（需 ~33GB > 32GB）不可行；RTX 6000 Ada 单卡 INT8 可行（需 ~33GB < 48GB），但其带宽 960 GB/s 低于 4090 的 1008 GB/s，Decode 速度约为 4090 的 95%。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090显存32GB<33GB需求，RTX 6000 Ada显存48GB>33GB需求，带宽960/1008≈95.25%，数值与逻辑均自洽。

## Search Query

RTX 6000 Ada vs RTX 5090 inference memory requirements
