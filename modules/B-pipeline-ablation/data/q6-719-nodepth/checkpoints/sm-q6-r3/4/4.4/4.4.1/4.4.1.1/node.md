# N287: WAF_Throughput_Cost = Peak_QPS_per_POP × Rule_Complexity_Factor × Unit_Pricing_P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N100

## Claim

WAF_Throughput_Cost = Peak_QPS_per_POP × Rule_Complexity_Factor × Unit_Pricing_Per_Rule_Sec，其中 Peak_QPS_per_POP = Total_Daily_Requests / 10 / 86400 × Peak_Factor(2.5)，Rule_Complexity_Factor 典型值为 1.5-3.0（取决于正则/CC规则数量），Unit_Pricing 需根据具体厂商（如阿里云/Cloudflare）按量计费标准确定。

## Corrected Claim

WAF_Throughput_Cost = Peak_QPS_per_POP × Rule_Complexity_Factor × Unit_Pricing_Per_Rule_Sec，其中 Peak_QPS_per_POP = Total_Daily_Requests / 10 / 86400 × Peak_Factor(2.5)，Rule_Complexity_Factor 典型值为 1.5-3.0（取决于正则/CC规则数量），Unit_Pricing 需根据具体厂商（如阿里云/Cloudflare）按量计费标准确定。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cloud WAF pricing per rule per second cost model
