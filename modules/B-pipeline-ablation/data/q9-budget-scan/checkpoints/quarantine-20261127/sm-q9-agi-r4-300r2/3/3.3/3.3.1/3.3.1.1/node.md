# N151: Google Scholar 非官方 API 的真实速率限制：由于无官方 API，第三方服务（如 SerpApi）的实际限额通常为 100-500 请求/天/账

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

Google Scholar 非官方 API 的真实速率限制：由于无官方 API，第三方服务（如 SerpApi）的实际限额通常为 100-500 请求/天/账户，而非 1000；超限后返回 429 或 CAPTCHA，需通过 IP 轮换或付费升级规避

## Corrected Claim

Google Scholar 无官方 API，第三方服务（如 SerpApi）的速率限制取决于具体服务商的套餐与政策，通常远低于 1000 请求/天，超限后常触发 429 错误或 CAPTCHA 验证，需通过 IP 轮换或升级付费计划来规避。

## Evidence

[质询]具体数值范围（100-500 请求/天）属于特定第三方服务商（如 SerpApi）的商业定价策略，随时间波动极大，且不同服务商差异显著，将其概括为‘实际限额通常’缺乏普适性和时效性保证，易误导用户认为这是固定标准。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且具体商业限额属动态经验数据，无法从第一性原理推导）

## Search Query

Google Scholar unofficial API rate limit SerpApi daily quota 429 error
