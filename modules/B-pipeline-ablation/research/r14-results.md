# r14 结果落盘（structural test + 信息量语义，commit d230a64d）

> origin: lead (承) · 2026-11-12 ~03:40 · 数据源: `runs-s5-sm-gpu.json`（DONE @02:44）+ checkpoints/sm-gpu-r{2,3}.json
> 口径声明：r14 树带 **id 撞号伤**（CC C3 已定位根因并修复，未重跑验证）。下表双口径：**records** = 原始记录数；**unique** = 按 id 去重（同 id 取末条）。unique 口径才是真实节点规模。

## 1. 总量与判定

| 指标 | r14 records | r14 unique | 任务书区间 | 判定 |
|---|---|---|---|---|
| 节点数 | 137 | **40** | 100–150 | ⚠️ unique 远低于区间（撞号伤 + max_depth=4 截断双重因素） |
| quotient 占比 | 12.4% | **10.0%** | ≤20% 正常 / >30% 再修 prompt | ✅ 方向正确（r13 为 90% hack） |
| verified 率 | 38.0% | 32.5% | <30% 且节点<80 → 放宽 fanout | 边缘（records 口径过线） |
| leaks | 0 | — | 0 | ✅ |
| rework events | 91（33 个唯一节点被返工） | — | — | ⚠️ 偏高，见 §4 |
| contribution-filter 触发 | **0 次**（日志 grep 无命中） | — | 预期首次生效 | ❌ 未触发——阈值 0.10 可能过松，或 LLM 给分系统性偏高 |

**Phase 1 判定**：quotient 维度达标（不触发"再修 prompt 跑 r15"）；节点数在 unique 口径下低于区间下限，但主因是 id 撞号 bug（已修、待 drb-1 顺带验证）+ max_depth=4 封顶（CC C3 列为待 Lead 判断项），不是机制失效。**结论：不进 r15，进 Phase 2 DRB pilot**——理由：① structural test 方向已证实（90%→12.4%）；② 端到端分数才是裁决信号（L2 04:05 授权直接开 DRB）；③ 节点规模问题等 drb-1 用新 id 逻辑跑出干净树后再判。

## 2. 逐轮轨迹（records 口径）

| round | n_new | total | gain | S_α' | verified/n_new |
|---|---|---|---|---|---|
| 1 | 17 | 17 | 0.971 | — | 7/17 |
| 2 | 37 | 59 | 0.905 | 51.9 | 13/37 |
| 3 | 78 | 137 | 0.892 | 129.8 | 32/78 |

max_depth=4 hit 后停，final_state=rework（非 STOP——退出路径停在当时状态值，属正常 break，非异常）。

## 3. Edge 类型分布

| edge | records | unique |
|---|---|---|
| cartesian | 120 (87.6%) | 36 (90.0%) |
| quotient | 17 (12.4%) | 4 (10.0%) |
| stochastic | 0 | 0 |

edge-reclassify 双向活跃（日志可见 quotient→cartesian 与 cartesian→quotient 互相翻转多次），说明 structural test 在工作而非单向偏置。

## 4. Status 与 degraded 归因

| status | records | unique |
|---|---|---|
| verified | 52 (38.0%) | 13 (32.5%) |
| degraded | 78 (56.9%) | 21 (52.5%) |
| pending | 5 | 5 |
| failed | 2 | 1 |

degraded 超 40% 警戒线。CC C2 已完成根因取证（DDG-lite IP 级封锁 + Bing fallback 对中文 query 系统性返垃圾，r14-r3 窗口 junk 21%/generic 16%，rework 配对净回收≈0）——degraded 主体是 P3 verify 对无支撑 claim 的正当降档，病在上游检索质量不在核验阈值。候选修法 4 条在 CC C2-D（proposal-only，未动代码），排序：DRB 先跑 → 若分数被检索拖累 → junk-detector 提前兜底（最小改动）→ 节流/双语改写。

## 5. 对比表（r11 baseline / r13 / r14）

| 项 | r11 baseline（sm-gpu-r11-crash-303） | r13 | r14 |
|---|---|---|---|
| 终止 | crash@303（旧版无限膨胀） | DONE, state=rework | DONE, state=rework |
| 节点数 | 303 records / 130 unique | 70 records | 137 records / 40 unique |
| edge_types | 字段不存在（旧版无 structural test） | 未落盘（console 仅记 70 节点；r13 教训=63/70 判 quotient ≈90% hack） | cartesian 87.6% / quotient 12.4% |
| verified 率 | 18.2% (55/303) | 未单独统计 | 38.0% |
| degraded 率 | 17.5% (53/303) | — | 56.9% |
| leaks | 0 | 0 | 0 |
| reworks | 0（旧版无返工循环） | 44 | 91 |
| sources | given 22 / knowledge 203 / search 78 | — | given 12 / knowledge 75 / search 50 |

解读：r14 相对 r13 的核心变化 = structural test 生效（quotient 90%→12.4%）+ 返工循环实际运转（44→91，配合 degraded 56.9% 说明核验真的在拦无支撑 claim）。verified 率 18.2%→38.0% 翻倍，代价是 degraded 堆积——这是"证据质量不足"的症状不是"核验过严"（CC C2 取证支持前者）。

## 6. 遗留问题（转 Phase 2 / 待 D 醒决策）

1. **contribution-filter 零触发**：阈值 0.10 下 137 条边无一被过滤。要么 LLM 给的 contribution 分系统性偏高，要么该题所有子项贡献都真的高。drb-1 出干净树后看分布再定是否调阈值（参数改动走三问）。
2. **max_depth=4 封顶**：gpu 题 TCO/微架构下钻按 Decision 8 需要 L4-L5，当前 cap 可能系统性砍叶子层证据。调 cap 属参数改动，走三问提案——但先等 drb-1 端到端分数，若 readability/comprehensiveness 弱项指向深度不足再立。
3. **id 撞号 fix 未验证**：CC C3 已改全局计数器（commit 7cf91694），drb-1 是新 qid，首跑即验证；若 id 全唯一则 bug fix 闭环。
4. **rework 91 次偏高**：每 1.5 节点一次返工。CC C2 已归因到检索通道（DDG 封锁 + Bing 中文垃圾），与 degraded 同源，不单独立项。

## 7. 下一步

- CC 侧：内存已释放（free ~40GB，watcher 阈值 8GB 早已满足），应启动 drb-1（新 qid，顺带验证 id fix）→ tree→report 组装器已 smoke test 通过 → 四维判分 → s5-sm-bench-report.md 第一版。
- Lead 侧（本文件）：r14 校准收口完成，Phase 1 关闭。等 drb-1 出分。