# N431: 在 16GB 显存限制下，剩余可用于 KV Cache 的空间为 16GB - 12.1GB (W3权重+开销) ≈ 3.9GB。若 KV Cache 使用 I

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N144

## Claim

在 16GB 显存限制下，剩余可用于 KV Cache 的空间为 16GB - 12.1GB (W3权重+开销) ≈ 3.9GB。若 KV Cache 使用 INT4 量化，每 token 占用从 BF16 的 256KB 降至 128KB (2 * 64 layers * 8 heads * 128 dim * 1 byte)，3.9GB 可支持约 31,000 tokens 的上下文，勉强覆盖 32K 需求但无并发余量。

## Corrected Claim

在 16GB 显存限制下，剩余可用于 KV Cache 的空间为 16GB - 12.1GB (W3权重+开销) ≈ 3.9GB。若 KV Cache 使用 INT4 量化，每 token 占用从 BF16 的 256KB 降至 128KB (2 * 64 layers * 8 heads * 128 dim * 1 byte)，3.9GB 可支持约 31,000 tokens 的上下文，勉强覆盖 32K 需求但无并发余量。

## Evidence

先验知识/题面给定，逻辑校验通过：16GB-12.1GB=3.9GB；INT4下每token 128KB，3.9GB/128KB≈31,000 tokens，数值量级与计算逻辑自洽。
