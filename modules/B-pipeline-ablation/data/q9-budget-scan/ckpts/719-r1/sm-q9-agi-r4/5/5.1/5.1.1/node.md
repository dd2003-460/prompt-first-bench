# N66: 工作点A（纯本地）在满负载（4x V100-SXM2-16GB 持续满载）下的实际功率消耗为 250W，而非之前估算的 1000W（单卡TDP 250W，四卡满

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19, N20, N21

## Claim

工作点A（纯本地）在满负载（4x V100-SXM2-16GB 持续满载）下的实际功率消耗为 250W，而非之前估算的 1000W（单卡TDP 250W，四卡满载理论上限1000W，但受限于27B NVFP4推理负载特性及vLLM调度，实际稳态功耗约为单卡峰值的100%即每卡250W，总计1000W为保守上限，此处修正为实测均值约600W-800W区间，取中值700W计算成本更准确）

## Corrected Claim

工作点A（纯本地）在满负载（4x V100-SXM2-16GB 持续满载）下的实际功率消耗需重新测量确认，原陈述中250W、700W、1000W等数值相互矛盾，无法作为可靠事实节点。

## Evidence

[质询]陈述内部存在严重的逻辑矛盾和数值不一致：开头声称实际功率为250W，结尾却修正为700W；同时声称'实际稳态功耗约为单卡峰值的100%'（即每卡250W，总计1000W），却又说'总计1000W为保守上限，此处修正为...700W'，前后数据完全冲突，无法确定最终结论。 | 陈述内部数值自相矛盾（250W vs 700W vs 1000W），且无外部来源支持，逻辑校验失败。

## Search Query

Tesla V100 SXM2 power consumption under inference load vLLM 27B model
