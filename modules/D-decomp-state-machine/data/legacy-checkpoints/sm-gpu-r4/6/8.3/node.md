# N83: H100 的 TDP 为 700W，但实际运行 LLM 推理时功耗波动在 600W-700W 之间，需取均值计算年电力成本

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28, N29, N30

## Claim

H100 的 TDP 为 700W，但实际运行 LLM 推理时功耗波动在 600W-700W 之间，需取均值计算年电力成本

## Corrected Claim

H100 SXM5 版本的 TDP 为 700W，在典型 LLM 推理负载下功耗通常接近 TDP 上限，计算年电力成本时建议采用接近 TDP 的均值或实测均值。

## Evidence

[质询]H100 存在 SXM5 (700W) 和 PCIe (350W/550W) 两种主要形态，未指定具体型号即断言 TDP 为 700W 存在口径混淆风险；且“实际运行 LLM 推理时功耗波动在 600W-700W”这一具体数值区间属于经验性观测数据，缺乏通用性，不同负载下波动范围可能不同。 | 参考来源 [1] 讨论的是华为昇腾生态下的 LLM 架构优化，与 NVIDIA H100 的硬件功耗参数完全无关，属于「无可用外部证据」。该陈述为经验事实（硬件规格及运行功耗），逻辑上自洽（700W TDP 下运行功耗接近上限符合直觉），但缺乏来源直接支持，依据经验事实排除条款降级。

## Search Query

H100 TDP actual power draw LLM inference average watts

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/2606.05868v1', 'type': 'arxiv', 'title': 'YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transiti'}
