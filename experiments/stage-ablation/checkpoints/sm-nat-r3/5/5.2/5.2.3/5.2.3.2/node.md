# N225: 在 LRU 命中率接近 100% 的基准下，LFU 的命中率 H_LFU 受频率统计滞后影响，其滞后导致的命中率损失 ΔH_lag 可量化为：ΔH_lag ≈ 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

在 LRU 命中率接近 100% 的基准下，LFU 的命中率 H_LFU 受频率统计滞后影响，其滞后导致的命中率损失 ΔH_lag 可量化为：ΔH_lag ≈ - (1 / (1 + f_avg * T_window)) * (1 - H_LRU)，其中 f_avg 为平均请求频率，T_window 为 LFU 的频率统计窗口。

## Corrected Claim

在特定假设下，LFU 的命中率损失 ΔH_lag 可近似量化为与频率统计窗口及平均请求频率相关的函数，具体形式依赖于系统模型假设。

## Evidence

[质询]该公式缺乏公认的学术或工程标准支持，属于特定模型下的经验拟合或假设性推导，而非通用物理/数学定律；且量纲上 f_avg * T_window 需为无量纲数（即 f_avg 需定义为频率而非速率，或 T_window 需归一化），若 f_avg 为 Hz 则量纲不匹配。 | 先验知识/题面给定，逻辑校验通过（量纲在特定定义下自洽，但公式本身非普适真理，属经验性量化模型）

## Search Query

LFU frequency counting lag cache hit rate loss formula
