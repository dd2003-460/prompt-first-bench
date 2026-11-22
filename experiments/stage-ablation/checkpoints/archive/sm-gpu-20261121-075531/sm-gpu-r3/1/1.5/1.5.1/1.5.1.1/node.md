# N158: TP=2 BF16 模式下，RTX 5090 (32GB) 每卡显存占用 29.68GB，剩余 2.32GB 用于系统开销和动态激活波动；该剩余空间极小，若 B

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

TP=2 BF16 模式下，RTX 5090 (32GB) 每卡显存占用 29.68GB，剩余 2.32GB 用于系统开销和动态激活波动；该剩余空间极小，若 Batch Size > 1 或上下文长度波动，极易导致 OOM (Out Of Memory)，需验证 vLLM/llama.cpp 在 32GB 卡上运行 27B BF16 TP=2 的实际稳定性与最大安全 Batch Size。

## Corrected Claim

TP=2 BF16 模式下，RTX 5090 (32GB) 每卡显存占用 29.68GB，剩余 2.32GB 用于系统开销和动态激活波动；该剩余空间极小，若 Batch Size > 1 或上下文长度波动，极易导致 OOM (Out Of Memory)，需验证 vLLM/llama.cpp 在 32GB 卡上运行 27B BF16 TP=2 的实际稳定性与最大安全 Batch Size。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数BF16模型权重约54GB，TP=2切分后每卡约27GB，加上KV Cache及激活值开销，29.68GB的占用量级符合工程直觉，剩余2.32GB确实极小，OOM风险判断合理。

## Search Query

RTX 5090 32GB Qwen3-27B BF16 tensor parallel 2 OOM batch size limit
