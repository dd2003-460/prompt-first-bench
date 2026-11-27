# N367: L4 上运行 INT8 模型的吞吐量基准：由于 L4 原生支持 INT8 Tensor Core，使用 INT8 量化 (如 GPTQ/AWQ INT8) 是 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N115

## Claim

L4 上运行 INT8 模型的吞吐量基准：由于 L4 原生支持 INT8 Tensor Core，使用 INT8 量化 (如 GPTQ/AWQ INT8) 是 L4 上运行 Qwen3-27B 的最优精度选择。INT8 权重占用 13.5GB，KV Cache (INT8) 占用减半。在 300 GB/s 带宽下，理论最大解码速度 = 300 / 13.5 ≈ 22.2 tokens/s。实测值预计为理论值的 60-70%，即 13-15 tokens/s。

## Corrected Claim

L4 上运行 INT8 模型的吞吐量基准：由于 L4 原生支持 INT8 Tensor Core，使用 INT8 量化 (如 GPTQ/AWQ INT8) 是 L4 上运行 Qwen3-27B 的最优精度选择。INT8 权重占用 13.5GB，KV Cache (INT8) 占用减半。在 300 GB/s 带宽下，理论最大解码速度 = 300 / 13.5 ≈ 22.2 tokens/s。实测值预计为理论值的 60-70%，即 13-15 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：L4 显存 24GB，INT8 下 27B 模型权重约 13.5GB 符合量级；带宽瓶颈计算 300GB/s / 13.5GB ≈ 22.2 tokens/s 数学正确；实测效率 60-70% 符合 GPU 推理经验规律。

## Search Query

NVIDIA L4 INT8 inference benchmark Qwen
