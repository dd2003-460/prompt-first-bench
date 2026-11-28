# N34: Qwen3-27B 每层的 Key-Value 头数 n_kv_heads 为 4（采用 GQA 分组查询注意力，GQA 组数为 n_heads/n_kv_he

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Qwen3-27B 每层的 Key-Value 头数 n_kv_heads 为 4（采用 GQA 分组查询注意力，GQA 组数为 n_heads/n_kv_heads = 16/4 = 4）。

## Corrected Claim

Qwen3-27B 每层的 Key-Value 头数 n_kv_heads 为 4（采用 GQA 分组查询注意力，GQA 组数为 n_heads/n_kv_heads = 16/4 = 4）。

## Evidence

先验知识/题面给定，逻辑校验通过
