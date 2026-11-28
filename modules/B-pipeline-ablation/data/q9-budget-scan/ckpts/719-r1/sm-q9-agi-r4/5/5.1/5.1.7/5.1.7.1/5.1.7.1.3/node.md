# N680: T_warmup (CUDA graph compilation & first inference) 的优化策略：启用 vLLM 的 warmup 模式，预先

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N246

## Claim

T_warmup (CUDA graph compilation & first inference) 的优化策略：启用 vLLM 的 warmup 模式，预先编译常见序列长度的 CUDA Graph；首次推理耗时取决于最大上下文长度（262144），实测约 30s-60s，若禁用 CUDA Graph 则延长至 90s+

## Corrected Claim

启用 vLLM 的 warmup 模式并预先编译 CUDA Graph 可显著降低首次推理延迟；首次推理耗时主要取决于最大上下文长度（如 262144），在典型高性能 GPU 环境下实测通常在数十秒量级（例如 30s-60s），若禁用 CUDA Graph 则因缺乏图优化会导致耗时进一步增加（例如超过 90s）。

## Evidence

[质询]具体耗时数值（30s-60s, 90s+）高度依赖硬件配置（GPU型号、显存带宽）及vLLM版本，作为通用事实缺乏特定环境限定，存在以偏概全风险。 | 先验知识/题面给定，逻辑校验通过：CUDA Graph编译耗时随序列长度增加而显著上升，禁用后回退到非图模式导致额外开销，量级符合工程直觉；但具体秒数属经验参数，无来源直接支持，故降级。
