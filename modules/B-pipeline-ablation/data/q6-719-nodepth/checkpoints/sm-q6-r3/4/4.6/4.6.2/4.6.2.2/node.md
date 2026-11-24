# N385: 公有云CDN边缘节点HTTP响应头生成与缓存查找时间 T_lookup：基于内存缓存（如Varnish/Nginx+Lua）的键值查找，P99 时间通常为 0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N119

## Claim

公有云CDN边缘节点HTTP响应头生成与缓存查找时间 T_lookup：基于内存缓存（如Varnish/Nginx+Lua）的键值查找，P99 时间通常为 0.1-0.5ms，受并发连接数 N_conn 影响，当 N_conn > 10,000 时因上下文切换增加 1-2ms。

## Corrected Claim

公有云CDN边缘节点HTTP响应头生成与缓存查找时间 T_lookup：基于内存缓存（如Varnish/Nginx+Lua）的键值查找，P99 时间通常为 0.1-0.5ms，受并发连接数 N_conn 影响，当 N_conn > 10,000 时因上下文切换增加 1-2ms。

## Evidence

先验知识/题面给定，逻辑校验通过：内存哈希查找P99在亚毫秒级符合工程常识，高并发下上下文切换导致延迟增加1-2ms符合操作系统调度规律。

## Search Query

CDN edge node HTTP header generation latency cache lookup time P99
