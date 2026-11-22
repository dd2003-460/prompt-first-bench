# N248: 计算独立假设下命中对象的平均大小 E[S|Hit]_indep：假设对象大小与热度独立，E[S|Hit] = E[S]_trunc ≈ 24.2KB，此时修正因

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N93

## Claim

计算独立假设下命中对象的平均大小 E[S|Hit]_indep：假设对象大小与热度独立，E[S|Hit] = E[S]_trunc ≈ 24.2KB，此时修正因子 R_byte = 1.0。

## Corrected Claim

计算独立假设下命中对象的平均大小 E[S|Hit]_indep：假设对象大小与热度独立，E[S|Hit] = E[S]_trunc ≈ 24.2KB，此时修正因子 R_byte = 1.0。

## Evidence

先验知识/题面给定，逻辑校验通过：在独立假设下，命中概率与大小无关，故条件期望等于截断后的总体期望，修正因子为1。
