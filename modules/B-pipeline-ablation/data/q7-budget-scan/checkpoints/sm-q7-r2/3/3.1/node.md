# N17: 冷数据访问SLA定义：极少访问意味着月度访问频率<1次，可接受延迟为分钟级；云对象存储Standard-IA/Infrequent Access层满足此SLA，

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

冷数据访问SLA定义：极少访问意味着月度访问频率<1次，可接受延迟为分钟级；云对象存储Standard-IA/Infrequent Access层满足此SLA，本地HDD层也满足，但NVMe SSD层存在资源浪费；隐性成本包括：过度配置高性能介质导致的CapEx溢价

## Corrected Claim

冷数据访问SLA定义：极少访问意味着月度访问频率<1次，可接受延迟为分钟级；云对象存储Standard-IA/Infrequent Access层满足此SLA，本地HDD层也满足，但NVMe SSD层存在资源浪费；隐性成本包括：过度配置高性能介质导致的CapEx溢价

## Evidence

父节点级核验未通过：不完备（虽然唯一的子节点在逻辑上自洽且无内部冗余，但它未能覆盖父节点中明确列出的其他关键方面。父节点不仅包含‘NVMe SSD层的资源浪费’和‘CapEx溢价’，还定义了‘SLA标准（月访问<1次，分钟级延迟）’以及‘其他满足SLA的方案（Standard-IA, HDD）’。当前子节点仅量化了单一方案的浪费，缺失了对SLA定义的分解以及其他合规方案（如HDD或云对象存储）的成本/优势对比分析，导致分解不完备。）
