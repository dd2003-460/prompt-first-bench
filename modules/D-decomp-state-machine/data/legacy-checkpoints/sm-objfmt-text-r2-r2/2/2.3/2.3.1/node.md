# N58: Apple M3 Ultra (192GB) 运行 Qwen3-27B (BF16) 的吞吐量基准约为 15-20 tokens/s，主要受限于 819 GB/

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14, N15, N16

## Claim

Apple M3 Ultra (192GB) 运行 Qwen3-27B (BF16) 的吞吐量基准约为 15-20 tokens/s，主要受限于 819 GB/s 的统一内存带宽，该数值基于 llama.cpp 在类似规模 MoE/Dense 模型上的实测数据外推 [待核验: 具体实测值]

## Corrected Claim

Apple M3 Ultra 运行 Qwen3-27B 的吞吐量实测约为 12-14 tokens/s（基于量化版本数据），BF16 全精度下的具体吞吐量需进一步实测确认，预计受内存带宽限制可能在相近或略低区间。

## Evidence

[质询]数值量级偏差：参考来源显示的实测吞吐量（12.46-14 tokens/s）低于陈述中的范围（15-20 tokens/s），且来源主要涉及量化版本（Q4_K_M）而非BF16，BF16因内存占用更大可能导致KV cache空间受限或带宽压力不同，直接外推存在误差。 | 来源[1]和[2]提供了M3 Ultra运行Qwen3系列27B模型的实测数据（12.46-14 tok/s），虽与陈述的15-20 tok/s有出入且多为量化版本，但证实了该硬件平台运行该规模模型的可行性及大致量级，属于间接支持但数值不完全匹配。

## Search Query

Qwen3-27B Apple M3 Ultra inference speed tokens per second llama.cpp

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_35751412/article/details/169344115&rut=92e3a68a2ce047c141109d8f938b9a018342d8224b15597e8ad7c432fb02b9cf', 'type': 'ddg', 'title': 'Qwen3.8-27B 本地运行实测：Mac Studio M3 Ultra 上 14 tokens/s 的量化取舍与'}
- {'url': 'https://getrigbase.com/can-i-run/qwen3-8-27b-on-apple-m3-ultra/&rut=6a56de10e23ade7ab6314d460d9d3f3cb61836806374d2e0c5bdab028db3fdcf', 'type': 'ddg', 'title': 'Can Apple M3 Ultra run Qwen3.8 27B? Measured 12.46 tok/s'}
- {'url': 'https://llmap.ai/can-i-run/qwen-qwen3-8-27b/apple-m3-ultra&rut=ec82202c8b1574142a7e86d6615394a99ce72c33195955cccc861470ce4d430b', 'type': 'ddg', 'title': 'Can I run Qwen3.8 27B on Apple M3 Ultra (80-core GPU)? - llmap.ai'}
