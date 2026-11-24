# #53 理论路线结果 (surface-vs-deep 判断修正)

> 2026-11-24 · 纯理论闭式计算 (spec + workload 先验 → 表面/深层判断), 无 LLM/实验.
> 脚本 idea53-theory-flip.py · 数据 idea53-theory-flip.json · 预注册锚 GOAL.md §0.5 @ eb1b0598c.

## 模型 (D 纠正后)
- **浅层枚举** = 表面判断: 假设 rate 全相等 → 时间∝workload → 瓶颈=主导 workload 类.
- **深层微架构判断** = 真实 rate ratio → 时间占比 t_i=f_i/rate_i → 瓶颈=argmax t_i.
- **深层信息增益** = 深层对表面判断的修正量 (方向修正 flip + 粒度细化 time shift).
- 这正是 D 两例: 5090 表面"非瓶颈"→微架构"慢40%"(方向修正) / T5000 表面"可能算力"→"FP16 78%+带宽暗杀"(粒度细化).

## 验证锚 (model_ok=True, 全复现)
| 例 | 期望 | 计算 | 匹配 |
|---|---|---|---|
| T5000 50/50 FP16/FP4 | FP16 占 80% | 0.800 | ✓ |
| T5000 70/30 | FP16 占 63% | 0.632 | ✓ |
| 5090 标量40%+issue砍半 | 标量40%, 慢40% | scal=0.400, T1/T0=1.400 | ✓ |

## 主结果 (每硬件, N=40000 workload 采样)
| 硬件 | rate-ratio | flip(判错率) | time shift | 典型翻转 |
|---|---|---|---|---|
| 4090 | 287.4 | 0.563 | 0.2307 | bw→fp4, scalar→fp4 |
| 5090 | 51.9 | 0.527 | 0.2004 | scalar→fp16, bw→fp16 |
| A100 | 44.3 | 0.556 | 0.2183 | scalar→fp4, bw→fp4 |
| T5000 | 9.9 | 0.434 | 0.1655 | scalar→fp16, scalar→bw |

## 对照臂
- **占位硬件 (rate 全=1)**: flip=0.0000, shift=0.0000 (恰好 0). 证明修正量**纯粹来自 rate-ratio**, 非 workload 转发 → 解转发平凡性.

## 生死线判定
- **主 claim (深层微架构判断 > 浅层枚举): 成立.** 浅层枚举在 43-56% workload 上判错瓶颈类型, 深层修正才是判断承重部分; flat 对照=0 证明深层信息=微架构 rate-ratio (非转发).
- **次级假设 (修正量随 rate-ratio 极端度单调升): 部分.** T5000(最温和)修正最小, 4090(最极端)最大, 但 A100(0.218)>5090(0.200) 打破严格单调 → 哪个组件主导比 max/min ratio 更重要. 非线性放大成立但非单调, 论文需改措辞为"修正量与 rate-ratio 结构相关, 非仅极端度".

## 局限
- flip/shift 是可解释的每节点得分, 非严格 MI; 论文需补形式互信息 H(surface)-H(surface|deep).
- 4090/A100 无原生 FP4, fp4 rate 用 0.5×fp16 推 [待核验].
- workload 先验=Dirichlet(1,1,1,1) (simplex 均匀), 真实 LLM 推理 workload 偏置未建模.
