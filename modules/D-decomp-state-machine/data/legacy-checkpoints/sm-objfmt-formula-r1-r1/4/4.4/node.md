# N19: Qwen3-27B 在 NVFP4 精度下的理论最小显存占用为 13.5GB (27B * 0.5 byte) + 块级缩放因子开销 (~1-2GB) + KV

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5, N6

## Claim

Qwen3-27B 在 NVFP4 精度下的理论最小显存占用为 13.5GB (27B * 0.5 byte) + 块级缩放因子开销 (~1-2GB) + KV Cache 开销，总显存需求约 15-17GB，但需硬件支持 FP4 运算

## Corrected Claim

Qwen3-27B 在 NVFP4 精度下的理论最小显存占用约为 13.5GB (权重) + 额外开销，实际部署显存需求通常在 20-22GB 左右（参考来源[2]实测），需硬件支持 FP4 运算。

## Evidence

[质询]来源[2]明确指出Qwen3.6-27B-NVFP4的实测显存占用为20-22GB，这与陈述中“总显存需求约15-17GB”存在显著差异（相差约3-5GB），表明该估算可能低估了KV Cache或运行时开销，或者不同版本/配置下显存需求波动较大。 | 逻辑上27B*0.5B=13.5GB权重基础正确，但来源[2]提供的实测数据（20-22GB）高于陈述范围（15-17GB），属于间接支持但数值不完全一致，故降级。

## Search Query

NVFP4 Qwen3-27B memory requirement block scaling overhead

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_01140/article/details/168246366&rut=3fc05cea2d0898e81e293cbdbf8c5548a3b34e7d0aa29061f14326e669bc2222', 'type': 'ddg', 'title': 'Qwen3.8-27B-NVFP4 部署常见问题全解：显存不足、精度取舍与关键参数调优-CSDN博客'}
- {'url': 'https://blog.csdn.net/chen695969/article/details/162604876&rut=2cc081b90a397c139f452365a429d1c067ce711fe093180eff38b87935048621', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 深度评测：英伟达官方量化，27B 长上下文本地部署新选择-CSDN博客'}
- {'url': 'https://blog.gitcode.com/5387cc4ddf5c16957195327d6fb15a19.html&rut=b3cc73a4875fbbc7781febf3721a5436d24a8697580586d8f126b53bce9abb1c', 'type': 'ddg', 'title': 'Qwen3.8-27B-NVFP4 部署常见问题全解：显存不足、精度取舍与关键参数调优 - AtomGit | GitCode博客'}
