# origin: ai
# 滚雪球调研：预算 tradeoff + 动态敏感性作为目标函数表述，有人做吗？
# 触发：D 2026-11-21 假设"模型能力够，是目标函数和预算 tradeoff 表述不清"
# 方法：arXiv API 9 组查询（2026-11-21 当轮执行，ID 均来自 API 返回，未逐条核 abs 页 [待核验]）

## 结论
**空白区**：把"预算 tradeoff + 时间尺度依赖的敏感性（动态 p99 贡献覆盖）"写进 LLM 目标函数表述、
测 LLM 能否产出完整决策模型——9 组查询未命中直接工作。三条相邻线如下。

## 相邻线 1：LLM 的预算分配（系统层，对象不对）
- AgentTTS (2508.00890)：test-time compute-optimal scaling 策略
- Knapsack RL (2509.25849)：预算分配解锁探索
- TRACE (2606.11119)：rollout 预算分配框架
- ContextBudget (2604.01664)：长程搜索 agent 的预算感知上下文管理
- Token-Budget Theory (2610.23246)：Think More or Read More
- ARC-AGI-3 speed-depth trade-off (2605.25931)：epistemic agent 的探索-深度 tradeoff
共性：预算在 rollout/工具/搜索间分配，系统层决策。非 prompt 内目标函数表述。

## 相邻线 2：LLM 做敏感性分析（方向对，域不对）
- OptMetaOpenFOAM (2503.01273)：LLM CoT 驱动 CFD 模型敏感性分析
- 2603.14273：LLM 做因果推断敏感性分析（case study）
共性：LLM 是执行者，对象是外部工程/统计模型。未让 LLM 对自己的决策模型做敏感性。

## 相邻线 3：LLM 部署 TCO（题域对，主体不对）
- 2404.08850：领域 LLM 部署 TCO 对比分析
- 2607.13239：成本最优基础模型部署组合
- PipeWeave (2601.14910)：GPU 性能预测（analytical+learning）
共性：TCO 决策由人/系统做，未要求 LLM 产出带扰动分析的决策树。

## 未命中方向（多尺度/动态敏感性 × LLM）
- Sobol × LLM：仅 2111.04138（Sobol 黑盒解释，LLM 是被解释对象）
- multi-scale sensitivity × LLM：0 命中（multi-scale 全在物理/视觉域）
- 市场周期/供需 × LLM 决策：0 命中

## 本地数据对 D 假设的支持/反对
- 反对：若纯目标表述问题，nat/soc 应同低；实际 nat/soc cov 0.54-0.90（T53b results.json）
- 支持：gpu 17 版本 depth 全卡 0.34-0.40（pipeline-checklist.md + T53b），卡位一致在
  L1-L2 概念层，L3 数字推导层从未到达 → 更像"完成判据未告知"而非"不会算"
- 支持：SM vs 裸 gpu 差距 +0.07 不显著（Welch p≈0.20）→ pipeline 救不了模糊目标

## 可验证设计（prompt-v2 A/B）
- 单变量：prompt 目标函数加"预算 tradeoff 表述"——每参数标注 (敏感度倍数, 时间尺度, 黑盒区间)，
  完备性判据 = 覆盖各时间尺度下 p99 贡献因素（D 的动态 p99 定义）
- 成功判据：gpu depth 0.34 → 0.5+（假设成立：表述问题）；不动 → 能力问题
- 前置：matched 批（bare pid 85866 / SM pid 87154）出完数据后开跑，保持同负载
- 评分标准缺口：当前 rubric 38 判定点无时间尺度/软件栈维护维度（grep 证据：市场/周期/波动 0 命中），
  prompt-v2 若要求动态覆盖，需同步扩 rubric（N-7 时间尺度敏感性 / N-8 软件栈维护），否则做到没分

## 撞车判断
- 无直接撞车；相邻线 2（LLM 做敏感性分析）最接近，可引为 related work
- novelty claim 可加维度：预算感知目标表述 × 细粒度过程评分 × 树结构评测
