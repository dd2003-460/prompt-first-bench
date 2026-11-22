# N95: Mac Studio M2 Ultra 192GB在MLX框架下推理Qwen3-27B（INT8精度，权重约13.5GB）的实测吞吐量约为3-5 tokens/

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

Mac Studio M2 Ultra 192GB在MLX框架下推理Qwen3-27B（INT8精度，权重约13.5GB）的实测吞吐量约为3-5 tokens/s，远低于RTX 4090的约50-80 tokens/s，主要瓶颈在于CPU-GPU统一内存带宽（1.2TB/s）虽高但缺乏专用Tensor Core加速及CUDA生态优化。

## Corrected Claim

Mac Studio M2 Ultra在MLX框架下推理Qwen3-27B（INT8精度）的吞吐量显著低于RTX 4090，主要受限于缺乏专用Tensor Core加速及CUDA生态优化，具体吞吐量需实测确认（参考来源未提供该特定配置数据）。

## Evidence

[质询]参考来源[1]测试的是Qwen3.6-35B（4bit量化）在M2 Ultra 128GB上的表现，与待核验事实中的Qwen3-27B（INT8，192GB）在模型规模、量化精度及硬件配置上均不一致，无法直接支持具体吞吐量数值（3-5 tokens/s）；且该吞吐量数值属于经验事实，缺乏直接来源支持。 | 逻辑上，M2 Ultra虽带宽高但缺乏专用Tensor Core，推理大模型时吞吐量远低于RTX 4090符合硬件特性直觉；但来源[1]仅涉及不同模型和配置，未提供Qwen3-27B INT8在MLX下的具体吞吐量数据，属于间接相关且无法排除其他可能性，故降级。

## Search Query

Mac Studio M2 Ultra MLX Qwen3-27B inference benchmark tokens per second

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2053193167466402148&rut=10704adddf8160a50e87785ed695a9e8af18c65c05e8e13e9f67ab4fa6e7e7ef', 'type': 'ddg', 'title': '我在 Mac Studio 上跑通 Qwen3.6-35B，这篇可能是你见过最实的加速配置'}
