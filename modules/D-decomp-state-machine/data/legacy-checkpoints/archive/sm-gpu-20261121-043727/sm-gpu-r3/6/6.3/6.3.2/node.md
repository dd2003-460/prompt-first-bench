# N236: Intel Max 1550 在 INT8 精度下运行 Qwen3-27B 的 T_decode 理论下限：基于内存带宽瓶颈公式 T_decode ≈ Weig

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88

## Claim

Intel Max 1550 在 INT8 精度下运行 Qwen3-27B 的 T_decode 理论下限：基于内存带宽瓶颈公式 T_decode ≈ Weight_Size / Memory_Bandwidth，代入 Weight_Size = 27.2 GB (INT8) 和 Bandwidth = 921.6 GB/s，计算得 T_decode ≈ 29.5 ms/token (即 ~34 tokens/s)，需对比同价位 NVIDIA 卡（如 L40S 或 4090）的实测吞吐以验证 20-40% 性能差距的说法

## Corrected Claim

Intel Max 1550 在 INT8 精度下运行 Qwen3-27B 的 T_decode 理论下限：基于内存带宽瓶颈公式 T_decode ≈ Weight_Size / Memory_Bandwidth，代入 Weight_Size = 27.2 GB (INT8) 和 Bandwidth = 921.6 GB/s，计算得 T_decode ≈ 29.5 ms/token (即 ~34 tokens/s)，需对比同价位 NVIDIA 卡（如 L40S 或 4090）的实测吞吐以验证 20-40% 性能差距的说法

## Evidence

先验知识/题面给定，逻辑校验通过：27.2 GB / 921.6 GB/s ≈ 0.0295 s = 29.5 ms，计算无误，符合内存带宽瓶颈理论模型。
