# N211: CPU 推理 Decode 阶段受限于内存带宽，理论上限公式为 Throughput_decode = Memory_Bandwidth / (KV_Cache

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

CPU 推理 Decode 阶段受限于内存带宽，理论上限公式为 Throughput_decode = Memory_Bandwidth / (KV_Cache_Per_Token + Weights_Size_Per_Layer_Access)，其中 Weights_Size_Per_Layer_Access 取决于是否启用层卸载或全量加载，若全量加载则分母接近总权重大小 13.5 GB

## Corrected Claim

CPU 推理 Decode 阶段受限于内存带宽，理论上限公式为 Throughput_decode = Memory_Bandwidth / (KV_Cache_Per_Token + Weights_Size_Per_Layer_Access)，其中 Weights_Size_Per_Layer_Access 取决于是否启用层卸载或全量加载，若全量加载则分母接近总权重大小 13.5 GB

## Evidence

先验知识/题面给定，逻辑校验通过：CPU推理Decode阶段确实受内存带宽限制，吞吐量公式符合Roofline模型基本逻辑，13.5GB权重大小与常见中等规模LLM（如7B-13B量化后）量级相符。
