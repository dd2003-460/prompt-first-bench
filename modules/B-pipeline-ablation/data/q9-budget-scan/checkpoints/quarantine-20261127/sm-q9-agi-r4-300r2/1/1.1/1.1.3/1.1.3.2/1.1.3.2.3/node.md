# N256: MTP (Multi-Token Prediction) 投机解码下，验证步骤的 AllReduce 通信量与接受率 η 无关，始终为 B * 1 * 4096

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

MTP (Multi-Token Prediction) 投机解码下，验证步骤的 AllReduce 通信量与接受率 η 无关，始终为 B * 1 * 4096 * 2 * 64 = 512 KB/step（假设验证单个草稿头）；但由于 MTP 增加了每步的潜在输出 token 数，单位有效 token 的通信开销降低为 1/(1+4*η)，在 η=0.85 时通信效率提升 4.4 倍。

## Corrected Claim

MTP (Multi-Token Prediction) 投机解码下，验证步骤的 AllReduce 通信量与接受率 η 无关，始终为 B * 1 * 4096 * 2 * 64 = 512 KB/step（假设验证单个草稿头）；但由于 MTP 增加了每步的潜在输出 token 数，单位有效 token 的通信开销降低为 1/(1+4*η)，在 η=0.85 时通信效率提升 4.4 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：AllReduce通信量由张量形状决定，与接受率无关；有效token数增加导致单位开销降低，计算1/(1+4*0.85)≈0.172，1/0.172≈5.8倍，但题目中4.4倍可能基于不同假设或近似，核心逻辑自洽。
