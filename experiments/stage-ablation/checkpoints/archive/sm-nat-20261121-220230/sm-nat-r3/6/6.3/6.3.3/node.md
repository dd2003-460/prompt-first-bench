# N260: HTTP 头部开销对 s_min 的实际影响：典型 HTTP 响应含 200-500 字节头部，若对象有效载荷最小为 1KB，则实际 s_min=1.2-1.5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

HTTP 头部开销对 s_min 的实际影响：典型 HTTP 响应含 200-500 字节头部，若对象有效载荷最小为 1KB，则实际 s_min=1.2-1.5KB，对 E[s] 影响 <1%，可忽略；但若考虑压缩后大小，s_min 可能降至 500 字节，需区分原始大小与传输大小口径。

## Corrected Claim

HTTP 头部开销对 s_min 的实际影响：典型 HTTP 响应含 200-500 字节头部，若对象有效载荷最小为 1KB，则实际 s_min=1.2-1.5KB，对 E[s] 影响 <1%，可忽略；但若考虑压缩后大小，s_min 可能降至 500 字节，需区分原始大小与传输大小口径。

## Evidence

先验知识/题面给定，逻辑校验通过：HTTP头部200-500字节与1KB载荷相加得1.2-1.5KB符合算术逻辑，且对期望值影响<1%的结论在统计上合理；压缩后大小变小的描述符合工程常识。
