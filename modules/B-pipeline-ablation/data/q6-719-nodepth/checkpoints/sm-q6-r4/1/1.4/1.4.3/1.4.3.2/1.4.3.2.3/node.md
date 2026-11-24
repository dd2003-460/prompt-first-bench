# N479: SLA 违约成本量化：若过载导致 P99 延迟超标，公有云 CDN 的 SLA 赔偿通常为月度服务费的 10%-30%（N18），需计算单次过载事件的预期赔偿金

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N153

## Claim

SLA 违约成本量化：若过载导致 P99 延迟超标，公有云 CDN 的 SLA 赔偿通常为月度服务费的 10%-30%（N18），需计算单次过载事件的预期赔偿金额 E[penalty] = P(overload) × Penalty_per_event，并与增加 Safety_Margin 的边际成本比较。

## Corrected Claim

SLA违约成本量化：若过载导致P99延迟超标，公有云CDN的SLA赔偿通常依据具体合同条款执行，常见形式为月度服务费的一定比例（如10%-100%不等，视服务等级和厂商政策而定），需计算单次过载事件的预期赔偿金额 E[penalty] = P(overload) × Penalty_per_event，并与增加 Safety_Margin 的边际成本比较。

## Evidence

[质询]SLA赔偿比例（10%-30%）属于具体商业合同条款，不同云厂商（AWS, Azure, GCP等）及不同服务等级（Basic vs Premium）差异巨大，且通常有月度赔偿上限（如不超过当月费用的100%或特定金额），直接断言为固定区间缺乏普适性依据，存在以偏概全风险。 | 经验事实，逻辑自洽但缺来源支持；SLA赔偿具体比例因厂商和合同而异，无法从第一性原理推出，且无外部来源验证该特定数值区间。
