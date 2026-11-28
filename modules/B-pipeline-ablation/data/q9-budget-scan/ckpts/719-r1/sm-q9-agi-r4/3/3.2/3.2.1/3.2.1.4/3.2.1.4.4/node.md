# N516: FP8 E4M3 格式在 KV Cache 中的字节数为 1 byte/element，需确认 vLLM 是否支持 FP8 KV Cache 及具体实现精度

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N184

## Claim

FP8 E4M3 格式在 KV Cache 中的字节数为 1 byte/element，需确认 vLLM 是否支持 FP8 KV Cache 及具体实现精度

## Corrected Claim

FP8 E4M3 格式在 KV Cache 中占用 1 字节/元素；vLLM 是否支持 FP8 KV Cache 及其具体实现精度需根据特定版本文档进一步确认。

## Evidence

[质询]vLLM 对 FP8 KV Cache 的支持状态及具体实现细节属于快速迭代的软件版本特性，不同版本间可能存在差异，且‘需确认’这一行动项本身依赖于特定上下文（如目标版本），缺乏静态事实支撑。 | FP8 E4M3 格式占用 1 字节符合 IEEE 754 标准定义，逻辑自洽；但 vLLM 的具体支持情况属于经验事实，且本轮检索无可用来源，无法提供直接支持，故降级。

## Search Query

vLLM FP8 KV Cache implementation E4M3 bytes per element
