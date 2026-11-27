# N608: AMD AMX 指令集仅在 Zen 4 (Server/EPYC) 架构上可用，消费级 Ryzen 7000/9000 系列 CPU 不支持 AMX 指令集，因

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N215

## Claim

AMD AMX 指令集仅在 Zen 4 (Server/EPYC) 架构上可用，消费级 Ryzen 7000/9000 系列 CPU 不支持 AMX 指令集，因此 N215 中提到的 AMX 加速仅适用于数据中心级 CPU 方案，消费级 CPU 推理必须依赖 AVX-512 或 AVX2 指令集。

## Corrected Claim

Intel AMX 指令集仅在 Intel Xeon (Server) 架构上可用，消费级 Intel Core 系列 CPU 不支持 AMX 指令集。AMD 的对应技术为 XDNA 或 Zen 架构中的矩阵扩展指令（具体名称随代际变化，如 Zen 5 的 Matrix Extensions），且 AMD 消费级 CPU 对矩阵指令的支持情况需具体查阅对应代际规格，不能直接套用 Intel AMX 的定义。

## Evidence

[质询]概念混淆与事实错误：AMX (Advanced Matrix Extensions) 是 Intel 的指令集扩展（用于 Xeon 处理器），AMD 对应的矩阵加速指令集是 XDNA 或早期的 Matrix Extensions (在 Zen 4/5 中并未以 'AMX' 命名且消费级 Zen 4 并不支持类似 Intel AMX 的硬件矩阵单元，Zen 4 主要依赖 AVX-512 和新的整数/浮点指令，而 Zen 5 引入了新的矩阵指令但也不叫 AMX)。将 Intel 的 AMX 错误地归因于 AMD 架构是根本性的事实错误。 | 逻辑校验失败：AMX 是 Intel 专有指令集，AMD 没有名为 AMX 的指令集。该陈述存在严重的领域知识错误（张冠李戴）。
