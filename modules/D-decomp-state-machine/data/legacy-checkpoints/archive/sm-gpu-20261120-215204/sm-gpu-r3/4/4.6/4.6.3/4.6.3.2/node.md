# N317: 工作点 B (批量预填充 Prefill 阶段)：RTX 4090 在 BF16 精度下，32K 序列 Prefill 受计算限制，理论峰值 82.6 TFLO

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N112

## Claim

工作点 B (批量预填充 Prefill 阶段)：RTX 4090 在 BF16 精度下，32K 序列 Prefill 受计算限制，理论峰值 82.6 TFLOPS，实际 MFU 40% 时有效算力 33 TFLOPS，耗时 1.77 TFLOPs / 33 TFLOPS ≈ 54ms，与单 Token 生成速度 (Tokens/s) 无直接线性关系

## Corrected Claim

工作点 B (批量预填充 Prefill 阶段)：RTX 4090 在 BF16 精度下，32K 序列 Prefill 受计算限制，理论峰值 82.6 TFLOPS，实际 MFU 40% 时有效算力 33 TFLOPS，耗时 1.77 TFLOPs / 33 TFLOPS ≈ 54ms，与单 Token 生成速度 (Tokens/s) 无直接线性关系

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 BF16 峰值算力约 82.6 TFLOPS 符合硬件规格，Prefill 阶段计算密集且与 Decode 阶段（内存带宽受限）机制不同，耗时计算逻辑自洽。
