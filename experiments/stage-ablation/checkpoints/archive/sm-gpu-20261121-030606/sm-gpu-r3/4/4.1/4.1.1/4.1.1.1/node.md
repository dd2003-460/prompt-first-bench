# N282: Qwen3-27B参数量27.0B的构成分解：包含Embedding层、28层Transformer Block（每层含QKV投影、FFN等）、LM Head层

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N120

## Claim

Qwen3-27B参数量27.0B的构成分解：包含Embedding层、28层Transformer Block（每层含QKV投影、FFN等）、LM Head层的总参数计数，需确认是否包含Tie Embedding参数以避免重复计算。

## Corrected Claim

Qwen3.5-27B（或相关变体）包含64层Transformer Block，而非28层；需确认Qwen3-27B的具体架构定义及层数。

## Evidence

[质询]参考来源[1]明确描述的是Qwen3.5-27B（或类似变体），其架构参数（64层、隐藏层5120、嵌入维度248320）与Qwen3-27B（通常基于Qwen2.5架构，层数通常为32或64但具体配置不同，且Qwen3系列通常不直接称为Qwen3.5）存在显著差异。更关键的是，来源标题和摘要均指向'Qwen3.5-27B'，而事实节点声称是'Qwen3-27B'。若Qwen3-27B实际存在且结构不同，则来源不匹配；若Qwen3-27B即指代该模型，则来源中的'64层'与事实节点中隐含的'28层'（或常见Qwen2.5-32B/72B的层数逻辑）可能存在冲突，且来源未直接支持'28层Transformer Block'这一具体分解。实际上，Qwen2.5-32B是32层，Qwen2.5-72B是80层。Qwen3-27B若存在，其具体层数需核实。来源[1]提到64层，这与事实节点中可能隐含的或常见的28层（如某些小模型）不符，且来源明确说是Qwen3.5，存在版本混淆风险。 | 来源[1]描述的是Qwen3.5-27B，层数为64，与事实节点中提到的'28层'（若指代Qwen3-27B的特定结构）或通用认知不符，且存在版本名称混淆（Qwen3 vs Qwen3.5），无法直接支持Qwen3-27B为28层的结论。

## Search Query

Qwen3-27B model architecture parameter breakdown embedding tie

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2010079474104963160&rut=725c7cff098d17c7d4f51c5362b5fa9f20078a8fe0233472d5b8a97dc40ea021', 'type': 'ddg', 'title': 'Qwen/Qwen3.5-27B模型结构（dense）分析 - 知乎'}
