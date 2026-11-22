# N195: 框架版本对静态显存的影响量化：vLLM 0.4.x 到 0.6.x 版本间，基础框架开销（不含 KV Cache）从约 1.2GB 增加至约 1.8GB，主要源

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

框架版本对静态显存的影响量化：vLLM 0.4.x 到 0.6.x 版本间，基础框架开销（不含 KV Cache）从约 1.2GB 增加至约 1.8GB，主要源于引入的新的调度器组件和更复杂的 tensor parallel 通信缓冲区；llama.cpp 的静态开销通常低于 0.5GB，因其采用更紧凑的内存管理策略。

## Corrected Claim

vLLM 0.4.x 到 0.6.x 版本间，基础框架开销（不含 KV Cache）有所增加，主要源于引入的新调度器组件和更复杂的 tensor parallel 通信缓冲区；llama.cpp 的静态开销通常较低，因其采用更紧凑的内存管理策略。

## Evidence

[质询]具体数值（1.2GB至1.8GB）缺乏公开基准测试支持，且将显存增加完全归因于调度器和通信缓冲区可能忽略了模型加载格式、CUDA上下文或默认配置变更等其他因素，存在归因偏差风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值及归因准确性）

## Search Query

vLLM version 0.4 vs 0.6 base memory overhead GB llama.cpp
