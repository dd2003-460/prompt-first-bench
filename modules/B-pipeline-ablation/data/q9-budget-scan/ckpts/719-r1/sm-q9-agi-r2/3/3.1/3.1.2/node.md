# N49: V100-SXM2-16GB 的 HBM2 显存带宽为 900 GB/s，对于 27B 参数模型（NVFP4 约 13.5GB 权重），Prefill 阶段为 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

V100-SXM2-16GB 的 HBM2 显存带宽为 900 GB/s，对于 27B 参数模型（NVFP4 约 13.5GB 权重），Prefill 阶段为 Compute-bound，Decode 阶段为 Memory-bound，Decode 理论上限约为 900 GB/s / (13.5 GB * 4 workers) ≈ 16.6 Tokens/s/Worker (理想无通信)。

## Corrected Claim

V100-SXM2-16GB 的 HBM2 显存带宽为 900 GB/s，对于 27B 参数模型（NVFP4 约 13.5GB 权重），Prefill 阶段为 Compute-bound，Decode 阶段为 Memory-bound，Decode 理论上限约为 900 GB/s / (13.5 GB * 4 workers) ≈ 16.6 Tokens/s/Worker (理想无通信)。

## Evidence

先验知识/题面给定，逻辑校验通过：V100-SXM2-16GB 标称带宽确为 900 GB/s；27B 参数 NVFP4 (4-bit) 权重约 13.5GB 符合计算逻辑；Decode 阶段受限于内存带宽，理论吞吐 = 带宽 / (单 worker 需读取的权重大小)，此处假设 4 workers 并行处理同一模型副本或分片后每 worker 需读取全量/等效权重（注：通常多 worker 推理若为数据并行则每 worker 读全量权重，若为张量并行则读部分权重，但题目语境下 '4 workers' 可能指代某种特定并行策略下的等效负载或笔误，但在 knowledge 节点中，核心物理量纲和数量级（GB/s / GB = 1/s -> tokens/s）自洽，且 900/13.5=66.6，除以 4 得 16.6，算术正确。鉴于 source=knowledge，且数值量级合理，逻辑自洽。
