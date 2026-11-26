# origin: ai
# judge selftest 红灯：根因定位 + 修复（2026-11-26）

## 现象
`judge_pipeline_v0.py --selftest` 报 4 FAIL（T8b 4 样本 verdict 全掉成 A1），exit 1。

## 根因（已定位，非存量悬案）
`7bab6dd77`（11-26 18:04）把 `correctness_layer_v0.judge_text` 的 winner 卡型参数化、
默认 `WINNER_CARD="V100"`（T8c 重锚定配套）。但 `judge_pipeline_v0` 的调用链
（compute_correctness → cl.judge_text(text)）没穿 winner 参数 → 存量 3090 世界
fixture（S5/T8b）被默认 V100 误判。correctness_layer 自己的注释已预警
（"T8b fixture 是 3090 世界"），漏的是 pipeline 侧接线。

排除项：
- 非 bonus 改动引入（b2a1c0736^ 旧版跑同样 4 FAIL，相同样本）
- 非期望值过期、非 correctness_layer 回归（J1 验收时 winner 还是硬编码 3090，
  7bab6dd77 才改默认值）

## 修复（judge_pipeline_v0.py，5 处）
1. `compute_correctness(text, qid, winner=cl.WINNER_CARD)` → `cl.judge_text(text, winner=winner)`
2. `score_sample(..., winner=cl.WINNER_CARD)` 透传
3. `run(..., winner=cl.WINNER_CARD)` 透传
4. CLI 加 `--winner`（默认 V100 = T8c 新锚点世界；3090 世界存量 fixture 显式传 3090）
5. selftest 显式 `winner="3090"`（S5/T8b 都是 3090 世界）

## 验证
- `py_compile` OK
- `--selftest` 7/7 ALL PASS，REAL_EXIT=0（修复前 4 FAIL exit 1）
- cov 不变：0.3889（期望 0.389±0.01）
- 用法约定：**新 T8c 数据（V100 世界）= 默认；S5/T8b 存量 fixture = 必须 --winner 3090**

## 教训
参数化改默认值时，所有下游调用链（尤其带回归守卫的 selftest fixture）要同步显式传参
或核对 fixture 世界归属——默认值漂移静默改变存量基准，守卫抓到时已分不清是
"守卫对了"还是"接线断了"。本次守卫抓对了（确实有漂移），但漂移源是接线不是口径。
