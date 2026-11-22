# N363: N130 1xA100 (FP8) 实际吞吐量的带宽瓶颈验证：理论峰值 = 2039 GB/s / 27 GB = 75.5 Tokens/s；考虑 FP8 解

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130

## Claim

N130 1xA100 (FP8) 实际吞吐量的带宽瓶颈验证：理论峰值 = 2039 GB/s / 27 GB = 75.5 Tokens/s；考虑 FP8 解码效率 (~85% 带宽利用率) 和 HBM 访问延迟，实际稳定吞吐 ~60-70 Tokens/s；需确认是否为单并发 (Batch=1) 场景。

## Corrected Claim

N130 1xA100 (FP8) 实际吞吐量的带宽瓶颈验证：理论峰值 = 2039 GB/s / 27 GB = 75.5 Tokens/s；考虑 FP8 解码效率 (~85% 带宽利用率) 和 HBM 访问延迟，实际稳定吞吐 ~60-70 Tokens/s；需确认是否为单并发 (Batch=1) 场景。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 HBM2e带宽2039GB/s与27GB显存参数符合硬件规格，75.5 Tokens/s的理论峰值计算（2039/27）数学正确，考虑85%带宽利用率及延迟后的60-70 Tokens/s实际吞吐量估算符合工程直觉。
