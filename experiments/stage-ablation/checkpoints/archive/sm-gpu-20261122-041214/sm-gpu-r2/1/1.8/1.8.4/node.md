# N72: INT8 单卡显存需求修正：权重 25.2GB (同 FP8) + KV Cache 2.4GB (INT8 KV Cache) + 激活值 ~5GB = 32

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

INT8 单卡显存需求修正：权重 25.2GB (同 FP8) + KV Cache 2.4GB (INT8 KV Cache) + 激活值 ~5GB = 32.6 GB，可行性与 FP8 相同，但需考虑 INT8 量化对 KV Cache 精度的额外损失 [待核验]。

## Corrected Claim

INT8 单卡显存需求修正：权重 25.2GB (同 FP8) + KV Cache 2.4GB (INT8 KV Cache) + 激活值 ~5GB = 32.6 GB，可行性与 FP8 相同，但需考虑 INT8 量化对 KV Cache 精度的额外损失 [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8与FP8权重体积相同（均为1字节/参数），KV Cache INT8体积约为FP16的1/2，数值量级与算术加和（25.2+2.4+5=32.6）均合理自洽。
