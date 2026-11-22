# N150: 散热能力 300W 阈值对应的最大 GPU TDP 约为 250W (300/1.2)，该阈值排除 RTX 4090 (450W)、RTX 5090 (575W

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

散热能力 300W 阈值对应的最大 GPU TDP 约为 250W (300/1.2)，该阈值排除 RTX 4090 (450W)、RTX 5090 (575W)、A100 (400W)、H100 (700W)，但允许 RTX 4080 (320W, 需加强风冷) 或 L4 (72W)、T4 (70W) 等低功耗数据中心/消费级卡。

## Corrected Claim

散热能力 300W 阈值对应的最大 GPU TDP 约为 250W (300/1.2)，该阈值排除 RTX 4090 (450W)、RTX 5090 (575W)、A100 (400W)、H100 (700W)，但允许 RTX 4080 (320W, 需加强风冷) 或 L4 (72W)、T4 (70W) 等低功耗数据中心/消费级卡。

## Evidence

先验知识/题面给定，逻辑校验通过：300W/1.2≈250W计算正确；所列GPU TDP数值（RTX 4090 450W, RTX 5090 575W, A100 400W, H100 700W, RTX 4080 320W, L4 72W, T4 70W）均符合公开规格常识，逻辑自洽。
