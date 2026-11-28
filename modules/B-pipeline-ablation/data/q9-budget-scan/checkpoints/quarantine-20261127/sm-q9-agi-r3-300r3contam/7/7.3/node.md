# N79: 显存占用率瓶颈验证：27B 模型 NVFP4 权重约占 13.5GB，加上 FP8 KV Cache（假设 262k context, batch=8），总显存

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29

## Claim

显存占用率瓶颈验证：27B 模型 NVFP4 权重约占 13.5GB，加上 FP8 KV Cache（假设 262k context, batch=8），总显存占用需实测确认是否超过 64GB 物理限制（4x16GB），若超过则需降低 max_num_seqs 或 context length。

## Corrected Claim

显存占用率瓶颈验证：27B 模型 NVFP4 权重约占 20-23.4GB，加上 FP8 KV Cache（假设 262k context, batch=8），总显存占用需实测确认是否超过 64GB 物理限制（4x16GB），若超过则需降低 max_num_seqs 或 context length。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于静态权重分布与基础显存余量计算，子节点2聚焦于动态KV Cache的公式推导及极端情况下的可行性验证。两者维度不同（静态vs动态），逻辑互补且无重叠，共同完整覆盖了父节点中关于权重、KV Cache、硬件限制及优化策略的所有关键要素。）

## Search Query

Qwen 27B NVFP4 memory footprint V100 KV cache size calculation

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_01140/article/details/168246366&rut=3fc05cea2d0898e81e293cbdbf8c5548a3b34e7d0aa29061f14326e669bc2222', 'type': 'ddg', 'title': 'Qwen3.8-27B-NVFP4 部署常见问题全解：显存不足、精度取舍与关键参数调优-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00110/article/details/153247350&rut=684f18e550974e62702a560904ff20b0c02a87b19f50cf789dd85c037aad2eee', 'type': 'ddg', 'title': '单卡部署27B模型不是梦：Qwen3.8-27B-NVFP4显存占用与推理性能实测解析-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/162604876&rut=ef98eea403d5bff14128be2d10e758d41cfa0d018fe3cfdd650cb45133acb313', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 深度评测：英伟达官方量化，27B 长上下文本地部署新选择'}
