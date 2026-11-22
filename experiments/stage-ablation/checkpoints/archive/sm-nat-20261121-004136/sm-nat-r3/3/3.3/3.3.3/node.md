# N50: LFU 计数器开销对性能的实际影响量化：除了频率老化，LFU 的内存开销（每个对象需存储计数器）会减少可用于缓存对象数据的内存。假设每个计数器占用 4-8 字节

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

LFU 计数器开销对性能的实际影响量化：除了频率老化，LFU 的内存开销（每个对象需存储计数器）会减少可用于缓存对象数据的内存。假设每个计数器占用 4-8 字节，10 万对象占用 0.4-0.8MB，相对于 128GB 可忽略不计。但若采用精确 LFU，需考虑哈希表开销。量化：可用缓存数据内存 C_data = 128GB - N_objects * counter_size。

## Corrected Claim

LFU 计数器开销对性能的实际影响量化：除了频率老化，LFU 的内存开销（每个对象需存储计数器）会减少可用于缓存对象数据的内存。假设每个计数器占用 4-8 字节，10 万对象占用 0.4-0.8MB，相对于 128GB 可忽略不计。但若采用精确 LFU，需考虑哈希表开销。量化：可用缓存数据内存 C_data = 128GB - N_objects * counter_size。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点基于'近似 vs 精确'这一核心维度划分，逻辑正交；涵盖了父节点中提到的两种主要实现方式（CM Sketch 和哈希表）及其对内存 C_data 和性能（误报/抖动）的不同影响，覆盖全面；两者代表了不同的技术权衡点（Trade-off），并非单一参数的简单数值变化，因此不构成冗余。）

## Search Query

LFU memory overhead counter size cache capacity reduction
