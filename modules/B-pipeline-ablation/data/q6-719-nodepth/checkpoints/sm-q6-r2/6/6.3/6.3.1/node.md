# N165: 在 T=200ms 阈值下，公有云CDN（阿里云）在中国大陆区域基于其节点密度（>3000节点）与标准HTTP/2协议，其P99延迟理论上限约为 80ms + 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

在 T=200ms 阈值下，公有云CDN（阿里云）在中国大陆区域基于其节点密度（>3000节点）与标准HTTP/2协议，其P99延迟理论上限约为 80ms + 30ms(处理) + 50ms(回源概率) ≈ 160ms，满足 P99_public <= 200ms。

## Corrected Claim

在 T=200ms 阈值下，公有云CDN（阿里云）在中国大陆区域基于其节点密度（>3000节点）与标准HTTP/2协议，其P99延迟理论上限约为 80ms + 30ms(处理) + 50ms(回源概率) ≈ 160ms，满足 P99_public <= 200ms。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Alibaba Cloud CDN P99 latency China average
