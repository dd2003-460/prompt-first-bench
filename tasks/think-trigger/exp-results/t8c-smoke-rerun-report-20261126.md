# T8c smoke 重跑报告（2026-11-26 夜）

# origin: ai · 执行者 pid 97852 死于 A 臂后，supervisor 接力 B 臂（pid 1383），eval 由 Lead 验收
# 数据: raw_outputs_t8c.json（A 臂=重跑数据, B 臂=接力数据）· 备份: *.pre-rerun.json
# 判据: t8c-preregistration.md §4 Stage 0（commit 8c168c2a4 冻结，判据先于数据）

## 判决：停止，不扩样（无分离迹象）

| 臂 | 标签 | s（有效样本） | 截断 | d_mean | repeat5max |
|---|---|---|---|---|---|
| A' | A3, A3, A3 | 0/3 = 0.0 | 0 | 3.0 | 8 |
| B' | indeterminate, A3, indeterminate(截断) | 1/2 = 0.5 | 1/3 | 3.5（有效 2 个） | 13 |

机械检查：截断率 ≤50% ✓（B 臂 1/3），judge 全出标签 ✓。
分流：分离迹象要求 s_B'≥2/3 且 s_A'≤1/3。B 臂 1 个截断样本按 §1 单独计数不进 s 分母
→ 有效分母 2，s_B'=1/2 < 2/3 → **无分离 → 停止**。方向为正（B 0.5 > A 0.0）但未达
pre-commit 阈值。按预注册纪律如实报告，不扩 n=9（n=3 对弱效应无检验力，烧 27b 换
不可检出的检验 = 浪费）。

## 关键发现（负结果的三个出口）

**F1 A 臂标签整体翻转（indeterminate→A3）= n=3 测量噪声的定量证据**
pre-rerun（第一次跑）A 臂 3/3 indeterminate（d=4.0）；重跑后 A 臂 3/3 A3（d=3.0）。
同一 judge 版本（correctness_layer_v0），不同数据批次 → 标签全翻。两批都是 s=0
（都断点），方向不受影响，但说明 **A 臂基线在 n=3 下不稳定**——这正是预注册
"n=3 无检验力、n=9 前验 power 对弱效应 <0.3"设计的实证支持。排除的错误解释：
"B 臂优势来自 judge 对 B 臂拼接文本的偏袒"——A 臂自己都在两批间翻转，judge 不是
单向偏置源。

**F2 B 臂复读退化是生产实例（repeat5max=13，1/3 截断）——严重度经审计降级**
B 臂 6 阶段里 5 个阶段触发复读警告（repeat5≥5），run3 的 04.5 阶段撞 12288 token
上限被截断（finish=length）。**但 5-gram 审计（audit_b_repeat.py → t8c-b-repeat-audit.json）
推翻"全局退化"印象**：各 run 的 5-gram 独特率 0.934/0.962/0.947（正常文本水平），
跨阶段重叠仅 1-6%。真实退化是**局部的**：max_5gram_repeat 大多 3-6（短句重复，
接近正常写作），唯一真严重 = run1-02.5（同一 5-gram ×18）。
**仪器结论：run_exp 的 repeat5 警告灵敏度过高**（警告 ≥5 次的阶段里 8/15 实际
5-gram 重复 ≤6）——日志警告 ≠ 退化，判退化要看 n-gram 审计。
修正后的 F2：B 臂退化程度轻于日志印象，不阻塞 T8c 推进；真正的阻塞项是
run3-04.5 的 length 截断（1/3 截断率吃掉 s 分母，把 s_B' 从可能的 2/3 压到 1/2）。
这恰好是 think-trigger T4（打转检测）的生产靶子：T4 检测的"同一试错重复"在
B 臂 stage 级已经出现，且 T4 若沿用 repeat5 阈值会大量误报——T4 判据应改用
n-gram 独特率（本次审计口径），repeat5 只作预警不作判死。
**交叉验证修正（2026-11-26 23:58，ChatGPT+GLM 双站独立收敛，回执
web-llm/t4-metric-crosscheck-20261126.json）**：两站都支持"原始计数=劣质 proxy"，
但都指出 n-gram 独特率**单独不够**——全局聚合漏短循环（A-B-A-B 模式保持高
5-gram 多样性）。T4 判据最终设计改为三层：
(a) 统计层：归一化重复率/独特率（校准 P99 报警）
(b) 统计层：主导 n-gram 覆盖率 >20-30%（单一短语占文本比例）
(c) 结构层：连续重复段 >=3 次（critical，覆盖短循环盲区）
判死 = 结构层命中 OR 统计层双信号同时超阈；repeat5 仅作预警。

