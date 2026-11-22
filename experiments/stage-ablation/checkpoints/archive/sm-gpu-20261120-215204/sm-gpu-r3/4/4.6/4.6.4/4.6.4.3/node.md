# N321: 基于 N110 的 1.77 TFLOPs 计算量和 N136 的实测 MFU 中值 50% (有效算力 156 TFLOPS)，A100 80GB 在 BF1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N113

## Claim

基于 N110 的 1.77 TFLOPs 计算量和 N136 的实测 MFU 中值 50% (有效算力 156 TFLOPS)，A100 80GB 在 BF16 下处理 32K 序列的纯计算耗时约为 11.3 ms (1.77e12 / 156e12)，需加上 HBM 读取权重的内存延迟 (54GB / 2039 GB/s ≈ 26.5 ms)，总 TTFT 下限约为 37.8 ms。

## Corrected Claim

基于 N110 的 1.77 TFLOPs 计算量和 N136 的实测 MFU 中值 50% (有效算力 156 TFLOPS)，A100 80GB 在 BF16 下处理 32K 序列的纯计算耗时约为 11.3 ms (1.77e12 / 156e12)，需加上 HBM 读取权重的内存延迟 (54GB / 2039 GB/s ≈ 26.5 ms)，总 TTFT 下限约为 37.8 ms。

## Evidence

先验知识/题面给定，逻辑校验通过：计算耗时 1.77e12/156e12 ≈ 11.35ms，内存耗时 54e9/2039e9 ≈ 26.48ms，总和 ≈ 37.83ms，数值量级与算术逻辑自洽。
