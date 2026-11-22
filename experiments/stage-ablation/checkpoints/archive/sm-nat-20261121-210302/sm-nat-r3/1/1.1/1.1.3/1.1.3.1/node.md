# N97: 工作点A（内存受限）：设定 S_max = 100MB，确保单个对象不占用超过 0.08% 的缓存容量（100MB/128GB），防止单一大对象独占内存导致 L

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

工作点A（内存受限）：设定 S_max = 100MB，确保单个对象不占用超过 0.08% 的缓存容量（100MB/128GB），防止单一大对象独占内存导致 LRU 失效，适用于高并发小文件场景。

## Corrected Claim

工作点A（内存受限）：设定 S_max = 100MB，确保单个对象不占用超过 0.08% 的缓存容量（100MB/128GB），防止单一大对象独占内存导致 LRU 失效，适用于高并发小文件场景。

## Evidence

先验知识/题面给定，逻辑校验通过：100MB/128GB ≈ 0.076%，四舍五入为0.08%符合数学事实；限制单对象大小以防止LRU失效是合理的缓存设计策略。
