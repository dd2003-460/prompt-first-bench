# N112: 自建POP BGP路由切换延迟：BGP路由收敛时间取决于IGP收敛（OSPF/IS-IS，通常<1秒）+ BGP路由传播（多跳AS间，每跳1-5秒）+ 客户端D

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N36

## Claim

自建POP BGP路由切换延迟：BGP路由收敛时间取决于IGP收敛（OSPF/IS-IS，通常<1秒）+ BGP路由传播（多跳AS间，每跳1-5秒）+ 客户端DNS缓存，总切换时间 = $T_{igp} + N_{hops} \times T_{bgp\_prop} + T_{dns\_cache}$，需量化10个POP间的AS跳数及典型收敛时间

## Corrected Claim

自建POP BGP路由切换延迟：BGP路由收敛时间取决于IGP收敛（OSPF/IS-IS，通常<1秒）+ BGP路由传播（多跳AS间，每跳1-5秒）+ 客户端DNS缓存，总切换时间 = $T_{igp} + N_{hops} \times T_{bgp\_prop} + T_{dns\_cache}$，需量化10个POP间的AS跳数及典型收敛时间

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的四个独立变量（$T_{igp}$, $N_{hops}$, $T_{bgp\_prop}$, $T_{dns\_cache}$），彼此之间无逻辑重叠或矛盾。它们共同构成了总延迟公式的所有组成部分，覆盖了父节点要求量化的所有关键方面（IGP收敛、BGP传播、跳数、DNS缓存）。各子节点提供的是不同物理层/协议层的具体参数范围，而非同一参数的重复取值，因此不存在冗余。）
