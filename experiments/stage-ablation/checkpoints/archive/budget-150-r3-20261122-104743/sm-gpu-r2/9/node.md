# N36: 性能基准数据基准（2024 Q4）：RTX 4090 在 Llama-3-70B/27B 类模型上的 Decode 速度约为 15-20 tokens/s（单卡

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性能基准数据基准（2024 Q4）：RTX 4090 在 Llama-3-70B/27B 类模型上的 Decode 速度约为 15-20 tokens/s（单卡 BF16），H100 SXM5 约为 50-80 tokens/s（单卡 BF16/FP8），需标记为 [实时检索/第三方评测] 以验证 N16 的带宽瓶颈理论值

## Corrected Claim

性能基准数据基准（2024 Q4）：RTX 4090 在 Llama-3-70B/27B 类模型上的 Decode 速度约为 15-20 tokens/s（单卡 BF16），H100 SXM5 约为 50-80 tokens/s（单卡 BF16/FP8），需标记为 [实时检索/第三方评测] 以验证 N16 的带宽瓶颈理论值（注：当前参考来源未提供直接数值支持，建议补充具体评测报告）

## Evidence

[质询]参考来源[1]和[2]均未提供RTX 4090在Llama-3-70B/27B模型上BF16精度的具体Decode速度数值，也未提供H100 SXM5在相同条件下的对比数据，无法直接验证15-20 tokens/s和50-80 tokens/s的具体量级。 | 逻辑上，RTX 4090显存带宽约1008 GB/s，H100 SXM5约3.35 TB/s，带宽比约3.3倍，性能比3-4倍符合带宽瓶颈理论；但来源[1]仅提及4090运行Qwen3.8-27B，未给出具体tokens/s数值，来源[2]主要测试RTX 5090且为量化模型，缺乏对BF16精度下Llama-3系列模型的具体基准数据支持。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2073510788808041813&rut=5af31fd95e09554f992ec8e2f84bcae496d2187e043e34774c77cb04baca84fa', 'type': 'ddg', 'title': '超强端侧大模型!一张 4090，把 Qwen3.8-27B 跑到真能干活：能力实测、快速部署与最佳参数分享 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/2035362472828344137&rut=1fd9f2c4b925a1bba453711ca2009677dfa7abfb3999dbca7726049edebec211', 'type': 'ddg', 'title': '2026年5月本地大模型硬件Benchmark终极指南：50+硬件平台全横评 - 知乎'}
