{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          [
            "\"\"\"\n==============\nInfinite lines\n==============\n\n`~.axes.Axes.axvline` and `~.axes.Axes.axhline` draw infinite vertical /\nhorizontal lines, at given *x* / *y* positions. They are usually used to mark\nspecial data values, e.g. in this example the center and limit values of the\nsigmoid function.\n\n`~.axes.Axes.axline` draws infinite straight lines in arbitrary directions.\n\"\"\"",
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
            "\n",
            "",
            ""
          ],
          [
            "t",
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
            "-",
            "",
            "o"
          ],
          [
            "10",
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
            "10",
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
            "100",
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
            "sig",
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
            "1",
            "",
            "mi"
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
            "(",
            "",
            ""
          ],
          [
            "1",
            "",
            "mi"
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
            "t",
            "builtins.tuple",
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
            "axhline",
            "matplotlib.pyplot.axhline",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "y",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
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
            "color",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "\"",
            "",
            "s2"
          ],
          [
            "black",
            null,
            "s2"
          ],
          [
            "\"",
            "",
            "s2"
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
            "linestyle",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "\"",
            "",
            "s2"
          ],
          [
            "--",
            "",
            "s2"
          ],
          [
            "\"",
            "",
            "s2"
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
            "axhline",
            "matplotlib.pyplot.axhline",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "y",
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
            "color",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "\"",
            "",
            "s2"
          ],
          [
            "black",
            null,
            "s2"
          ],
          [
            "\"",
            "",
            "s2"
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
            "linestyle",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "\"",
            "",
            "s2"
          ],
          [
            ":",
            "",
            "s2"
          ],
          [
            "\"",
            "",
            "s2"
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
            "axhline",
            "matplotlib.pyplot.axhline",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "y",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "1.0",
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
            "color",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "\"",
            "",
            "s2"
          ],
          [
            "black",
            null,
            "s2"
          ],
          [
            "\"",
            "",
            "s2"
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
            "linestyle",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "\"",
            "",
            "s2"
          ],
          [
            "--",
            "",
            "s2"
          ],
          [
            "\"",
            "",
            "s2"
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
            "axvline",
            "matplotlib.pyplot.axvline",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "color",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "\"",
            "",
            "s2"
          ],
          [
            "grey",
            null,
            "s2"
          ],
          [
            "\"",
            "",
            "s2"
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
            "axline",
            "matplotlib.pyplot.axline",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "(",
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
            "slope",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "0.25",
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
            "color",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "\"",
            "",
            "s2"
          ],
          [
            "black",
            null,
            "s2"
          ],
          [
            "\"",
            "",
            "s2"
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
            "linestyle",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "(",
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
            "(",
            "",
            ""
          ],
          [
            "5",
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
            "5",
            "",
            "mi"
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
            "plot",
            "matplotlib.pyplot.plot",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "t",
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
            "sig",
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
            "linewidth",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
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
            "r",
            "builtins.str",
            "sa"
          ],
          [
            "\"",
            "",
            "s2"
          ],
          [
            "$",
            "",
            "s2"
          ],
          [
            "\\",
            "",
            "s2"
          ],
          [
            "sigma(t) = ",
            "",
            "s2"
          ],
          [
            "\\",
            "",
            "s2"
          ],
          [
            "frac",
            null,
            "s2"
          ],
          [
            "{1}",
            "",
            "si"
          ],
          [
            "{",
            "",
            "s2"
          ],
          [
            "1 + e^",
            "",
            "s2"
          ],
          [
            "{",
            "",
            "s2"
          ],
          [
            "-t}}$",
            "",
            "s2"
          ],
          [
            "\"",
            "",
            "s2"
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
            "xlim",
            "matplotlib.pyplot.xlim",
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
            "10",
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
            "xlabel",
            "matplotlib.pyplot.xlabel",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "\"",
            "",
            "s2"
          ],
          [
            "t",
            null,
            "s2"
          ],
          [
            "\"",
            "",
            "s2"
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
            "14",
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
            "# `~.axes.Axes.axline` can also be used with a ``transform`` parameter, which",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# applies to the point, but not to the slope. This can be useful for drawing",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# diagonal grid lines with a fixed slope, which stay in place when the",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# plot limits are moved.",
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
            "for",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "pos",
            "numpy.ndarray",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "in",
            null,
            "ow"
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
            "axline",
            "matplotlib.pyplot.axline",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "pos",
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
            "0",
            "",
            "mi"
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
            "slope",
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
            "color",
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
            "k",
            null,
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
            "transform",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
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
            "gca",
            "matplotlib.pyplot.gca",
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
            ".",
            "",
            "o"
          ],
          [
            "transAxes",
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
            "ylim",
            "matplotlib.pyplot.ylim",
            ""
          ],
          [
            "(",
            "",
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
            "xlim",
            "matplotlib.pyplot.xlim",
            ""
          ],
          [
            "(",
            "",
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
            "#    - `matplotlib.axes.Axes.axhline` / `matplotlib.pyplot.axhline`",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "#    - `matplotlib.axes.Axes.axvline` / `matplotlib.pyplot.axvline`",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "#    - `matplotlib.axes.Axes.axline` / `matplotlib.pyplot.axline`",
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
        "value": "ex-axline.py-0.png"
      },
      "type": "Fig"
    }
  ],
  "title": null
}