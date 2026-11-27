# N296: Mac Studio 方案中，由于内存容量大（192GB）且无需高功耗离散 GPU，其待机/空闲功耗 P_idle 约为 15W-20W，在计算年均电力成本时需

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N91

## Claim

Mac Studio 方案中，由于内存容量大（192GB）且无需高功耗离散 GPU，其待机/空闲功耗 P_idle 约为 15W-20W，在计算年均电力成本时需引入负载因子 f_load（例如 50% 时间推理，50% 时间空闲），修正后的平均功耗 P_avg = f_load * P_infer + (1-f_load) * P_idle，若 f_load=0.5，则 P_avg 约为 100W-135W，导致年电费降至 $150-$200

## Corrected Claim

Mac Studio 方案中，由于内存容量大（192GB）且无需高功耗离散 GPU，其待机/空闲功耗 P_idle 约为 15W-20W，在计算年均电力成本时需引入负载因子 f_load（例如 50% 时间推理，50% 时间空闲），修正后的平均功耗 P_avg = f_load * P_infer + (1-f_load) * P_idle，若 f_load=0.5，则 P_avg 约为 100W-135W，导致年电费降至 $150-$200

## Evidence

先验知识/题面给定，逻辑校验通过：Mac Studio (M2 Ultra/M3 Ultra) 空闲功耗确实在 15-20W 量级，推理功耗 180-250W 量级，按 50% 负载因子加权平均后 100-135W 符合物理直觉与工程常识，年电费估算基于标准电价逻辑自洽。
