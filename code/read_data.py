import csv
import numpy as np
import pandas as pd
import datetime
from pathlib import Path
import matplotlib as mpl
from matplotlib import rcParams
import matplotlib.pyplot as plt
from scipy import stats

_colors = [
    (0, 0, 0),
    (0.9, 0.6, 0),
    (0.35, 0.7, 0.9),
    (0, 0.6, 0.5),
    (0.95, 0.9, 0.25),
    (0, 0.45, 0.7),
    (0.8, 0.4, 0),
    (0.8, 0.6, 0.7),
]


def plot_hr(df, mpl_dates, plotdir):
    """plot the resting heart rate"""
    fig, axarr = plt.subplots(
        1, 2, sharey=True, figsize=(7, 5), gridspec_kw={"width_ratios": [3, 1]}
    )
    # fig, axarr = plt.subplots(1, 2, sharey=True, figsize=(7, 5))
    fig.subplots_adjust(wspace=0, bottom=0.15)
    axarr[0].scatter(mpl_dates, df["HR"], color=_colors[0])
    axarr[0].xaxis.set_major_formatter(mpl.dates.DateFormatter("%Y-%m-%d"))
    axarr[0].set_xlabel("date")
    axarr[0].set_ylabel("Resting HR")
    # xlabels = ax.get_xticklabels()
    # axarr[0].set_xticklabels(
    #     xlabels,
    #     fontsize="x-small",
    #     rotation=15,
    #     ha="right",
    #     rotation_mode="anchor",
    # )
    axarr[0].tick_params(axis="x", rotation=15)
    axarr[0].grid(True, alpha=0.3)
    axarr[0].xaxis.set_major_formatter(mpl.dates.DateFormatter("%Y-%m"))
    axarr[0].xaxis.set_major_locator(mpl.dates.MonthLocator())

    # Calculate the kernel-density estimate to plot a smooth function over the histogram
    # xvalues = np.linspace(np.min(df["HR"]) - 10, np.max(df["HR"]) + 10)
    xvalues = np.linspace(np.min(df["HR"]) * 0.95, np.max(df["HR"]) * 1.05)
    yvalues = stats.gaussian_kde(df["HR"]).evaluate(xvalues)

    axarr[1].hist(
        df["HR"], bins=20, orientation="horizontal", density=True, color=_colors[2]
    )
    axarr[1].plot(yvalues, xvalues, color=_colors[1])
    axarr[1].set_xticks([])

    plt.savefig(plotdir / Path("hr_against_time.pdf"))
    plt.close()
    return


def plot_hrvpoints(df, mpl_dates, plotdir):
    """plot the HRV recovery points"""
    fig, axarr = plt.subplots(
        1, 2, sharey=True, figsize=(7, 5), gridspec_kw={"width_ratios": [3, 1]}
    )
    fig.subplots_adjust(wspace=0, bottom=0.15)

    # ax = fig.add_subplot(121)
    axarr[0].scatter(mpl_dates, df["HRV4T_Recovery_Points"], color=_colors[0])
    axarr[0].xaxis.set_major_formatter(mpl.dates.DateFormatter("%Y-%m-%d"))
    axarr[0].set_xlabel("date")
    axarr[0].set_ylabel("HRV recovery points")
    # xlabels = axarr[0].get_xticklabels()
    # axarr[0].set_xticklabels(
    #     xlabels,
    #     fontsize="x-small",
    #     rotation=15,
    #     ha="right",
    #     rotation_mode="anchor",
    # )
    axarr[0].tick_params(axis="x", rotation=15)
    # plt.xticks(rotation=15)
    axarr[0].grid(True, alpha=0.3)
    axarr[0].xaxis.set_major_formatter(mpl.dates.DateFormatter("%Y-%m"))
    axarr[0].xaxis.set_major_locator(mpl.dates.MonthLocator())

    # Calculate the kernel-density estimate to plot a smooth function over the histogram
    xvalues = np.linspace(
        np.min(df["HRV4T_Recovery_Points"]) * 0.95,
        np.max(df["HRV4T_Recovery_Points"]) * 1.05,
    )
    yvalues = stats.gaussian_kde(df["HRV4T_Recovery_Points"]).evaluate(xvalues)

    axarr[1].hist(
        df["HRV4T_Recovery_Points"],
        bins=20,
        orientation="horizontal",
        density=True,
        color=_colors[2],
    )
    axarr[1].plot(yvalues, xvalues, color=_colors[1])
    axarr[1].set_xticks([])

    # histogram = np.histogram(df["HRV4T_Recovery_Points"])
    # print(histogram[0], histogram[1])
    # print(len(histogram[0]), len(histogram[1]))
    # axarr[1].barh(histogram[0], histogram[1])
    # d = plt.make_axes_locatable(ax)
    # ax2 = d.new_horizontal("10%")

    # axarr[1] = fig.add_subplot(122, sharey=ax, aspect=1)
    # axarr[1].set_yticks([], majorticks=False)
    # plt.subplots_adjust(
    #     left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.35
    # )
    # plt.subplots_adjust(
    #     left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0, hspace=0.0
    # )

    plt.savefig(plotdir / Path("hrv_against_time.pdf"))
    plt.close()
    return


