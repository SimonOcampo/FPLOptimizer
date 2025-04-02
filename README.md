# fploptimizer
Fantasy Premier League Optimizer

# 📊 FPL Optimizer — Week 1 Progress Tracker

🎯 **Goal for this week:** Complete all data scraping and cleaning to prepare a training-ready dataset for the prediction model and team optimization engine.

---

## ✅ Task Checklist

### 1. Raw Data Collection (API)
- [Done] `fetch_data.py` pulls:
  - [Done] `bootstrap-static.json`
  - [Done] `fixtures.json`
  - [Done] `events.json`
- [ ] Add script to fetch `/api/element-summary/{player_id}/`
- 📁 Output: `data/`

**Owner:** `@TeammateA`

---

### 2. Custom Fixture Difficulty Table
- [ ] Use `fixtures.json` and `teams` data
- [ ] Add opponent attack/defense strength per fixture
- [ ] Normalize or rescale strengths if needed
- 📁 Output: `cleaned_data/fixture_difficulty.csv`

**Owner:** `@TeammateB`

---

### 3. Clean & Enrich Player Dataset
- [Done] Load player data from `elements`
- [ ] Add:
  - [Done] `team_name`
  - [Done] `position` (via element_type)
  - [ ] `next_fixture`, opponent strength (join with fixture table)
  - [ ] Other useful stats (`form`, `value_per_million`) #Look for minutes played, XGoals + XAssists, G+A, Shots
- 📁 Output: `cleaned_data/players_cleaned.csv`

**Owner:** `@TeammateC`

---

### 4. Player Match History
- [ ] Fetch `/api/element-summary/{player_id}/`
- [ ] Build table of match-level stats per player
- [ ] Calculate rolling stats (form last 3 GWs, home vs away, etc.)
- 📁 Output: `cleaned_data/player_match_history.csv`

**Owner:** `@TeammateD`

---

### 5. Final Data Integration
- [ ] Merge player + fixture difficulty data
- [ ] Validate all key columns exist:
