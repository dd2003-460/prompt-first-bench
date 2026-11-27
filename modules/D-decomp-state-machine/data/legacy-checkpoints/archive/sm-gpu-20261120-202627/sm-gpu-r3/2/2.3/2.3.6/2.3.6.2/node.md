# N234: KV Cache 量化误差累积的物理机制参数：需确定 NVFP4 下 KV Cache 的缩放因子（Scale Factor）更新频率及块大小（Block Si

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

KV Cache 量化误差累积的物理机制参数：需确定 NVFP4 下 KV Cache 的缩放因子（Scale Factor）更新频率及块大小（Block Size），计算单个 Token 的量化误差方差 σ² 随序列长度 L 的累积公式 σ²_total = L * σ²_single，以解释长文本误差放大效应

## Corrected Claim

KV Cache 量化误差累积的物理机制参数：需确定 NVFP4 下 KV Cache 的缩放因子（Scale Factor）更新频率及块大小（Block Size），计算单个 Token 的量化误差方差 σ² 随序列长度 L 的累积公式 σ²_total = L * σ²_single，以解释长文本误差放大效应

## Evidence

先验知识/题面给定，逻辑校验通过：独立同分布误差的方差随样本数线性累积符合统计学第一性原理，且NVFP4量化机制描述符合工程常识。
