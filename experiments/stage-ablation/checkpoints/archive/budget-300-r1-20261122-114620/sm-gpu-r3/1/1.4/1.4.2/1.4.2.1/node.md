# N167: llama.cpp 对 Qwen3-27B 的 GGUF 量化支持中，Q4_K_M 模型文件大小 16.2GB，Q8_0 模型文件大小 28.5GB，Q5_K_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

llama.cpp 对 Qwen3-27B 的 GGUF 量化支持中，Q4_K_M 模型文件大小 16.2GB，Q8_0 模型文件大小 28.5GB，Q5_K_M 模型文件大小 21.5GB [待核验]；在 24GB 显存 GPU 上，Q4_K_M 需设置 --n-gpu-layers 64 以完全 offload 至 GPU，Q8_0 需设置 --n-gpu-layers 48 以避免 CPU offload 导致延迟增加 3-5x

## Corrected Claim

llama.cpp 对 Qwen3-27B 的 GGUF 量化支持中，Q4_K_M、Q8_0 和 Q5_K_M 模型文件大小分别约为 16.2GB、28.5GB 和 21.5GB；在 24GB 显存 GPU 上，Q4_K_M 通常需设置 --n-gpu-layers 64 以完全 offload 至 GPU，Q8_0 需设置 --n-gpu-layers 48 以避免 CPU offload 导致显著延迟增加

## Evidence

[质询]具体数值（文件大小、层数、延迟倍数）属于经验事实，且缺乏来源支持，无法验证其准确性；特别是'延迟增加3-5x'这一具体倍数缺乏普遍性依据，可能因硬件配置不同而有显著差异。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

llama.cpp Qwen3-27B GGUF Q4_K_M Q8_0 file size n-gpu-layers offload latency
