# N93: 2×RTX 3090在BF16精度下运行Qwen3-27B的实测吞吐量（tokens/s）约为8-12 tokens/s（单用户，32K上下文），该数值低于单卡

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

2×RTX 3090在BF16精度下运行Qwen3-27B的实测吞吐量（tokens/s）约为8-12 tokens/s（单用户，32K上下文），该数值低于单卡RTX 4090 INT8性能（15-25 tokens/s）的主要原因包括：(1) PCIe通信开销导致的有效计算时间占比降低，(2) RTX 3090的内存带宽（936GB/s）低于RTX 4090（1008GB/s）导致KV Cache读取延迟增加，(3) BF16相比INT8的数据量翻倍导致内存带宽压力增大；需引用vLLM或llama.cpp在双卡PCIe环境下的具体benchmark日志

## Corrected Claim

2×RTX 3090在BF16精度下运行Qwen3-27B的吞吐量通常低于单卡RTX 4090 INT8性能，主要原因包括PCIe通信开销、RTX 3090内存带宽（936GB/s）低于RTX 4090（1008GB/s）以及BF16相比INT8数据量翻倍导致的带宽压力；具体吞吐量数值需参考特定环境下的实测benchmark日志。

## Evidence

[质询]该陈述包含具体的硬件性能实测数据（吞吐量数值）和特定软件环境下的基准测试结果，属于经验事实。由于检索无可用来源，无法验证这些具体数值（8-12 tokens/s vs 15-25 tokens/s）的准确性，且不同量化方案、批处理大小及具体模型版本可能导致数值波动，缺乏直接证据支持。 | 经验事实，逻辑自洽但缺来源支持。虽然BF16数据量翻倍、PCIe通信开销及带宽差异导致性能下降的逻辑在物理和工程原理上是成立的，但具体的吞吐量数值属于经验测量数据，无法从第一性原理严格推导，且无外部来源佐证。

## Search Query

2x RTX 3090 PCIe 4.0 Qwen 27B BF16 inference benchmark tokens per second
