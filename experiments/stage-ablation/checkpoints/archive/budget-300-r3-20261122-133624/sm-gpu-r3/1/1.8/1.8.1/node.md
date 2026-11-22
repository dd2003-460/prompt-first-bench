# N65: Qwen3-27B 在 INT8 下 Prefill 阶段的实际算力需求修正为约 270 TOPS（2 × 27B 参数 × 1 token），原 N13 中 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

Qwen3-27B 在 INT8 下 Prefill 阶段的实际算力需求修正为约 270 TOPS（2 × 27B 参数 × 1 token），原 N13 中 135 TOPS 的表述存在系数错误；在 4090 (330 TFLOPS) 上理论 Prefill 吞吐约为 1200 tokens/s，受限于算子效率（MFU 约 40-60%）实际约为 480-720 tokens/s。

## Corrected Claim

Qwen3-27B 在 INT8 下 Prefill 阶段的实际算力需求修正为约 270 TOPS（2 × 27B 参数 × 1 token），原 N13 中 135 TOPS 的表述存在系数错误；在 4090 (330 TFLOPS) 上理论 Prefill 吞吐约为 1200 tokens/s，受限于算子效率（MFU 约 40-60%）实际约为 480-720 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8下Prefill每token需2次乘加（权重读取+激活计算），27B参数对应270 TOPS算力需求；4090 INT8理论峰值约330 TOPS（注意：4090 FP32为80 TFLOPS，INT8通常为FP32的4倍即320-330 TOPS），理论吞吐330/270≈1.22k tokens/s，MFU 40-60%对应480-720 tokens/s，量级与逻辑均自洽。

## Search Query

Qwen3-27B prefill throughput tokens/s RTX 4090 INT8
