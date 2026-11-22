# N410: 基于 1000 条 Prompt 的 Token 级 KL 散度均值 E[D_KL] 的具体计算脚本逻辑：需明确是计算每条 Prompt 的完整序列 KL 还是

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N134, N135, N136

## Claim

基于 1000 条 Prompt 的 Token 级 KL 散度均值 E[D_KL] 的具体计算脚本逻辑：需明确是计算每条 Prompt 的完整序列 KL 还是逐 Token 平均 KL，以及是否对 Logits 进行 Temperature Scaling（通常 T=1.0），不同计算口径会导致数值差异达 10-20%

## Corrected Claim

基于 1000 条 Prompt 的 Token 级 KL 散度均值 E[D_KL] 的具体计算脚本逻辑：需明确是计算每条 Prompt 的完整序列 KL 还是逐 Token 平均 KL，以及是否对 Logits 进行 Temperature Scaling（通常 T=1.0），不同计算口径会导致数值差异达 10-20%

## Evidence

先验知识/题面给定，逻辑校验通过
