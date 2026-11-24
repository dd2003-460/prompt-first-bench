# N241: 公有云 CDN 基础设施成本中的 API 调用费项 C_api = Q_day * P_request_public / 1000，其中 P_request_p

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N62, N63, N68

## Claim

公有云 CDN 基础设施成本中的 API 调用费项 C_api = Q_day * P_request_public / 1000，其中 P_request_public 典型值为 ¥0.05-0.10/1000 requests（阿里云/Cloudflare 标准价），该部分在总成本中占比通常低于 5%。

## Corrected Claim

公有云 CDN 基础设施成本中的 API 调用费项 C_api = Q_day * P_request_public / 1000，其中 P_request_public 需根据具体云厂商（如阿里云、Cloudflare）的实时定价策略确定，该部分在总成本中的占比通常较低，具体比例取决于业务请求量与带宽/存储成本的相对规模。

## Evidence

[质询]P_request_public 的典型值（¥0.05-0.10/1000 requests）属于具体商业定价经验事实，且不同厂商（阿里云 vs Cloudflare）及不同计费模式（按量 vs 包年包月）差异巨大，该数值范围缺乏统一标准，易产生误导；此外，'占比低于5%' 高度依赖于 Q_day 与带宽/存储成本的相对比例，并非绝对真理。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体价格与占比属于经验数据，无法从第一性原理严格推出）

## Search Query

Alibaba Cloud CDN API request pricing per 1000 requests CNY
