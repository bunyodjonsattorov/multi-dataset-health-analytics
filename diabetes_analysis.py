import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(".mplconfig").resolve()))

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

matplotlib.use("Agg")


def main() -> None:
    diabetes_df = pd.read_csv("cleaned_data/clean_diabetes.csv")

    print("Diabetes Health Analysis: Impact of Life Factors on Health Outcomes")
    print("=" * 60)

    plt.figure(figsize=(8, 5))
    diabetes_df.boxplot(column="BMI", by="Diabetes_012", ax=plt.gca())
    plt.suptitle("")
    plt.title("BMI Distribution by Diabetes Stage")
    plt.xlabel("Diabetes Stage (0=No, 1=Prediabetes, 2=Diabetes)")
    plt.ylabel("BMI")

    plt.tight_layout()
    plt.savefig("diabetes_health_insights.png", dpi=300, bbox_inches="tight")
    plt.close()

    print("\nKey Insights:")
    print("1. BMI increases with diabetes progression")

    diabetes_summary = diabetes_df.groupby("Diabetes_012").agg({"BMI": "mean"}).round(2)
    print("\nAverage BMI by Diabetes Stage:")
    print(diabetes_summary)

    print("\nDataset Overview:")
    print(f"- Total Records: {len(diabetes_df)}")
    print(f"- Diabetes Prevalence: {(diabetes_df['Diabetes_012'] > 0).mean() * 100:.1f}%")
    print(f"- Average BMI: {diabetes_df['BMI'].mean():.1f}")


if __name__ == "__main__":
    Path(".mplconfig").mkdir(exist_ok=True)
    main()