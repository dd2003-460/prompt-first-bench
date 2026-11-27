# N357: N128 临界小时数公式的完整展开：H_critical = (Capex_dc - Capex_cons) / (P_dc - P_cons) * 1000 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N128

## Claim

N128 临界小时数公式的完整展开：H_critical = (Capex_dc - Capex_cons) / (P_dc - P_cons) * 1000 / Price_electricity，其中 P 为总系统功耗（含主机/散热/电源损耗），需将纯 GPU 功耗修正为整机功耗（如 2x4090 整机 ~1200W vs 1xA100 整机 ~1000W）。

## Corrected Claim

N128 临界小时数公式的完整展开：H_critical = (Capex_dc - Capex_cons) / (P_dc - P_cons) * 1000 / Price_electricity，其中 P 为总系统功耗（含主机/散热/电源损耗），需将纯 GPU 功耗修正为整机功耗（如 2x4090 整机 ~1200W vs 1xA100 整机 ~1000W）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（成本差/功率差=时间，乘以1000将kW转换为W以匹配功率单位，再除以电价得到小时数），且整机功耗数值（2x4090~1200W, 1xA100~1000W）符合工程常识。
