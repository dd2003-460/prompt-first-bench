# N83: H100 的 TDP 为 700W，但实际运行 LLM 推理时功耗波动在 600W-700W 之间，需取均值计算年电力成本

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28, N29, N30

## Claim

H100 的 TDP 为 700W，但实际运行 LLM 推理时功耗波动在 600W-700W 之间，需取均值计算年电力成本

## Corrected Claim

H100 SXM 的 TDP 为 700W，H100 PCIe 的 TDP 为 350W；实际运行 LLM 推理时功耗随负载波动，计算年电力成本时建议根据具体型号和实际负载曲线取均值。

## Evidence

[质询]H100 SXM 的标准 TDP 通常为 700W，但 H100 PCIe 版本 TDP 为 350W，陈述未指明具体型号，存在口径混淆风险；且“实际运行 LLM 推理时功耗波动在 600W-700W”这一具体数值范围属于经验性观测数据，缺乏通用性，不同负载下波动范围可能不同。 | 经验事实，逻辑自洽但缺来源支持（来源[1]为NVIDIA官网首页新闻，未包含H100具体功耗参数；来源[2]为华为昇腾生态论文，与NVIDIA H100无关）。

## Search Query

H100 TDP actual power draw LLM inference average watts

## Retrieval Sources

- {'url': 'https://nvidia.com', 'type': None, 'title': 'direct-browser: nvidia.com'}
- {'url': 'http://arxiv.org/abs/2606.05868v1', 'type': 'arxiv', 'title': 'YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transiti'}
