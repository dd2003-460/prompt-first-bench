# N28: 量化精度对延迟的影响：INT8/FP8 推理相比 BF16 通常提速 1.2-1.5 倍（因内存带宽减半且计算单元支持），但需验证 Qwen3-27B 在 IN

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5

## Claim

量化精度对延迟的影响：INT8/FP8 推理相比 BF16 通常提速 1.2-1.5 倍（因内存带宽减半且计算单元支持），但需验证 Qwen3-27B 在 INT8 下的困惑度 (Perplexity) 增加 < 5% [待核验]

## Corrected Claim

INT8/FP8 推理相比 BF16 通常可带来显著加速（具体倍数取决于硬件与模型结构，常见范围约1.2-1.5倍），但 Qwen3-27B 在 INT8 下的困惑度增加幅度需通过实际基准测试验证，通常预期在可接受范围内（如<5%），但具体数值需实测确认。

## Evidence

[质询]该陈述包含两个独立断言：1. 量化提速1.2-1.5倍；2. Qwen3-27B INT8困惑度增加<5%。参考来源仅讨论FP8/INT8格式定义，未提供具体加速比数据，更未涉及Qwen3-27B的具体困惑度指标。对于特定模型（Qwen3-27B）的量化后困惑度变化属于经验事实，无法从第一性原理推导，且缺乏直接来源支持。 | 来源[1]仅介绍FP8/INT8格式，未提供加速比或Qwen3-27B困惑度数据；量化提速1.2-1.5倍符合一般工程经验（逻辑自洽），但特定模型困惑度<5%为经验事实，缺来源直接支持，故降级。

## Search Query

Qwen3-27B INT8 FP8 quantization perplexity degradation speedup ratio

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/694120813&rut=b050f10cd52322a967cd5925571a176c796887b5ab743e23b9f10f91c7f84dac', 'type': 'ddg', 'title': 'LLM推理量化：FP8 versus INT8 - 知乎'}
