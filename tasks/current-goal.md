# Goal: RV3G3-threshold-crossdomain-reverify — batch2 跨域重验 assert 骨架（schema 预注册）

> 创建：2026-10-30 · ralph loop runner（`tasks/goal-queue.md` 新导出候选，r138+ 446f4cc 登记）
> 依据：goldrank-threshold-proof.md L4.2「改回 top-10 主判据」条件 (a)(b) 的跨域验证义务；当前 blocked-on-external（等 batch2 数据），纯仓库内推导可先行落 assert 骨架（同 r136 kappa-receipt 模式）

## 【目标】
写 assert 骨架脚本 `bench/rubric-v3/ablation/scripts/assert-goldrank-crossdomain.py`：消费第二域 hit-matrix + 方案权重 JSON（schema 预注册），机判 goldrank-threshold-proof.md L4.2 条件 (a) t=4 过线集合跨域稳定性 + (b) tie-sensitivity 审计（全量合法 tie-break 置换枚举）。**本轮交付 = 骨架 + schema 文档**；对当前 ablation 面（无第二域数据）常态输出 SIGNAL blocked-on-external + exit 0（不伪造数据转绿，同 r136 先例）。batch2 数据到来后零改动接入。

**范围定位**：纯仓库内工作（协议提取自既有 assert-goldrank-threshold.py ④⑤ + 骨架实现 + 变异测试），零外部依赖。

## 【阶段】
01 分解 → 02 研究（仓库内既有实现精读）→ 02.5 交叉核对 → 03 行动分解 → 04 执行验证（骨架落盘 + 变异测试 ≥3 场景）→ 04.5 反方复核

## 【SOP 索引】
- `loop/prompt-first/01..04.5` + `sop/arena-loop-pipeline.md`
- 协议参考（只读）：`ablation/scripts/assert-goldrank-threshold.py`（④ 超几何 / ⑤ top-10 复算协议，节点 ID 字典序 tie-break）+ `assert-kappa-receipt.py`（schema 预注册 + 三分支判定写法）
- 事实源（只读冻结）：`bench/rubric-v3/goldrank-threshold-proof.md`（L2 tie 段 / L4.2 条件）/ `ablation/{hit-matrix.json, prior-estimates.json, stats-w3w4.json}`

## 【验收标准】
- [ ] `assert-goldrank-crossdomain.py` 落盘；当前 ablation 面实跑 = SIGNAL blocked-on-external + exit 0
- [ ] schema 预注册（输入文件最小字段集 + D1-D3 判定语义）byte-stable 于脚本 docstring
- [ ] 变异测试 ≥3 场景实证分支可达：伪造第二域数据 → (a)/(b) verdict 路径 / tie-sensitive 构造 → (b) FAIL / 换题面无 gold_nodes 声明 → ERROR fail-loud
- [ ] 冻结数据零修改（git status 验证）
- [ ] 04.5 verdict pass；queue 更新（本 goal 划掉 + 结果注记 + 追加 batch2 数据到来后的闭环候选）

## 【失败降级】
- 若共享协议提取发现与 assert-goldrank-threshold.py 口径不可对齐（tie-break 细节不一致）→ 登记边界，骨架降级为「schema 存在性校验 + 判定逻辑占位」，不强行统一口径
- 若 tie 枚举算法复杂度在骨架规模下不可控 → 限定枚举范围（边界 ±1 邻域）并显式声明覆盖边界