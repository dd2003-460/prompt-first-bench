# N144: 单台边缘存储成本 C_storage = 本地SSD容量(2TB * ¥1.5/GB) = ¥3,072，假设每个POP点配置2TB本地SSD用于热点缓存。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

单台边缘存储成本 C_storage = 本地SSD容量(2TB * ¥1.5/GB) = ¥3,072，假设每个POP点配置2TB本地SSD用于热点缓存。

## Corrected Claim

单台边缘存储成本 C_storage = 本地SSD容量(2TB * ¥1.5/GB) = ¥3,072，假设每个POP点配置2TB本地SSD用于热点缓存。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点代表了不同容量档位的工作点，彼此互斥且覆盖从低到高不同场景，符合正交性和完备性要求；虽然结构相似，但属于典型的多档位对比分析，不宜压缩为单一变量，因为每个档位对应不同的业务场景（命中率、缓存类型）和成本效益权衡，保留为独立子节点有助于清晰表达决策空间。）
