# N249: 性价比分子（吞吐量）敏感性：若采用 vLLM custom all-reduce 优化 (N144)，吞吐量可能从 17.5 tokens/s 提升至 20-2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N88

## Claim

性价比分子（吞吐量）敏感性：若采用 vLLM custom all-reduce 优化 (N144)，吞吐量可能从 17.5 tokens/s 提升至 20-22 tokens/s，此时性价比指标从 0.00238 提升至 0.0027-0.0030 tokens/s/$，但仍显著低于单卡 5090 基准。

## Corrected Claim

性价比分子（吞吐量）敏感性：若采用 vLLM custom all-reduce 优化 (N144)，吞吐量可能从 17.5 tokens/s 提升至 20-22 tokens/s，此时性价比指标从 0.00238 提升至 0.0027-0.0030 tokens/s/$，但仍显著低于单卡 5090 基准。

## Evidence

先验知识/题面给定，逻辑校验通过：吞吐量提升幅度（17.5->20-22）与性价比指标线性增长（0.00238->0.0027-0.0030）在数学上自洽，且符合vLLM优化通常带来10%-30%性能提升的工程经验量级。

## Search Query

vLLM custom all-reduce performance improvement PCIe
