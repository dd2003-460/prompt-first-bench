# CC 实验员 → Lead（追加式，格式见 PROTOCOL.md）

## C1 02:58 — r14 DONE + degraded 超线根因定位 + drb-1 死因排查（困惑+完成混合）

### A. r14 完成汇报（工作单元 1-2 done）

r14（structural test 修正版）跑完：**137 nodes, 3 rounds, leaks=0, reworks=91**。
分析已落盘 `experiments/stage-ablation/research/r14-calibration-analysis.md`。对照任务书两条线：

| 指标 | 值 | 判定 |
|---|---|---|
| quotient 占比 | **12.4%** (r13=90%) | ✅ ≤30% 线，hack 方向已反转 |
| degraded 率 | **56.9%** (78/137) | ⚠️ >40% 警戒线，需诊断（已做，见 B） |
| leaks | 0 | ✅ |
| verified 率 | 38.0% | — |

level 分布 L1=5/L2=17/L3=37/L4=78；edge cartesian 87.6%/quotient 12.4%/stochastic 0；source knowledge 75/search 50/given 12。

**顺带确认一个疑点**：r14 final_state="rework" 是表面现象——代码里 max_depth=4 hit 直接 break（s5_state_machine.py:684-687），不设 State.STOP，state 停在上一轮的值。不是 bug，但 bench report 里我会注明口径。

### B. degraded 56.9% 根因（已完成取证，结论待你确认方向）

取证链（全部本地证据，无猜测成分）：

1. `.research-cache/` 02:25–02:44 窗口（r14 r3 核验期）**64 条检索记录，全部是中文长 query**（节点 claim 直传）。
2. 结果质量分类：**garbage 14 / homepage-generic 18 / maybe_relevant 32**；**wikipedia 通道命中 = 0**（`_wiki_search` 硬编码 en.wikipedia.org，中文技术 query 全灭）。
3. garbage 实例："Qwen3-27B 架构参数"→XHS 爬虫 repo；"W4-A8 MMLU"→磁力链接工具页；"vLLM Docker 维护"→Blueair 空气净化器页面；"TP=2 通信优化"→VFS 签证网站。
4. rework 回收率：search 节点重搜后 **verified 仅 3/39**——因为 `_rework` 换 `" alternative"` 后缀重走同一批坏通道，等于原样再撞一次墙。knowledge 节点重核 41/53 转 verified（无检索依赖，纯 LLM 复核）。

**我的判读**：degraded 的主体不是 verify 过严（P3 judge 把无支撑 claim 降档是对的），而是**检索通道对中文技术 query 系统性失效**（DDG-lite/Bing fallback 为主力时返回垃圾/首页）。三个候选修法方向（都属机制改动，未动代码，等你定方向再写三问提案）：
- **(a) query 层**：中文 claim → 拆英文检索词/双语 query（改 search_node 的 query 构造，general 规则）；
- **(b) 通道层**：中文题启用 zh 语料/wiki 中文维基通道（research_hook 加通道选择逻辑）;
- **(c) 接受现状**：gpu 域 degraded 高是通道能力上限，DRB pilot 直接用官方 judge 看端到端分数是否可接受——若 DRB 分不差，degraded 率就不是真问题（Goodhart 反例：别为过程指标改机制）。

我倾向先跑 **(c)**：DRB pilot 本来就要跑，端到端分数才是 U(T) 侧的真实信号；(a)/(b) 等 DRB 数据证明"检索质量确实拖了分数"再立项。这样避免为一个过程指标引入新机制（违反三问 Q2 正交性纪律）。**请裁决。**

### C. drb-1 死因排查（bug 类，不确定修复 → 按协议先报告）

昨晚 ~02:31 启动的 drb-1 run 在 **L1 skeleton 之后、round-1 decompose 之前静默死亡**：
- log 止于 "L1: 5 top-level dimensions"（5 个维度打印完整），无 FATAL/traceback 行；
- 无任何 checkpoint（E12 crash-dump 也没触发 → 进程是被 **SIGKILL** 而非 Python 异常，与 T2 报告的 r14 两次假死同型）；
- 时间窗 02:31–02:44 与 r14 round-3 重叠——本机 free RAM 当时 ~2.3GB/64GB，memory pressure 嫌疑最大（teamer-state.json 也记了这条）。

**代码层面我还发现一个结构性弱点**（非本次死因，但值得你知道）：L1 之后、round-1 checkpoint 之前没有任何落盘点，且这段含 5×edge-classify + decompose + gap_check + necessary-judge + verify + rework 共 ~10+ 次 LLM 调用，单次最长 timeout 600s——**任何 SIGKILL 都会丢掉整个 round-1**（E12 只兜 Python 异常，兜不住 kill）。缓解选项：① batch 级中间落盘（机制改动，走三问）；② 运维层：run 前检查 free RAM + 避开与长跑任务重叠（零代码改动，我现在就能执行）。**我建议先 ②**，① 等 DRB pilot 暴露实际频率再立项。

### D. DRB 数据集状态（好消息）

`/tmp/drbench/` **已存在完整仓库**（criteria_data/criteria.jsonl + prompt_data/query.jsonl 100 题 zh50/en50 + test_data reference articles + utils/score_calculator.py 官方加权逻辑）。我本地的 3 个 query 文件（drb-1/2/16）就是它的子集。**不需要你再拉数据**——除非你要用 HF 上游版本核对一致性。

我已写好官方四维判分器 `drb-pilot/drb_judge.py`（逐条 criterion 0/1 + dimension_weight 加权，对齐 criteria.jsonl 的 comprehensiveness 0.3 / insight 0.36 / instruction_following 0.2 / readability 0.14；qid=1 共 26 条 criterion；judge=本地 qwen3.8-27b，绝对值仍需 GPT-5.5 复核——那步需要你提供 key 或指定异源端点，T8-C3-v3 的 blocked_human 还挂着）。

### E. 下一步计划（等你回复前我先动的部分）

1. ✅ 本消息 + cc-state.json 更新 + git commit（分析产物）；
2. 准备 drb-1 重启命令（`--question-file drb-pilot/queries/drb-1.json --qid drb-1`，run 前 pgrep + free RAM 检查）——**是否现在重启由你定**：单独跑会占满 8787 proxy 的时间片，如果你想让我先跑别的（比如 drb-2/16 排队），说一声；
3. 最终答案生成步骤（树 → 报告 md）目前 pipeline 里没有现成组件——sm 产出的是节点树，DRB judge 吃的是研究报告。我需要写一个 tree→report 组装器（属于新增代码，不动现有机制，应该不用三问，但动手前会在下一条 bus 报备）。