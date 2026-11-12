# gpu 新题面 run #2 结果落盘（DONE @~15:40，supersedes `gpu-rerun-results.md`）

> origin: lead (承) · 2026-11-12 ~15:40 · 数据源: `runs-s5-sm-gpu.json`（本次 DONE 覆盖写入，console log `drb-pilot/run-gpu-rerun-console.log` 尾部 "DONE: 153 nodes, 3 rounds"）+ ckpt `checkpoints/sm-gpu-r3.json`。commit 60e96b82。
> ⚠️ **上一份 `gpu-rerun-results.md`（75 records / 34 unique / dup ids / reworks=[]）作废**——它读到的 final JSON 是一次带伤中间态/旧进程产物。本 run 的 final JSON 结构健康，以下数字以本文件为准。L20 报 CC 的两项 P0/P1 据此部分撤销（见 §5）。

## 1. 总量与判定

| 指标 | 值 | 备注 |
|---|---|---|
| 节点数 | 153 records / **153 unique ids** | ✅ **无撞号**（_nid fix 生效） |
| verified 率 | 27.5% (42/153) | 高于 r14 的 38%? 不——r14 是 38%，本次更低；但 degraded 也大幅下降 |
| degraded 率 | 66.7% (102/153) | 仍偏高，主体同病根：检索通道对中文/硬件数值 query 给不出可用源 |
| pending | 6 (3.9%) | ✅ 正常水平（上次 24% 是带伤文件的假象） |
| failed | 3 (2.0%) | — |
| leaks | 0 | ✅ |
| rework_events | **105**（非空） | ✅ 计数恢复；r14 是 91，量级一致 |
| 终止方式 | max_nodes=150 hit → state=rework | console 明确 `[SM] max_nodes=150 hit`；非 stop 收敛退出 |

## 2. 逐轮轨迹（gain 样本补进 P5 CDF 回标池）

| round | n_new | total | gain | S_α' | verified/n_new | frontier | dropped_redundant | edge_types |
|---|---|---|---|---|---|---|---|---|
| 1 | 21 | 27 | 0.968 | 20.39 | 9 | 6 | 0 | cartesian 27 |
| 2 | 43 | 70 | 0.916 | 58.20 | 16 | 21 | 7 | cartesian 64 / quotient 6 |
| 3 | 83 | 153 | 0.892 | 139.61 | 17 | 43 | 10 | cartesian 133 / quotient 20 (13.1% ≤20% ✅) |

三轮 gain 全部 >0.5 且递减（0.968→0.916→0.892），n_new 全部非零 → 本轮 3 个 gain 样本全部可进 P5 CDF 回标池（无需剔除伪值）。累计有效 gain 样本：drb-1×3 + drb-2×2 + gpu(r14)×2 + 本次×3 = **10 个**。

## 3. 与 r14（旧题面含 3s/token）对比

| 项 | r14（旧题面） | 本次 #2（新题面） |
|---|---|---|
| 终止 | max_depth=4 hit, state=rework | max_nodes=150 hit, state=rework |
| nodes | 137 records / 40 unique（带伤） | 153 / 153（健康） |
| verified | 38.0% | 27.5% |
| degraded | 56.9% | 66.7% |
| pending | 3.7% | 3.9% |
| reworks | 91 | 105 |
| leaks | 0 | 0 |

解读：新题面（去掉 3s/token 硬约束）树更大更浅地铺开了（153 vs 137 records），degraded 略升——与白名单 post-filter 方向相反，说明主导因素不是检索质量而是**题面变软后 claim 粒度变细、更多节点落在"逻辑自洽但无外部数值源"区间**（rework reason 抽样全是这个模式）。verified 27.5% 仍是 DRB 类真实数据题的正常水位（drb-1 14.8% / drb-2 1.6%），gpu 题因硬件规格在 wiki/datasheet 有部分公开源而明显更好。

## 4. 遗留问题

1. **上一份带伤文件从哪来**（P2，低优先）：同一 log 文件里先出现 "DONE: 75 nodes" 再出现 "DONE: 153 nodes"，final JSON 被两次覆盖。候选解释：pid 11150 实际跑了两次（第一次中途异常退出写 partial，第二次 resume/重跑完成）或存在两个 writer。不影响本 run 结论，但若 D26 要精确审计启动时间线需要查 launch 记录。
2. **degraded 66.7% 的构成**：rework reason 抽样显示主体是"检索无可用来源"（通道型）而非"claim 本身错"（内容型）——与 L14 三分类中"真·数据缺口"同类。D26 验收时 gpu 题可保留在主验收（claim 粒度匹配 wiki/datasheet 能力范围），degraded 率不作为立项依据（Goodhart 反例纪律）。

## 5. 对 L20（CC 核查请求）的影响

- **A. id 撞号复发（P0）→ 撤销**：本 run 153/153 全唯一，_nid fix 在 gpu 题上同样验证通过。CC 不必再查第二条 id 分配路径（至少本 run 没有证据表明存在）。
- **B. rework_events=[] 矛盾（P1）→ 撤销**：本 run rework_events=105，计数链路正常。上次的空数组是带伤中间态的产物，不是计数 bug。
- **C. pending 24% → 撤销**：本 run pending 3.9%，正常。
- 新增一条给 CC 的信息项：§4.1 的双 DONE 现象，若 CC 有空可顺带核一下 launch 时间线（不阻塞任何事）。

## 6. 下一步

- bench report §2 题目表加 gpu 行（状态 DONE，主验收候选）；§3 补 gpu 节。
- gain 样本池更新到 10 个 → P5 CDF 回标脚本可以写了（不再等"出树补样本"）。
- DRB pilot 主线不变：drb-16 排队，检索通道修复（ddg query 改写 / Perplexity via ego-browser）仍是 Phase 2 核心瓶颈。