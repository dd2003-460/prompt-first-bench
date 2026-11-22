# N252: 在 INT8 量化且 Batch Size=1 的工作点下，显存需求为 权重 27.1 GB + KV Cache 1.57 GB + 开销 2.03 GB =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

在 INT8 量化且 Batch Size=1 的工作点下，显存需求为 权重 27.1 GB + KV Cache 1.57 GB + 开销 2.03 GB = 30.7 GB，加 10% 余量为 33.77 GB。该值低于 N95 中保守估算的 50 GB，意味着 48 GB 显存的 A6000 Ada 单卡即可运行 INT8 模型，无需双卡；而 24 GB 显存的消费级显卡（如 4090）因 33.77 GB > 24 GB 而完全不可行，必须使用双卡或更高显存硬件。

## Corrected Claim

在 INT8 量化且 Batch Size=1 的工作点下，显存需求为 权重 27.1 GB + KV Cache 1.57 GB + 开销 2.03 GB = 30.7 GB，加 10% 余量为 33.77 GB。该值低于 N95 中保守估算的 50 GB，意味着 48 GB 显存的 A6000 Ada 单卡即可运行 INT8 模型，无需双卡；而 24 GB 显存的消费级显卡（如 4090）因 33.77 GB > 24 GB 而完全不可行，必须使用双卡或更高显存硬件。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（27.1+1.57+2.03=30.7，30.7*1.1=33.77），且33.77GB < 48GB 与 33.77GB > 24GB 的比较逻辑自洽，符合INT8量化显存估算的工程常识。

## Search Query

INT8 quantized LLM 27B parameter memory footprint 48GB GPU feasibility
