# N140: 字节命中率 vs 请求命中率的区分修正：N58 中 '70-80%' 若指请求命中率，则需转换为字节命中率 H_bytes = H_req * (E[S|Hit

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N58

## Claim

字节命中率 vs 请求命中率的区分修正：N58 中 '70-80%' 若指请求命中率，则需转换为字节命中率 H_bytes = H_req * (E[S|Hit] / E[S])。由于热点对象小（ρ=-0.3），E[S|Hit] < E[S]，因此 H_bytes < H_req。若 H_req=80%，且 E[S|Hit]/E[S] ≈ 0.5，则 H_bytes ≈ 40%，与 N37 的 52-55% 更接近，澄清了单位混淆导致的矛盾。

## Corrected Claim

字节命中率 vs 请求命中率的区分修正：N58 中 '70-80%' 若指请求命中率，则需转换为字节命中率 H_bytes = H_req * (E[S|Hit] / E[S])。由于热点对象小（ρ=-0.3），E[S|Hit] < E[S]，因此 H_bytes < H_req。若 H_req=80%，且 E[S|Hit]/E[S] ≈ 0.5，则 H_bytes ≈ 40%，与 N37 的 52-55% 更接近，澄清了单位混淆导致的矛盾。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 H_bytes = H_req * (E[S|Hit] / E[S]) 符合定义，且基于热点对象较小（E[S|Hit] < E[S]）的假设，推导出的 H_bytes < H_req 及数值估算（80% * 0.5 = 40%）在逻辑和量级上均自洽，无内部矛盾。
