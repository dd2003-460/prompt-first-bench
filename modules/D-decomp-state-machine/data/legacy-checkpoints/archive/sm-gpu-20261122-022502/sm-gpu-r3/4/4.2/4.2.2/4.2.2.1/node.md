# N194: CPU功耗具体值：Intel i9-14900K在LLM推理负载下平均功耗约120W（PBO开启），AMD Ryzen 9 7950X约110W，需根据具体CP

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N63

## Claim

CPU功耗具体值：Intel i9-14900K在LLM推理负载下平均功耗约120W（PBO开启），AMD Ryzen 9 7950X约110W，需根据具体CPU型号和PBO设置确定，功耗差异影响总系统功耗±10W

## Corrected Claim

Intel i9-14900K和AMD Ryzen 9 7950X在LLM推理负载下平均功耗通常在100W-150W区间（取决于PBO设置和具体负载特征），需根据具体CPU型号和PBO设置确定，功耗差异影响总系统功耗约±10-20W

## Evidence

[质询]具体数值（120W/110W）属于经验事实，且LLM推理负载下CPU功耗受线程数、频率、内存带宽瓶颈影响极大，不同基准测试数据差异显著，缺乏统一标准值，具体数值可能因测试环境不同而偏差较大。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

i9-14900K Ryzen 7950X power consumption LLM inference workload measured watts
