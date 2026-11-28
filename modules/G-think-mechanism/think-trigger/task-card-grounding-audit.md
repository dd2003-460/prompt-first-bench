# origin: ai
# 任务卡: 接地真伪判别器 v1 (grounding audit)
# 派发: 2026-11-27 18:52 | 载体: sub-27b | 预计: 读~200行 写~90行 1 commit

## 目标
写 `modules/B-pipeline-ablation/research/q9_grounding_audit.py`：
机器可检的"接地真伪"判别器——不信模型自报"已验证/已实测"，只看轨迹里有没有真工具溯源。

## 背景 (为什么)
GPU 探针 C 臂 (无工具) 自称"实测基准值"但 search=0/code=0 = 散文模拟。
现有 JSON 里 trajectory 记录了每个 tool_call 的 result_head，code_runs 记录了 output_head——
判别器 = 把 final 输出里的数字和工具输出做溯源匹配。

## 判据 (v1, 严格按此实现)
对每个 episode:
1. **数字提取**: 从 `final_text` 提取所有数字 token (正则 `\d+(?:\.\d+)?`, 长度 1-8 位,
   排除年份 19xx/20xx 和纯 0/1)。记集合 D。
2. **溯源池**: 拼接该 episode 所有 `trajectory[*].tool_calls[*].result_head`
   + 所有 `code_runs[*].output_head` 成一个字符串 P。
3. **接地率**: grounded_rate = |{d∈D: d 作为子串出现在 P 中}| / |D| (D 为空则记 1.0)。
4. **散文模拟标志**: sim_flag = (final_text 含任一关键词 "实测|已验证|已查证|measured|verified
   |benchmark" 且大小写不敏感) AND (n_search_calls==0 AND n_code_calls==0)。
5. 输出每 episode: {ep, arm, n_numbers, grounded_rate, sim_flag, n_search_calls, n_code_calls}

## 输入
- `modules/B-pipeline-ablation/data/q9-budget-scan/gpu-model-probe-20261127.json` (A/B 臂)
- `modules/B-pipeline-ablation/data/q9-budget-scan/gpu-model-probe-20261127_C.json` (C 臂)
- **严禁整读这两个 JSON (共 90KB, 会撑爆上下文)**。只跑一行命令看顶层键结构:
  `python3 -c "import json; d=json.load(open('...')); print(list(d.keys())); print(list(d['arms'].keys()))"`
  确认 `arms.arm_X_*.per_episode[]` 的字段名即可。全文由你写的脚本 json.load 处理, 不进你的上下文。
- 字段: 每 episode 有 final_text/tools_used/n_search_calls/n_code_calls/code_runs/trajectory。

## 输出
- stdout: 每臂汇总 (mean grounded_rate, sim_flag 计数)
- 落盘: `data/q9-budget-scan/grounding-audit-<YYYYMMDD>.json` (脚本自动建目录)

## 验收 (真值锚点, 必须满足)
C 臂 (无工具, 自称实测) 的 sim_flag 必须全 True, grounded_rate 必须全 0.0 或 1.0(无数字时)。
A/B 臂应有 grounded_rate > 0 (它们真跑了 code_exec)。若 C 臂 sim_flag 出现 False,
说明关键词没抓到——读 C 臂 final_text 找它实际用的措辞, 补关键词后重跑, 直到锚点满足。

## 边界
- 只读上述 JSON, 写一个新 .py + 一个新 .json, 1 个 commit (scoped git add, 禁 git add -A)
- 不碰 8787 端口, 不调模型, 不跑 probe 脚本
- commit message: "grounding-audit: v1 判别器(数字↔tool_call溯源 + 散文模拟flag) — C臂锚点验证通过"
