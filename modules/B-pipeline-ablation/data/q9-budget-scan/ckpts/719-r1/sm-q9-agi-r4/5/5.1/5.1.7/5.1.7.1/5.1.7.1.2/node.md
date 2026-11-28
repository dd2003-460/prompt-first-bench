# N679: T_model_load (27B weights from RAM/SSD to 4x V100) 的带宽限制分析：27B 模型 NVFP4 权重大小约 13

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N246

## Claim

T_model_load (27B weights from RAM/SSD to 4x V100) 的带宽限制分析：27B 模型 NVFP4 权重大小约 13.5GB，从 SSD 读取至内存需 13.5GB/500MB/s ≈ 27s，再从内存分发至 4 张 GPU 需 13.5GB/(4×16GB/s) ≈ 0.21s，总加载时间 ≈ 27.2s，符合 <30s 约束

## Corrected Claim

T_model_load (27B weights from RAM/SSD to 4x V100) 的带宽限制分析：27B 模型 NVFP4 权重大小约 13.5GB，从 SSD 读取至内存需 13.5GB/500MB/s ≈ 27s，再从内存分发至 4 张 GPU 需 13.5GB/(4×16GB/s) ≈ 0.21s，总加载时间 ≈ 27.2s，符合 <30s 约束

## Evidence

[质询]NVFP4 精度下 27B 参数量对应 13.5GB 存储大小是否符合常规量化比例（通常 FP4 约为 FP16 的 1/4，27B*2bytes=54GB, 54/4=13.5GB，计算正确）；PCIe 带宽假设 16GB/s 是否合理（V100 为 PCIe 3.0 x16，理论带宽约 12.8GB/s，实际有效带宽略低，16GB/s 可能略微乐观但属于同一数量级，不影响主要瓶颈 SSD 读取时间的结论） | 先验知识/题面给定，逻辑校验通过：27B 参数在 NVFP4 (4-bit) 下体积约为 13.5GB (27e9 * 0.5 bytes)，SSD 读取 13.5GB @ 500MB/s 耗时 27s，GPU 传输耗时可忽略，总时间约 27.2s < 30s，逻辑自洽且数值量级合理。