**F2 补 Lead 复核（usage 字段权威归因，2026-11-26 深夜）**: run3-04.5 的截断归因**二次修正**——
真因不是正文长，是 **reasoning（思考）token 爆炸**。raw_outputs_t8c.json 的 usage 字段（权威口径）：
run0-04.5 reasoning_tokens=2740(stop) / run1=1192(stop) / run3=**11338**(length)。
run3 的思考 token 吃掉 12288 预算的 92%，正文（content 仅 ~950 token）根本没写完就被截断。
27b 的 reasoning 长度方差极大（1192↔11338，9.5×）——同一条 04.5 指令，不同 run 思考量天差地别。
**前一轮「04.5 输出长度方差（1552 词）」归因作废**：审计 JSON 的 words 字段只数了 content，
漏了 reasoning 字段，导致误判。repeat5=13 仍是 5-gram 计数误报（uniq5=0.975 健康），非复读。
→ 修法目标从「限正文长度」改为「控思考预算溢出」，见下方修法设计。
F2 降级结论（预警不判死）不变，但机制归因从「复读」→「长度方差」→「思考 token 爆炸」三次修正。

**F3 执行者死亡模式确认（pid 97852 死于 A 臂后，无 traceback）**
第二次观察到"长跑进程无声死亡"（第一次见 11-15 教训：6 个 run 全死无 traceback）。
共同点：`&` 起的进程绑在当轮进程组，turn 切换时被回收。executor-protocol 已要求
setsid nohup + PID 写 goal state，但本次执行者用的是 Hermes 跟踪后台（收据 start_note
有记录）——**Hermes 跟踪后台 ≠ setsid 脱离**，这个等价假设被证伪。协议需修订：
长跑进程必须 setsid nohup，Hermes 跟踪只用于短任务。

## 对 T8c 主 claim 的影响

H1（多阶段赢）在 n=3 无分离信号 → 按预注册停止。claim 状态：
**"27b + 本题面 + 73728 预算下多阶段流程的 correctness 优势未检出（n=3 smoke，
方向弱正 0.5 vs 0.0，B 臂伴 1/3 截断）"**。
若要推进 H1，前置条件不是扩样，而是先修 04.5 截断（F2 补 Lead 复核已归因：
长度方差撞上限，非复读）——截断中的 B 臂即使扩到 n=9，测的也是"被截断的流程
vs 直接求解"，不是"完整流程 vs 直接求解"。

## 下一步（按性价比）

1. ~~B 臂复读退化审计~~ **done（本轮）**：audit_b_repeat.py → t8c-b-repeat-audit.json，
   结论=退化局部、不阻塞（见 F2 修正 + F2 补 Lead 复核）
2. T4 检测器判据改三层设计（交叉验证修正节：统计层双信号 + 结构层连续段；
   repeat5 降为预警）
3. executor-protocol 修订：长跑进程 setsid 硬性要求（F3）
4. T8c 若推进 H1：前置不是扩样而是先处理 04.5 截断——**修法（2026-11-26 深夜定稿，
   基于 usage 归因 + thinking_budget 探测）**：harness 层截断重试。
   - 探测结论：本地 proxy（8787）接受 `thinking_budget` 参数但**不强制**（budget=50→
     实际思考 228 token，两次复测均超限）→ 参数封顶思考不可行。
   - 修法：`run_exp_t8c.py` 的 call() 增加 finish_reason==length 时的重试逻辑——
     同 prompt 同 max_tokens（12288 cap 不变）重采样 ≤2 次（reasoning 长度随机，
     重采样大概率恢复有效样本）；3 次全 length → 该阶段判 indeterminate（截断），
     按预注册 §1 截断条款处理。
   - 不变量保护：per-stage cap 不变 → token-matched 硬约束（两臂名义预算 73728
     严格相等）不受影响；重试只作用于截断样本，不偏置非截断样本。
   - 验证：修 harness 后重跑 B 臂 1 样本（04.5 阶段）确认 finish=stop，再谈 n=9。
   - **副产品（think-trigger 资产）**：`usage.reasoning_tokens` 是免费的思考量度量
     （harness 早已捕获，scores_v2.md 用过 v1 量级 484-789）。T8c 首次给出权威量级：
     同指令 04.5 阶段 reasoning 1192↔11338 token（9.5× 方差）。→ 对 T4（思考触发/
     打转检测）的价值：触发阈值若按思考量分级，校准基准从此有数据支撑（薄思考
     ~1-3K，深度思考可达 11K+，中间地带待更多样本标定）。不立新机制，只记入 T4 校准。
