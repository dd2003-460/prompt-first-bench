# N143: RTX 5090 在 FP8 推理模式下的平均实际功耗（非 TDP 575W 峰值），需依据负载监控数据计算 5 年 OpEx 电费，假设平均功耗为 TDP 的

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

RTX 5090 在 FP8 推理模式下的平均实际功耗（非 TDP 575W 峰值），需依据负载监控数据计算 5 年 OpEx 电费，假设平均功耗为 TDP 的 70-80% 进行估算并标注 [待核验]。

## Corrected Claim

RTX 5090 在 FP8 推理模式下的平均实际功耗需依据具体负载监控数据确定；若缺乏实测数据，可暂按 TDP (575W) 的 70-80% 区间进行保守估算，但需标注该数值为经验估算值而非固定规格。

## Evidence

[质询]该陈述将‘平均实际功耗’这一经验事实（硬件运行参数）设定为 TDP 的 70-80%，但缺乏具体负载场景（如并发数、序列长度、利用率）的支持，且不同推理框架和驱动版本下功耗波动较大，70-80% 仅为粗略估算区间，并非固定物理常数。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该参数属于硬件运行经验值，不可由第一性原理严格推出，故降级）。

## Search Query

RTX 5090 average power consumption FP8 inference load
