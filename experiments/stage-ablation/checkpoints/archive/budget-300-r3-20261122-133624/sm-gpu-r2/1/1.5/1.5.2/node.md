# N57: INT8 量化下 KV Cache 显存占用是否减半：取决于 KV Cache 是否也进行 INT8 量化。若仅权重 INT8 而 KV Cache 保持 BF

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

INT8 量化下 KV Cache 显存占用是否减半：取决于 KV Cache 是否也进行 INT8 量化。若仅权重 INT8 而 KV Cache 保持 BF16，则 KV 占用仍为 4.09GB；若 KV Cache 也 INT8，则降至 ~2GB。主流框架（vLLM）默认 KV Cache 保持 BF16 或 FP16，需确认配置。

## Corrected Claim

INT8量化下KV Cache显存占用是否减半取决于KV Cache是否也进行INT8量化。若仅权重INT8而KV Cache保持BF16，则KV占用仍为4.09GB；若KV Cache也INT8，则降至~2GB。主流框架（如vLLM）的KV Cache数据类型默认值随版本和配置变化，需查阅具体文档确认。

## Evidence

[质询]关于vLLM默认KV Cache数据类型的陈述可能过时或过于绝对，vLLM在较新版本中已支持并可能默认启用FP8 KV Cache，且不同硬件/配置下默认行为可能不同，需具体版本确认。 | 逻辑推导成立（INT8为BF16的一半，4.09GB/2≈2GB），但关于vLLM默认配置的经验事实缺乏来源支持，且该配置随版本变化，无法确认为当前绝对事实。

## Search Query

vLLM INT8 weight only quantization KV cache dtype default
