import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "raw" / "marketing_utm_sample.csv"

def main():
    df = pd.read_csv(DATA_PATH)
    df['conversion_rate'] = df['conversions'] / df['sessions']
    df['cost_per_conversion'] = df['cost'] / df['conversions'].replace({0: pd.NA})
    df['revenue_per_cost'] = df['revenue'] / df['cost'].replace({0: pd.NA})
    by_source = df.groupby('utm_source', as_index=False).agg({
        'sessions':'sum','clicks':'sum','cost':'sum','conversions':'sum','revenue':'sum'
    })
    by_source['conversion_rate'] = by_source['conversions'] / by_source['sessions']
    by_source['cost_per_conversion'] = by_source['cost'] / by_source['conversions'].replace({0: pd.NA})
    by_source['revenue_per_cost'] = by_source['revenue'] / by_source['cost'].replace({0: pd.NA})
    print("\nПідсумки по джерелах:\n", by_source.sort_values('revenue_per_cost', ascending=False))

    by_campaign = df.groupby('utm_campaign', as_index=False).agg({
        'sessions':'sum','clicks':'sum','cost':'sum','conversions':'sum','revenue':'sum'
    })
    by_campaign['conversion_rate'] = by_campaign['conversions'] / by_campaign['sessions']
    by_campaign['cost_per_conversion'] = by_campaign['cost'] / by_campaign['conversions'].replace({0: pd.NA})
    by_campaign['revenue_per_cost'] = by_campaign['revenue'] / by_campaign['cost'].replace({0: pd.NA})
    print("\nПідсумки по кампаніях:\n", by_campaign.sort_values('revenue_per_cost', ascending=False))

if __name__ == "__main__":
    main()
