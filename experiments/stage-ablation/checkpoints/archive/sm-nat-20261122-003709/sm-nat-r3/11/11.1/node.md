# N256: 计算独立假设下的缓存覆盖对象数 K_indep：假设对象大小独立于热度，平均大小 E[S]=10KB，则 K_indep = 128GB / 10KB = 13

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N96

## Claim

计算独立假设下的缓存覆盖对象数 K_indep：假设对象大小独立于热度，平均大小 E[S]=10KB，则 K_indep = 128GB / 10KB = 131,072。由于总对象数 N=100,000 < K_indep，独立假设下缓存可覆盖所有对象，K_indep_eff = 100,000。

## Corrected Claim

计算独立假设下的缓存覆盖对象数 K_indep：假设对象大小独立于热度，平均大小 E[S]=10KB，则 K_indep = 128GB / 10KB = 131,072。由于总对象数 N=100,000 < K_indep，独立假设下缓存可覆盖所有对象，K_indep_eff = 100,000。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB / 10KB = 131,072 计算正确，且 100,000 < 131,072 推导有效
