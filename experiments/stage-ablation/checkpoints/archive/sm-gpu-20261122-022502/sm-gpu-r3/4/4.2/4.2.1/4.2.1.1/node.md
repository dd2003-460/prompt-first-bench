# N191: 2×RTX 4090在BF16推理负载下的GPU利用率实测值：基于vLLM/TensorRT-LLM在Qwen3-27B 32K上下文下的nvidia-smi监

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N62

## Claim

2×RTX 4090在BF16推理负载下的GPU利用率实测值：基于vLLM/TensorRT-LLM在Qwen3-27B 32K上下文下的nvidia-smi监控数据，GPU利用率平均为55%-65%（对应功耗420-490W），标准差约±8%，需n>5样本验证

## Corrected Claim

2×RTX 4090在BF16推理负载下（基于vLLM/TensorRT-LLM在Qwen3-27B 32K上下文），GPU利用率通常未达饱和，具体数值需实测验证，典型范围可能在50%-70%之间，功耗接近TDP上限。

## Evidence

[质询]该陈述包含具体的实测数值（55%-65%利用率、420-490W功耗），属于经验事实。由于检索失败，无法验证这些具体数值是否准确，且不同硬件配置、驱动版本及具体负载分布可能导致显著差异，存在数值偏差风险。 | 经验事实，逻辑自洽（BF16推理下GPU利用率未达100%符合常见瓶颈特征，功耗在TDP范围内），但缺来源支持。

## Search Query

RTX 4090 GPU utilization LLM inference BF16 32K context power consumption measured
