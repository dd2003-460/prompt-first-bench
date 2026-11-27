# N14: 32K上下文KV Cache显存占用计算：KV Cache = 2 * num_layers * num_kv_heads * head_dim * seq_l

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

32K上下文KV Cache显存占用计算：KV Cache = 2 * num_layers * num_kv_heads * head_dim * seq_len * bytes_per_elem。Qwen3-27B假设num_layers=32, num_kv_heads=8, head_dim=128, seq_len=32768, BF16(2 bytes): 2*32*8*128*32768*2 = 4.29 GB；FP8/INT8(1 byte): 2.15 GB；W4(0.5 byte): 1.07 GB [待核验：Qwen3-27B实际层数与KV头数]

## Corrected Claim

KV Cache 计算公式正确，但 Qwen3-27B 的具体显存占用需依据其实际架构参数（层数、KV头数）计算，当前假设参数下的数值（4.29 GB @ BF16）仅供参考，未经官方配置确认。

## Evidence

[质询]Qwen3-27B 的具体架构参数（num_layers=32, num_kv_heads=8）属于经验事实，且与参考来源中提到的 Qwen3-32B 参数不一致，无法从第一性原理推导，需依赖具体模型配置确认。 | 公式逻辑自洽，但 Qwen3-27B 的具体层数和 KV 头数未在参考来源中直接证实（来源[3]提及 Qwen3-32B 为 256 KiB/token，对应不同参数），属于经验事实缺直接来源支持。

## Search Query

Qwen3-27B num_layers num_kv_heads head_dim KV cache size 32K tokens

## Retrieval Sources

- {'url': 'https://bigolab.com/guides/5620-llm-kv-cache-vram-formula-32k-context-16gb-oom-guide&rut=46ddc7bba8caf539601fc365c9d5b08b8cfdf55e495188e9aaa34cb410c49af8', 'type': 'ddg', 'title': '大模型上下文 KV Cache 显存计算公式详解：为什么 32K 上下文一开 16GB 显卡就 OOM'}
- {'url': 'https://blog.csdn.net/weixin_33402252/article/details/167827622&rut=557effe43b9e3109df40de9fb060dd1f7aa71ec1f3aa82903585f1848473bb2b', 'type': 'ddg', 'title': '大模型本地部署显存占用全解析：量化、KV Cache与上下文长度的计算指南-CSDN博客'}
- {'url': 'https://cloudgpu.app/blog/kv-cache-vram-context-length-calculator-2026&rut=e02a4f729a4b3d3168b05bc38e0a45c441e4fb4c9f6ced82554496ff8aebec6a', 'type': 'ddg', 'title': 'KV Cache VRAM Calculator: How Much Memory Does Context Length Need? (2026)'}
