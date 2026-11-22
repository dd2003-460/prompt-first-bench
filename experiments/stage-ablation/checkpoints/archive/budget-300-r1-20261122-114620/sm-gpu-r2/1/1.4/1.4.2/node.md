# N51: llama.cpp 对 Qwen3-27B 的 GGUF 量化支持：Q4_K_M (4-bit) 模型文件大小约 16.2GB，Q8_0 (8-bit) 约 2

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

llama.cpp 对 Qwen3-27B 的 GGUF 量化支持：Q4_K_M (4-bit) 模型文件大小约 16.2GB，Q8_0 (8-bit) 约 28.5GB；在 24GB 显存 GPU 上，Q4_K_M 需配合 --n-gpu-layers 64 才能完全 offload，Q8_0 需 --n-gpu-layers 48 否则 CPU offload 导致延迟增加 3-5x

## Corrected Claim

llama.cpp 支持 Qwen3-27B 的 GGUF 量化。Q4_K_M 和 Q8_0 是常见的量化格式，文件大小随量化位数增加而增大。在 24GB 显存 GPU 上，使用 Q4_K_M 通常比 Q8_0 更容易完全 offload 到 GPU，从而减少 CPU offload 带来的延迟增加。具体文件大小和最佳 --n-gpu-layers 设置需根据实际模型文件和硬件环境测试确定。

## Evidence

[质询]具体数值（16.2GB, 28.5GB, 64/48 layers, 3-5x latency）属于高度依赖具体硬件、llama.cpp版本及模型权重的经验事实，且Qwen3-27B的精确量化大小和offload层数需实测验证，无法仅凭逻辑推导得出精确值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

llama.cpp Qwen3-27B GGUF Q4_K_M size n-gpu-layers
