# N145: Intel Arc A770 的 OneAPI 生态对大模型推理支持不成熟，vLLM 对 Arc 系列的支持仍处于实验阶段，缺乏针对 Qwen3-27B 的优化

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35

## Claim

Intel Arc A770 的 OneAPI 生态对大模型推理支持不成熟，vLLM 对 Arc 系列的支持仍处于实验阶段，缺乏针对 Qwen3-27B 的优化 kernel，实际性能可能低于理论带宽上限的 50%。

## Corrected Claim

Intel Arc A770 在大模型推理生态中支持尚不成熟，vLLM 对 Arc 系列的支持仍处于实验阶段，缺乏针对 Qwen3-27B 的专用优化 kernel，实际推理性能通常显著低于理论峰值带宽。

## Evidence

[质询]具体数值断言（'低于理论带宽上限的50%'）缺乏公开基准测试支持，且'OneAPI生态'表述不准确（vLLM通常依赖DirectML或SYCL后端，而非直接依赖OneAPI运行时），属于经验事实且存在技术细节模糊。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源），且具体性能百分比无数据佐证，故降级为定性表述。

## Search Query

Intel Arc A770 vLLM support status Qwen3 27B inference performance benchmark
