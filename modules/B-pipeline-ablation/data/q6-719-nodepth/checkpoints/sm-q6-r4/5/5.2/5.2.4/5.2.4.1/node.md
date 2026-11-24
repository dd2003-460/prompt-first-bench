# N283: 公有云边缘节点本地处理延迟 L_edge_cloud = L_dns + L_tcp + L_processing，其中 L_dns ≈ 5-10ms，L_tc

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

公有云边缘节点本地处理延迟 L_edge_cloud = L_dns + L_tcp + L_processing，其中 L_dns ≈ 5-10ms，L_tcp ≈ 2-5ms（RTT优化），L_processing ≈ 1-3ms，合计 L_edge_cloud ≈ 8-18ms。

## Corrected Claim

公有云边缘节点本地处理延迟 L_edge_cloud = L_dns + L_tcp + L_processing，其中 L_dns ≈ 5-10ms，L_tcp ≈ 2-5ms（RTT优化），L_processing ≈ 1-3ms，合计 L_edge_cloud ≈ 8-18ms。

## Evidence

先验知识/题面给定，逻辑校验通过：DNS解析(5-10ms)、TCP握手优化后(2-5ms)及边缘节点本地处理(1-3ms)的量级符合网络工程常识，且算术求和(8-18ms)正确。

## Search Query

CDN edge node latency breakdown DNS TCP processing
