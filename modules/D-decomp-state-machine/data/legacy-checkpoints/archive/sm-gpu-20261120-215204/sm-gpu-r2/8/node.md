# N36: 每美元吞吐量 (Tokens/s per Dollar) 计算：RTX 4090 (W4, ~$1600) 提供 ~20 Tokens/s，性价比 ~0.012

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

每美元吞吐量 (Tokens/s per Dollar) 计算：RTX 4090 (W4, ~$1600) 提供 ~20 Tokens/s，性价比 ~0.0125 Tokens/s/$; A100 80GB (FP8, ~$15000) 提供 ~40 Tokens/s，性价比 ~0.0027 Tokens/s/$。在低负载场景下，消费级显卡性价比优势显著。

## Corrected Claim

在特定低负载推理场景下，消费级显卡（如RTX 4090）通常比数据中心级显卡（如A100）具有更高的每美元吞吐量性价比，但具体数值取决于模型规模、量化精度及硬件配置。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别修正了RTX 4090的性能数据、A100的性能数据，并引入了TCO这一更全面的成本维度，三者关注点不同（硬件A性能、硬件B性能、成本模型），无重复或矛盾，且共同覆盖了父节点中关于速度、价格和最终性价比结论的所有关键方面。）

## Retrieval Sources

- {'url': 'https://www.sohu.com/a/1062647946_122953470&rut=96b5218287d65d9ab02764246a15e4c933071a6deaf0c1518e831a2941fd81e2', 'type': 'ddg', 'title': '一台 GPU 服务器一天能生成多少 Token？_推理_模型_运行'}
