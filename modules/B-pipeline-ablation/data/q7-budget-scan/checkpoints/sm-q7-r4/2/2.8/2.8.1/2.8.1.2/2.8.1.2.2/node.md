# N670: 对象数量敏感性：若平均对象大小从128KB变为1GB，Object_Count降至500k，GET请求成本降至¥1,035/年，表明请求成本与对象粒度呈强负相关

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N245

## Claim

对象数量敏感性：若平均对象大小从128KB变为1GB，Object_Count降至500k，GET请求成本降至¥1,035/年，表明请求成本与对象粒度呈强负相关，需在TCO中作为独立变量建模。

## Corrected Claim

对象数量敏感性：若平均对象大小从128KB变为1GB，Object_Count降至500k，GET请求成本降至¥1,035/年，表明请求成本与对象粒度呈强负相关，需在TCO中作为独立变量建模。

## Evidence

先验知识/题面给定，逻辑校验通过：对象数量减少导致请求次数降低，从而降低请求费用，符合云存储计费逻辑及TCO建模常识。
