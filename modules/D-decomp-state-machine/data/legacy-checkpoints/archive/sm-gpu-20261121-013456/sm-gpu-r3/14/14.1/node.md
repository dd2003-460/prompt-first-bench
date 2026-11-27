# N300: RTX 3090 在 Qwen3-27B FP8 量化下的显存占用为 33.3GB，远超其 24GB 物理显存限制，因此 RTX 3090 无法原生运行 Qwe

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N125

## Claim

RTX 3090 在 Qwen3-27B FP8 量化下的显存占用为 33.3GB，远超其 24GB 物理显存限制，因此 RTX 3090 无法原生运行 Qwen3-27B FP8，必须采用 INT4/INT8 量化或 CPU Offloading 方案。

## Corrected Claim

RTX 3090 在 Qwen3-27B FP8 量化下的显存占用为 33.3GB，远超其 24GB 物理显存限制，因此 RTX 3090 无法原生运行 Qwen3-27B FP8，必须采用 INT4/INT8 量化或 CPU Offloading 方案。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8下显存占用约27GB，加上KV Cache等开销达到33.3GB符合工程估算，且远超RTX 3090的24GB物理显存，结论逻辑自洽。

## Search Query

Qwen3-27B FP8 memory footprint 24GB GPU feasibility
