# PFB 管道组件状态 Checklist

**用途**: 每轮开始时对照此表，确认哪些组件已修、哪些未验、哪个是当前瓶颈。
**更新规则**: 每次 commit / 验证完成后更新对应行的日期和状态。

## 管道组件（P1→P2/P3→P4 链）

| # | 组件 | 文件 | 最后修复 | 最后验证 | 状态 | 备注 |
|---|------|------|----------|----------|------|------|
| 1 | P1 分解 prompt (rules 1-9) | s5_pipeline.py L63-130 | ac3618b2 (11-09) | ❌ 未重跑 nat | 🔴 待验证 | rule 8 子问全覆盖 + rule 9 定量承诺+分布参数实例化 |
| 2 | P1 max_tokens + 截断重试 | s5_pipeline.py | (v13 r5 fix) | v13 r6-r10 无截断 | 🟢 OK | r5 后未再出现 |
| 3 | P2 检索: wiki extracts API | research_hook.py `_wiki_search` | 061759d0 (11-09) | replay 15 nodes | 🟡 部分 | snippet ~1000ch，但 P3 仍说"来源无关" |
| 4 | P2 检索: DDG→Bing fallback | research_hook.py `_ddg_search` | 061759d0 (11-09) | 单测 10 results | 🟢 OK | cn.bing.com setlang=en&cc=us |
| 5 | P2 检索: arXiv channel | research_hook.py | — | 非学术题 0 results | ⚪ 已知限制 | GPU 价格/电费类事实查不到，靠其他通道补 |
| 6 | P2 检索: local corpus gate | research_hook.py `_local_corpus_search` | f92fa19f (11-09) | nat→0, gpu→2 | 🟢 OK | qid 直判，非 gpu 域返回 [] |
| 7 | P2 检索: sources_block cap | s5_pipeline.py | 061759d0 (11-09) | — | 🟢 OK | 400→800ch |
| 8 | P3 验证逻辑 | s5_pipeline.py P3 prompt | 未改（用户要求不改） | replay: 2up/2down/11same | 🟡 瓶颈上游 | P3 靠第一性原理 rubber-stamp，本身没错；问题是喂给它的 source 质量 |
| 9 | P4 综合 prompt (rules 1-7) | s5_pipeline.py L185-210 | d49d44e0 (11-09) | ❌ 未重跑 nat | 🔴 主瓶颈 | rule 5 anti-hedging + rule 6 node-to-answer bridge，均未验证 |
| 10 | Judge (coverage scoring) | judge_v2_depth.py | — | S0-nat 391 reps 稳定 | 🟢 OK | 同 judge 对比有效 |

## 当前数据状态 (2026-11-09 ~14:00 CST)

| Run | 进度 | 关键指标 | 目标 |
|-----|------|----------|------|
| v13 GPU ×50 | 10/50 | depth mean=0.379, cov=0.141 | depth≥0.50 |
| s5-prod soc ×100 | 28/100 | cov mean=0.898 | ≥0.85 ✅ 已达标 |
| s5-prod nat ×100 (旧代码) | 100/100 | cov mean=0.533 | < 0.634 ❌ |
| **nat 重跑 (新代码)** | **未启动** | — | **cov≥0.634** |

## 下一步（按优先级）

1. **等 v13 (11/50) + soc (30/100) 跑完**（~1.5h）
2. **启动 nat 100-rep 重跑**（用 ac3618b2 后的代码，含全部 6 个 fix）— Phase 1→Phase 1-validate 门禁
3. nat 重跑结果 → mean cov vs 0.634 → 过则 advance stage
4. 如果仍 < 0.634 → 第三轮 per-node audit（这次看 rule 8/9 是否生效：请求命中率节点出现率、分布参数实例化率）

## p4/p2 miss 精确归因（2026-11-09 第二轮 audit）

| Gold point | Miss 数 | 根因分布 | 对应 fix |
|---|---|---|---|
| p4 口径分离 | 40 | 88% 无请求命中率节点(P1没拆) / 80%答案只提字节不提请求 / 69%有公式节点却hedge | rule 8 + rule 5 anti-hedge + rule 6 bridge |
| p2 头部集中度 | 40 | 72% 无累积质量节点(P1没给参数) / 28%有节点但P4没用 | rule 9 分布参数实例化 + rule 6 bridge |

**结论**: 主瓶颈是 P1 分解不完整（缺节点）> P4 综合不力（有节点不用）> 检索质量。
三个 fix 分别打三个层：P1 rule 8/9（源头）、P4 rule 5/6（出口）、retrieval（中间）。

## "漏风"诊断（2026-11-09）

系统反复失效的结构性原因：
1. Goal 是 markdown 不是活状态机 → 压缩后丢细节 → **已修：注册进 stage-gate**
2. 修复散弹式，无组件级 checklist → **已修：本文件**
3. 无断点恢复协议 → 进程挂/session 断后靠 summary 碎片恢复 → **待修：写 recovery 脚本**
## Round-3 结果（2026-11-09）

### v13 GPU 50-rep 最终

| 指标 | 值 | target | 判定 |
|------|-----|--------|------|
| depth mean | 0.3947 (std 0.0419) | ≥0.50 | **FAIL** (+0.105) |
| cov mean | 0.2141 | — | — |
| valid reps | 33/34 | — | r5 decompose empty |
| wall mean | 581s (9.7min) | — | — |

对比：v8=0.354, v12=0.377, v13=0.395。三个版本 depth 都卡在 ~0.38-0.40，说明 P1.5 gap_check 加 generic node 的策略不够——需要 per-candidate spec table。

**新 fix**: P1 rule 9b（硬件 spec-table 强制展开 + TCO 公式分解）已提交。待 v14-gpu 验证。

### nat-v14 早期信号（35/100，502 中断后补跑中）

| 指标 | 旧 S5 (pre-fix) | nat-v14 (35 reps) | S0 baseline |
|------|----------------|-------------------|-------------|
| cov mean | 0.5350 | **0.6048** | 0.6338 |
| gap vs S0 | -0.1008 | **-0.0290** | — |

6 个 fix 提升了 +0.070，从"比 S0 差 10 点"缩到"差 3 点"。方向正确但还差一口气。补跑 65 reps 后看完整均值。

### 当前状态

- nat-v14 补跑：PID 91250, workers=1, 预计 ~10h
- v14-gpu 未启动（等 nat-v14 完成或 8787 负载降低）
- Arena T52：撞车调研进行中
