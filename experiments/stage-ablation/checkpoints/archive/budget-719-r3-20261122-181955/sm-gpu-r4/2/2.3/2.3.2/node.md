# N80: llama.cpp 的静态开销（Static Overhead）主要包括 CPU 端的上下文缓冲区、KV Cache 的索引结构及少量临时张量；在 32K 上下

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16

## Claim

llama.cpp 的静态开销（Static Overhead）主要包括 CPU 端的上下文缓冲区、KV Cache 的索引结构及少量临时张量；在 32K 上下文下，其额外开销通常小于 500 MB，因为 llama.cpp 采用紧凑的内存布局且主要依赖 CPU 内存或 GPU 共享内存，具体数值需运行 `llama-cli -m qwen3-27b.gguf -p 32k` 并监控 `n_gpu_layers` 下的实际显存占用 [待核验]。

## Corrected Claim

llama.cpp 的静态开销主要包括 CPU 端的上下文缓冲区、KV Cache 的索引结构及少量临时张量；在 32K 上下文下，其额外开销取决于模型参数量和精度，具体数值需运行实际命令并监控显存占用，通常对于中小规模模型（如 7B-13B）可能小于 500 MB，但大模型会显著更高。

## Evidence

[质询]陈述中关于“32K 上下文下额外开销通常小于 500 MB”的具体数值属于经验事实，且未明确指定模型参数量（如 7B, 13B, 70B 等），不同规模模型的 KV Cache 大小差异巨大，该数值缺乏普适性且来源未提供具体数据支持。 | 来源 [1] 主题相关（llama.cpp 代码浅析），但摘要仅提及目录结构，未提供具体的内存开销数值或 32K 上下文下的显存占用数据，属于间接支持/无直接证据；该数值为经验事实，逻辑自洽但缺来源直接支持。

## Search Query

llama.cpp memory overhead 32k context Qwen 27B GB static buffer size

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/672289691&rut=d8299bb4b6a2a77ff2a0aa7644371c00930fbc2509f830473089c0c851a7027a', 'type': 'ddg', 'title': '笔记：Llama.cpp 代码浅析（三）：计算开销 - 知乎'}
