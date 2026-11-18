# N74: RTX 4090 在 Qwen3-27B INT8 量化下，vLLM 框架与 llama.cpp 框架的实测吞吐量差异，以及驱动版本（535 vs 550）对 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N22

## Claim

RTX 4090 在 Qwen3-27B INT8 量化下，vLLM 框架与 llama.cpp 框架的实测吞吐量差异，以及驱动版本（535 vs 550）对 CUDA kernel 效率的影响百分比

## Corrected Claim

RTX 4090 在 Qwen3-27B INT8 量化下，vLLM 与 llama.cpp 的吞吐量存在差异，且驱动版本（535 vs 550）可能影响 CUDA kernel 效率，但具体差异百分比需查阅特定基准测试报告。

## Evidence

[质询]该陈述包含具体的经验性数值断言（吞吐量差异、驱动版本影响百分比），属于硬件性能与软件框架实测数据，无法从第一性原理推导，且参考来源中完全缺失相关数据支持。 | 经验事实，逻辑自洽但缺来源支持（来源[1]为GitHub首页无关内容，来源[2]为RTX 4060规格，均与RTX 4090及具体框架/驱动性能测试无关）

## Search Query

RTX 4090 Qwen 27B INT8 vLLM vs llama.cpp throughput driver version impact

## Retrieval Sources

- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
