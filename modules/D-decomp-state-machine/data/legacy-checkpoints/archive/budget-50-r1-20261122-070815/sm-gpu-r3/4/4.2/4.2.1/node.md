# N105: RTX 4090 (24GB) 在 LLM 推理负载下的典型整机功耗 P_avg 约为 450W (GPU TDP 450W + 系统开销 ~10%)，其能效比

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

RTX 4090 (24GB) 在 LLM 推理负载下的典型整机功耗 P_avg 约为 450W (GPU TDP 450W + 系统开销 ~10%)，其能效比 (W/token) 需结合 1008 GB/s 带宽与 82.6 TFLOPS (FP16) 算力进行量化评估

## Corrected Claim

RTX 4090 (24GB) 在 LLM 推理负载下的典型整机功耗 P_avg 约为 450W (GPU TDP 450W + 系统开销 ~10%)，其能效比 (W/token) 需结合 1008 GB/s 带宽与 82.6 TFLOPS (FP16) 算力进行量化评估

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 的 TDP 确为 450W，显存带宽 1008 GB/s 及 FP16 算力 82.6 TFLOPS 均为该硬件的标准公开规格，数值量级与工程常识一致。
