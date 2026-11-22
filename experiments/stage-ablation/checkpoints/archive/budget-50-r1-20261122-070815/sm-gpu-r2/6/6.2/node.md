# N128: Qwen3-27B 采用混合注意力架构（部分层线性注意力），若存在线性注意力层，其 KV Cache 占用为 0，需确认 64 层中全注意力层数 N_full_

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

Qwen3-27B 采用混合注意力架构（部分层线性注意力），若存在线性注意力层，其 KV Cache 占用为 0，需确认 64 层中全注意力层数 N_full_attn 与线性注意力层数 N_linear_attn 的具体比例，以修正 KV Cache 总显存公式为 2 * N_full_attn * 4 * 128 * 32768 * dtype_size

## Corrected Claim

Qwen3-27B 采用混合注意力架构（部分层线性注意力），若存在线性注意力层，其 KV Cache 占用为 0，需确认 64 层中全注意力层数 N_full_attn 与线性注意力层数 N_linear_attn 的具体比例，以修正 KV Cache 总显存公式为 2 * N_full_attn * 4 * 128 * 32768 * dtype_size

## Evidence

来源[1][2][3]一致确认Qwen3-27B（文中称Qwen3.8-27B）采用64层架构，其中48层为线性注意力（Gated DeltaNet），16层为全注意力，直接支持了N_full_attn=16的修正公式前提。

## Search Query

Qwen3-27B hybrid attention linear attention layers ratio

## Retrieval Sources

- {'url': 'https://happyrock.cloud/zh/blog/2026-08-16_qwen3.8-27b/&rut=a7d764fc762910ca9e2b13877451933cafd0da78e6b8c4cd0a98654ddeda2997', 'type': 'ddg', 'title': 'Qwen3.8-27B混合注意力架构深度解析：48层Gated DeltaNet + 16层Attention如何让270亿参数模型跑在消费级 ...'}
- {'url': 'https://blog.csdn.net/weixin_29057237/article/details/163968271&rut=3ef765ea3833151d0fd0ad1ffb7fe768854a9c7909e748c39d4175d97c439924', 'type': 'ddg', 'title': 'Qwen3.8 27B架构解析：线性注意力与混合设计如何实现百万级上下文-CSDN博客'}
- {'url': 'https://blog.csdn.net/liu8485/article/details/164724304&rut=b7c08168b53b511f68674c156d96aa9524b8914fb42107a4a9b9b614dca3f054', 'type': 'ddg', 'title': 'Qwen3.8-27B 混合注意力拆解：48 层线性 + 16 层全注意力，75 万 token KV 显存打到 1/4'}
