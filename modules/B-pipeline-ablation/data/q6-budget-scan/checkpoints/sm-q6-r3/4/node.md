# N13: 日均请求量估算：基于日均下载2TB和假设的平均对象大小（如图片500KB，短视频5MB），推算日均请求数约为 4,000,000 至 400,000 次，用于后

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

日均请求量估算：基于日均下载2TB和假设的平均对象大小（如图片500KB，短视频5MB），推算日均请求数约为 4,000,000 至 400,000 次，用于后续成本归一化分母。

## Corrected Claim

日均请求量估算：基于日均下载2TB和假设的平均对象大小（如图片500KB，短视频5MB），推算日均请求数约为 4,000,000 至 400,000 次，用于后续成本归一化分母。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点2和子节点3存在严重逻辑冗余和重复计算。子节点2已经计算出了具体的加权平均大小（950KB）和对应的请求量逻辑，而子节点3又重复列举了不同假设下的请求量计算，且子节点2中的公式推导与子节点1的定义部分重叠。此外，子节点1是定义公式，子节点2和3是具体数值代入，三者界限模糊，未做到正交（即各自独立且互不包含）。）

## Retrieval Sources

- {'url': 'https://sdeoffer.com/zh/system-design/capacity-calculator/&rut=a3ada8bc8f4926e6812e5e93cb2a76df051503da2b88a48e9c5b438b22fffd96', 'type': 'ddg', 'title': '系统设计容量估算器：QPS、带宽与存储计算 | sdeoffer'}
- {'url': 'https://ask.csdn.net/questions/9632827&rut=1e67692a3dc7e77467f75bf08f3aaf838a03ae15f23185de641920d1ae09b621', 'type': 'ddg', 'title': '如何根据日均访问量和页面大小估算所需服务器带宽？_编程语言-csdn问答'}
- {'url': 'https://cloud.tencent.com/developer/article/2460147&rut=c4e3e79b4b4bd21d367b555ca16ef11a17812705e48d6ad39c1d5fb2fa19f12e', 'type': 'ddg', 'title': '如何精确计算cdn的并发流量?-腾讯云开发者社区-腾讯云'}
