# N42: Qwen3-27B 的 KV Cache 参数：L=32 (layers), H=128 (head_dim), 用于验证 KV Cache 计算公式中的参数取

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

Qwen3-27B 的 KV Cache 参数：L=32 (layers), H=128 (head_dim), 用于验证 KV Cache 计算公式中的参数取值

## Corrected Claim

Qwen3.8-27B 采用混合注意力架构，总层数 L=64，其中仅 16 层为全注意力层，其余为线性注意力层；其 KV Cache 参数不能简单用 L=32 的全注意力模型公式验证。

## Evidence

[质询]来源明确指出 Qwen3.8-27B 采用混合注意力机制（64层中仅16层全注意力），且每token KV Cache为32/64 KiB，这与陈述中假设的 L=32 全注意力层及隐含的 dense 架构参数不符，存在架构与参数量的根本性矛盾。 | 来源[1]指出 Qwen3.8-27B 为混合注意力模型（16层全注意力+48层线性注意力），总层数64，与陈述中 L=32 的全注意力假设矛盾，且 KV Cache 大小计算逻辑不同。

## Search Query

Qwen3-27B hidden size head dim layers configuration

## Retrieval Sources

- {'url': 'https://github.com/wuhy80/wuhy-notes/blob/main/%E5%A4%A7%E6%A8%A1%E5%9E%8B/04-%E9%83%A8%E7%BD%B2%E4%B8%8E%E5%B7%A5%E5%85%B7%E9%93%BE/%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2/Qwen3.8-27B%20%E6%98%BE%E5%AD%98%E4%B8%8E%20KV%20Cache%20%E9%A2%84%E7%AE%97.md&rut=a94eec89f1a98dac6ec35d4ca8663ef3619808cf53158f3466fe82f509863d12', 'type': 'ddg', 'title': 'Qwen3.8-27B 显存与 KV Cache 预算.md - GitHub'}
