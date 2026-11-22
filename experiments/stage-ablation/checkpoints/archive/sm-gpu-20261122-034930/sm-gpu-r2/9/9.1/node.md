# N145: RTX 4090在INT8精度下推理Qwen3-27B (Batch=1, 32K ctx) 的理论吞吐上限为 1008 GB/s / 37.7 GB ≈ 26

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N43

## Claim

RTX 4090在INT8精度下推理Qwen3-27B (Batch=1, 32K ctx) 的理论吞吐上限为 1008 GB/s / 37.7 GB ≈ 26.7 tokens/s，该值由显存带宽除以单次token生成需读取的数据量（权重27GB + KV Cache 10.7GB）决定。

## Corrected Claim

RTX 4090在INT8精度下推理Qwen3-27B (Batch=1, 32K ctx) 的理论吞吐上限为 1008 GB/s / 37.7 GB ≈ 26.7 tokens/s，该值由显存带宽除以单次token生成需读取的数据量（权重27GB + KV Cache 10.7GB）决定。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存带宽1008GB/s与Qwen3-27B INT8权重约27GB、32K上下文KV Cache约10.7GB的估算符合工程常识，算术推导1008/37.7≈26.7正确。
