# N114: Apple Silicon 推理框架 llama.cpp/MLX 在 Qwen3-27B Q4_K_M 量化下的实测吞吐量 (34 tokens/s) 与 CU

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

Apple Silicon 推理框架 llama.cpp/MLX 在 Qwen3-27B Q4_K_M 量化下的实测吞吐量 (34 tokens/s) 与 CUDA 方案 (2x 4090 INT8) 吞吐量对比：CUDA 方案预计 50-80 tokens/s，Apple 方案低 30-55%，但无需跨卡通信开销

## Corrected Claim

Apple Silicon 推理框架在 Qwen3-27B Q4_K_M 量化下的实测吞吐量通常低于双卡 CUDA 方案（如 2x 4090 INT8），但具有无需跨卡通信开销的优势。

## Evidence

[质询]具体吞吐量数值（34 tokens/s 和 50-80 tokens/s）属于高度依赖硬件具体型号（如 M1/M2/M3/M4 及内存大小）和软件版本的经验事实，且参考来源摘要中未包含这些具体实测数据，存在数值来源不可靠或口径混淆的风险。 | 参考来源[1]主题相关但摘要未提供具体吞吐量数值支持，属于经验事实且缺乏直接来源佐证，逻辑上 Apple Silicon 单卡无跨卡通信开销优于双卡 CUDA 方案是合理的，但具体数值无法验证。

## Search Query

llama.cpp MLX Qwen3-27B tokens per second vs CUDA inference benchmark

## Retrieval Sources

- {'url': 'https://ai-classroom.qubitlab.cc/articles/tools/ollama-mlx-vllm-compare&rut=bd56332ea75f045fa0cf426aece6f0af00894eebfbc4d52790660d07ef02e6ce', 'type': 'ddg', 'title': 'Mac 本地大模型部署方案对比：Ollama、MLX、llama.cpp、LM Studio、vLLM'}
