# N136: HTTP解析与缓存查找延迟 T_lookup 取决于缓存索引结构：LRU链表查找约为 O(1) 即 <0.1ms，哈希表查找约为 O(1) 即 <0.1ms，若

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

HTTP解析与缓存查找延迟 T_lookup 取决于缓存索引结构：LRU链表查找约为 O(1) 即 <0.1ms，哈希表查找约为 O(1) 即 <0.1ms，若涉及复杂正则匹配或URI规范化则增加 0.5-2ms。

## Corrected Claim

HTTP解析与缓存查找延迟 T_lookup 取决于缓存索引结构：LRU链表查找约为 O(1) 即 <0.1ms，哈希表查找约为 O(1) 即 <0.1ms，若涉及复杂正则匹配或URI规范化则增加 0.5-2ms。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN cache lookup latency microseconds Nginx
