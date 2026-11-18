# N152: 工作点 C（部分块失效/比例失效）：大对象被分块存储，仅部分块内容变更。若对象平均分为 M 个块，单块更新概率为 u_block，则对象级失效概率为 1 - (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

工作点 C（部分块失效/比例失效）：大对象被分块存储，仅部分块内容变更。若对象平均分为 M 个块，单块更新概率为 u_block，则对象级失效概率为 1 - (1-u_block)^M ≈ M * u_block。C_miss/C_total = M * u_block / u_object。例如 M=10, u_object=0.01/day, 则 C_miss/C_total ≈ 0.1，折损降低 90%。

## Corrected Claim

工作点 C（部分块失效/比例失效）：大对象被分块存储，仅部分块内容变更。若对象平均分为 M 个块，单块更新概率为 u_block，则对象级失效概率为 1 - (1-u_block)^M ≈ M * u_block。C_miss/C_total = M * u_block / u_object。例如 M=10, u_object=0.01/day, 则 C_miss/C_total ≈ 0.1，折损降低 90%。

## Evidence

先验知识/题面给定，逻辑校验通过
