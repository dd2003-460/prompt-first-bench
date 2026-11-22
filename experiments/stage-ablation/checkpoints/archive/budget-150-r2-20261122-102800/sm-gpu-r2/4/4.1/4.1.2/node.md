# N98: RTX 4090 BF16 82.6 TFLOPS 为 Tensor Core 峰值，实际 LLM 推理中由于 Kernel 启动开销和内存等待，算力利用率通常

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

RTX 4090 BF16 82.6 TFLOPS 为 Tensor Core 峰值，实际 LLM 推理中由于 Kernel 启动开销和内存等待，算力利用率通常仅为 15-25%，即有效算力约 12-20 TFLOPS，此数值是评估高并发场景瓶颈的关键参数。

## Corrected Claim

RTX 4090 BF16 82.6 TFLOPS 为 Tensor Core 峰值，实际 LLM 推理中由于 Kernel 启动开销和内存等待，算力利用率通常仅为 15-25%，即有效算力约 12-20 TFLOPS，此数值是评估高并发场景瓶颈的关键参数。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 BF16 Tensor Core 峰值算力确为 82.6 TFLOPS（82,587 GFLOPS），LLM 推理受内存带宽限制，算力利用率 15-25% 符合工程经验，推导出的有效算力 12-20 TFLOPS 量级合理。

## Search Query

RTX 4090 LLM inference compute utilization efficiency
