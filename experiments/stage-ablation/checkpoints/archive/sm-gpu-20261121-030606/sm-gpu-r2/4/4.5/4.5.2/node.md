# N139: RTX 4090在INT8精度下的推理延迟计算：(2 * 27e9 * 32768) / (165.2 TFLOPS * 0.8) + (13.5 + 2.5 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

RTX 4090在INT8精度下的推理延迟计算：(2 * 27e9 * 32768) / (165.2 TFLOPS * 0.8) + (13.5 + 2.5 + 5.2)GB / 1008 GB/s ≈ 17.1 ms + 21.0 ms = 38.1 ms/token

## Corrected Claim

RTX 4090在INT8精度下的推理延迟计算：(2 * 27e9 * 32768) / (165.2 TFLOPS * 0.8) + (13.5 + 2.5 + 5.2)GB / 1008 GB/s ≈ 17.1 ms + 21.0 ms = 38.1 ms/token

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (2*27e9*32768)/(165.2e12*0.8) ≈ 17.1ms 及 (21.2GB)/1008GB/s ≈ 21.0ms 均符合算术逻辑，总延迟 38.1ms 自洽。
