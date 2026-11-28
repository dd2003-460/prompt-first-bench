# N57: NVIDIA L40S 的 BF16 理论峰值算力为 362 TFLOPS，GDDR6 带宽 864 GB/s，显存 48GB；由于 48GB < 54GB (

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

NVIDIA L40S 的 BF16 理论峰值算力为 362 TFLOPS，GDDR6 带宽 864 GB/s，显存 48GB；由于 48GB < 54GB (BF16 权重)，无法以 BF16 精度驻留 27B 模型，仅支持 FP8/INT8 (27GB) 或 W4 (13.5GB) 推理，且带宽限制导致 Decode 吞吐率较低。

## Corrected Claim

NVIDIA L40S 的 BF16 理论峰值算力为 362 TFLOPS，GDDR6 带宽 864 GB/s，显存 48GB；由于 48GB < 54GB (BF16 权重)，无法以 BF16 精度驻留 27B 模型，仅支持 FP8/INT8 (27GB) 或 W4 (13.5GB) 推理，且带宽限制导致 Decode 吞吐率较低。

## Evidence

先验知识/题面给定，逻辑校验通过：L40S 规格（48GB GDDR6, 864GB/s, ~362 TFLOPS BF16）符合公开数据；27B 模型 BF16 需 54GB > 48GB，故无法全量驻留，需量化至 FP8/INT8/W4，逻辑自洽。
