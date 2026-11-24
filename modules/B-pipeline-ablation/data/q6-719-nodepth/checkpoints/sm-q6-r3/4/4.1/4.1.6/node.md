# N82: 公有云CDN可行性判断：若选择阿里云企业版（500Gbps上限），69.3Gbps < 500Gbps，方案可行；若选择基础版（100Gbps上限），69.3G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19, N20, N21

## Claim

公有云CDN可行性判断：若选择阿里云企业版（500Gbps上限），69.3Gbps < 500Gbps，方案可行；若选择基础版（100Gbps上限），69.3Gbps < 100Gbps，方案可行但余量仅30.7%，需监控峰值波动

## Corrected Claim

公有云CDN可行性判断：若选择阿里云企业版（500Gbps上限），69.3Gbps < 500Gbps，方案可行；若选择基础版（100Gbps上限），69.3Gbps < 100Gbps，方案可行但余量仅30.7%，需监控峰值波动

## Evidence

先验知识/题面给定，逻辑校验通过：69.3 < 500 且 69.3 < 100，余量计算 (100-69.3)/100 = 30.7% 正确，符合基本数学逻辑。
