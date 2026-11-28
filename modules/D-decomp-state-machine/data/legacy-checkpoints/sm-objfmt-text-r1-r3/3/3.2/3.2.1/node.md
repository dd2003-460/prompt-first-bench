# N55: NVIDIA A100 80GB SXM 的 BF16 理论峰值算力为 312 TFLOPS，HBM2e 带宽 2039 GB/s，显存 80GB 可容纳 BF

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

NVIDIA A100 80GB SXM 的 BF16 理论峰值算力为 312 TFLOPS，HBM2e 带宽 2039 GB/s，显存 80GB 可容纳 BF16 权重 (54GB) 加上 32K 上下文 KV Cache (~20GB)，总计 ~74GB，余量 6GB，满足容量需求且支持最高精度推理。

## Corrected Claim

NVIDIA A100 80GB SXM 的 BF16 理论峰值算力为 312 TFLOPS，HBM2e 带宽 2039 GB/s，显存 80GB 可容纳 BF16 权重 (54GB) 加上 32K 上下文 KV Cache (~20GB)，总计 ~74GB，余量 6GB，满足容量需求且支持最高精度推理。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB SXM 的 BF16 峰值算力确为 312 TFLOPS，HBM2e 带宽确为 2039 GB/s；显存容量计算（54GB 权重 + 20GB KV Cache = 74GB < 80GB）符合算术逻辑，且 6GB 余量足以应对运行时开销，结论自洽。
