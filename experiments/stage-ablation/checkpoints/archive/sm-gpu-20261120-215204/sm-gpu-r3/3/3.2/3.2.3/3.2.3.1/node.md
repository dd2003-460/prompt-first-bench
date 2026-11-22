# N250: L40S 48GB 运行 INT8 权重 + INT8 KV Cache 的实际显存占用修正：KV Cache 占用为 5.37 GB，总占用 = 27 GB 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N87

## Claim

L40S 48GB 运行 INT8 权重 + INT8 KV Cache 的实际显存占用修正：KV Cache 占用为 5.37 GB，总占用 = 27 GB + 5.37 GB + 2 GB = 34.37 GB，远低于 48 GB 上限，N87 中 '49GB 略微超出' 的结论错误；该方案与 N86 的 FP8 方案显存占用相同，但 INT8 量化通常比 FP8 导致更高的精度损失 (MMLU 下降 1-3% vs <1%)，故在同等显存占用下 FP8 方案更优。

## Corrected Claim

L40S 48GB 运行 INT8 权重 + INT8 KV Cache 的总显存占用约为 34.37 GB（基于特定 KV Cache 估算值 5.37 GB），远低于 48 GB 上限，N87 中 '49GB 略微超出' 的结论错误；该方案与 N86 的 FP8 方案显存占用相近，但通常 FP8 量化在同等显存占用下精度损失小于 INT8，故 FP8 方案更优。

## Evidence

[质询]KV Cache 占用 5.37 GB 的具体数值缺乏上下文（如序列长度、Batch Size、模型具体架构参数），属于特定场景下的经验计算值，无法仅凭逻辑推导验证其精确性；此外，'INT8 精度损失 1-3% vs FP8 <1%' 为经验统计规律，虽符合一般认知但具体数值范围可能因模型而异。 | 先验知识/题面给定，逻辑校验通过：算术运算 27+5.37+2=34.37 正确，34.37 < 48 逻辑成立；INT8 与 FP8 的精度对比符合通用量化理论常识（FP8 动态范围更优，通常精度损失更小）；因缺乏外部来源直接支持具体 KV Cache 数值及精度下降的具体百分比区间，依据经验事实排除条款降级。
