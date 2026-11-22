# N250: ExLlama2 在 32K 上下文下，若启用 KV Cache 量化（如 INT8/INT4），KV Cache 内存占用可降低至 BF16 的 50%-25

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N81

## Claim

ExLlama2 在 32K 上下文下，若启用 KV Cache 量化（如 INT8/INT4），KV Cache 内存占用可降低至 BF16 的 50%-25%，但引入的解量化计算开销导致 Prefill 吞吐量下降约 10-15% [待核验]，其内存碎片率低于 5% 的 claim 需通过实际 profiling 验证，通常其内存效率比 vLLM 高 5-10% 在长上下文场景。

## Corrected Claim

ExLlama2 在 32K 上下文下，若启用 KV Cache 量化（如 INT8/INT4），KV Cache 内存占用理论上可降低至 BF16 的 50%-25%。量化引入的解量化计算开销通常会导致 Prefill 吞吐量有所下降，具体幅度取决于硬件实现；其内存管理效率在长上下文场景下通常优于 vLLM，但具体性能增益需通过实际 profiling 验证。

## Evidence

[质询]该陈述包含多个具体的经验性数值指标（Prefill吞吐量下降10-15%、内存碎片率<5%、内存效率比vLLM高5-10%），这些属于特定软件版本在特定硬件环境下的性能基准数据，无法从第一性原理推导，且缺乏来源支持，存在数值不准确或过时风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

ExLlama2 KV cache quantization memory efficiency vs vLLM 32k context
