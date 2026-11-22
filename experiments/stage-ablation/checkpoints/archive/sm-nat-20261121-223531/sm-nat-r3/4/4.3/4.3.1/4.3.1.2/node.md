# N166: Write-Through 模式下读缓存总带宽需求 Total BW_cap 的具体数值计算：Total BW_cap = (Total Requests/Da

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59

## Claim

Write-Through 模式下读缓存总带宽需求 Total BW_cap 的具体数值计算：Total BW_cap = (Total Requests/Day * E[S] * (1 - Hit_Rate)) / 86400s。假设 Hit_Rate=100%（容量充足），读带宽趋近于0；若考虑 Miss 流量，需基于 N76 修正后的 S_total 或实际 Miss 率计算。

## Corrected Claim

Write-Through 模式下读缓存总带宽需求 Total BW_cap 的具体数值计算：Total BW_cap = (Total Requests/Day * E[S] * (1 - Hit_Rate)) / 86400s。假设 Hit_Rate=100%（容量充足），读带宽趋近于0；若考虑 Miss 流量，需基于 N76 修正后的 S_total 或实际 Miss 率计算。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（Bytes/s），Hit_Rate=100%时读带宽为0符合Write-Through缓存原理，逻辑自洽。
