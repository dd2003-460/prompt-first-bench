# N266: Opportunity_Cost_per_hour 的精确分解：在本地工作站场景下，Opportunity_Cost ≈ (Electricity_Cost_p

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85, N86, N87

## Claim

Opportunity_Cost_per_hour 的精确分解：在本地工作站场景下，Opportunity_Cost ≈ (Electricity_Cost_per_hour + Depreciation_Cost_per_hour)；其中 Electricity_Cost_per_hour = TDP * 0.1 USD/kWh (如 4090: 0.045 USD/h)，Depreciation_Cost_per_hour = CapEx / (Useful_Life_Years * 8760) (如 4090 $1600/3y: 0.061 USD/h)；总和约 $0.106/hour，而非 N85 假设的 $10/hour（$10/hour 仅适用于高价值云端多租户服务，本地单用户场景应修正为 ~$0.11/hour）。

## Corrected Claim

Opportunity_Cost_per_hour 的精确分解：在本地工作站场景下，Opportunity_Cost ≈ (Electricity_Cost_per_hour + Depreciation_Cost_per_hour)；其中 Electricity_Cost_per_hour = TDP * 0.1 USD/kWh (如 4090: 0.045 USD/h)，Depreciation_Cost_per_hour = CapEx / (Useful_Life_Years * 8760) (如 4090 $1600/3y: 0.061 USD/h)；总和约 $0.106/hour，而非 N85 假设的 $10/hour（$10/hour 仅适用于高价值云端多租户服务，本地单用户场景应修正为 ~$0.11/hour）。

## Evidence

先验知识/题面给定，逻辑校验通过：电费计算（450W*0.1$/kWh=0.045$/h）与折旧计算（1600$/3y/8760h≈0.061$/h）数学自洽，总和约0.106$/h，符合本地工作站低边际成本的经济直觉，且明确区分了云端高价值场景。
