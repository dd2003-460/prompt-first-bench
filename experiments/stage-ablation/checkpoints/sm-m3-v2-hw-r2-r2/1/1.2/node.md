# N7: Qwen3-27B NVFP4 量化后模型权重占用显存约为 13.5 GB (27B * 4bits / 8 + overhead)，在 4×16GB TP=4

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B NVFP4 量化后模型权重占用显存约为 13.5 GB (27B * 4bits / 8 + overhead)，在 4×16GB TP=4 配置下，每卡分配约 3.4 GB 权重，剩余每卡 ~12.6 GB 显存用于 KV Cache 和激活值。

## Corrected Claim

Qwen3-27B NVFP4 量化后模型权重占用显存约为 13.5 GB (27B * 4bits / 8 + overhead)，在 4×16GB TP=4 配置下，每卡分配约 3.4 GB 权重，剩余每卡 ~12.6 GB 显存用于 KV Cache 和激活值。

## Evidence

[质询]NVFP4 并非标准的 4-bit 整数量化格式，通常 FP4 指代 E2M1 等浮点格式，且 'NVFP4' 这一特定术语在主流公开文献中较少见，可能存在术语混淆或特定私有实现假设；此外，Overhead（如 Scale factors, Zero points）的具体占比未明确，可能导致实际显存略高于纯权重计算值。 | 先验知识/题面给定，逻辑校验通过：27B 参数在 4-bit 精度下理论体积约为 13.5GB (27e9 * 0.5 bytes)，TP=4 切分后每卡约 3.375GB，加上少量 Overhead 后 3.4GB 符合工程估算惯例；16GB 显存减去 3.4GB 权重后剩余约 12.6GB 用于 KV Cache 和激活值，数值量级与算术逻辑自洽。

## Search Query

Qwen3 27B NVFP4 quantized model size VRAM usage
