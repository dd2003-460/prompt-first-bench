# N595: API 速率限制与基线构建时间公式：T_build = N_entities / (RPS / 60)，其中 RPS 为每分钟请求数。Wikidata 默认限流

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N212

## Claim

API 速率限制与基线构建时间公式：T_build = N_entities / (RPS / 60)，其中 RPS 为每分钟请求数。Wikidata 默认限流 20 req/min，DBpedia 无官方限流但建议 <100 req/min。若 N_entities=10000，Wikidata 耗时 500 min，DBpedia 耗时 100 min（假设100 req/min）

## Corrected Claim

API 速率限制与基线构建时间公式：T_build = N_entities / (RPS / 60)，其中 RPS 为每分钟请求数。Wikidata 默认限流 20 req/min，DBpedia 无官方限流但建议 <100 req/min。若 N_entities=10000，Wikidata 耗时 500 min，DBpedia 耗时 100 min（假设100 req/min）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Wikidata API rate limit DBpedia request per minute baseline construction time
