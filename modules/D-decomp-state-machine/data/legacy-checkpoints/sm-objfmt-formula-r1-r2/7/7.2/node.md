# N105: RTX 4090 与 RTX 5090 在 FP8 推理时的每 Token 延迟（Time per Token, TPT）对比，需考虑 KV Cache 读取带

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

RTX 4090 与 RTX 5090 在 FP8 推理时的每 Token 延迟（Time per Token, TPT）对比，需考虑 KV Cache 读取带宽占比，对于长上下文（32K+），带宽优势转化为延迟优势的比例并非线性，需查找基准测试数据

## Corrected Claim

RTX 4090 与 RTX 5090 在 FP8 推理时的每 Token 延迟对比中，长上下文（32K+）场景下 KV Cache 读取带宽是关键瓶颈。理论上带宽优势会转化为延迟优势，但具体转化比例取决于软件栈优化及计算访存重叠效率，需具体基准测试数据确认，不能简单假设为线性关系。

## Evidence

[质询]该陈述包含具体的硬件型号（RTX 4090/5090）和特定的性能指标（FP8 TPT、KV Cache带宽占比），属于经验事实。由于缺乏具体的基准测试数据支持，无法验证‘非线性’这一具体结论的准确性，且不同实现（如FlashAttention版本、量化方式）可能导致结果差异巨大。 | 逻辑上，长上下文下KV Cache读取确实受显存带宽限制，带宽提升对延迟的影响通常是非线性的（受计算与访存重叠影响），符合计算机体系结构基本原理。但作为search节点，缺乏具体基准数据支持特定硬件对比结论，依据经验事实排除条款降级。

## Search Query

RTX 4090 vs RTX 5090 LLM inference latency time per token FP8 long context benchmark
