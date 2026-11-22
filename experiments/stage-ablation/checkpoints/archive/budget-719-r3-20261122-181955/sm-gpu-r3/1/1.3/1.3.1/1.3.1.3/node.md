# N177: RX 7900 XTX 24GB 显存容量在 Qwen3-27B BF16 推理下的可行性：权重占用 54 GB，远超 24 GB 显存容量，必须采用量化（如 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

RX 7900 XTX 24GB 显存容量在 Qwen3-27B BF16 推理下的可行性：权重占用 54 GB，远超 24 GB 显存容量，必须采用量化（如 INT4/FP8）或 CPU offload；若使用 INT4 量化（权重 13.5 GB），剩余 10.5 GB 用于 KV Cache，需验证 32K 上下文下 KV Cache 占用是否超出剩余显存。

## Corrected Claim

RX 7900 XTX 24GB 显存容量在 Qwen3-27B BF16 推理下的可行性：权重占用 54 GB，远超 24 GB 显存容量，必须采用量化（如 INT4/FP8）或 CPU offload；若使用 INT4 量化（权重 13.5 GB），剩余 10.5 GB 用于 KV Cache，需验证 32K 上下文下 KV Cache 占用是否超出剩余显存。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数BF16权重约54GB，INT4量化后约13.5GB，均符合显存占用计算逻辑，且24GB显存确实无法容纳BF16权重，结论自洽。

## Search Query

Qwen3-27B INT4 quantization VRAM requirements 24GB
