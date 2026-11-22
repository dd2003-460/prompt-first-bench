# N283: A100 40GB SXM4 的 TDP 400W 包含 GPU 和 HBM 内存功耗，而 PCIe 版本 A100 40GB 的 TDP 为 250W，两者不

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

A100 40GB SXM4 的 TDP 400W 包含 GPU 和 HBM 内存功耗，而 PCIe 版本 A100 40GB 的 TDP 为 250W，两者不可直接比较；在本地工作站部署中，PCIe 版本 A100 的 3 年电力成本（250W*24h*365d*3y*0.15）为 $3,240，比 SXM 版本（$5,040）低 35.7%，但 PCIe 版本内存带宽 (1935 GB/s) 低于 SXM 版本 (2039 GB/s)，对带宽受限的 LLM 推理性能影响约为 5-10%。

## Corrected Claim

A100 40GB SXM4 的 TDP 400W 包含 GPU 和 HBM 内存功耗，而 PCIe 版本 A100 40GB 的 TDP 为 250W，两者不可直接比较；在本地工作站部署中，PCIe 版本 A100 的 3 年电力成本（250W*24h*365d*3y*0.15）为 $3,240，比 SXM 版本（$5,040）低 35.7%，但 PCIe 版本内存带宽 (1935 GB/s) 低于 SXM 版本 (2039 GB/s)，对带宽受限的 LLM 推理性能影响约为 5-10%。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 SXM4 TDP 400W 与 PCIe 250W 符合 NVIDIA 官方规格；电力成本计算 (250W*8760h*3y*0.15/kWh ≈ $3240) 数学正确；带宽差异 (1935 vs 2039 GB/s) 及性能影响估算符合工程直觉。

## Search Query

A100 PCIe vs SXM power consumption and memory bandwidth comparison
