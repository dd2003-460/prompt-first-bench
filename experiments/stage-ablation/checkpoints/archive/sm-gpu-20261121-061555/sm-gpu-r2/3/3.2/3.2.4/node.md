# N82: W4A16 与 W4A8 的质量差异机制：W4A8 引入激活值量化误差，导致 PPL 损失通常比 W4A16 高 1-3 个百分点，但在支持 INT8 张量核心

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

W4A16 与 W4A8 的质量差异机制：W4A8 引入激活值量化误差，导致 PPL 损失通常比 W4A16 高 1-3 个百分点，但在支持 INT8 张量核心的 GPU 上吞吐量提升 1.5-2 倍 [待核验]

## Corrected Claim

W4A8 引入激活值量化误差，通常导致 PPL 损失高于 W4A16，但在支持 INT8 张量核心的 GPU 上可获得显著的吞吐量提升。

## Evidence

[质询]数值量级与具体倍数（PPL高1-3个百分点、吞吐量提升1.5-2倍）属于高度依赖具体模型架构、数据集及硬件实现的经验性数据，缺乏通用性，且‘通常’一词掩盖了巨大的方差风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该陈述包含具体经验数值，不适用第一性原理推导条款）

## Search Query

W4A8 vs W4A16 perplexity loss and throughput comparison
