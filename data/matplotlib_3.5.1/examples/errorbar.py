{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          [
            "\"\"\"\n=================\nErrorbar function\n=================\n\nThis exhibits the most basic use of the error bar method.\nIn this case, constant values are provided for the error\nin both the x- and y-directions.\n\"\"\"",
            "",
            "sd"
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
            "\n",
            "",
            ""
          ],
          [
            "# example data",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "x",
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
            "0.1",
            "",
            "mf"
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
            "4",
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
            "y",
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
            "exp",
            "numpy.ufunc",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "-",
            "",
            "o"
          ],
          [
            "x",
            "numpy.ndarray",
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
            "errorbar",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "x",
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
            "y",
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
            "xerr",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "0.2",
            "",
            "mf"
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
            "yerr",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "0.4",
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
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "#############################################################################",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "#",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# .. admonition:: References",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "#",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "#    The use of the following functions, methods, classes and modules is shown",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "#    in this example:",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "#",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "#    - `matplotlib.axes.Axes.errorbar` / `matplotlib.pyplot.errorbar`",
            "",
            "c1"
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
        "value": "ex-errorbar.py-0.png"
      },
      "type": "Fig"
    }
  ],
  "title": null
}