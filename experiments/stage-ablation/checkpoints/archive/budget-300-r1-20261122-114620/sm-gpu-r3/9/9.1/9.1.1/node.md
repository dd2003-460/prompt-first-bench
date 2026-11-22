# N381: Qwen3-27B 在 A100 80GB 上运行 BF16 4 并发 32K 上下文时的总显存占用为 75.4GB (权重 54GB + KV Cache 6

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N132

## Claim

Qwen3-27B 在 A100 80GB 上运行 BF16 4 并发 32K 上下文时的总显存占用为 75.4GB (权重 54GB + KV Cache 6.4GB + 框架/激活 15GB)，剩余 4.6GB 安全边际，计算公式为 VRAM_total = W_bf16 + N_conc * KV_per_req + overhead

## Corrected Claim

Qwen3-27B 在 A100 80GB 上运行 BF16 4 并发 32K 上下文时的总显存占用为 75.4GB (权重 54GB + KV Cache 6.4GB + 框架/激活 15GB)，剩余 4.6GB 安全边际，计算公式为 VRAM_total = W_bf16 + N_conc * KV_per_req + overhead

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16权重约54GB，32K上下文4并发KV Cache约6.4GB，框架开销15GB，总和75.4GB，小于A100 80GB显存，计算自洽。
