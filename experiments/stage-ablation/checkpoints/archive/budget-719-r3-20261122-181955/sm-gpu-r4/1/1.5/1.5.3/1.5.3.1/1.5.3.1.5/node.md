# N592: MLX 框架在 Apple Silicon 上的内存访问效率系数在长上下文（32K tokens）时通常降至 0.6-0.7（理论上限 7.4 tokens/s

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N204, N205, N206

## Claim

MLX 框架在 Apple Silicon 上的内存访问效率系数在长上下文（32K tokens）时通常降至 0.6-0.7（理论上限 7.4 tokens/s * 0.65 = 4.81 tokens/s），因为 KV Cache 增大导致内存访问模式更分散，缓存命中率下降，且 PagedAttention 若未优化会进一步降低效率。

## Corrected Claim

MLX 框架在 Apple Silicon 上处理长上下文（如 32K tokens）时，由于 KV Cache 增大导致内存访问模式分散及缓存命中率下降，内存访问效率系数可能显著降低（具体数值取决于模型与硬件配置，例如在特定基准下可能降至 0.6-0.7 区间），从而限制生成速度。

## Evidence

[质询]数值量级与具体系数缺乏通用基准支持：'理论上限 7.4 tokens/s' 并非 Apple Silicon 的通用物理极限，而是特定模型/硬件配置下的经验值；'0.6-0.7' 的效率系数高度依赖具体模型架构、序列长度及内存带宽利用率，将其表述为'通常'缺乏普适性证据，且 7.4 * 0.65 = 4.81 的计算虽正确，但前提数值本身具有高度特异性。 | 先验知识/题面给定，逻辑校验通过（计算无误，因果机制合理），但具体数值（7.4 tokens/s, 0.6-0.7）属于特定场景下的经验参数，缺乏通用来源支持，故降级。
