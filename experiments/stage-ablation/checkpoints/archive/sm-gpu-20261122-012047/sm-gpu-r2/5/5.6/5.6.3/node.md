# N155: llama.cpp 对 Apple M3 Ultra 的推理优化包括 Metal 后端加速，但 Qwen3-27B 在 M3 Ultra 上的吞吐量约为 5-8

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N41

## Claim

llama.cpp 对 Apple M3 Ultra 的推理优化包括 Metal 后端加速，但 Qwen3-27B 在 M3 Ultra 上的吞吐量约为 5-8 tokens/s，比 NVIDIA H100 低 50-70%，且不支持 FP8 量化加速。

## Corrected Claim

llama.cpp 对 Apple M3 Ultra 的推理优化包括 Metal 后端加速，但 Qwen3-27B 在 M3 Ultra 上的吞吐量通常低于 NVIDIA H100，且不支持 FP8 量化加速。

## Evidence

[质询]具体数值（5-8 tokens/s）和对比结论（比H100低50-70%）缺乏来源直接支持，且M3 Ultra带宽极高，27B模型在合理量化下吞吐量可能高于此范围，存在数值量级偏差风险。 | 来源[1][2][3]确认llama.cpp支持Metal后端及优化，但未提供Qwen3-27B在M3 Ultra的具体吞吐量数据或与H100的对比数据，属于经验事实且缺来源支持。

## Search Query

llama.cpp Apple M3 Ultra Qwen3-27B inference performance Metal backend

## Retrieval Sources

- {'url': 'https://macgpu.com/zh/blog/2026-0402-mac-metalrt-mlx-llamacpp-bendi-tuili-yinqing-duibi.html&rut=71cc5a696e7019238d9a677c21c02e01685bfdd40ac27136bd6a16ef777e632b', 'type': 'ddg', 'title': '2026 年 Apple Silicon 本地 LLM 推理引擎怎么选？MetalRT、MLX 与 llama.cpp 对比调参清单 ...'}
- {'url': 'https://blog.csdn.net/2301_81410839/article/details/162652893&rut=e96c4d259bfde261d4ba4b635260213bdf35a0a8c1ccaea6b1576482e9fb8061', 'type': 'ddg', 'title': 'llama.cpp 的 Metal/CPU 混合推理调度：Apple Silicon 上的线程绑定与内存带宽优化'}
- {'url': 'https://www.mindlynx.top/2026/09/28/llama-cpp-0-5-0%EF%BC%9Ametal-moe-%E8%9E%8D%E5%90%88%E8%AE%A9-mac-%E6%8E%A8%E7%90%86%E6%8F%90%E9%80%9F/&rut=fdd42ba55f48767fb33fcea9186fcd7cdf26c17a730a45d6d9a3b691efdc81e7', 'type': 'ddg', 'title': 'llama.cpp 0.5.0：Metal MoE 融合让 Mac 推理提速 - MindLynx开源模型探索站'}
