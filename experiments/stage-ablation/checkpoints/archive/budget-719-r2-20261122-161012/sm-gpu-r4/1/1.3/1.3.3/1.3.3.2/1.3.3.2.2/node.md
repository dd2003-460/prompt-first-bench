# N376: RTX 4090 在 Torrent 机箱双卡安装场景下的热降频触发阈值温度设定为 83°C（NVIDIA 默认安全上限），若第二张卡因风量减少导致稳态温度超过

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N157, N158, N159

## Claim

RTX 4090 在 Torrent 机箱双卡安装场景下的热降频触发阈值温度设定为 83°C（NVIDIA 默认安全上限），若第二张卡因风量减少导致稳态温度超过 83°C，则必须启动 P-state 降频，此时实际算力输出下降约 10-15%。

## Corrected Claim

RTX 4090 在 Torrent 机箱双卡安装场景下，若因风量不足导致稳态温度超过 NVIDIA 默认热保护阈值（通常为 83°C 左右），将触发 P-state 降频，导致实际算力输出显著下降（具体幅度取决于散热条件，通常估计在 10-20% 区间）。

## Evidence

[质询]将NVIDIA通用的83°C热保护阈值直接等同于特定机箱（Torrent）双卡场景下的实际降频触发点，且断言算力下降幅度精确为10-15%，缺乏该特定硬件组合的实测数据支持，属于过度具体的经验性推断。 | 先验知识/题面给定，逻辑校验通过：83°C是RTX 40系列常见的热保护阈值，高温导致降频符合物理规律，但具体机箱下的稳态温度和算力损失比例属于经验事实，无来源支持具体数值。

## Search Query

RTX 4090 thermal throttling threshold 83C performance drop percentage
