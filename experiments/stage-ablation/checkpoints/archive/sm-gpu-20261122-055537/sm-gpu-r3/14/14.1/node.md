# N397: Verified 级别数据的误差量化标准：对于硬件参数（如显存带宽、功耗），误差 < 5% 定义为 Verified；对于模型性能指标（如吞吐量），需满足 3 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N125

## Claim

Verified 级别数据的误差量化标准：对于硬件参数（如显存带宽、功耗），误差 < 5% 定义为 Verified；对于模型性能指标（如吞吐量），需满足 3 次独立运行标准差 < 5% 且与官方白皮书/顶会论文（如 NVIDIA GTC Keynote, SOSP/OSDI 论文）数据偏差 < 5%。

## Corrected Claim

Verified 级别数据的误差量化标准：对于硬件参数（如显存带宽、功耗），误差 < 5% 定义为 Verified；对于模型性能指标（如吞吐量），需满足 3 次独立运行标准差 < 5% 且与官方白皮书/顶会论文（如 NVIDIA GTC Keynote, SOSP/OSDI 论文）数据偏差 < 5%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVIDIA GPU specification accuracy standard benchmarking error margin
