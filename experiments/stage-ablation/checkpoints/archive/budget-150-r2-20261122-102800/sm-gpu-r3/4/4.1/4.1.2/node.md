# N98: RTX 4090 BF16 82.6 TFLOPS 为 Tensor Core 峰值，实际 LLM 推理中由于 Kernel 启动开销和内存等待，算力利用率通常

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

RTX 4090 BF16 82.6 TFLOPS 为 Tensor Core 峰值，实际 LLM 推理中由于 Kernel 启动开销和内存等待，算力利用率通常仅为 15-25%，即有效算力约 12-20 TFLOPS，此数值是评估高并发场景瓶颈的关键参数。

## Corrected Claim

RTX 4090 BF16 82.6 TFLOPS 为 Tensor Core 峰值，实际 LLM 推理中由于 Kernel 启动开销和内存等待，算力利用率通常仅为 15-25%，即有效算力约 12-20 TFLOPS，此数值是评估高并发场景瓶颈的关键参数。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于低并发/典型Decode阶段的利用率基准（15-25%），子节点2聚焦于高并发场景下的利用率变化趋势及显存限制（30-40%及Batch Size上限）。两者在场景（典型vs高并发）和结论（基础利用率vs优化后利用率/硬件瓶颈）上互补且不矛盾，共同覆盖了父节点中关于利用率范围、原因（Kernel开销）及高并发瓶颈评估的关键信息。）

## Search Query

RTX 4090 LLM inference compute utilization efficiency
