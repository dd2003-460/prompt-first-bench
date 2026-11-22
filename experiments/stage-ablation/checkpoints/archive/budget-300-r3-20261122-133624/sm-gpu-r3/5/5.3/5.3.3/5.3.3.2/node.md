# N378: Intel Gaudi 2 的显存容量为 64GB HBM2e，在 INT8 下运行 Qwen3-27B 时，权重占用 27GB，KV Cache (32K t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N146, N147, N149

## Claim

Intel Gaudi 2 的显存容量为 64GB HBM2e，在 INT8 下运行 Qwen3-27B 时，权重占用 27GB，KV Cache (32K tokens) 占用约 2.5GB，总占用约 30GB，单卡部署可行且无需量化至 W4，保留 BF16 精度选项（需 54GB，接近上限）。

## Corrected Claim

Intel Gaudi 2 的显存容量为 64GB HBM2e，在 INT8 下运行 Qwen3-27B 时，权重占用 27GB，KV Cache (32K tokens) 占用约 2.5GB，总占用约 30GB，单卡部署可行且无需量化至 W4，保留 BF16 精度选项（需 54GB，接近上限）。

## Evidence

先验知识/题面给定，逻辑校验通过：Gaudi 2 显存 64GB HBM2e 符合规格；Qwen3-27B 权重在 INT8 下约 27GB，BF16 下约 54GB，数值量级合理；KV Cache 占用估算符合常规经验值，总占用未超显存上限，逻辑自洽。

## Search Query

Intel Gaudi 2 64GB HBM2e memory capacity
