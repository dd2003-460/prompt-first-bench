# N21: 消费级GPU候选集（2024Q4-2025Q1）：RTX 4090 (24GB), RTX 4080 Super (16GB), RTX 4070 Ti Sup

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

消费级GPU候选集（2024Q4-2025Q1）：RTX 4090 (24GB), RTX 4080 Super (16GB), RTX 4070 Ti Super (16GB), RTX 3090 (24GB, 二手/翻新), RTX 3090 Ti (24GB, 二手/翻新), RTX 4060 Ti 16GB (16GB), AMD RX 7900 XTX (24GB), AMD RX 7900 XT (20GB)。筛选标准：显存容量≥24GB以支持Qwen3-27B INT4/FP8权重+32K KV Cache，或16GB需严格量化+短上下文。

## Corrected Claim

消费级GPU候选集（2024Q4-2025Q1）包括RTX 4090 (24GB), RTX 4080 Super (16GB)等。建议优先选择显存≥24GB的型号以更好地支持大模型推理，16GB型号需配合严格量化和短上下文使用。

## Evidence

[质询]筛选标准中关于显存容量的量化估算（Qwen3-27B INT4/FP8 + 32K KV Cache 需 ≥24GB）属于经验性工程估算，且参考来源仅涉及价格对比，未提供显存需求的技术依据，无法验证该阈值是否准确或是否过于保守/激进。 | 来源[1]仅提及RTX 4090为消费级旗舰及价格，未覆盖其他GPU型号或显存筛选标准，属于间接/无关支持；显存需求为经验事实，逻辑自洽但缺直接来源支持。

## Search Query

best consumer GPU for 27B LLM inference 32k context 2024 2025 VRAM requirements

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2029878314618324784&rut=b0b833bc6ed876c1c71e1f5437702e972fffabe8dff573d3bb3aeb5abb912a67', 'type': 'ddg', 'title': '4090 vs A6000：同为消费级，专业卡真的更值得吗？ - 知乎'}
