# N156: AMD RX 7900 XTX (24GB) 运行 Qwen3-27B W4 (GGUF Q4_K_M) 在 ROCm 环境下的实测 TPS 与 NVIDIA 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45

## Claim

AMD RX 7900 XTX (24GB) 运行 Qwen3-27B W4 (GGUF Q4_K_M) 在 ROCm 环境下的实测 TPS 与 NVIDIA 4090 的差距，由于 W4 量化对内存带宽敏感且 ROCm 优化滞后，预计 TPS 比 4090 低 15-25%，但价格低 $200-$400，需计算 Cost_Per_Token 以确定是否值得选择。

## Corrected Claim

AMD RX 7900 XTX (24GB) 运行 Qwen3-27B W4 (GGUF Q4_K_M) 在 ROCm 环境下，由于 W4 量化对内存带宽敏感且 ROCm 优化通常滞后于 NVIDIA CUDA 生态，其 TPS 预计低于 NVIDIA 4090，具体差距取决于软件栈优化程度；同时其价格通常低于 4090，需结合实时价格计算 Cost_Per_Token 以评估性价比。

## Evidence

[质询]该陈述包含具体的性能差距预测（15-25%）和价格区间（$200-$400），属于经验事实。虽然逻辑上W4量化确实对带宽敏感且ROCm优化通常滞后于CUDA，但具体的百分比差距和价格差随时间、驱动版本、具体模型实现（llama.cpp vs vLLM等）波动极大，无法仅凭第一性原理严格推出固定数值，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持；性能差距和价格属于动态市场/技术数据，非第一性原理可推导，故降级。

## Search Query

RX 7900 XTX Qwen3-27B GGUF Q4_K_M throughput vs RTX 4090
