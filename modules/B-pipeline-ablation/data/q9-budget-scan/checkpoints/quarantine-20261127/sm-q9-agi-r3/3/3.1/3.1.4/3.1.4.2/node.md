# N153: MTP (Multi-Token Prediction) 模块在 V100 上的额外计算开销 T_mtp 约为标准单 token 生成耗时的 15%，即若标准吞

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N53

## Claim

MTP (Multi-Token Prediction) 模块在 V100 上的额外计算开销 T_mtp 约为标准单 token 生成耗时的 15%，即若标准吞吐为 15 tokens/s，MTP 有效吞吐需扣除该开销后重新计算。

## Corrected Claim

MTP 模块在 V100 上的额外计算开销 T_mtp 取决于具体配置（如预测头数量 K），通常需根据实测基准测试确定，不宜简单假设为标准耗时的固定 15%。

## Evidence

[质询]MTP 的额外计算开销并非固定为 15%，它高度依赖于具体的 MTP 头数（K值）、模型架构以及硬件利用率。在 V100 这种较旧的 GPU 上，由于内存带宽瓶颈和计算单元特性，实际开销可能显著高于或低于此数值，将其固化为“约 15%”缺乏普适性依据，属于过度简化的经验估计。 | 先验知识/题面给定，逻辑校验通过（量纲合理，无内部矛盾），但该具体数值（15%）为经验参数，缺乏通用理论支撑或来源直接确认，故降级。

## Search Query

vLLM MTP multi-token prediction overhead V100 latency
