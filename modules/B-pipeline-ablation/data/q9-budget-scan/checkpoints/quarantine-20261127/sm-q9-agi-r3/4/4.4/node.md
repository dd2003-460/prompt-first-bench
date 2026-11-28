# N24: 专用小模型本地部署可行性：评估在剩余 V100 显存（扣除 27B 后）或 MacBook M1 Max (64GB) 上部署 7B-14B 规模模型（如 Ll

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5, N6

## Claim

专用小模型本地部署可行性：评估在剩余 V100 显存（扣除 27B 后）或 MacBook M1 Max (64GB) 上部署 7B-14B 规模模型（如 Llama-3-8B/Qwen2.5-14B）用于辅助任务（摘要、分类、简单代码生成）的推理速度（tokens/sec）与内存占用，作为 27B 的预处理/后处理加速器。

## Corrected Claim

专用小模型本地部署可行性：评估在剩余 V100 显存（扣除 27B 后）或 MacBook M1 Max (64GB) 上部署 7B-14B 规模模型（如 Llama-3-8B/Qwen2.5-14B）用于辅助任务的可行性，其推理速度通常高于 27B 模型，内存占用显著降低，可作为 27B 的预处理/后处理加速器。

## Evidence

[质询]该陈述包含具体的性能指标（tokens/sec）和内存占用预期，属于经验事实。参考来源仅涉及 27B 模型在 V100 上的部署，未提供 7B-14B 模型在剩余显存或 MacBook M1 Max 上的具体推理速度和内存数据，缺乏直接来源支持。 | 逻辑上，7B-14B 模型比 27B 小，在相同硬件或更小硬件（M1 Max 64GB）上运行更可行且速度更快，符合常识；但具体数值（如 tokens/sec）属于经验事实，来源 [1] 仅覆盖 27B 模型，未覆盖 7B-14B 模型的具体性能数据，故降级。

## Search Query

Llama 3 8B Qwen 2.5 14B inference speed tokens per second Apple M1 Max 64GB VRAM usage benchmark

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2083714185020683992&rut=9996bbbbfc5e86ac10d78bd089b852b1904e7626815aff2efa87238f885ed409', 'type': 'ddg', 'title': '从 4 到 64 tok/s：一块 V100 部署 Qwen 27B 大模型的调优实录'}
