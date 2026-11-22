# N136: AMD MI300X 在 ROCm 栈下运行 vLLM 或 SGLang 推理 Qwen3-27B (BF16, 32K context) 的吞吐量 (toke

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

AMD MI300X 在 ROCm 栈下运行 vLLM 或 SGLang 推理 Qwen3-27B (BF16, 32K context) 的吞吐量 (tokens/s) 需检索 AMD 官方白皮书或第三方评测，预期值在 20-40 tokens/s 区间 [待核验]，需确认软件栈兼容性导致的性能折损系数。

## Corrected Claim

AMD MI300X 在 ROCm 栈下运行 vLLM 或 SGLang 推理 Qwen3-27B (BF16, 32K context) 的吞吐量需通过实际基准测试确认，预期值可能在 20-40 tokens/s 区间，但受软件栈兼容性及优化程度影响较大，具体数值待实测验证。

## Evidence

[质询]该吞吐量数值（20-40 tokens/s）属于特定硬件、软件栈及模型配置下的经验性能指标，无法从第一性原理推导，且缺乏官方白皮书或权威第三方评测的直接数据支持，存在因软件栈优化程度不同导致数值偏差的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值区间及兼容性折损系数）

## Search Query

AMD MI300X Qwen3-27B vLLM ROCm inference benchmark throughput