def plot_rmssd(df, mpl_dates, plotdir):
    """plot the rMSSD measurements"""

    fig, axarr = plt.subplots(
        1, 2, sharey=True, figsize=(7, 5), gridspec_kw={"width_ratios": [3, 1]}
    )
    fig.subplots_adjust(wspace=0, bottom=0.15)
    axarr[0].scatter(mpl_dates, df["rMSSD"], color=_colors[0])
    axarr[0].xaxis.set_major_formatter(mpl.dates.DateFormatter("%Y-%m-%d"))
    axarr[0].set_xlabel("date")
    axarr[0].set_ylabel("rMSSD")
    # xlabels = ax.get_xticklabels()
    # axarr[0].set_xticklabels(
    #     xlabels,
    #     fontsize="x-small",
    #     rotation=15,
    #     ha="right",
    #     rotation_mode="anchor",
    # )
    axarr[0].tick_params(axis="x", rotation=15)
    axarr[0].grid(True, alpha=0.3)
    axarr[0].xaxis.set_major_formatter(mpl.dates.DateFormatter("%Y-%m"))
    axarr[0].xaxis.set_major_locator(mpl.dates.MonthLocator())

    # Calculate the kernel-density estimate to plot a smooth function over the histogram
    xvalues = np.linspace(np.min(df["rMSSD"]) * 0.95, np.max(df["rMSSD"]) * 1.05)
    yvalues = stats.gaussian_kde(df["rMSSD"]).evaluate(xvalues)

    axarr[1].hist(
        df["rMSSD"], bins=20, orientation="horizontal", density=True, color=_colors[2]
    )
    axarr[1].plot(yvalues, xvalues, color=_colors[1])
    axarr[1].set_xticks([])

    plt.savefig(plotdir / Path("rmssd_against_time.pdf"))
    plt.savefig(plotdir / Path("rmssd_against_time.png"), dpi=100)
    plt.close()
    return


def main():
    """Read the csv data file and plot some things from it"""

    plt.rc("text", usetex=True)
    # rcParams.update({"figure.autolayout": True})

    datadir = Path.home() / Path("Dropbox/Apps/HRV4Training/")
    analysisdir = Path.home() / Path("Dropbox/code/hrv4t_analysis/")
    plotdir = analysisdir / Path("plots/")
    data_file_name = datadir / Path("MyMeasurements_Android.csv")

    df = pd.read_csv(data_file_name, header=0, index_col=False)
    # print(df)
    # print([key for key in df])

    df.columns = df.columns.str.replace(" ", "")

    df = df.drop(df.index[[3, 44]], axis=0)
    df = df.drop(df.index[np.where(df["HR"] == 0)], axis=0)

    print([key for key in df])

    date_values = [datetime.datetime.strptime(date, "%Y-%d-%m") for date in df["date"]]
    mpl_dates = mpl.dates.date2num(date_values)

    plot_hr(df, mpl_dates, plotdir)
    plot_hrvpoints(df, mpl_dates, plotdir)
    plot_rmssd(df, mpl_dates, plotdir)


if __name__ == "__main__":
    main()
