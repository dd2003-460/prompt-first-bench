# N211: 对象大小对 GET 费用的敏感性：若平均对象大小从 1 MB 增大至 10 MB，请求数减少 10 倍，年 GET 费用降至约 $2,295/年；若减小至 10

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N71

## Claim

对象大小对 GET 费用的敏感性：若平均对象大小从 1 MB 增大至 10 MB，请求数减少 10 倍，年 GET 费用降至约 $2,295/年；若减小至 100 KB，费用增至约 $229,480/年；因此对象粒度选择是云存储 TCO 的最敏感变量之一。

## Corrected Claim

对象大小对 GET 费用的敏感性：若平均对象大小从 1 MB 增大至 10 MB，请求数减少 10 倍，年 GET 费用降至约 $2,295/年；若减小至 100 KB，费用增至约 $229,480/年；因此对象粒度选择是云存储 TCO 的最敏感变量之一。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

AWS S3 object size impact on GET request cost
