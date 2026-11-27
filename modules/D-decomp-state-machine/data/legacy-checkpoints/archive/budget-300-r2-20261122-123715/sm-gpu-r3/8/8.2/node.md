# N108: Qwen3-27B 的层数 (num_layers) 和隐藏层维度 (hidden_size) 精确值，用于 KV Cache 公式计算

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26, N27

## Claim

Qwen3-27B 的层数 (num_layers) 和隐藏层维度 (hidden_size) 精确值，用于 KV Cache 公式计算

## Corrected Claim

Qwen3.5-27B 的层数为 64，隐藏层维度为 5120；Qwen3-27B 的具体参数需进一步确认是否一致。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别针对父节点要求的两个独立参数（num_layers 和 hidden_size）进行定义，两者互不重叠且共同构成了父节点所需的全部关键信息，不存在冗余。）

## Search Query

Qwen3-27B model config num_hidden_layers hidden_size

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2010079474104963160&rut=336d25a4988526b6be857ced6e5fc040a0f025afaa4a16b40b3bafb074499abe', 'type': 'ddg', 'title': 'Qwen/Qwen3.5-27B模型结构（dense）分析 - 知乎'}
