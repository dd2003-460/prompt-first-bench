# N628: P99(T_proc_edge) 对缓存命中率的敏感性：当缓存命中率 H < 0.95 时，P99 处理时间将包含部分回源预处理逻辑（如 302 重定向或异步回

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N206

## Claim

P99(T_proc_edge) 对缓存命中率的敏感性：当缓存命中率 H < 0.95 时，P99 处理时间将包含部分回源预处理逻辑（如 302 重定向或异步回源触发），导致 P99(T_proc_edge) 从 7.5ms 上升至 12-15ms；确保 H > 0.99 是维持 7.5ms 基准的前提条件。

## Corrected Claim

P99(T_proc_edge) 对缓存命中率的敏感性：当缓存命中率 H < 0.95 时，P99 处理时间将包含部分回源预处理逻辑（如 302 重定向或异步回源触发），导致 P99(T_proc_edge) 从 7.5ms 上升至 12-15ms；确保 H > 0.99 是维持 7.5ms 基准的前提条件。

## Evidence

先验知识/题面给定，逻辑校验通过
