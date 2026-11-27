# N191: 在 A100 80GB 上运行 BF16 模型时，剩余 15.7GB 显存支持的最大并发 Batch Size (假设单请求 32K 上下文) 约为 7-8 个

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

在 A100 80GB 上运行 BF16 模型时，剩余 15.7GB 显存支持的最大并发 Batch Size (假设单请求 32K 上下文) 约为 7-8 个 (15.7GB / 2.15GB per request ≈ 7.3)，若上下文缩短至 16K，Batch Size 可提升至 14-15 个，这直接决定了短期运营下的最大并发服务能力

## Corrected Claim

在 A100 80GB 上运行 BF16 模型时，剩余 15.7GB 显存支持的最大并发 Batch Size (假设单请求 32K 上下文) 约为 7-8 个 (15.7GB / 2.15GB per request ≈ 7.3)，若上下文缩短至 16K，Batch Size 可提升至 14-15 个，这直接决定了短期运营下的最大并发服务能力

## Evidence

先验知识/题面给定，逻辑校验通过：15.7GB / 2.15GB ≈ 7.3，15.7GB / 1.075GB ≈ 14.6，数值量级与算术推导自洽。
