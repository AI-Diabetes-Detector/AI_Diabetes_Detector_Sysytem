import pandas as pd


def create_sample_time_series():

      dates = pd.date_range(
            "2026-01",
            periods=6,
            freq="M"
      )

      sample_counts = [
            10,
            12,
            11,
            14,
            16,
            15
      ]

      time_series = pd.Series(
            sample_counts,
            index=dates
      )

      return time_series


def show_time_series_information(time_series):

      print("\nSAMPLE TIME SERIES")
      print(time_series)

      print("\nMean:",time_series.mean())
      print("Minimum:",time_series.min())
      print("Maximum:",time_series.max())


def main():

      print("=" * 60)
      print("TIME SERIES ANALYSIS")
      print("=" * 60)

      print("The BRFSS 2015 diabetes dataset used by Dia Detect AI does not contain a date or time column.")
      print("A genuine time-series analysis cannot therefore be performed on the project dataset.")
      print("The following sequence is an illustrative sample only and is not taken from the BRFSS dataset.")

      time_series = create_sample_time_series()

      show_time_series_information(time_series)


if __name__ == "__main__":
      main()
