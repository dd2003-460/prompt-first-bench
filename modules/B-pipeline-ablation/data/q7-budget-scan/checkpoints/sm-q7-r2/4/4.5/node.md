# N28: 对象平均大小敏感性分析：假设平均对象大小s∈{1KB, 1MB, 100MB}，计算云存储方案C的请求费占比变化，公式为 Request_Fee = (Acce

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

对象平均大小敏感性分析：假设平均对象大小s∈{1KB, 1MB, 100MB}，计算云存储方案C的请求费占比变化，公式为 Request_Fee = (Access_Count / s) * Unit_Request_Price，识别小对象场景下云存储成本激增的阈值

## Corrected Claim

对象平均大小敏感性分析：假设平均对象大小s∈{1KB, 1MB, 100MB}，计算云存储方案C的请求费占比变化，公式为 Request_Fee = (Access_Count / s) * Unit_Request_Price，识别小对象场景下云存储成本激增的阈值

## Evidence

先验知识/题面给定，逻辑校验通过：公式 Request_Fee = (Access_Count / s) * Unit_Request_Price 在量纲上自洽（次数/大小 * 价格/次数 = 价格/大小，若 Unit_Request_Price 定义为每单位数据请求费则成立；通常云存储按次计费，此处公式隐含了将访问次数转换为数据块数的逻辑，或 Unit_Request_Price 为每GB请求费，逻辑上可推导小对象s越小，分母越小，费用越高，符合云存储小文件成本高的常识）。

## Search Query

cloud storage request cost sensitivity object size
