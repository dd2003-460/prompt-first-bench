# N754: 工作点A（高性低成/高延迟）：S3 Glacier Flexible Retrieval取回400TB冷数据，单价$0.01/GB，总成本 = 400,000 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N282

## Claim

工作点A（高性低成/高延迟）：S3 Glacier Flexible Retrieval取回400TB冷数据，单价$0.01/GB，总成本 = 400,000 * 0.01 * 7.2 = ¥28,800，预计完成时间1-5小时，适用于RTO容忍度>5小时的场景。

## Corrected Claim

工作点A（高性低成/高延迟）：S3 Glacier Flexible Retrieval取回400TB冷数据，单价$0.01/GB，总成本 = 400,000 * 0.01 = $4,000（约合人民币28,800元，按1 USD ≈ 7.2 CNY估算），预计完成时间1-5小时，适用于RTO容忍度>5小时的场景。

## Evidence

[质询]货币单位混淆：AWS S3 Glacier 的官方定价单位为美元（USD），计算中直接使用 $0.01/GB 却得出人民币（¥）结果，且未提供汇率换算依据，导致最终金额在量纲和实际价值上存在严重歧义或错误。 | 逻辑校验发现货币单位不一致（输入为 USD，输出为 CNY 且无汇率），属于内部矛盾；虽 source 为 knowledge，但存在可信攻击点且无法排除，故降级。

## Search Query

AWS S3 Glacier Flexible Retrieval pricing per GB
