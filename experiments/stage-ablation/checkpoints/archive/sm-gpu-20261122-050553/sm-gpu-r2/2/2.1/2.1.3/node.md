# N56: BF16 推理时的激活值 (Activations) 显存占用：在 Decode 阶段，激活值占用较小（仅当前 Token 的中间结果），约 1-2 GB；但在

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

BF16 推理时的激活值 (Activations) 显存占用：在 Decode 阶段，激活值占用较小（仅当前 Token 的中间结果），约 1-2 GB；但在 Prefill 阶段（处理 32K 上下文），激活值占用可达 10-20 GB（取决于 Batch Size 和序列长度），需确保总显存 = 权重 (54GB) + KV Cache (8.6GB) + 激活值 (20GB) + 框架开销 (2GB) ≈ 85GB，这意味着 BF16 下需要至少 80GB+ 显存的单卡（如 H100 80GB 可能仍紧张，需 A100 80GB 或 2x A100 40GB）。

## Corrected Claim

BF16 推理时的激活值 (Activations) 显存占用：在 Decode 阶段，激活值占用较小（仅当前 Token 的中间结果），约 1-2 GB；但在 Prefill 阶段（处理 32K 上下文），激活值占用可达 10-20 GB（取决于 Batch Size 和序列长度），需确保总显存 = 权重 (54GB) + KV Cache (8.6GB) + 激活值 (20GB) + 框架开销 (2GB) ≈ 85GB，这意味着 BF16 下需要至少 80GB+ 显存的单卡（如 H100 80GB 可能仍紧张，需 A100 80GB 或 2x A100 40GB）。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16下大模型推理显存构成（权重+KV Cache+激活值+开销）符合工程常识，Prefill阶段激活值随序列长度线性增长且占用较大（10-20GB量级合理），Decode阶段仅处理单Token激活值较小（1-2GB量级合理），总显存估算85GB与80GB+单卡需求逻辑自洽。

## Search Query

LLM inference activation memory usage prefill vs decode BF16 32K context
