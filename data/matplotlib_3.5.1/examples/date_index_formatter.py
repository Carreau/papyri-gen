{
  "children": [
    {
      "data": {
        "ce_status": "None",
        "entries": [
          [
            "\"\"\"\nWhen plotting time series, eg financial time series, one often wants\nto leave out days on which there is no data, eh weekends.  The example\nbelow shows how to use an 'index formatter' to achieve the desired plot\n\"\"\"",
            "",
            "sd"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "from",
            null,
            "kn"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "__future__",
            "__future__",
            "nn"
          ],
          [
            " ",
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
            "print_function",
            "__future__._Feature",
            ""
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
            "mlab",
            "matplotlib.mlab",
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
            "mlab",
            "matplotlib.mlab",
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
            "ticker",
            "matplotlib.ticker",
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
            "ticker",
            "matplotlib.ticker",
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
            "datafile",
            "io.TextIOWrapper",
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
            "aapl.csv",
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
            "asfileobj",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "False",
            null,
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
            "print",
            "builtins.print",
            "nb"
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
            "'",
            "",
            "s1"
          ],
          [
            "loading ",
            "",
            "s1"
          ],
          [
            "%s",
            "",
            "si"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "%",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "datafile",
            "io.TextIOWrapper",
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
            "r",
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
            "mlab",
            "matplotlib.mlab",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "csv2rec",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "datafile",
            "io.TextIOWrapper",
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
            "r",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "sort",
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
            "r",
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
            "r",
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
            "30",
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
            "# get the last 30 days",
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
            "\n",
            "",
            ""
          ],
          [
            "# first we'll do it the default way, with gaps on weekends",
            "",
            "c1"
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
            "plot",
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
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "date",
            null,
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
            "r",
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
            "'",
            "",
            "s1"
          ],
          [
            "o-",
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
            "autofmt_xdate",
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
            "# next we'll write a custom formatter",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "N",
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
            "len",
            "builtins.len",
            "nb"
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "r",
            null,
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
            "ind",
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
            "arange",
            "numpy.arange",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "N",
            "builtins.int",
            ""
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "  ",
            "",
            ""
          ],
          [
            "# the evenly spaced plot indices",
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
            "def",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "format_date",
            "__main__.format_date",
            "nf"
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "x",
            null,
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
            "pos",
            "builtins.NoneType",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "None",
            null,
            "kc"
          ],
          [
            ")",
            "",
            ""
          ],
          [
            ":",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "    ",
            "",
            ""
          ],
          [
            "thisind",
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
            "clip",
            "numpy.core.fromnumeric.clip",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "int",
            "builtins.int",
            "nb"
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "x",
            null,
            ""
          ],
          [
            "+",
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
            "0",
            "",
            "mi"
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
            "N",
            "builtins.int",
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
            "    ",
            "",
            ""
          ],
          [
            "return",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "r",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "date",
            null,
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            "thisind",
            null,
            ""
          ],
          [
            "]",
            "",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "strftime",
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
            "%",
            "",
            "s1"
          ],
          [
            "Y-",
            "",
            "s1"
          ],
          [
            "%",
            "",
            "s1"
          ],
          [
            "m-",
            "",
            "s1"
          ],
          [
            "%d",
            "",
            "si"
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
            "plot",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "ind",
            "numpy.ndarray",
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
            "r",
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
            "'",
            "",
            "s1"
          ],
          [
            "o-",
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
            "xaxis",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "set_major_formatter",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "ticker",
            "matplotlib.ticker",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "FuncFormatter",
            "matplotlib.ticker.FuncFormatter",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "format_date",
            "__main__.format_date",
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
            "autofmt_xdate",
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
    }
  ],
  "title": null
}