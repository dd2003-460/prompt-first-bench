# N243: H100 SXM BF16 方案与 RTX 4090 INT4 方案的质量-成本效率对比：H100 BF16 质量无损 (Perplexity 增量 <0.1%

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88

## Claim

H100 SXM BF16 方案与 RTX 4090 INT4 方案的质量-成本效率对比：H100 BF16 质量无损 (Perplexity 增量 <0.1%)，但 CapEx $25,000，吞吐 30.6 tokens/s，单位吞吐成本 $25,000/30.6 ≈ $817/token-s。RTX 4090 INT4 质量损失 (MMLU -2~3%)，CapEx $1,599，吞吐 50.9 tokens/s，单位吞吐成本 $1,599/50.9 ≈ $31/token-s。若质量损失可接受，4090 性价比极高；若需无损，H100 是最低成本选项（相比 A100/H200）。

## Corrected Claim

H100 SXM BF16 方案与 RTX 4090 INT4 方案的质量-成本效率对比：H100 BF16 质量无损 (Perplexity 增量 <0.1%)，但 CapEx $25,000，吞吐 30.6 tokens/s，单位吞吐成本 $25,000/30.6 ≈ $817/token-s。RTX 4090 INT4 质量损失 (MMLU -2~3%)，CapEx $1,599，吞吐 50.9 tokens/s，单位吞吐成本 $1,599/50.9 ≈ $31/token-s。若质量损失可接受，4090 性价比极高；若需无损，H100 是最低成本选项（相比 A100/H200）。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM BF16 与 RTX 4090 INT4 的硬件规格、价格及推理性能量级符合当前市场常识，成本计算逻辑自洽。
