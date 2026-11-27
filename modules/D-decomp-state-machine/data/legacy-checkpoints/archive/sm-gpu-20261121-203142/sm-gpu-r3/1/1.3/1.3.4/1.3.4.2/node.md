# N154: W4 量化推理中 CPU-GPU 数据搬运开销：若反量化在 CPU 进行，PCIe 4.0 带宽瓶颈导致每层权重反量化传输时间 ≈ (Weight_Size /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

W4 量化推理中 CPU-GPU 数据搬运开销：若反量化在 CPU 进行，PCIe 4.0 带宽瓶颈导致每层权重反量化传输时间 ≈ (Weight_Size / PCIe_BW)；对于 27B 模型 W4 权重 (约 6.75 GB)，全量传输一次需 6.75 GB / 32 GB/s ≈ 210 ms，若每 Token 需重新反量化则不可行，必须依赖 GPU 侧缓存或预反量化

## Corrected Claim

W4 量化推理中 CPU-GPU 数据搬运开销：若反量化在 CPU 进行，PCIe 4.0 带宽瓶颈导致每层权重反量化传输时间 ≈ (Weight_Size / PCIe_BW)；对于 27B 模型 W4 权重 (约 6.75 GB)，全量传输一次需 6.75 GB / 32 GB/s ≈ 210 ms，若每 Token 需重新反量化则不可行，必须依赖 GPU 侧缓存或预反量化

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型W4量化权重约6.75GB，PCIe 4.0 x16理论带宽32GB/s，计算6.75/32≈0.21s即210ms，量级与逻辑自洽。
