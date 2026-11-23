# N192: 写流量不占用边缘缓存读容量的前提条件：边缘节点采用 W-TinyLFU 或类似缓存算法时，写请求仅触发源站写入，不污染读缓存，除非配置了 Write-Throu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

写流量不占用边缘缓存读容量的前提条件：边缘节点采用 W-TinyLFU 或类似缓存算法时，写请求仅触发源站写入，不污染读缓存，除非配置了 Write-Through 策略

## Corrected Claim

写流量不占用边缘缓存读容量的前提条件：边缘节点采用 W-TinyLFU 或类似缓存算法时，写请求仅触发源站写入，不污染读缓存，除非配置了 Write-Through 策略

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN cache pollution write traffic impact
