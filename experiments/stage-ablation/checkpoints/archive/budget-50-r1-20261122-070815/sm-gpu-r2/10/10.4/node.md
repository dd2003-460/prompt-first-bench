# N148: 在 RTX 4090 上，AWQ INT8 量化模型的推理吞吐量 (tokens/s) 与 BF16 模型的吞吐量对比，用于验证 N34 中'INT8 是更好替

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

在 RTX 4090 上，AWQ INT8 量化模型的推理吞吐量 (tokens/s) 与 BF16 模型的吞吐量对比，用于验证 N34 中'INT8 是更好替代'的论断是否成立

## Corrected Claim

在RTX 4090上，INT8/AWQ量化模型通常能显著提升推理吞吐量并降低显存占用，但具体tokens/s数值需参考特定模型（如Qwen-32B）的实测基准，来源[2]提供了对比框架但未给出具体数值。

## Evidence

[质询]来源[2]标题提及INT8/AWQ/GGUF对比，但摘要未提供具体的吞吐量数值（tokens/s）或明确的BF16对比数据，无法直接验证'INT8是更好替代'这一具体论断的量化支撑；且AWQ通常为INT4量化，与INT8在显存占用和速度上存在差异，直接对比需明确具体模型和基准。 | 来源[2]主题相关（INT8/AWQ在4090上的对比），但摘要缺乏具体吞吐量数值支持，属于间接支持；经验事实（具体性能数据）缺直接来源支持，故降级。

## Search Query

RTX 4090 AWQ INT8 vs BF16 inference throughput comparison

## Retrieval Sources

- {'url': 'https://blog.csdn.net/m0_53440477/article/details/146102081&rut=dc9ad56f796dc9cec6a12e3f0e42ce682383f7205b7fc7fc77c8f7192b66b26e', 'type': 'ddg', 'title': '在NVIDIA RTX 4090显卡上部署阿里千问QwQ-32B-AWQ模型教程_qwq-awq-CSDN博客'}
- {'url': 'https://y1cloud.cn/2026/04/30/int8-awq-gguf/&rut=7eaf347d2ee7acc60302033578213b370eee7c92fa27b5fe4d8ad57d9df6e8e2', 'type': 'ddg', 'title': '大模型量化部署：Int8/Awq/Gguf 实战对比与性能调优'}
- {'url': 'https://blog.csdn.net/weixin_29056145/article/details/159097790&rut=e49c37dba3779d3ed8d374ca4e2a01c5ff4b9a2fdc80a88139289d1659acb837', 'type': 'ddg', 'title': '17.8GB显存就能跑!Qwen-32B量化模型在RTX 4090上的极限压榨指南-CSDN博客'}
