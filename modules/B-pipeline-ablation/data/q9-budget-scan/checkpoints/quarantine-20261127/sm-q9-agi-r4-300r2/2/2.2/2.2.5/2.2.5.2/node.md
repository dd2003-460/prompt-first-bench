# N132: 代码执行工具（Python Sandbox）的执行时间分布：与文献检索不同，本地 Python 代码执行时间呈重尾分布（Log-Normal 或 Pareto）

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

代码执行工具（Python Sandbox）的执行时间分布：与文献检索不同，本地 Python 代码执行时间呈重尾分布（Log-Normal 或 Pareto），均值 μ_code 取决于代码复杂度（典型 50-500ms），P99 可达 2-5s（涉及导入大型库或复杂数值计算）；若 Hook 频率相同（1/500 tokens），代码执行引入的平均延迟占比 = μ_code / T_gen_window，若 μ_code=200ms, T_gen_window=10s，则占比 2%，但若遇到 P99=2s，单次阻塞占比达 20%，需引入异步执行队列以避免阻塞推理流。

## Corrected Claim

代码执行工具（Python Sandbox）的执行时间分布：与文献检索不同，本地 Python 代码执行时间呈重尾分布（Log-Normal 或 Pareto），均值 μ_code 取决于代码复杂度（典型 50-500ms），P99 可达 2-5s（涉及导入大型库或复杂数值计算）；若 Hook 频率相同（1/500 tokens），代码执行引入的平均延迟占比 = μ_code / T_gen_window，若 μ_code=200ms, T_gen_window=10s，则占比 2%，但若遇到 P99=2s，单次阻塞占比达 20%，需引入异步执行队列以避免阻塞推理流。

## Evidence

先验知识/题面给定，逻辑校验通过：代码执行时间重尾分布符合工程常识，算术推导（200ms/10s=2%, 2s/10s=20%）准确无误，异步优化建议合理。

## Search Query

python code execution time distribution sandbox latency heavy tail lognormal
