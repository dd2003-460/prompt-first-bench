# N143: Intel Arc A770 16GB 在 W4 量化下运行 Qwen3-27B 时，模型权重 (13.5GB) + KV Cache (4.5GB) + 激活

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

Intel Arc A770 16GB 在 W4 量化下运行 Qwen3-27B 时，模型权重 (13.5GB) + KV Cache (4.5GB) + 激活值 (2GB) 总计 20GB，超出 16GB 显存 4GB，必须将至少 4GB 权重或 KV Cache Offload 至 CPU 内存。

## Corrected Claim

Intel Arc A770 16GB 在 W4 量化下运行 Qwen3-27B 时，模型权重 (13.5GB) + KV Cache (4.5GB) + 激活值 (2GB) 总计 20GB，超出 16GB 显存 4GB，必须将至少 4GB 权重或 KV Cache Offload 至 CPU 内存。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B在W4量化下权重约13.5GB，加上KV Cache和激活值后总显存需求20GB，确实超出16GB显存，需Offload 4GB至CPU内存，数值量级合理且逻辑自洽。
