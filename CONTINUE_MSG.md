# CONTINUE_MSG — 2026-11-02 r241

## 本轮完成
**C3 v3 M8-cover 独立复算回执（pfb @ main 95b17c3 pushed）**：
- 动机：r210 主分析收口后唯一未独立核验的指标是 M8-cover（覆盖率 = 冻结核验清单里模型实际答到的比例，防"少做事反而高分"的分母漏洞）。本轮不读 receipt 方法，用宽松关键词法对全部 54 run（r5 D3 18 + r6 D1/D2 36）重算。
- **关键发现 1（结构性）**：B-none（全删组件）truth=0.042 但 cover=0.913——固定分母没堵死遗漏规避漏洞，因为 truth 仍按模型自产条目打分。truth×cover 相关仅 Pearson 0.634 / Spearman 0.683（n=9 configs），联合判读必须保留，不能单报任一维。
- **关键发现 2（方法 gap）**：receipt-r6 声称 A-full/B-noevidence/B-noowner/B-2del-eo/B-sham cover=1.0，宽松复算只有 0.90-0.975；receipt-r5 声称 6/9 config cover=1.0，复算最高 0.944。方向一致（低 cover 集中在删 freeze 组），绝对值因命中规则不同有 gap——登记为方法差异非数据矛盾，但任何显著性宣称前需先对齐口径。
- **不受影响**：F1 freeze 负效应三域一致、sham≈baseline、B-2del-fo 行为污染等方向性结论全部成立（truth 值逐配置复算与 receipt 完全一致：A .929 / nofreeze .111 / none .000 等）。
- 回执 `experiments/T8-matrix/runs/c3-v3/receipt-r7-cover-recompute.json`（54 run 逐条 cover + missed 项 + by-config 表 + 相关性）。

## 当前状态
- pfb @ main 95b17c3 pushed
- decomp-bench @ main 767291a（T8 loop-state 对账已收口，Part B done ce20b23）
- 第三 seed 功效 run（~2h ninfer 算力）仍在 APPROVALS #2 等成璐放行，未获批不动算力
- G1b family_check 仍卡模型身份披露（不变）
- ninfer :8000 本轮 ping 仍超时（connection reset），llama.cpp :8099 探针同机不可达——Part C 双实例通道暂不可用

## 下一步
1. **T8 Part C 派发（P1，双阻塞待解）**：①arena decomp-bench binding 仍 403（r200 起未修，需成璐在 arena UI 重绑仓库或授权列表加 dd2003-460/decomp-bench）②ninfer 服务器 :8000/:8099 均不可达（r240 ping 超时，r241 复测 connection reset）——两个都解开才能派 Part C（C1 双实例对照需要 ninfer 行为层 + 探针层）。可自主部分：Part C 任务书可先写好落 decomp 仓 tasks/（不依赖通道），下轮直接派发。
2. **第三 seed 功效提升 run（P1，卡预算审批）**：APPROVALS #2 待批——9 configs × D1/D2 各加 seedc 共 18 run + J1/J2 双判 36 调用，n 从 6/cell 提到 9/cell。注意：本轮复算显示 n=6 时 truth×cover 相关只有 0.63，seedc 补完后应复跑本复算脚本验证联合判读稳定性。放行即派（通道用 localhost:8787 proxy，不依赖 ninfer :8000）。
3. **M8-cover 口径对齐（新导出，P2）**：receipt 方法 vs 宽松关键词法的命中规则差异需 Lead 裁定统一口径（建议：冻结集每项定义 2-3 个等价命中 pattern，assert 脚本机判），否则跨轮 cover 数值不可比。可与 seedc 同批做。
4. G1b family_check 仍卡模型身份披露（不变）
5. ACTIVE-candidates #4 ORF arXiv 手动上传 / #3 健康 strand 镜像源（需人工）