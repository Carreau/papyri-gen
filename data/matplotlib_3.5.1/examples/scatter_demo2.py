{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          [
            "\"\"\"\n=============\nScatter Demo2\n=============\n\nDemo of scatter plot with varying marker colors and sizes.\n\"\"\"",
            "",
            "sd"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "import",
            null,
            "kn"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "numpy",
            "numpy",
            "nn"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "as",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "np",
            "numpy",
            "nn"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "import",
            null,
            "kn"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "matplotlib",
            "matplotlib",
            "nn"
          ],
          [
            ".",
            "",
            "nn"
          ],
          [
            "pyplot",
            "matplotlib.pyplot",
            "nn"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "as",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "plt",
            "matplotlib.pyplot",
            "nn"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "import",
            null,
            "kn"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "matplotlib",
            "matplotlib",
            "nn"
          ],
          [
            ".",
            "",
            "nn"
          ],
          [
            "cbook",
            "matplotlib.cbook",
            "nn"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "as",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "cbook",
            "matplotlib.cbook",
            "nn"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# Load a numpy record array from yahoo csv data with fields date, open, close,",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# volume, adj_close from the mpl-data/example directory. The record array",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# stores the date as an np.datetime64 with a day unit ('D') in the date column.",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "price_data",
            null,
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "cbook",
            "matplotlib.cbook",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "get_sample_data",
            "matplotlib.cbook.get_sample_data",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "goog.npz",
            "",
            "s1"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            ",",
            "",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "np_load",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "True",
            null,
            "kc"
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "price_data",
            null,
            "s1"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "]",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "              ",
            "",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "view",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "np",
            "numpy",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "recarray",
            "numpy.recarray",
            ""
          ],
          [
            ")",
            "",
            ""
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "price_data",
            null,
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "price_data",
            null,
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            "-",
            "",
            "o"
          ],
          [
            "250",
            "",
            "mi"
          ],
          [
            ":",
            "",
            ""
          ],
          [
            "]",
            "",
            ""
          ],
          [
            "  ",
            "",
            ""
          ],
          [
            "# get the most recent 250 trading days",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "delta1",
            "numpy.ndarray",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "np",
            "numpy",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "diff",
            "numpy.lib.function_base.diff",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "price_data",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "adj_close",
            null,
            ""
          ],
          [
            ")",
            "",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "/",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "price_data",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "adj_close",
            null,
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            ":",
            "",
            ""
          ],
          [
            "-",
            "",
            "o"
          ],
          [
            "1",
            "",
            "mi"
          ],
          [
            "]",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# Marker size in units of points^2",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "volume",
            "builtins.int",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "15",
            "",
            "mi"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "*",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "price_data",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "volume",
            null,
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            ":",
            "",
            ""
          ],
          [
            "-",
            "",
            "o"
          ],
          [
            "2",
            "",
            "mi"
          ],
          [
            "]",
            "",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "/",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "price_data",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "volume",
            null,
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            "0",
            "",
            "mi"
          ],
          [
            "]",
            "",
            ""
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "*",
            "",
            "o"
          ],
          [
            "*",
            "",
            "o"
          ],
          [
            "2",
            "",
            "mi"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "close",
            "builtins.float",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "0.003",
            "",
            "mf"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "*",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "price_data",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "close",
            null,
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            ":",
            "",
            ""
          ],
          [
            "-",
            "",
            "o"
          ],
          [
            "2",
            "",
            "mi"
          ],
          [
            "]",
            "",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "/",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "0.003",
            "",
            "mf"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "*",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "price_data",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "open",
            null,
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            ":",
            "",
            ""
          ],
          [
            "-",
            "",
            "o"
          ],
          [
            "2",
            "",
            "mi"
          ],
          [
            "]",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "fig",
            "builtins.int",
            ""
          ],
          [
            ",",
            "",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "ax",
            null,
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "plt",
            "matplotlib.pyplot",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "subplots",
            "matplotlib.pyplot.subplots",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "ax",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "scatter",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "delta1",
            "numpy.ndarray",
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            ":",
            "",
            ""
          ],
          [
            "-",
            "",
            "o"
          ],
          [
            "1",
            "",
            "mi"
          ],
          [
            "]",
            "",
            ""
          ],
          [
            ",",
            "",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "delta1",
            "numpy.ndarray",
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            "1",
            "",
            "mi"
          ],
          [
            ":",
            "",
            ""
          ],
          [
            "]",
            "",
            ""
          ],
          [
            ",",
            "",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "c",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "close",
            "builtins.float",
            ""
          ],
          [
            ",",
            "",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "s",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "volume",
            "builtins.int",
            ""
          ],
          [
            ",",
            "",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "alpha",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "0.5",
            "",
            "mf"
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "ax",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "set_xlabel",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "r",
            "builtins.str",
            "sa"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "$",
            "",
            "s1"
          ],
          [
            "\\",
            "",
            "s1"
          ],
          [
            "Delta_i$",
            "",
            "s1"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            ",",
            "",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "fontsize",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "15",
            "",
            "mi"
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "ax",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "set_ylabel",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "r",
            "builtins.str",
            "sa"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "$",
            "",
            "s1"
          ],
          [
            "\\",
            "",
            "s1"
          ],
          [
            "Delta_",
            null,
            "s1"
          ],
          [
            "{",
            "",
            "s1"
          ],
          [
            "i+1}$",
            "",
            "s1"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            ",",
            "",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "fontsize",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "15",
            "",
            "mi"
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "ax",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "set_title",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "Volume and percent change",
            "",
            "s1"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "ax",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "grid",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "True",
            "builtins.bool",
            "kc"
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "fig",
            "builtins.int",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "tight_layout",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "plt",
            "matplotlib.pyplot",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "show",
            "matplotlib.pyplot.show",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ]
        ],
        "out": ""
      },
      "type": "Code"
    },
    {
      "data": {
        "value": "ex-scatter_demo2.py-0.png"
      },
      "type": "Fig"
    }
  ],
  "title": null
}