# gpu 新题面 run 结果落盘（无 3s/token 硬约束版，DONE @14:30）

> origin: lead (承) · 2026-11-12 ~14:45 · **⚠️ SUPERSEDED by `gpu-rerun2-results.md`（~15:40）**——本文件读到的 final JSON 是带伤中间态（75 records / dup ids / reworks=[]），随后同一 run 完成并覆盖写出健康 final JSON（153/153 unique, reworks=105）。本文件仅作历史对照样本保留，数字一律以 gpu-rerun2-results.md 为准。
> ⚠️ **撞号伤复发**：75 records / **34 unique ids**（12 个 id 重复，N19–N26 各 ×5）。CC C3 的 `_nid` 全局计数器修复在 drb-1/drb-2 上验证过（169/169、62/62 全唯一），但本 run 仍出现跨 level 撞号——要么 pid 11150 启动时未带 fix commit，要么存在第二条 id 生成路径。已报 CC（L20）。**按 L8 先例：本文件整体只作历史对照样本，D26 验收与下游引用一律文本匹配，不查 id。**

## 1. 总量与判定

| 指标 | records | unique | 备注 |
|---|---|---|---|
| 节点数 | 75 | **34** | 撞号伤 + r2 零新增双重因素 |
| verified 率 | 45.3% (34/75) | — | 比 r14 的 38% 高，但 degraded 同样偏高 |
| degraded 率 | 30.7% (23/75) | — | 低于 r14 的 56.9%（白名单 post-filter 14:11 后生效，检索质量有改善的迹象，样本小不下结论） |
| pending | 18 (24%) | — | 占比异常高——r2 停在前线未核验 |
| leaks | 0 | — | ✅ |
| rework_events | **[] 空** | — | ⚠️ r14 是 91 次；本轮日志里 edge-reclassify/fanout cap 都在跑，rework 计数没记上，疑似计数 bug 或 rework 走了别的路径，需 CC 核 |

## 2. 逐轮轨迹

| round | n_new | total | gain | S_α' | verified/n_new | frontier | dropped_redundant |
|---|---|---|---|---|---|---|---|
| 1 | 57 | 75 | 0.905 | 48.26 | 34 | 18 | 0 |
| 2 | **0** | 75 | 1.0 | 48.28 | 0 | 57 | **142** |

**终止方式 = `stop`（正常收敛退出，非 max_depth hit）**：r2 分解产出 0 新节点 + 砍掉 142 条冗余边 → low_gain_streak=1 → pass_rate 触发停止。对比 r14（max_depth=4 hit 后停在 rework state），这次是机制自己判"没东西可拆了"就收手——行为不同，需要判断是题面变软（去掉延迟硬约束后维度空间变小）还是分解器退化。

## 3. 撞号细节（精确数据）

12 个 dup id：N19×5, N20×5, N21×5, N22×5, N23×5, N24×5, N25×5, N26×5, N27×4, N28×4, N29×3, N30×2。每个 dup id 下挂的是**完全不同的 claim**（如 N19 同时挂着 "Prefill FLOPs 阈值" 和 "评估指标基准 PPL"），不是同一条记录被写多遍——与 r14 旧文件的病征一致（同一 decompose 批次内 id 重新从 N19 起编）。

孤儿/top-level 分布未单独统计（结构带伤，forest 口径待定，等 CC 定 depth 口径后补）。

## 4. 与 r14（旧题面含 3s/token）对比

| 项 | r14（旧题面） | 本次（新题面） |
|---|---|---|
| 终止 | max_depth=4 hit, state=rework | stop（收敛退出） |
| nodes | 137 records / 40 unique | 75 records / 34 unique |
| verified | 38.0% | 45.3% |
| degraded | 56.9% | 30.7% |
| pending | 3.7% | 24.0% |
| reworks | 91 | []（计数缺失？） |
| leaks | 0 | 0 |

解读：新题面去掉了硬性延迟约束后，树明显变浅变小（75 vs 137 records），且提前收敛。degraded 下降可能部分来自 14:11 合入的白名单 post-filter（EN query 实测从 5 条噪声变 3 条 wiki 干净源），但本轮主体仍是中文 query，改善幅度不能全归因于此。**pending 24% 是新信号**——大批节点停在待核验就随 stop 退出了，报告组装时会缺证据。

## 5. 遗留问题（转 CC / 待 D 醒）

1. **id 撞号复发**（P0）：fix 为何没覆盖这个 run？两条候选：① pid 11150 启动早于 fix commit 生效时间；② 存在第二处 id 分配逻辑（resume 重放 or 多进程）。CC 查启动参数与代码路径。
2. **rework_events=[] 与日志矛盾**（P1）：console 里 fanout cap / edge-reclassify 持续触发，rework 计数却是空数组。若 rework 循环实际在跑但没计数，E-block 的 low_gain_streak 判据输入就有偏。
3. **pending 24% 随 stop 退出**（P1）：stop 前是否应强制 flush 一轮 verify？还是接受"未核验节点不进报告"的现状？影响 assemble_report 的证据回填量。
4. **gain 样本补充**：r1 gain=0.905, r2 gain=1.0（零新增导致）——r2 的 1.0 是伪值（n_new=0），P5 CDF 回标脚本写的时候要把 n_new=0 的轮剔除。

## 6. 下一步

- CC 侧：撞号根因 + rework 计数核查（L20 已发）。
- Lead 侧：本文件落盘完成；gpu 主数据暂缺（带伤不可用），端到端 bench 分数继续等 DRB 题（drb-1 已有 judge 分 0.0，见 bench report §3；drb-16 排队）。