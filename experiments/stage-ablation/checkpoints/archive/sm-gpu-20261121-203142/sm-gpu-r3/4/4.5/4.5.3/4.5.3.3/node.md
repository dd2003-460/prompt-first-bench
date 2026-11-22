# N291: 软件栈对带宽利用率的影响因子：vLLM (PagedAttention) vs llama.cpp vs TensorRT-LLM 在不同 Batch Size

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N93

## Claim

软件栈对带宽利用率的影响因子：vLLM (PagedAttention) vs llama.cpp vs TensorRT-LLM 在不同 Batch Size 下的带宽效率差异；通常 vLLM 在 Batch Size > 1 时能更好地隐藏延迟，提高有效带宽利用率 5-10%。

## Corrected Claim

vLLM (PagedAttention) 通过连续批处理（Continuous Batching）和内存优化，在 Batch Size > 1 时通常能比 llama.cpp 更好地隐藏延迟并提高有效带宽利用率，但具体提升幅度（如5-10%）因硬件和负载而异。

## Evidence

[质询]具体数值范围（5-10%）缺乏通用性，实际带宽利用率提升高度依赖于硬件架构（如HBM vs DDR）、模型大小及具体Batch Size阈值，不同场景下差异可能极大或极小，该固定区间可能误导。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

vLLM vs llama.cpp vs TensorRT-LLM memory bandwidth efficiency benchmark
