# N300: w_ctr=0.6, w_cvr=0.4 的品类异质性分解：在二手非标品（如奢侈品/收藏品）中，CVR 权重通常高于标品，假设 w_cvr_unique = 0

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N106

## Claim

w_ctr=0.6, w_cvr=0.4 的品类异质性分解：在二手非标品（如奢侈品/收藏品）中，CVR 权重通常高于标品，假设 w_cvr_unique = 0.6, w_ctr_unique = 0.4，与标品相反；需确认目标分析平台的主要交易品类占比，若非标品占比 > 50%，则整体加权平均权重应调整为 w_ctr_avg < 0.5。

## Corrected Claim

在二手非标品（如奢侈品/收藏品）中，CVR权重可能高于标品（具体数值需根据实际业务数据校准，例如假设 w_cvr_unique > w_ctr_unique）；若非标品占比 > 50%，整体加权平均CTR权重 w_ctr_avg 可能低于 0.5（具体阈值取决于各品类的具体权重设定）。

## Evidence

[质询]该陈述包含具体的经验性参数（如非标品中CVR权重通常高于标品、具体数值0.6/0.4）以及基于品类占比的线性加权假设，这些属于特定业务场景下的经验事实或模型假设，无法从第一性原理或数学公理中严格推导出来，且缺乏通用性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该事实属于特定业务经验而非通用物理/数学定律，不适用第一性原理验证条款）

## Search Query

CTR CVR weight difference non-standard goods luxury items e-commerce ranking
