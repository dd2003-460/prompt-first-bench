# N322: 带宽受限推理的算术强度 (Arithmetic Intensity) 计算：对于 Batch Size=1 的 Decode 阶段，每生成 1 个 Token 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

带宽受限推理的算术强度 (Arithmetic Intensity) 计算：对于 Batch Size=1 的 Decode 阶段，每生成 1 个 Token 需读取的权重字节数 ≈ 27GB (INT8) + 1.93GB (KV Cache) ≈ 28.93GB；计算量 ≈ 2 * 27B FLOPs (INT8) = 54 GFLOPs；算术强度 ≈ 54/28.93 ≈ 1.86 FLOPs/Byte，远低于 GPU 的 Roofline 拐点 (通常 > 100 FLOPs/Byte)，证明 Decode 阶段严格受限于内存带宽。

## Corrected Claim

带宽受限推理的算术强度 (Arithmetic Intensity) 计算：对于 Batch Size=1 的 Decode 阶段，每生成 1 个 Token 需读取的权重字节数 ≈ 27GB (INT8) + 1.93GB (KV Cache) ≈ 28.93GB；计算量 ≈ 2 * 27B FLOPs (INT8) = 54 GFLOPs；算术强度 ≈ 54/28.93 ≈ 1.86 FLOPs/Byte，远低于 GPU 的 Roofline 拐点 (通常 > 100 FLOPs/Byte)，证明 Decode 阶段严格受限于内存带宽。

## Evidence

先验知识/题面给定，逻辑校验通过：算术强度计算逻辑自洽（54 GFLOPs / 28.93 GB ≈ 1.86 FLOPs/Byte），且符合大模型Decode阶段内存带宽受限的普遍工程共识。
