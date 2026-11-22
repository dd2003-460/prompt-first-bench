# N81: 框架选择对内存效率的影响系数：vLLM 使用 PagedAttention，其内存碎片率低于 5%，但引入 Block Table 管理开销（约 1-2% 额外

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16

## Claim

框架选择对内存效率的影响系数：vLLM 使用 PagedAttention，其内存碎片率低于 5%，但引入 Block Table 管理开销（约 1-2% 额外显存）；ExLlama2 使用 KV Cache 压缩，可能减少 10-20% 的 KV 内存但增加计算开销；llama.cpp 无分页，内存利用率最高但缺乏并发支持。需量化各框架在 32K 上下文下的实际显存峰值与理论最小值的比值 [待核验]。

## Corrected Claim

vLLM 使用 PagedAttention，其内存碎片率低于 5%（来源显示低于 4%），引入 Block Table 管理开销；ExLlama2 和 llama.cpp 的内存效率及并发特性需进一步量化验证，当前缺乏具体显存峰值与理论最小值比值的可靠数据。

## Evidence

[质询]陈述中关于 ExLlama2 和 llama.cpp 的具体量化数据（如 KV 内存减少 10-20%、无分页导致缺乏并发支持等）属于经验事实，且参考来源仅覆盖 vLLM，未提供其他框架的对比数据或具体数值支持，存在来源缺失风险。 | 来源 [1] 直接支持 vLLM PagedAttention 将显存浪费降至 4% 以下（与陈述中 <5% 一致），但来源未覆盖 ExLlama2 和 llama.cpp 的具体性能指标，且这些指标属于经验事实，缺乏多源一致或第一性原理推导支持，故降级。

## Search Query

vLLM PagedAttention vs ExLlama2 vs llama.cpp memory efficiency comparison 32k context

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29046035/article/details/167025951&rut=425446d730128ef3ceefe51c155f3dbc378a703114bc63ade11d0a56f39bb185', 'type': 'ddg', 'title': 'vLLM 推理框架实战：PagedAttention 显存优化与部署调优指南'}
- {'url': 'https://blog.csdn.net/weixin_30225755/article/details/165341972&rut=af5a55ada4467f9b1c6a44242da4e39ff16c5cf024fe0c68ba3e1429d29e1fbc', 'type': 'ddg', 'title': 'vLLM框架解析：大模型推理加速与PagedAttention技术-CSDN博客'}
- {'url': 'https://developer.aliyun.com/article/1664805&rut=8ad4a0d35a72b6d9eb52ecadbbb01bd6ffe6047e692b6c154b5a037041cb7b6c', 'type': 'ddg', 'title': '详解vLLM PagedAttention优化大模型推理KV Cache内存的原理-开发者社区-阿里云'}
