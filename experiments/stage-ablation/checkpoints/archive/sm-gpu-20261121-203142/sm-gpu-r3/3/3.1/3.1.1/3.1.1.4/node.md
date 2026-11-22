# N207: RTX 5090 的显存带宽为 1.79 TB/s，在 FP8 量化下，27B 模型权重占用 13.5GB，KV Cache 占用 4GB，总占用 17.5GB

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N64, N65, N66

## Claim

RTX 5090 的显存带宽为 1.79 TB/s，在 FP8 量化下，27B 模型权重占用 13.5GB，KV Cache 占用 4GB，总占用 17.5GB，剩余 14.5GB 可支持约 3-4 个并发请求（Batch Size=3-4），其理论最大 TPS 约为 1.79 TB/s / 17.5 GB ≈ 102 tokens/s。

## Corrected Claim

RTX 5090 显存带宽为 1.79 TB/s，27B FP8 模型权重约 13.5GB，KV Cache 4GB，总占用 17.5GB，剩余 14.5GB 可支持约 3-4 个并发请求。其理论最大 TPS 需结合计算能力（FLOPS）与内存带宽综合评估，不能简单由带宽除以内存占用得出，实际吞吐量远高于 102 tokens/s。

## Evidence

[质询]TPS 计算逻辑存在严重错误：将显存带宽（1.79 TB/s）直接除以模型总占用内存（17.5 GB）得出的 102 tokens/s 并非理论最大 TPS。TPS 受限于计算能力（FLOPS）和内存带宽的平衡（Arithmetic Intensity），且 102 tokens/s 对于 RTX 5090 这种旗舰级 GPU 处理 27B 模型而言数值过低（通常单卡推理可达数百至数千 TPS，取决于具体实现和精度），该公式混淆了带宽上限与吞吐量概念。 | source=knowledge，逻辑校验发现 TPS 推导公式错误（带宽/内存大小 ≠ 吞吐量），且数值量级与硬件性能直觉不符，故降级。

## Search Query

RTX 5090 1.79 TB/s bandwidth FP8 27B model TPS calculation
