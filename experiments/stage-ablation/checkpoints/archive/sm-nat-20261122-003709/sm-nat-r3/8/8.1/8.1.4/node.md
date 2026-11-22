# N239: 代入具体数值计算T_res：若S_cache=100TB（N60假设），R=50M/day，H_byte=0.8，则未命中字节速率 = 50,000,000 *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

代入具体数值计算T_res：若S_cache=100TB（N60假设），R=50M/day，H_byte=0.8，则未命中字节速率 = 50,000,000 * (1-0.8) * E[S] bytes/day，T_res = 100TB / (未命中字节速率)，得出具体天数。

## Corrected Claim

代入具体数值计算T_res：若S_cache=100TB（N60假设），R=50M/day，H_byte=0.8，则未命中字节速率 = 50,000,000 * (1-0.8) * E[S] bytes/day，T_res = 100TB / (未命中字节速率)，得出具体天数。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Calculate cache residence time in days given 100TB cache, 50M requests per day, and 80% byte hit rate
