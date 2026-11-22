# N24: 候选集架构覆盖：列出当前主流 GPU 架构（NVIDIA Ada Lovelace/Hopper, AMD RDNA3/CDNA3, Intel Arc/Map

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

候选集架构覆盖：列出当前主流 GPU 架构（NVIDIA Ada Lovelace/Hopper, AMD RDNA3/CDNA3, Intel Arc/Maple Ridge）及其对 Qwen3-27B 推理的兼容性（CUDA vs ROCm vs SYCL），确保候选集包含至少 2 种不同架构以评估生态锁定风险。

## Corrected Claim

NVIDIA Ada Lovelace架构是主流GPU架构之一，支持CUDA生态；但关于AMD RDNA3/CDNA3、Intel Arc/Maple Ridge及其对Qwen3-27B推理的具体兼容性（ROCm/SYCL）需进一步核实。

## Evidence

[质询]参考来源仅覆盖NVIDIA Ada Lovelace架构，完全缺失AMD RDNA3/CDNA3、Intel Arc/Maple Ridge以及Qwen3-27B模型兼容性（CUDA/ROCm/SYCL）的相关证据，无法验证陈述中关于多架构覆盖及生态锁定风险评估的核心内容。 | 来源[1][2][3]仅证实NVIDIA Ada Lovelace架构存在，与陈述中关于AMD/Intel架构及Qwen3-27B兼容性的部分无关，属于经验事实且缺乏多源支持。

## Search Query

NVIDIA AMD Intel GPU architecture comparison LLM inference compatibility Qwen3

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1913371855005419286&rut=13bce744aecf0bc69691ce6f3de67dd4f52b53bbf0f9879fed13723c6c004b3d', 'type': 'ddg', 'title': 'NVIDIA GPU架构解析 - Ada Lovelace 篇（4090/L40/4080/L4）'}
- {'url': 'https://zh.wikipedia.org/wiki/Ada_Lovelace_(%E5%BE%AE%E6%9E%B6%E6%9E%84)&rut=5268bbac2971c26fc19933cc99fc7a9e62a74c09d78fed960e8c68f95df6c2f6', 'type': 'ddg', 'title': 'Ada Lovelace (微架构) - 维基百科，自由的百科全书'}
- {'url': 'https://zh.wikipedia.org/zh-tw/Ada_Lovelace_(%E5%BE%AE%E6%9E%B6%E6%9E%84)&rut=8f5e44db96eaa9c0d2b300fc4b88ee72a95dc7d488663d1657cb3aa60829f547', 'type': 'ddg', 'title': 'Ada Lovelace (微架構) - 維基百科，自由的百科全書'}
