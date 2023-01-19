{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          {
            "link": {
              "data": "\"\"\"\n=====================================\nCustom tick formatter for time series\n=====================================\n\n.. redirect-from:: /gallery/text_labels_and_annotations/date_index_formatter\n.. redirect-from:: /gallery/ticks/date_index_formatter2\n\nWhen plotting daily data, e.g., financial time series, one often wants\nto leave out days on which there is no data, for instance weekends, so that\nthe data are plotted at regular intervals without extra spaces for the days\nwith no data.\nThe example shows how to use an 'index formatter' to achieve the desired plot.\n\"\"\"",
              "type": "str"
            },
            "type": "sd"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "import",
              "type": "str"
            },
            "type": "kn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy",
                  "version": "*"
                },
                "value": "numpy"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "as",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy",
                  "version": "*"
                },
                "value": "np"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "import",
              "type": "str"
            },
            "type": "kn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib",
                  "version": "*"
                },
                "value": "matplotlib"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.pyplot",
                  "version": "*"
                },
                "value": "pyplot"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "as",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.pyplot",
                  "version": "*"
                },
                "value": "plt"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "import",
              "type": "str"
            },
            "type": "kn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib",
                  "version": "*"
                },
                "value": "matplotlib"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.cbook",
                  "version": "*"
                },
                "value": "cbook"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "as",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.cbook",
                  "version": "*"
                },
                "value": "cbook"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "import",
              "type": "str"
            },
            "type": "kn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib",
                  "version": "*"
                },
                "value": "matplotlib"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.lines",
                  "version": "*"
                },
                "value": "lines"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "as",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.lines",
                  "version": "*"
                },
                "value": "ml"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "from",
              "type": "str"
            },
            "type": "kn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib",
                  "version": "*"
                },
                "value": "matplotlib"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.dates",
                  "version": "*"
                },
                "value": "dates"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "import",
              "type": "str"
            },
            "type": "kn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.dates.DateFormatter",
                  "version": "*"
                },
                "value": "DateFormatter"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.dates.DayLocator",
                  "version": "*"
                },
                "value": "DayLocator"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "from",
              "type": "str"
            },
            "type": "kn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib",
                  "version": "*"
                },
                "value": "matplotlib"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.ticker",
                  "version": "*"
                },
                "value": "ticker"
              },
              "type": "Link"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "import",
              "type": "str"
            },
            "type": "kn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.ticker.Formatter",
                  "version": "*"
                },
                "value": "Formatter"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "# Load a numpy record array from yahoo csv data with fields date, open, high,",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "# low, close, volume, adj_close from the mpl-data/sample_data directory. The",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "# record array stores the date as an np.datetime64 with a day unit ('D') in",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "# the date column (``r.date``).",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "r",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.cbook",
                  "version": "*"
                },
                "value": "cbook"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.cbook.get_sample_data",
                  "version": "*"
                },
                "value": "get_sample_data"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "goog.npz",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np_load",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "True",
              "type": "str"
            },
            "type": "kc"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "[",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "price_data",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "]",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "     ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "view",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy",
                  "version": "*"
                },
                "value": "np"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy.recarray",
                  "version": "*"
                },
                "value": "recarray"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "r",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "r",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "[",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "9",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": "]",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "  ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# get the first 9 days",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "fig",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "ax1",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "ax2",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.pyplot",
                  "version": "*"
                },
                "value": "plt"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.pyplot.subplots",
                  "version": "*"
                },
                "value": "subplots"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "nrows",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "2",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "figsize",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "6",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "6",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "                               ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "constrained_layout",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "{",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "hspace",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".15",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": "}",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "# First we'll do it the default way, with gaps on weekends",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "ax1",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "plot",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "r",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "date",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "r",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "adj_close",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "o-",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "# Highlight gaps in daily data",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy.ndarray",
                  "version": "*"
                },
                "value": "gaps"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy",
                  "version": "*"
                },
                "value": "np"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy.core.numeric.flatnonzero",
                  "version": "*"
                },
                "value": "flatnonzero"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy",
                  "version": "*"
                },
                "value": "np"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy.lib.function_base.diff",
                  "version": "*"
                },
                "value": "diff"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "r",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "date",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ">",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy",
                  "version": "*"
                },
                "value": "np"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy.timedelta64",
                  "version": "*"
                },
                "value": "timedelta64"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "1",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "D",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "for",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "gap",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "in",
              "type": "str"
            },
            "type": "ow"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "r",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "[",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "[",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "date",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "adj_close",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "]",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "]",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "[",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy",
                  "version": "*"
                },
                "value": "np"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy.core.shape_base.stack",
                  "version": "*"
                },
                "value": "stack"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy.ndarray",
                  "version": "*"
                },
                "value": "gaps"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy.ndarray",
                  "version": "*"
                },
                "value": "gaps"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "+",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "1",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "numpy",
                  "path": "numpy._ArrayOrScalarCommon.T",
                  "version": "*"
                },
                "value": "T"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "]",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "ax1",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "plot",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "gap",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "date",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "gap",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "adj_close",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "w--",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "lw",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "2",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "ax1",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "legend",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "handles",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "[",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.lines",
                  "version": "*"
                },
                "value": "ml"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.lines.Line2D",
                  "version": "*"
                },
                "value": "Line2D"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "[",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "]",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "[",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "]",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "ls",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "--",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "label",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "Gaps in daily data",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "]",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "ax1",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "set_title",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\"",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "Plot y at x Coordinates",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "\"",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "ax1",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "xaxis",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "set_major_locator",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.dates.DayLocator",
                  "version": "*"
                },
                "value": "DayLocator"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "ax1",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "xaxis",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "set_major_formatter",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.dates.DateFormatter",
                  "version": "*"
                },
                "value": "DateFormatter"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "%a",
              "type": "str"
            },
            "type": "si"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "# Next we'll write a custom index formatter. Below we will plot",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "# the data against an index that goes from 0, 1,  ... len(data).  Instead of",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "# formatting the tick marks as integers, we format as times.",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "def",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.format_date",
                  "version": "*"
                },
                "value": "format_date"
              },
              "type": "Link"
            },
            "type": "nf"
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "x",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "_",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "try",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# convert datetime64 to datetime, and use datetime's strftime:",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "return",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "r",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "date",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "[",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.round",
                  "version": "*"
                },
                "value": "round"
              },
              "type": "Link"
            },
            "type": "nb"
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "x",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "]",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "item",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "strftime",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "%a",
              "type": "str"
            },
            "type": "si"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "except",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.IndexError",
                  "version": "*"
                },
                "value": "IndexError"
              },
              "type": "Link"
            },
            "type": "ne"
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "pass",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "# Create an index plot (x defaults to range(len(y)) if omitted)",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "ax2",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "plot",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "r",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "adj_close",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "o-",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "ax2",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "set_title",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\"",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "Plot y at Index Coordinates Using Custom Formatter",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "\"",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "ax2",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "xaxis",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "set_major_formatter",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.format_date",
                  "version": "*"
                },
                "value": "format_date"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "  ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# internally creates FuncFormatter",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "#############################################################################",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "# Instead of passing a function into `.Axis.set_major_formatter` you can use",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "# any other callable, e.g. an instance of a class that implements __call__:",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "class",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.MyFormatter",
                  "version": "*"
                },
                "value": "MyFormatter"
              },
              "type": "Link"
            },
            "type": "nc"
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "matplotlib",
                  "path": "matplotlib.ticker.Formatter",
                  "version": "*"
                },
                "value": "Formatter"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "def",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.MyFormatter.__init__",
                  "version": "*"
                },
                "value": "__init__"
              },
              "type": "Link"
            },
            "type": "fm"
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.MyFormatter",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "dates",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.str",
                  "version": "*"
                },
                "value": "fmt"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "%a",
              "type": "str"
            },
            "type": "si"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.MyFormatter",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "dates",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "dates",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.MyFormatter",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.str",
                  "version": "*"
                },
                "value": "fmt"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.str",
                  "version": "*"
                },
                "value": "fmt"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "def",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.MyFormatter.__call__",
                  "version": "*"
                },
                "value": "__call__"
              },
              "type": "Link"
            },
            "type": "fm"
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.MyFormatter",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "x",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.int",
                  "version": "*"
                },
                "value": "pos"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "0",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "\"\"\"Return the label for time x at position pos.\"\"\"",
              "type": "str"
            },
            "type": "sd"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "try",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "return",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.MyFormatter",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "dates",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "[",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.round",
                  "version": "*"
                },
                "value": "round"
              },
              "type": "Link"
            },
            "type": "nb"
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "x",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "]",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "item",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "strftime",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.MyFormatter",
                  "version": "*"
                },
                "value": "self"
              },
              "type": "Link"
            },
            "type": "bp"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.str",
                  "version": "*"
                },
                "value": "fmt"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "except",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "builtins",
                  "path": "builtins.IndexError",
                  "version": "*"
                },
                "value": "IndexError"
              },
              "type": "Link"
            },
            "type": "ne"
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "pass",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          },
          {
            "link": {
              "data": "ax2",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "xaxis",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "set_major_formatter",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": {
                "anchor": null,
                "exists": true,
                "kind": "module",
                "reference": {
                  "kind": "module",
                  "module": "__main__",
                  "path": "__main__.MyFormatter",
                  "version": "*"
                },
                "value": "MyFormatter"
              },
              "type": "Link"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "r",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "date",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "%a",
              "type": "str"
            },
            "type": "si"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": "w"
          }
        ],
        "out": ""
      },
      "type": "Code2"
    },
    {
      "data": {
        "value": {
          "kind": "assets",
          "module": "matplotlib",
          "path": "ex-date_index_formatter.py-0.png",
          "version": "3.6.2"
        }
      },
      "type": "Fig"
    }
  ],
  "level": 0,
  "target": null,
  "title": null
}