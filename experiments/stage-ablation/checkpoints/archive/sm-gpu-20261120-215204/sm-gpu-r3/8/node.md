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

父节点级核验通过：正交+完备+无冗余（子节点1和2分别修正了两种硬件的具体吞吐量数据（基于带宽计算），属于不同硬件实例的参数修正，互不重叠；子节点3引入了TCO维度，修正了成本计算基准，与子节点1/2的吞吐量修正维度不同（一个是分子Tokens/s，一个是分母$）。三者共同构成了对父节点中‘吞吐量’和‘成本’两个核心变量的全面修正，逻辑正交且完备。）

## Retrieval Sources

- {'url': 'https://www.sohu.com/a/1062647946_122953470&rut=96b5218287d65d9ab02764246a15e4c933071a6deaf0c1518e831a2941fd81e2', 'type': 'ddg', 'title': '一台 GPU 服务器一天能生成多少 Token？_推理_模型_运行'}
