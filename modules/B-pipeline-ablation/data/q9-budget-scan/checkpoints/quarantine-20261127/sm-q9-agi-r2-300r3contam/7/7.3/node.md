# N79: 显存占用率瓶颈验证：27B 模型 NVFP4 权重约占 13.5GB，加上 FP8 KV Cache（假设 262k context, batch=8），总显存

- **status**: degraded
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

[质询]权重显存数值与来源矛盾：陈述称NVFP4权重约占13.5GB，但来源[2]明确指出该模型权重压缩至23.4GB，来源[3]也指出约为20-22GB，13.5GB的量级明显偏低，可能是混淆了不同量化精度或计算错误。 | 来源[2]和[3]均表明27B模型NVFP4权重显存占用在20-23.4GB之间，与陈述中的13.5GB存在显著差异，导致总显存估算基础错误。

## Search Query

Qwen 27B NVFP4 memory footprint V100 KV cache size calculation

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_01140/article/details/168246366&rut=3fc05cea2d0898e81e293cbdbf8c5548a3b34e7d0aa29061f14326e669bc2222', 'type': 'ddg', 'title': 'Qwen3.8-27B-NVFP4 部署常见问题全解：显存不足、精度取舍与关键参数调优-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00110/article/details/153247350&rut=684f18e550974e62702a560904ff20b0c02a87b19f50cf789dd85c037aad2eee', 'type': 'ddg', 'title': '单卡部署27B模型不是梦：Qwen3.8-27B-NVFP4显存占用与推理性能实测解析-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/162604876&rut=ef98eea403d5bff14128be2d10e758d41cfa0d018fe3cfdd650cb45133acb313', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 深度评测：英伟达官方量化，27B 长上下文本地部署新选择'}
