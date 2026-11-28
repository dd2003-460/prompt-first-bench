# N270: 高偏移场景下的上下文窗口利用率：数学证明任务平均需要 8k-12k tokens 的上下文（包含定理、引理、推导过程），占 262k 窗口的 <5%；因此 '迷

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N107

## Claim

高偏移场景下的上下文窗口利用率：数学证明任务平均需要 8k-12k tokens 的上下文（包含定理、引理、推导过程），占 262k 窗口的 <5%；因此 '迷失在中间' 效应（N195）在此场景下影响可忽略，主要瓶颈为逻辑一致性而非位置编码衰减；建议将 max_model_len 临时调整为 32k 以释放 KV Cache 显存，支持更多并发序列（从 8 提升至 16），提升吞吐量 100%。

## Corrected Claim

高偏移场景下的上下文窗口利用率：数学证明任务平均需要 8k-12k tokens 的上下文，占 262k 窗口的 <5%；'迷失在中间' 效应影响可忽略，主要瓶颈为逻辑一致性。建议将 max_model_len 临时调整为 32k 以释放 KV Cache 显存，理论上支持更多并发序列（如从 8 提升至 16），有望显著提升吞吐量（具体提升幅度取决于硬件瓶颈类型，通常接近但未必严格等于 100%）。

## Evidence

[质询]吞吐量提升100%的结论依赖于并发数翻倍且系统处于计算受限（compute-bound）而非内存带宽受限（memory-bound）的假设，这在LLM推理中并非绝对成立，尤其是当KV Cache显著减少后，注意力机制的计算模式可能改变，导致线性加速假设失效。 | source=knowledge，逻辑自洽但吞吐量线性增长为经验性推断，缺乏特定硬件/模型配置下的实证支持，故降级。

## Search Query

vLLM dynamic max model length adjustment for short context tasks throughput gain
