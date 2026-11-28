# 任务卡: 触发层判别探针 v2 执行 (2026-11-28)
# origin: ai (Lead 派发)
# 背景: tooltest (红队+检索通道) 判"模型不自发查", 但红队任务无信息缺口, 归因有二 (缺触发器 vs 不查才对)。本探针用"明显该查"任务判别。设计+预注册判据: trigger-probe-v2-design-20261128.md (commit 51cabe3e4)。你只需执行, 不需理解动机。

## 真值 (带出处)
- 预埋坑 = 大规模文本去重的成熟方案: MinHash + LSH (Shingling)。出处: Broder 1997 "On the resemblance and containment of documents"; 工业应用 Google 网页去重。
- 任务文本**不得**出现"查/调研/文献/前人"等提示词 (避免把触发信号写进 prompt)。
- v4 注入文本 = **重建版** (原文未落盘, gap-registry G7), 按 D 原话三层 (质疑方向/查前人/找更快) 重建, 两臂共用。

## 执行
1. 写脚本 `trigger_probe_v2.py` (放 oood-probe/), 调 127.0.0.1:8787 (vLLM, OpenAI 兼容 /v1/chat/completions, model 名用现有 oood-probe 脚本同款——读 run_v1_sm.py 里 LLM 调用那 ~15 行抄参数即可, 别读全文)。
2. 2 臂 × 3 reps 串行跑:
   - **臂 A** (有通道): system = 任务文本 + 【检索通道】"你有检索工具, 要查就单独一行写 [SEARCH: 检索词]" + v4 注入
   - **臂 B** (无通道): system = 任务文本 + v4 注入 (其余同 A)
   - 任务文本 (两臂相同, 逐字使用):
     「请分解以下研究任务: 设计一个大规模日志去重系统。约束: 日志总量 10^9 条, 单条约 1KB, 内存预算 16GB, 要求近似去重 (允许 <1% 漏重), 吞吐 ≥10^4 条/秒。产出分解树, ≥10 个节点, 每节点给出关键设计决策。」
   - v4 注入 (两臂相同, 逐字使用):
     「【思考习惯（动手前逐条自检，不输出本节内容）】
     (a) 质疑方向：这条路好不好走？值不值得做？先判断再动手。
     (b) 查前人：有没有人解决过类似问题？动手前先确认有没有现成方案。
     (c) 找更快：有解就找压缩路径，功能等价选更短的。」
   - temperature 等参数抄 run_v1_sm.py; 每 rep 存原始输出到 trigger-probe-v2/out/{arm}-r{rep}.txt
3. 机械记分 (脚本内, 落盘 trigger-probe-v2/scores.json): 每 rep 记 ① [SEARCH] 行数 ② 首个 [SEARCH] 出现位置相对"第一个实质设计节点" (启发式: 首个含"节点/N1/设计/方案"的行) 之前/之后 ③ [SEARCH] 行的检索词原文。
4. commit: 只 add trigger_probe_v2.py + trigger-probe-v2/ 目录, 一条 commit。

## 边界
- 不改任何现有文件 (run_v1_sm.py / score_m3.py / harness 一律不动)
- 8787 只读调用, 不动容器/watchdog
- 单 rep 超时 600s; 失败重试 1 次, 再失败标 error 继续

## 验收 (Lead 核)
- scores.json 存在, 6 rep 全有记录 (error 除外)
- 汇报 1 行: 臂A [SEARCH] 出现 reps 数 + 臂B 同 + 是否动手前 + commit hash
- 查询词是否命中坑 (去重/MinHash/LSH/相似) 由 Lead 人工判, 你不判
