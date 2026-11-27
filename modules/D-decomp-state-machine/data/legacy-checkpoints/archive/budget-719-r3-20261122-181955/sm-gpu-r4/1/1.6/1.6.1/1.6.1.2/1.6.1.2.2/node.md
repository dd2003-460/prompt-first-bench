# N599: Intel Xeon 8480+ 方案 3 年 TCO 约为 $3,200 USD（主机 $1,800 + 内存 $800 + 电力 $600），与 AMD E

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N209

## Claim

Intel Xeon 8480+ 方案 3 年 TCO 约为 $3,200 USD（主机 $1,800 + 内存 $800 + 电力 $600），与 AMD EPYC 方案成本相近，但吞吐量更低，因此单位 token 成本更高，在‘无硬性延迟指标’前提下，CPU 方案因初始投入与 GPU 方案差距缩小（<50%）但性能差距巨大（>10x），被排除在性价比最优候选集之外。

## Corrected Claim

Intel Xeon 8480+ 方案 3 年 TCO 约为数千美元量级，与 AMD EPYC 方案成本相近，但吞吐量显著低于 GPU 方案（通常差距在10倍以上），因此单位 token 成本更高，在‘无硬性延迟指标’前提下，CPU 方案因性能差距巨大，通常被排除在性价比最优候选集之外。

## Evidence

[质询]具体数值（如$3,200 TCO、$1,800主机成本）属于特定市场条件下的经验事实，缺乏实时市场数据支持，且‘性能差距>10x’的具体倍数依赖于具体的模型规模和推理框架，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持；虽然CPU与GPU在LLM推理上的性能差距通常确实巨大（>10x），且CPU方案因吞吐量低导致单位token成本高，但具体TCO数值和精确性能倍数需依赖具体硬件配置和市场报价，无法仅凭逻辑推导验证具体金额。

## Search Query

Intel Xeon 8480+ server cost LLM inference TCO comparison
