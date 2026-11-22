# N149: llama.cpp (GGUF) 在 CUDA 后端下的静态显存开销通常低于 100MB，因为其使用静态内存分配且无 PyTorch 张量元数据开销，但需预留约

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

llama.cpp (GGUF) 在 CUDA 后端下的静态显存开销通常低于 100MB，因为其使用静态内存分配且无 PyTorch 张量元数据开销，但需预留约 50-100MB 用于 KV Cache 的动态扩展缓冲。

## Corrected Claim

llama.cpp (GGUF) 在 CUDA 后端下的静态显存开销通常显著低于 PyTorch 框架，具体数值取决于模型规模与配置，一般较小；KV Cache 的显存占用随上下文长度线性增长，需根据最大上下文长度预留相应空间，而非固定的 50-100MB 缓冲。

## Evidence

[质询]数值量级与具体实现细节存在不确定性：'低于100MB'的静态开销和'50-100MB'的KV Cache缓冲并非绝对固定的物理常数，而是高度依赖于模型架构（如层数、头数）、上下文长度配置以及具体的CUDA实现版本（如是否启用Flash Attention等优化）。将动态变化的工程参数表述为固定的'通常'范围，且缺乏特定条件下的限定，属于经验事实的过度概括。 | 经验事实，逻辑自洽但缺来源支持。llama.cpp确实比PyTorch框架更轻量，静态开销低是合理的，但具体数值（<100MB, 50-100MB）属于特定配置下的经验值，非第一性原理可严格推导，且无外部来源验证具体数值区间。
