# N727: 实验设计的随机化偏差控制：100 组实验中，研究方向（物理/生物/CS）的分布不均可能导致协方差干扰；需按研究方向分层抽样，确保每类方向至少 30 组样本，以消

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N266

## Claim

实验设计的随机化偏差控制：100 组实验中，研究方向（物理/生物/CS）的分布不均可能导致协方差干扰；需按研究方向分层抽样，确保每类方向至少 30 组样本，以消除领域特异性对 P_success 的系统性偏移，量化分层前后的标准差变化

## Corrected Claim

实验设计的随机化偏差控制：100 组实验中，研究方向（物理/生物/CS）的分布不均可能导致协方差干扰；需按研究方向分层抽样，确保每类方向至少 30 组样本，以消除领域特异性对 P_success 的系统性偏移，量化分层前后的标准差变化

## Evidence

先验知识/题面给定，逻辑校验通过：分层抽样是控制已知混杂变量（如研究方向）的标准统计方法，能减少组间方差并消除系统性偏差，符合统计学基本原理。

## Search Query

stratified sampling experimental design LLM evaluation bias control
