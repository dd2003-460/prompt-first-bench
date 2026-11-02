# CONTINUE_MSG — 2026-11-02 r239

## 本轮完成
**battle-kappa.py 双 bug 修复 + κ 数值修正（pfb @ main aaa13d9 pushed）**：
- **bug1（致命）**：`fleiss_kappa()` docstring 声明 list 输入，`main()` 实际传 dict——迭代 dict 拿到 key（字符串）与 0/1 比较全 False → n_mat 全零 → κ 恒等于 -1/(r-1)（4 raters 时恒为 -0.3333，与数据无关）。历史落盘的 κ=-1.5 是更早版本同类形态 bug（当时 r=3）。
- **bug2**：P_e 用 Σp̄² 而非 Fleiss 原式 Σp̄(1-p̄)。旧代码里被 bug1 掩盖（P_e=0 时两式同值），修 bug1 后暴露。
- **验证**：三例独立手算比对全过（本数据 κ≈0 / 全一致 κ=1 / 文献型小例一致）。
- **重算结果**：M7 gate 4 族 scorer × 3 run，κ = 0.0000（P_o=P_e=0.4444）——「比随机还差」(-1.5) 的结论作废，真实口径是「恰如随机」。方向判断不变：仍 <0.6 → SIGNAL+人工裁决，β 维持 0.6 阈值不受影响。回执 `tasks/receipts/kappa-battle-r239.json` @ a746bdc；queue L25 KAPPA-U1K1 行补修正注记 @ aaa13d9。
- 插曲：cbff721 曾误把 -0.3333（bug1 产物）当正确值提交，a746bdc 修正覆盖，两 commit 留痕可追溯。

## 当前状态
- pfb @ main aaa13d9 pushed
- 第三 seed 功效 run（~2h ninfer 算力）仍在 APPROVALS #2 等成璐放行，未获批不动算力
- G1b family_check 仍卡模型身份披露（不变）

## 下一步
1. **T8 Part C 派发（P1，可自主）**：decomp-bench loop-state 已对账（767291a pushed，T8=completed_partA_done_ce20b23）。Part C = 可解释性加速（C1 双实例对照协议：V-full vs 变体各 ≥3 seed，内部状态归因缩 top-k 嫌疑段再 paired runs 确认；r46 修订分工 ninfer :8000 行为层 + llama.cpp :8099 最后一层探针）。待办：①写 Part C 任务书落 decomp 仓 tasks/ ②arena 固定会话派发（decomp binding 曾 403，先 ls-remote 探活）③ninfer 本轮 ping 超时（curl 5s 无响应），派发前复测。
2. **第三 seed 功效提升 run（P1，卡预算审批）**：APPROVALS #2 待批——9 configs × D1/D2 各加 seedc 共 18 run + J1/J2 双判 36 调用，n 从 6/cell 提到 9/cell。放行即派。
3. G1b family_check 仍卡模型身份披露（不变）
4. ACTIVE-candidates #4 ORF arXiv 手动上传 / #3 健康 strand 镜像源（需人工）