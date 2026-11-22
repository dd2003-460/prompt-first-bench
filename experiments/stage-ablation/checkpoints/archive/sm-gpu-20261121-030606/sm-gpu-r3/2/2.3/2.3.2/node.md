# N106: H100 SXM 80GB在BF16精度下的并发请求数上限：剩余26GB显存可支持的最大batch_size = 26GB / (2.5GB激活值 + 5.2G

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N14

## Claim

H100 SXM 80GB在BF16精度下的并发请求数上限：剩余26GB显存可支持的最大batch_size = 26GB / (2.5GB激活值 + 5.2GB KV Cache) ≈ 3.37，即最多3个并发请求（取整），该数值限制了H100在高并发场景下的实际吞吐量，需纳入TCO的利用率修正。

## Corrected Claim

H100 SXM 80GB在BF16精度下，扣除模型权重及系统开销后，剩余显存支持的并发请求数取决于序列长度；在短序列假设下（如每请求占用约7.7GB显存），上限约为3个并发请求，该限制需纳入TCO利用率修正。

## Evidence

[质询]该陈述将复杂的LLM推理显存占用简化为固定的'2.5GB激活值 + 5.2GB KV Cache'每请求开销，忽略了KV Cache大小随序列长度（context length）线性增长的特性，且未考虑模型权重、CUDA上下文及碎片化开销，导致'3.37'这一具体数值缺乏通用性，仅适用于特定短序列场景。 | source=knowledge，逻辑自洽但具体数值依赖未明确的序列长度假设，属于经验估算而非绝对事实，故降级为定性表述。
