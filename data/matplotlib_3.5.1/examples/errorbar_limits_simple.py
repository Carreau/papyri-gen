{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          [
            "\"\"\"\n========================\nErrorbar limit selection\n========================\n\nIllustration of selectively drawing lower and/or upper limit symbols on\nerrorbars using the parameters ``uplims``, ``lolims`` of `~.pyplot.errorbar`.\n\nAlternatively, you can use 2xN values to draw errorbars in only one direction.\n\"\"\"",
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
            "figure",
            "matplotlib.pyplot.figure",
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
            "10",
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
            "y",
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
            "2.5",
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
            "sin",
            "numpy.ufunc",
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
            "20",
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
            "pi",
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
            "yerr",
            "builtins.tuple",
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
            "linspace",
            "numpy.core.function_base.linspace",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "0.05",
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
            "10",
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
            "errorbar",
            "matplotlib.pyplot.errorbar",
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
            "builtins.float",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "+",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "3",
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
            "yerr",
            "builtins.tuple",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "yerr",
            "builtins.tuple",
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
            "label",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "both limits (default)",
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
            "errorbar",
            "matplotlib.pyplot.errorbar",
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
            "builtins.float",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "+",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "2",
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
            "yerr",
            "builtins.tuple",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "yerr",
            "builtins.tuple",
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
            "uplims",
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
            "label",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "uplims=True",
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
            "errorbar",
            "matplotlib.pyplot.errorbar",
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
            "builtins.float",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "+",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "1",
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
            "yerr",
            "builtins.tuple",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "yerr",
            "builtins.tuple",
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
            "uplims",
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
            "lolims",
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
            ",",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "             ",
            "",
            ""
          ],
          [
            "label",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "uplims=True, lolims=True",
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
            "upperlimits",
            "builtins.list",
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
            "[",
            "",
            ""
          ],
          [
            "True",
            null,
            "kc"
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
            "False",
            null,
            "kc"
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
            "5",
            "",
            "mi"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "lowerlimits",
            "builtins.list",
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
            "[",
            "",
            ""
          ],
          [
            "False",
            null,
            "kc"
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
            "True",
            null,
            "kc"
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
            "5",
            "",
            "mi"
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
            "errorbar",
            "matplotlib.pyplot.errorbar",
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
            "yerr",
            "builtins.tuple",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "yerr",
            "builtins.tuple",
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
            "uplims",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "upperlimits",
            "builtins.list",
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
            "lolims",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "lowerlimits",
            "builtins.list",
            ""
          ],
          [
            ",",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "             ",
            "",
            ""
          ],
          [
            "label",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "subsets of uplims and lolims",
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
            "legend",
            "matplotlib.pyplot.legend",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "loc",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "lower right",
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
            "\n",
            "",
            ""
          ],
          [
            "##############################################################################",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# Similarly ``xuplims`` and ``xlolims`` can be used on the horizontal ``xerr``",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# errorbars.",
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
            "fig",
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
            "figure",
            "matplotlib.pyplot.figure",
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
            "x",
            "builtins.NoneType",
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
            "10",
            "",
            "mi"
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
            "10",
            "",
            "mi"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "y",
            "builtins.NoneType",
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
            "x",
            "builtins.NoneType",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "+",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "0.1",
            "",
            "mf"
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
            "errorbar",
            "matplotlib.pyplot.errorbar",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "x",
            "builtins.NoneType",
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
            "builtins.NoneType",
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
            "xlolims",
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
            "label",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "xlolims=True",
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
            "y",
            "builtins.NoneType",
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
            "x",
            "builtins.NoneType",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "+",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "0.1",
            "",
            "mf"
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
            "3",
            "",
            "mi"
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
            "errorbar",
            "matplotlib.pyplot.errorbar",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "x",
            "builtins.NoneType",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "+",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "0.6",
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
            "y",
            "builtins.NoneType",
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
            "xuplims",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "upperlimits",
            "builtins.list",
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
            "xlolims",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "lowerlimits",
            "builtins.list",
            ""
          ],
          [
            ",",
            "",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "             ",
            "",
            ""
          ],
          [
            "label",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "subsets of xuplims and xlolims",
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
            "y",
            "builtins.NoneType",
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
            "x",
            "builtins.NoneType",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "+",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "0.1",
            "",
            "mf"
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
            "4",
            "",
            "mi"
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
            "errorbar",
            "matplotlib.pyplot.errorbar",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "x",
            "builtins.NoneType",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "+",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "1.2",
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
            "y",
            "builtins.NoneType",
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
            "xuplims",
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
            "label",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "xuplims=True",
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
            "legend",
            "matplotlib.pyplot.legend",
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
            "##############################################################################",
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
        "value": "ex-errorbar_limits_simple.py-0.png"
      },
      "type": "Fig"
    },
    {
      "data": {
        "value": "ex-errorbar_limits_simple.py-1.png"
      },
      "type": "Fig"
    }
  ],
  "title": null
}