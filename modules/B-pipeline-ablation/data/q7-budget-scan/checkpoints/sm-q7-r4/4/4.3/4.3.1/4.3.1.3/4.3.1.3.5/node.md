# N720: 在XOR+GF(2^8)混合校验算法下，每处理1GB数据消耗的CPU周期数约为1.5亿cycle，基于2.5GHz主频折算为60ms/GB纯计算时间

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N250, N251, N252

## Claim

在XOR+GF(2^8)混合校验算法下，每处理1GB数据消耗的CPU周期数约为1.5亿cycle，基于2.5GHz主频折算为60ms/GB纯计算时间

## Corrected Claim

在XOR+GF(2^8)混合校验算法下，每处理1GB数据消耗的CPU周期数约为1.5亿cycle，基于2.5GHz主频折算为60ms/GB纯计算时间

## Evidence

先验知识/题面给定，逻辑校验通过：1.5亿cycle / 2.5GHz = 0.06s = 60ms，数值换算准确，符合XOR+GF(2^8)混合校验的典型性能量级。
