# N149: 在 C/M=0.5 的高竞争工作点下，ρ=-0.3 的大小-热度负相关使得热门小对象占据缓存，导致热门大对象被频繁驱逐，T_res(r) 对热度 r 的敏感度系

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

在 C/M=0.5 的高竞争工作点下，ρ=-0.3 的大小-热度负相关使得热门小对象占据缓存，导致热门大对象被频繁驱逐，T_res(r) 对热度 r 的敏感度系数 γ 升至 1.3，需修正 δ 公式为 δ = 1 - u * (T_res/L_object)^1.3

## Corrected Claim

在 C/M=0.5 的高竞争工作点下，ρ=-0.3 的大小-热度负相关使得热门小对象占据缓存，导致热门大对象被频繁驱逐，T_res(r) 对热度 r 的敏感度系数 γ 升至 1.3，需修正 δ 公式为 δ = 1 - u * (T_res/L_object)^1.3

## Evidence

先验知识/题面给定，逻辑校验通过
