import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(".mplconfig").resolve()))

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

matplotlib.use("Agg")


def main() -> None:
    heart_df = pd.read_csv("cleaned_data/clean_heart.csv")

    print("Heart Disease Analysis: Impact of Life Factors on Health Outcomes")
    print("=" * 60)

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    heart_df.boxplot(column="Cholesterol", by="Heart Disease", ax=plt.gca())
    plt.suptitle("")
    plt.title("Cholesterol Distribution by Heart Disease")
    plt.xlabel("Heart Disease Status")
    plt.ylabel("Cholesterol (mg/dl)")

    plt.subplot(1, 3, 2)
    heart_df["Age_Group"] = pd.cut(
        heart_df["Age"], bins=[0, 50, 60, 70, 100], labels=["Under 50", "50-60", "60-70", "70+"]
    )
    age_heart = heart_df.groupby("Age_Group", observed=False)["Heart Disease"].apply(lambda x: (x == "Presence").mean())
    age_heart.plot(kind="bar", color="orange", alpha=0.7, ax=plt.gca())
    plt.title("Heart Disease Risk by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Heart Disease Rate")
    plt.xticks(rotation=45)

    plt.subplot(1, 3, 3)
    heart_df.boxplot(column="BP", by="Heart Disease", ax=plt.gca())
    plt.suptitle("")
    plt.title("Blood Pressure Distribution by Heart Disease")
    plt.xlabel("Heart Disease Status")
    plt.ylabel("Blood Pressure (mmHg)")

    plt.tight_layout()
    plt.savefig("heart_disease_insights.png", dpi=300, bbox_inches="tight")
    plt.close()

    print("\nKey Insights:")
    print("1. Higher cholesterol levels associated with heart disease")
    print("2. Heart disease risk increases significantly with age")
    print("3. Higher blood pressure associated with heart disease")

    heart_summary = heart_df.groupby("Heart Disease").agg({"Cholesterol": "mean", "BP": "mean", "Age": "mean"}).round(2)
    print("\nAverage Values by Heart Disease Status:")
    print(heart_summary)

    print("\nDataset Overview:")
    print(f"- Total Records: {len(heart_df)}")
    print(f"- Heart Disease Rate: {(heart_df['Heart Disease'] == 'Presence').mean() * 100:.1f}%")
    print(f"- Average Cholesterol: {heart_df['Cholesterol'].mean():.0f} mg/dl")
    print(f"- Average Blood Pressure: {heart_df['BP'].mean():.0f} mmHg")


if __name__ == "__main__":
    Path(".mplconfig").mkdir(exist_ok=True)
    main()