# N10: 主流推理框架对 Qwen3-27B 的支持状态：vLLM 已支持 Qwen2.5 系列，Qwen3 支持情况需查最新版本 release notes；llama

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

主流推理框架对 Qwen3-27B 的支持状态：vLLM 已支持 Qwen2.5 系列，Qwen3 支持情况需查最新版本 release notes；llama.cpp 支持 GGUF 格式，需确认 Qwen3 是否已转换为 GGUF

## Corrected Claim

主流推理框架对 Qwen3-27B 的支持状态：vLLM 已支持 Qwen3 系列（包括 Qwen3.5-27B），llama.cpp 支持 GGUF 格式，Qwen3 系列已有 GGUF 转换版本可用。

## Evidence

[质询]陈述中关于 vLLM 支持 Qwen2.5 系列是事实，但关于 Qwen3 支持情况需查最新版本 release notes 的表述过于保守且滞后，参考来源显示 vLLM 已支持 Qwen3.5-27B（暗示 Qwen3 系列已获支持），且 llama.cpp 对 Qwen3 的 GGUF 支持在模型发布后通常很快跟进，无需‘需确认’这种模糊状态。 | 来源 [1] 和 [2] 直接展示了 vLLM 部署 Qwen3.5-27B 的实战指南，证明 vLLM 已支持 Qwen3 系列（Qwen3.5 属于 Qwen3 系列迭代），这与陈述中‘需查最新版本’的模糊状态相比，提供了更确定的支持证据，但陈述本身逻辑自洽，只是信息滞后，故降级为定性表述。

## Search Query

vLLM Qwen3 support release notes llama.cpp Qwen3 GGUF

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_30296995/article/details/162254873&rut=6b7a1a19cf3ee095b56a4fe040ffd119ad3a5e9e8e2ecef25c6f49b6f28d3d5c', 'type': 'ddg', 'title': 'Qwen3.5-27B+vLLM+Claude-Code本地部署实战指南-CSDN博客'}
- {'url': 'https://bbs.csdn.net/weixin_30308101/article/details/100148108&rut=812111438b7b1a596db2180bf6b8c79c74b84b23e1f06cab2ea8e50b5f7e345b', 'type': 'ddg', 'title': 'vLLM部署Qwen3.5-27B实战：高吞吐低延迟推理全指南'}
