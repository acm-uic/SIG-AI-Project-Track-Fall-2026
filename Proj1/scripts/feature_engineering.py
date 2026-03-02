"""
File to create new features for the pokemon dataset. This includes:
- Offensive Index: Attack + Special Attack
- Defensive Index: (HP * 0.5) + Defense + Special Defense
- Speed Percentile: rank(speed) / N 
- Physical Special Bias: (attack - sp_attack) / (attack + sp_attack)
- Bulk to Speed Ratio: defense_index / speed


Testing feature engineering with different pokemon -->
Physical Offensive Index: Leafeon
Special Offensive Index: Espeon
Defense Index: Umbreon
Speed Percentile: Jolteon
Physical Special Bias: Flareon
Bulk to Speed Ratio: Vaporeon


"""

import pathlib
import pandas as pd


data_folder = pathlib.Path(__file__).resolve().parents[1] / "data"
pokemon_stats_csv = data_folder / "fully_evolved_pokemon_stats.csv"


def calculate_all_features(Series: pd.Series) -> pd.DataFrame:
    # Calculate Offensive Index (Attack + Special Attack)
    Series["offensive_index"] = Series["attack"] + Series["special-attack"]

    # Calculate Defensive Index (HP * 0.5) + Defense + Special Defense
    Series["defensive_index"] = (Series["hp"] * 0.5) + Series["defense"] + Series["special-defense"]

    # Calculate Physical Special Bias (Attack - Special Attack) / (Attack + Special Attack)
    Series["physical_special_bias"] = (Series["attack"] - Series["special-attack"]) / (Series["attack"] + Series["special-attack"])

    # Calculate Bulk to Speed Ratio (Defensive Index / Speed)
    Series["bulk_to_speed_ratio"] = Series["defensive_index"] / Series["speed"]
    
    # return Series
    return Series





if __name__ == "__main__":
    df = pd.read_csv(pokemon_stats_csv)

    pokemon = df[df["name"] == "leafeon"].iloc[0]
    print(pokemon)

    pokemon = calculate_all_features(pokemon)

    





    # print(df[["name", "offensive_index", "defensive_index", "speed_percentile", "physical_special_bias", "bulk_to_speed_ratio"]].head())

