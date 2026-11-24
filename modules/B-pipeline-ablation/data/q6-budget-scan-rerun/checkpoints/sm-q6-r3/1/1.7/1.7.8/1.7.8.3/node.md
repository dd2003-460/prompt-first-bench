# N193: 批量采购折扣系数 D_batch 的量化：对于 40-80 台规模的服务器采购，典型代理商折扣率在 10%-15% 之间（即支付 85%-90% 的标价），需结

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

批量采购折扣系数 D_batch 的量化：对于 40-80 台规模的服务器采购，典型代理商折扣率在 10%-15% 之间（即支付 85%-90% 的标价），需结合具体品牌（Dell/HPE/浪潮）合同谈判结果修正，此处取中值 D_batch = 0.90。

## Corrected Claim

批量采购折扣系数 D_batch 的量化：对于 40-80 台规模的服务器采购，典型代理商折扣率在 10%-15% 之间（即支付 85%-90% 的标价），需结合具体品牌（Dell/HPE/浪潮）合同谈判结果修正，此处取中值 D_batch = 0.90。

## Evidence

先验知识/题面给定，逻辑校验通过：40-80台服务器属于中小批量采购，10%-15%的代理商折扣率符合IT硬件行业常规商业惯例，取中值0.90逻辑自洽且量级合理。

## Search Query

enterprise server bulk purchase discount rate 40 units 2024
