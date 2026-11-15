# DRB 三臂对比：arena vs 27b vs 混合（2026-11-14）

> origin: human 指令（"要不让arena自己跑一套，27b给完整工具以及流程跑一套，还有27b指挥arena跑"）
> 关联：T53 状态机、DRB pilot、arena-outsource SOP

## 0. 一句话

同一个 DRB 题，三种架构各跑一遍，对比报告质量。核心问题：**27b 做思考 + arena 做检索的混合架构，能不能超过 arena 裸跑？** 如果能，说明 27b 的拆解/核验能力是真实增量，不是摆设。

## 1. 三臂定义

| 臂 | 27b 角色 | arena 角色 | 实现 | 状态 |
|---|---|---|---|---|
| A（arena-only） | 无 | 全流程：拆解+搜集+推理+核验+报告 | 外包 arena agent mode，直接给 DRB 题 | 待派 |
| B（27b-only） | 全流程：S5 管线（拆解+核验+报告） | 无（web-llm 超时） | 已有 F/T/M 三臂代码 | F/T 完成，M 跑中 |
| C（27b+arena） | 拆解+推理+核验+思考 | 只搜集信息（27b 生成 query → arena 检索 → 27b 核验） | 改 S5 管线 search_node → arena API | 待建 |

### 单变量设计

三臂共用同一个 DRB 题（选 drb-16：非接触式感知算法，Software Development 类，中文）。
- A vs B：测"arena 裸能力 vs 27b 裸能力"
- B vs C：测"加 arena 检索是否提升 27b 管线质量"（C 臂的增量 = arena 检索 - web-llm 检索）
- A vs C：测"27b 的拆解/核验是否比 arena 的全流程思考更强"（如果 C > A，说明 27b 的思考层是真实增量）

## 2. 测量指标

每臂 n≥1（先跑 1 题看方向，n≥3 补统计）：
1. **DRB 四维加权总分**（drb_judge.py，官方 criteria.jsonl，judge=27b）
2. **严格 verified 率**（真实来源 verified / 总节点数）
3. **报告长度 + 节点数**（膨胀指标）
4. **检索成功率**（C 臂：arena 检索返回有效结果的比例）

## 3. 缺口

| 子项 | 缺什么 | 怎么补 |
|---|---|---|
| A 臂 | arena 任务书 | 按 arena-outsource SOP 写，给 DRB 题 + 要求输出完整报告 |
| B 臂 | M 臂跑完 + 报告组装 | M 臂 pid 27188 跑中，完事后 assemble + judge |
| C 臂 | search_node → arena 的接口 | 需查 arena API 是否有检索端点；若无，用 arena agent mode 做"只检索不推理" |
| 题目选择 | drb-16 是否适合三臂对比 | 需确认 drb-16 的 criteria 质量（criterion 数、覆盖度） |
| judge 偏差 | 27b judge 对 27b 答案有同族偏好 | 已知限制，标注；后续用 GPT-5.5 或 arena 交叉验证 |

## 4. 预测（先写后跑）

- P1: A 臂总分 > B 臂（arena 有真实检索，27b web-llm 超时率高）
- P2: C 臂总分 > B 臂（arena 检索 > web-llm 检索，27b 思考层不变）
- P3: C 臂 vs A 臂不确定——如果 27b 的拆解/核验比 arena 全流程思考更强，C > A；如果 arena 的思考层更强，A > C
- P4: C 臂严格 verified 率 > B 臂（arena 检索返回真实来源，logic-only 比例下降）

## 5. 执行顺序

1. [进行中] M 臂跑完 → assemble + judge → B 臂三臂（F/T/M）数据齐
2. [待派] A 臂：写 arena 任务书，派单
3. [待建] C 臂：改 search_node 接口，跑 drb-16
4. [待跑] 三臂 judge + 对比表
