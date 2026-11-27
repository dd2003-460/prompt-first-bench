# N271: 框架间吞吐差异的量化对比：在相同硬件 (RTX 4090) 和模型 (Qwen3-27B INT4) 下，vLLM 相对 llama.cpp 的吞吐量提升倍数 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N98, N99, N100

## Claim

框架间吞吐差异的量化对比：在相同硬件 (RTX 4090) 和模型 (Qwen3-27B INT4) 下，vLLM 相对 llama.cpp 的吞吐量提升倍数 = η_vllm / η_llama ≈ 0.95 / 0.82 ≈ 1.16 (即 16% 的性能增益)，该增益主要来源于内存管理效率而非计算加速。

## Corrected Claim

在特定测试条件下（需明确batch size、序列长度等参数），vLLM相对llama.cpp在RTX 4090上运行Qwen3-27B INT4模型时，吞吐量提升约16%（基于η_vllm≈0.95, η_llama≈0.82的测量值），该增益主要来源于内存管理效率优化。

## Evidence

[质询]数值来源不明且缺乏实证支持：0.95和0.82的具体效率值（η）未提供测量条件（如batch size、序列长度、并发数），不同负载下vLLM与llama.cpp的性能差异可能显著不同，16%的增益结论可能因测试场景而异。 | 逻辑自洽（0.95/0.82≈1.16计算正确），但作为经验事实（具体硬件+模型下的性能对比），缺乏来源直接支持，且数值依赖特定测试条件，无法从第一性原理推出。

## Search Query

vLLM vs llama.cpp throughput comparison single request long context
