# N124: 在 2x RTX 4090 (TP=2) 配置下，PCIe x8 带宽限制导致的推理吞吐量下降百分比 (Latency Penalty %)，对比理想 NVLi

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N33, N34

## Claim

在 2x RTX 4090 (TP=2) 配置下，PCIe x8 带宽限制导致的推理吞吐量下降百分比 (Latency Penalty %)，对比理想 NVLink 或无限带宽场景的理论最大 TPS 损失。

## Corrected Claim

在 2x RTX 4090 (TP=2) 配置下，PCIe x8 带宽限制会导致推理吞吐量相比理想 NVLink 或无限带宽场景有所下降，具体下降百分比取决于模型架构、Batch Size 及推理框架优化程度，通常在小 Batch 或大模型通信密集场景下更为显著。

## Evidence

[质询]该陈述试图给出一个具体的百分比数值，但推理吞吐量受模型大小、Batch Size、序列长度及具体框架（如vLLM/TensorRT-LLM）影响极大，不存在通用的固定百分比；且参考来源仅包含硬件规格，完全未涉及多卡互联带宽对推理性能的具体量化影响数据。 | 经验事实，逻辑自洽但缺来源支持（来源[1][2][3]仅描述RTX 4090基础规格，未提供TP=2下的PCIe vs NVLink性能对比数据）

## Search Query

dual RTX 4090 tensor parallel PCIe x8 performance loss percentage LLM

## Retrieval Sources

- {'url': 'https://www.techpowerup.com/gpu-specs/geforce-rtx-4090.c3889&rut=f3fd62fb3a17cf66f8fcdb3e9d0ca3a0d0e7a0001f30460e655c83367db02ebf', 'type': 'ddg', 'title': 'NVIDIA GeForce RTX 4090 Specs | TechPowerUp GPU Database'}
- {'url': 'https://www.techpowerup.com/gpu-specs/geforce-rtx-4090-d.c4189&rut=014bf0166a36dbe867a89bd3221d7717fdfabbdd37f28b7f42b2284ce5518784', 'type': 'ddg', 'title': 'NVIDIA GeForce RTX 4090 D Specs - TechPowerUp'}
- {'url': 'https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/&rut=11b98d320cf47aeec871ad2386a40c482a734496251579a2cb18bf590062dee9', 'type': 'ddg', 'title': 'GeForce RTX 4090 Graphics Cards for Gaming | NVIDIA'}
