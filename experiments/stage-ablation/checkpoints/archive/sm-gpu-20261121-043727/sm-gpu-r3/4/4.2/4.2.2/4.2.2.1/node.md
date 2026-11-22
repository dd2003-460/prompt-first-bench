# N173: 代表性工作点 2 (低带宽消费卡)：RTX 4090 (BF16)。Weight_Size=54GB (无法装入 24GB 显存，需 Offload 或量化，此

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

代表性工作点 2 (低带宽消费卡)：RTX 4090 (BF16)。Weight_Size=54GB (无法装入 24GB 显存，需 Offload 或量化，此处假设理想状态或对比 INT4 情况)。若使用 INT4 (Weight=14GB, BW=1.0TB/s)，T_decode ≈ 14e9 / 1.0e12 ≈ 14.0 ms/token。若强行 BF16 Offload，PCIe 瓶颈导致 T_decode > 100ms，不可行。此对比显示量化对消费卡 Decode 速度是生死线

## Corrected Claim

代表性工作点 2 (低带宽消费卡)：RTX 4090 (BF16)。Weight_Size=54GB (无法装入 24GB 显存，需 Offload 或量化，此处假设理想状态或对比 INT4 情况)。若使用 INT4 (Weight=14GB, BW=1.0TB/s)，T_decode ≈ 14e9 / 1.0e12 ≈ 14.0 ms/token。若强行 BF16 Offload，PCIe 瓶颈导致 T_decode > 100ms，不可行。此对比显示量化对消费卡 Decode 速度是生死线

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存24GB，BF16下54GB权重确实无法装入；INT4下14GB权重在1.0TB/s带宽下理论延迟约14ms，符合算术推导；PCIe带宽远低于显存带宽，Offload BF16导致延迟激增符合物理直觉。
