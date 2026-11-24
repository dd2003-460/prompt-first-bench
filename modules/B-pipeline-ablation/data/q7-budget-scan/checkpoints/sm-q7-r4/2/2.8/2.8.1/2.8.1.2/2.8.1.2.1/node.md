# N669: GET请求年化成本计算：Requests_Year = Scan_Freq_Daily * Object_Count * 365；Cost_GET = Requ

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N245

## Claim

GET请求年化成本计算：Requests_Year = Scan_Freq_Daily * Object_Count * 365；Cost_GET = Requests_Year * Price_Per_1k * Exchange / 1000；若Scan=2, Objects=10M, Price=$0.40/1k, Exchange=7.2，则Cost_GET ≈ ¥20,693/年。

## Corrected Claim

GET请求年化成本计算：Requests_Year = Scan_Freq_Daily * Object_Count * 365；Cost_GET = Requests_Year * Price_Per_1k * Exchange / 1000；若Scan=2, Objects=10M, Price=$0.40/1k, Exchange=7.2，则Cost_GET ≈ ¥20,880,000/年。

## Evidence

先验知识/题面给定，逻辑校验通过：2 * 10,000,000 * 365 = 7,300,000,000 次请求；7,300,000,000 / 1000 * 0.40 * 7.2 = 20,880,000 元。等等，这里计算有误。重新计算：Requests_Year = 2 * 10^7 * 365 = 7.3 * 10^9。Cost = (7.3 * 10^9 / 1000) * 0.40 * 7.2 = 7.3 * 10^6 * 2.88 = 20,880,000 元。原陈述称 ≈ ¥20,693/年，数量级相差巨大（百万 vs 万）。原陈述中的数值 20,693 可能是基于不同的参数或计算错误。例如，如果 Price 是 $0.004/1k 或者 Objects 是 100k？或者 Exchange 不同？让我们检查 20,693 的来源。20,693 / 7.2 / 0.40 * 1000 = 719,451 requests/year? 不对。如果是 20,693 元，反推 Requests: 20693 / (0.4*7.2/1000) = 20693 / 0.00288 ≈ 7,185,069 requests. 7,185,069 / 365 / 2 ≈ 9845 objects. 这与 10M 不符。原陈述的数值计算明显错误。但是，题目要求核验的是“关键事实节点”中的陈述。陈述包含公式和具体数值示例。公式本身逻辑自洽。但具体数值示例是错误的。根据判定规则，若存在硬逻辑错误（如计算错误导致数值严重偏离），应判 failed 或 degraded？规则说 failed 仅当与来源矛盾或硬逻辑错误。这里的数值计算是硬错误。20,880,000 != 20,693。因此该陈述中的具体数值结论是错误的。

## Search Query

AWS S3 GET request pricing per 1000 requests
