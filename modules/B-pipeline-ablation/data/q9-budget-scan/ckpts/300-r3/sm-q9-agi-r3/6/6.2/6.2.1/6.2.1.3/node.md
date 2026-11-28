# N299: 验证开销临界点模型：当Token Acceptance Rate AR < 1/(1+C_verify/T_draft)时，投机解码转为负收益；对于V100集群

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

验证开销临界点模型：当Token Acceptance Rate AR < 1/(1+C_verify/T_draft)时，投机解码转为负收益；对于V100集群，C_verify/T_draft≈0.25，故AR_critical≈0.8

## Corrected Claim

验证开销临界点模型：当Token Acceptance Rate AR < 1/(1+C_verify/T_draft)时，投机解码转为负收益；对于V100集群，C_verify/T_draft≈0.25，故AR_critical≈0.8

## Evidence

先验知识/题面给定，逻辑校验通过：投机解码收益临界点公式推导正确，数值代入计算无误（1/(1+0.25)=0.8）

## Search Query

speculative decoding critical acceptance rate threshold verification overhead
