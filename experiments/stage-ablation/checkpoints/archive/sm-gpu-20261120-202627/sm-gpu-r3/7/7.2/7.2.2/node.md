# N414: AMD MI300X 的显存带宽优势量化：MI300X 带宽 (5300 GB/s) 是 RTX 4090 (1008 GB/s) 的 5.25 倍，是 A10

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N133

## Claim

AMD MI300X 的显存带宽优势量化：MI300X 带宽 (5300 GB/s) 是 RTX 4090 (1008 GB/s) 的 5.25 倍，是 A100 (2039 GB/s) 的 2.6 倍。若软件栈优化到位，其理论解码延迟可低至 ~1.6ms/token，显著优于现有 NVIDIA 主流数据中心卡，需评估其软件成熟度对实际吞吐量的折损。

## Corrected Claim

AMD MI300X 的显存带宽优势量化：MI300X 带宽 (5300 GB/s) 是 RTX 4090 (1008 GB/s) 的 5.25 倍，是 A100 (2039 GB/s) 的 2.6 倍。若软件栈优化到位，其理论解码延迟可低至 ~1.6ms/token，显著优于现有 NVIDIA 主流数据中心卡，需评估其软件成熟度对实际吞吐量的折损。

## Evidence

先验知识/题面给定，逻辑校验通过：MI300X (5.3TB/s) 与 RTX 4090 (1.0TB/s) 及 A100 (2.0TB/s) 的带宽比值计算正确，且符合硬件规格常识。
