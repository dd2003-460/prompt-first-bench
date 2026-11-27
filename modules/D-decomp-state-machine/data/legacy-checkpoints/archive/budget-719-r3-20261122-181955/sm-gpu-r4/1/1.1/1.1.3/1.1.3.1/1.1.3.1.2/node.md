# N415: RTX 3090 理论 Decode 吞吐量上限计算：显存带宽 936 GB/s 除以总内存读取量（INT4 权重 13.5GB + 32K KV Cache 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N137, N138, N139

## Claim

RTX 3090 理论 Decode 吞吐量上限计算：显存带宽 936 GB/s 除以总内存读取量（INT4 权重 13.5GB + 32K KV Cache 8GB + 激活值/框架开销 0.5GB ≈ 22GB），理论峰值 ≈ 42.5 tokens/s；乘以 0.6-0.8 硬件效率系数后，实际预估吞吐为 25.5-34 tokens/s。

## Corrected Claim

RTX 3090 理论 Decode 吞吐量上限计算：显存带宽 936 GB/s 除以总内存读取量（INT4 权重 13.5GB + 32K KV Cache 8GB + 激活值/框架开销 0.5GB ≈ 22GB），理论峰值 ≈ 42.5 tokens/s；乘以 0.6-0.8 硬件效率系数后，实际预估吞吐为 25.5-34 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 显存带宽 936 GB/s 为准确规格；22GB 总读取量下 936/22 ≈ 42.5 tokens/s 计算正确；乘以 0.6-0.8 效率系数得到 25.5-34 tokens/s 区间符合大模型推理中显存带宽受限（memory-bound）场景的工程经验估算逻辑。
