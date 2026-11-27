# N67: 非典型方案的软件生态风险量化：Intel Arc 和 Apple Silicon 的 CUDA 替代方案（ONE API, Metal）在 LLM 推理中的算子

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

非典型方案的软件生态风险量化：Intel Arc 和 Apple Silicon 的 CUDA 替代方案（ONE API, Metal）在 LLM 推理中的算子覆盖率为 80-90% [待核验]，缺失算子可能导致回退到 CPU 执行，性能下降 5-10 倍

## Corrected Claim

Intel Arc 和 Apple Silicon 的 CUDA 替代方案（ONE API, Metal）在 LLM 推理中的算子覆盖率尚未达到 100%，缺失算子可能导致回退到 CPU 执行，造成显著性能下降（具体倍数视算子复杂度而定，通常远高于 GPU 原生执行）。

## Evidence

[质询]算子覆盖率80-90%及性能下降5-10倍属于具体经验数据，缺乏统一基准测试支持，且不同模型和算子组合下波动极大，数值过于精确且缺乏来源佐证。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Intel ONE API vs CUDA LLM inference operator coverage benchmark
