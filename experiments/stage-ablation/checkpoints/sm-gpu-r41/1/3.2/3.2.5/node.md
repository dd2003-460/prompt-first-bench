# N43: KV Cache 量化技术（如 FP8 KV Cache）对精度损失的影响评估，需引用相关论文或框架（如 vLLM）的实测数据

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

KV Cache 量化技术（如 FP8 KV Cache）对精度损失的影响评估，需引用相关论文或框架（如 vLLM）的实测数据

## Corrected Claim

KV Cache 量化技术（如 FP8 KV Cache）通常能显著降低显存占用，但可能引入精度损失，具体影响需参考 vLLM 等框架的实测数据或相关学术论文（如 SmoothQuant, KIVI 等）进行评估。

## Evidence

[质询]参考来源均为通用平台首页或无关主题（arXiv首页、GitHub首页、Gmail维基），未包含任何关于KV Cache量化精度损失的具体实测数据或论文引用，无法验证该经验事实。 | 经验事实，逻辑自洽但缺来源支持（来源[1][2][3]均与KV Cache量化精度无关）

## Search Query

FP8 KV cache quantization accuracy loss vLLM

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'https://en.m.wikipedia.org/wiki/Gmail', 'type': 'bing', 'title': 'Gmail - Wikipedia'}
