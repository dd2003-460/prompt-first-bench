# N168: RTX 5090 在 W4 量化下，理论 TPS 上限同样受 KV Cache 影响；32K 上下文下 KV Cache 占用更大（因带宽高可支持更长上下文，但

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N50

## Claim

RTX 5090 在 W4 量化下，理论 TPS 上限同样受 KV Cache 影响；32K 上下文下 KV Cache 占用更大（因带宽高可支持更长上下文，但此处固定 32K），假设 KV Cache 为 3 GB，总读取量 16.5 GB，理论 TPS ≈ 1792 / 16.5 ≈ 108.6 TPS；实际受 Blackwell 架构计算单元效率及 W4 解码单元（Tensor Core 对 INT4 支持）限制，实测可能在 80-95 TPS 区间，需验证 W4 解码效率是否低于 W8。

## Corrected Claim

RTX 5090 在 W4 量化下，理论 TPS 上限同样受 KV Cache 影响；32K 上下文下 KV Cache 占用更大（因带宽高可支持更长上下文，但此处固定 32K），假设 KV Cache 为 3 GB，总读取量 16.5 GB，理论 TPS ≈ 1792 / 16.5 ≈ 108.6 TPS；实际受 Blackwell 架构计算单元效率及 W4 解码单元（Tensor Core 对 INT4 支持）限制，实测可能在 80-95 TPS 区间，需验证 W4 解码效率是否低于 W8。

## Evidence

先验知识/题面给定，逻辑校验通过：1792/16.5≈108.6计算正确，带宽瓶颈逻辑自洽，W4量化对KV Cache影响及Blackwell架构限制符合硬件常识。

## Search Query

RTX 5090 W4 quantized LLM inference throughput KV cache 32k context memory bandwidth utilization
