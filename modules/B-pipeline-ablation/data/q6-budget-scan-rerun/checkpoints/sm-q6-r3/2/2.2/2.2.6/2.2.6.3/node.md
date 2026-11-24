# N203: 自建策略下回源带宽成本对总成本的敏感性系数 Sensitivity_Share_Backbone = (Total_Origin_Traffic_TB * Pr

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

自建策略下回源带宽成本对总成本的敏感性系数 Sensitivity_Share_Backbone = (Total_Origin_Traffic_TB * Price_Per_TB_Backbone) / Total_Cost_Self，由于回源流量仅占下行流量的20%且单价较低，该占比通常<10%，远低于公有云策略中带宽成本60-80%的占比

## Corrected Claim

自建策略下回源带宽成本对总成本的敏感性系数 Sensitivity_Share_Backbone = (Total_Origin_Traffic_TB * Price_Per_TB_Backbone) / Total_Cost_Self，由于回源流量仅占下行流量的20%且单价较低，该占比通常<10%，远低于公有云策略中带宽成本60-80%的占比

## Evidence

先验知识/题面给定，逻辑校验通过：自建策略中回源流量占比低（约20%）且带宽单价远低于公有云出口带宽，导致其成本占比通常低于10%，符合经济直觉与工程常识。
