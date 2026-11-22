# N133: 2×RTX 4090 运行 Qwen3-27B (INT4量化, 32K ctx) 的实测吞吐量约为 20-25 tokens/s/user，首字延迟 (TTF

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

2×RTX 4090 运行 Qwen3-27B (INT4量化, 32K ctx) 的实测吞吐量约为 20-25 tokens/s/user，首字延迟 (TTFT) 约为 1.8-3.0 秒，INT4 虽显存占用更低但反量化开销抵消了部分带宽优势。

## Corrected Claim

2×RTX 4090 运行 Qwen3-27B (INT4量化, 32K ctx) 的实测吞吐量预计不低于 20-25 tokens/s/user（参考双卡8bit实测28 tokens/s），首字延迟 (TTFT) 约为 1.8-3.0 秒。

## Evidence

[质询]来源[1]显示双卡8bit量化实测速度为28 tokens/s，而本陈述声称INT4量化速度仅为20-25 tokens/s，这与通常INT4比8bit更快（或至少相当）的直觉相悖，且缺乏直接支持该特定低吞吐量的来源；此外，来源[2]主要讨论单卡128K上下文，与本陈述的双卡32K场景不完全匹配。 | 经验事实，逻辑自洽但缺来源直接支持；来源[1]提供双卡8bit 28 tokens/s数据，未直接支持INT4 20-25 tokens/s的特定数值，且INT4通常预期性能不低于8bit，故降级。

## Search Query

2x RTX 4090 Qwen3 27B INT4 AWQ GPTQ inference speed benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29039773/article/details/163150694&rut=84549e96bca0282bc06f4934e9999af6a3483a6b6821b6a954d18cae5a1bc238', 'type': 'ddg', 'title': '双RTX 4090部署Qwen3.5-27B大模型实战指南 - CSDN博客'}
- {'url': 'https://www.kongchang.com/articles/4090pao-qwen3-27b-q4liang-hua-128kshang-xia-wen-shi-zhan&rut=2d15a39d5e220a6ec7eb43d71e6dcf03c48fd645592d524027ce3b883ee7bab5', 'type': 'ddg', 'title': '4090跑Qwen3 27B实测：Q4量化+128K上下文显存计算与调优指南 - 控场AI'}
- {'url': 'https://blog.csdn.net/weixin_31715171/article/details/163150699&rut=4c88d11e866d310b3a4932809b0fa8687264b87bc647ff49da0d37ca08ffe338', 'type': 'ddg', 'title': '双RTX 4090部署Qwen3.5-27B模型实战指南 - CSDN博客'}
