# r14 校准分析（structural test 修正版）
> origin: cc-experimentalist · 2026-11-12 · 数据源: `runs-s5-sm-gpu.json` (DONE: 137 nodes, state=rework, leaks=None, reworks=91)

## 1. 总量
- 节点数: **137** (r13 基线 70 → r14 中间 r2 ckpt 59 → r14 final 137)- 轮数: 3 (max_depth=4 hit 后停)- leaks: None | rework events: 91
## 2. Level 分布
| level | nodes |
|---|---|
| L1 | 5 |
| L2 | 17 |
| L3 | 37 |
| L4 | 78 |

## 3. Edge 类型分布（核心指标：r13 quotient 90% 被 hack）
| edge | nodes | % |
|---|---|---|
| cartesian | 120 | 87.6% |
| quotient | 17 | 12.4% |
| stochastic | 0 | 0.0% |

### 3a. Level × Edge 交叉表
| level \ edge | cartesian | quotient | stochastic |
|---|---|---|---|
| L1 | 5 | 0 | 0 |
| L2 | 14 | 3 | 0 |
| L3 | 30 | 7 | 0 |
| L4 | 71 | 7 | 0 |

## 4. Status 分布（degraded 率是优化信号）
| status | nodes | % |
|---|---|---|
| degraded | 78 | 56.9% |
| verified | 52 | 38.0% |
| pending | 5 | 3.6% |
| failed | 2 | 1.5% |

### 4a. Level × Status
| level \ status | verified | degraded | pending | failed |
|---|---|---|---|---|
| L1 | 0 | 0 | 5 | 0 |
| L2 | 7 | 9 | 0 | 1 |
| L3 | 13 | 24 | 0 | 0 |
| L4 | 32 | 45 | 0 | 1 |

## 5. Source 分布
| source | nodes |
|---|---|
| knowledge | 75 |
| search | 50 |
| given | 12 |

## 6. 逐轮轨迹
| round | n_new | total | gain | S_α' | verified/n_new | streak |
|---|---|---|---|---|---|---|
| 1 | 17 | None | 0.971 | None | 7/17 | None |
| 2 | 37 | None | 0.905 | None | 13/37 | None |
| 3 | 78 | None | 0.892 | None | 32/78 | None |

## 7. Rebuild 检查：rework 事件抽样
共 91 条 rework 事件。前 8 条：
- N? N7 attempt=1 :: KV Cache动态显存公式：每token占用 = 2 * num_kv_heads * head_ — 逻辑校验通过（公式及量级估算正确：2*8*128*32768*2bytes ≈ 16GB），但参考来源全部缺失，无法进行
- N? N8 attempt=1 :: 推理带宽下限推导：单流延迟<3s/token要求有效显存带宽 > (模型激活读取量+KV读写量)/3 — 逻辑量级校验合理（27B W4权重约13.5GB，加上KV缓存及读写开销，3秒延迟确实需要TB/s级别带宽），但检索无可
- N? N9 attempt=1 :: 互联拓扑带宽阈值：单卡方案要求GPU HBM/DDR带宽独立满足N8；多卡方案（如2x消费卡）要求P — 逻辑校验通过（PCIe Gen4 x16带宽~32GB/s及0.5TB/s互联阈值符合当前硬件常识），但本轮检索无可用来
- N? N10 attempt=1 :: 候选集-消费级旗舰：NVIDIA RTX 4090 (24GB GDDR6X, ~1TB/s带宽,  — 来源[1][2][3]直接支持RTX 4090的24GB GDDR6X规格，但所有参考来源均未包含RTX 5090的信息
- N? N12 attempt=1 :: 候选集-非典型/统一内存平台：AMD EPYC + Radeon Pro W7900 (48GB V — 逻辑自洽：AMD EPYC + Radeon Pro W7900 及 Mac Studio M2/M3 Ultra 的硬
- N? N13 attempt=1 :: 精度工作点1-高质低效(BF16): 质量损失≈0% (基准)，但显存占用55.6GB+KV，仅H1 — 逻辑自洽（BF16显存占用约为FP32的50%，符合物理直觉；H100/A100 80GB显存充足而4090/5090显
- N? N7 attempt=1 :: 工作点B（多卡消费级集群）：TCO_Nyr = N * (P_card_low + P_infra( — 逻辑自洽（量纲正确，TCO构成合理），但source标记为search且本轮检索无可用来源，无法提供外部证据支持具体的$
- N? N8 attempt=1 :: 通信开销侵蚀量化：有效吞吐量效率 η_eff = 1 / (1 + α * L_layer * D_ — 逻辑校验通过：公式量纲自洽（时间/时间），将通信延迟叠加到计算时间上符合分布式训练基本直觉；但外部核验显示本轮检索无可用

## 8. 判读（对照任务书阈值）
- degraded 率 = 56.9% （任务书警戒线 >40%）→ ⚠️ 超线，需诊断- quotient 占比 = 12.4% （r13 为 90%，方向已反转）- max_depth=4 即停：树在深度 4 处截断——是机制生效还是提前封顶？见 §9。

## 9. 待 Lead 判断的问题
1. **state=rework 终止**：run 结束时状态是 rework 而非 STOP——是 max_depth 触发的正常退出路径吗？（代码里 max_depth hit 直接 break，state 停在当时值）2. **reworks=91 偏高**：91 次 rework 事件 / 137 节点 ≈ 每 1.5 节点一次返工。是核验过严（verify_threshold 0.6），还是检索通道（arXiv DDG）对 gpu 题命中率低？需要看 rework 失败原因分布（§7 只抽了前 8 条）。3. **max_depth=4 是否够**：gpu 题的 TCO/微架构下钻按 Decision 8 至少需要 L4-L5；当前 depth cap 可能系统性砍掉叶子层证据。调 max_depth 属于参数改动，走三问提案。