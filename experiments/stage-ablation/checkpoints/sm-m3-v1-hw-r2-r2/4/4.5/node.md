# N21: 并行度对时间的非线性影响：max-num-seqs=8 时，由于 KV Cache 内存限制（16GB/卡），实际有效并发数受限于上下文长度；若 avg_ctx

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

并行度对时间的非线性影响：max-num-seqs=8 时，由于 KV Cache 内存限制（16GB/卡），实际有效并发数受限于上下文长度；若 avg_ctx > 32k tokens，有效并发降至 2-4，导致吞吐量下降约 50%

## Corrected Claim

并行度对时间的影响受KV Cache内存限制制约：在16GB/卡显存限制下，若平均上下文长度超过32k tokens，有效并发数将显著降低（通常降至个位数），导致吞吐量出现明显下降。

## Evidence

[质询]具体数值（如avg_ctx>32k时并发降至2-4、吞吐量下降50%）缺乏通用性，高度依赖具体模型架构、硬件配置及调度策略，属于特定场景下的经验估算而非普适规律。 | 先验知识/题面给定，逻辑校验通过：KV Cache占用随上下文线性增长，16GB显存下长上下文确实会显著降低并发度，进而影响吞吐，但具体降幅和并发数需实测验证。

## Search Query

vLLM max_num_seqs KV cache memory limit V100 16GB context length throughput degradation
