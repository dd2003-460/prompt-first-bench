# N199: 每点服务器数量(10台)需根据单节点带宽处理能力与总流量需求验证：单台服务器带宽上限为10Gbps，10台总带宽为100Gbps，而日均2TB下载流量峰值仅约2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N62

## Claim

每点服务器数量(10台)需根据单节点带宽处理能力与总流量需求验证：单台服务器带宽上限为10Gbps，10台总带宽为100Gbps，而日均2TB下载流量峰值仅约23MB/s (0.184Gbps)，10台服务器严重过剩；实际所需服务器数量 = 峰值带宽需求(0.184Gbps) / 单台有效带宽(5Gbps) ≈ 0.04台，即1台服务器即可承载，10台假设存在巨大冗余

## Corrected Claim

每点服务器数量(10台)需根据单节点带宽处理能力与总流量需求验证：单台服务器带宽上限为10Gbps，10台总带宽为100Gbps，而日均2TB下载流量峰值仅约23MB/s (0.184Gbps)，10台服务器严重过剩；实际所需服务器数量 = 峰值带宽需求(0.184Gbps) / 单台有效带宽(5Gbps) ≈ 0.04台，即1台服务器即可承载，10台假设存在巨大冗余

## Evidence

先验知识/题面给定，逻辑校验通过：2TB/天平均速率约23MB/s，峰值按常规系数估算远低于单台服务器带宽，10台服务器确实存在巨大冗余，计算逻辑自洽。

## Search Query

CDN edge node server sizing bandwidth requirement 2TB daily
