# 任务卡 P2 — OOD 探针 S0 气象臂记分（指标抽取+对照）
> 你是纯执行 sub。本卡是唯一指令来源，不要读其他项目文件做判断（判据文件除外，路径已给）。
> 零改动生产代码，零 git 操作（commit 由 Lead 做）。

## 输入（只读）
- SM 臂产物: `/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/oood-probe/sm-arm.json`
  （40 节点，每节点 {id, claim, level, source, status, edge_type, parent_ids}；另有 rounds_log/wall_sec/final_state）
- 裸基线臂: `/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/oood-probe/baseline-arm.txt`（27b 单发全文）
- 预注册判据: `/Users/a1-6/Desktop/workspace/pfb-thinkmech/tasks/oood-general-probe/decomposition.md` §3（只读 §3，~15 行）

## 题面（Q10 气象域，因果解释结构）
为什么热带气旋登陆后会迅速减弱？要求：识别所有物理机制 / 每机制量化 / 指出主导项 / 不同强度气旋差异 / 不确定点收黑盒。

## gold 机制清单（4 项，判"机制覆盖"用）
1. **能量源丧失**：登陆后海气热湿通量（潜热）切断，主能量供给消失
2. **地表摩擦**：陆地粗糙度增大，边界层摩擦耗散动能
3. **垂直风切变**：环境风切变破坏暖心对称结构
4. **流出阻塞**：高层辐散流出受阻，低层抽吸减弱

## 要做的事（写一个 Python 脚本落盘，输出走脚本不手打）
脚本 `/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/oood-probe/score_p2.py`：
1. 读 sm-arm.json，抽客观指标：
   - `sm_n_nodes` / `sm_wall_sec` / `sm_final_state` / `sm_llm_calls`（= nodes 数 + rounds_log 里 verify/rework 调用，若无法精确就从 sm-arm.log 里 grep "call done" 计数）
   - `sm_l1_claims`: level=L1 的 claim 列表（id+claim 全文）
   - `sm_quant_claims`: 所有 claim 里含"数值+单位"（kt, km/h, %, W/m², hPa, °C, 天/小时 等）的条数 + 原文摘录（前 10 条）
   - `sm_levels_dist`: 各 level 节点数
2. 读 baseline-arm.txt，抽：
   - `base_chars` / `base_quant_claims`（同 regex）
   - `base_mechanism_hits`: 4 机制各自在基线全文中是否出现（关键词匹配：能量源→"潜热|热通量|能量|蒸发"；摩擦→"摩擦|粗糙"；风切变→"切变"；流出阻塞→"辐散|流出|阻塞"），每项 true/false + 命中片段
3. 机制覆盖判断（SM 臂）：把 40 个 claim 全文拼成一个字符串，同样 4 组关键词匹配 → `sm_mechanism_hits` 四项 true/false + 命中 claim id。
   **注意**：关键词匹配只出初判；如果某项 false 但你从 claim 文本看到明显同义表述（如"暖源切断"≈能量源丧失），在 `sm_mechanism_note` 字段写明人工复核意见，不擅自改判。
4. 落盘 `/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/oood-probe/metrics-s0-cyclone.json`（上面所有字段 + `sm_mechanism_hits`/`base_mechanism_hits` 的覆盖计数 `sm_mech_cov`/`base_mech_cov` = true 项数/4）。

## 验收（最终汇报，≤5 行）
1. `sm_mech_cov`/`base_mech_cov`（各 x/4，列出哪几项命中）
2. `sm_quant_claims` vs `base_quant_claims`
3. `sm_l1_claims` 条数 + 是否跑题（L1 里有无与气旋减弱无关的域，如硬件/LLM 推理）
4. `sm_llm_calls` + `sm_wall_sec`
5. metrics json 路径 + 脚本路径
**不做判决**（transfer/handcrafted 由 Lead 按 decomposition §3 判），只给指标 + 跑题观察。

## 边界
- 不碰 run_q9_gated.py / checkpoints/ / 其他 oood 文件
- 不 git commit
- 27b 输出上限保护：脚本落盘，你的输出流只放脚本代码 + 运行 + 5 行汇报
