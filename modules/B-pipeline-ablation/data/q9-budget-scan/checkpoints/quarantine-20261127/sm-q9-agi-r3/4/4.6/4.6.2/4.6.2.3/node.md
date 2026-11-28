# N227: PubMed E-utilities (esearch/efetch) 的速率限制为 10 requests/second per IP，若并发请求超过此限制将

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

PubMed E-utilities (esearch/efetch) 的速率限制为 10 requests/second per IP，若并发请求超过此限制将收到 429 错误；在科研闭环中，单次假设验证通常需检索 3-5 个实体，总请求量低于限制，但若批量验证需引入令牌桶限流器，间隔 100ms。

## Corrected Claim

PubMed E-utilities (esearch/efetch) 的速率限制为 10 requests/second per IP，若并发请求超过此限制将收到 429 错误；在科研闭环中，单次假设验证通常需检索 3-5 个实体，总请求量低于限制，但若批量验证需引入令牌桶限流器，间隔 100ms。

## Evidence

先验知识/题面给定，逻辑校验通过：PubMed E-utilities 官方文档明确规定非 API key 用户限速为 10 req/s，超限返回 429；100ms 间隔对应 10 req/s 的令牌桶策略符合工程常识。

## Search Query

PubMed E-utilities rate limit 10 requests per second 429 error handling
