# N145: llama.cpp 在 TP=2 (多卡) 模式下通常采用层拆分或数据并行策略，而非标准的 KV Head 拆分，导致每卡仍需存储全量 KV Cache (51

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

llama.cpp 在 TP=2 (多卡) 模式下通常采用层拆分或数据并行策略，而非标准的 KV Head 拆分，导致每卡仍需存储全量 KV Cache (512 MB BF16) 或仅拆分部分层，需查阅其 multi-GPU 文档确认具体分布逻辑。

## Corrected Claim

llama.cpp 在多卡模式下的具体 KV Cache 分布策略（如层拆分、数据并行或 KV Head 拆分）取决于版本和配置，需查阅其官方文档或源码确认，不能一概而论为仅采用层拆分。

## Evidence

[质询]该陈述属于具体的软件实现细节（经验事实），且断言 llama.cpp 在 TP=2 下“通常”采用层拆分而非 KV Head 拆分，这与部分社区认知或特定版本行为可能存在偏差，且缺乏来源支持以确认其“通常”行为的准确性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

llama.cpp multi-GPU tensor parallel KV cache distribution strategy
