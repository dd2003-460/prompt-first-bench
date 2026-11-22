# N740: GPU 计算时间基准：RTX 4090 在 BF16 下理论算力为 330 TFLOPS，实际矩阵乘法效率约 60-70%，即 ~200-230 TFLOPS。

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N228

## Claim

GPU 计算时间基准：RTX 4090 在 BF16 下理论算力为 330 TFLOPS，实际矩阵乘法效率约 60-70%，即 ~200-230 TFLOPS。Qwen3-27B 单 token 推理 FLOPs 约为 $2 \times 27 \times 10^9 \approx 54 \text{ GFLOPs}$，单卡计算延迟约为 $54 \text{ GFLOPs} / 200 \text{ TFLOPS} \approx 270 \mu s$。通信延迟 17 μs 仅占计算时间的 ~6%，证明通信非瓶颈。

## Corrected Claim

GPU 计算时间基准：RTX 4090 在 BF16 下理论算力为 330 TFLOPS，实际矩阵乘法效率约 60-70%，即 ~200-230 TFLOPS。Qwen3-27B 单 token 推理 FLOPs 约为 $2 \times 27 \times 10^9 \approx 54 \text{ GFLOPs}$，单卡计算延迟约为 $54 \text{ GFLOPs} / 200 \text{ TFLOPS} \approx 270 \mu s$。通信延迟 17 μs 仅占计算时间的 ~6%，证明通信非瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 BF16 理论算力约 330 TFLOPS 符合硬件规格常识，27B 模型单 token 推理 FLOPs 估算（2*参数量）及延迟计算逻辑自洽，通信占比推导合理。
