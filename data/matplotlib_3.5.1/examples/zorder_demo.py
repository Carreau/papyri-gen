{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          [
            "\"\"\"\n===========\nZorder Demo\n===========\n\nThe drawing order of artists is determined by their ``zorder`` attribute, which\nis a floating point number. Artists with higher ``zorder`` are drawn on top.\nYou can change the order for individual artists by setting their ``zorder``.\nThe default value depends on the type of the Artist:\n\n================================================================    =======\nArtist                                                              Z-order\n================================================================    =======\nImages (`.AxesImage`, `.FigureImage`, `.BboxImage`)                 0\n`.Patch`, `.PatchCollection`                                        1\n`.Line2D`, `.LineCollection` (including minor ticks, grid lines)    2\nMajor ticks                                                         2.01\n`.Text` (including axes labels and titles)                          3\n`.Legend`                                                           5\n================================================================    =======\n\nAny call to a plotting method can set a value for the zorder of that particular\nitem explicitly.\n\n.. note::\n\n   `~.axes.Axes.set_axisbelow` and :rc:`axes.axisbelow` are convenient helpers\n   for setting the zorder of ticks and grid lines.\n\nDrawing is done per `~.axes.Axes` at a time. If you have overlapping Axes, all\nelements of the second Axes are drawn on top of the first Axes, irrespective of\ntheir relative zorder.\n\"\"\"",
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
            "\n",
            "",
            ""
          ],
          [
            "r",
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
            "0.3",
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
            "30",
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
            "theta",
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
            "4",
            "",
            "mi"
          ],
          [
            "*",
            "",
            "o"
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
            "30",
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
            "x",
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
            "r",
            "builtins.tuple",
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
            "theta",
            "builtins.tuple",
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
            "y",
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
            "r",
            "builtins.tuple",
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
            "cos",
            "numpy.ufunc",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "theta",
            "builtins.tuple",
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
            "###############################################################################",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# The following example contains a `.Line2D` created by `~.axes.Axes.plot()`",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# and the dots (a `.PatchCollection`) created by `~.axes.Axes.scatter()`.",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# Hence, by default the dots are below the line (first subplot).",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# In the second subplot, the ``zorder`` is set explicitly to move the dots",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# on top of the line.",
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
            "ax1",
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
            "ax2",
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
            "figsize",
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
            "6",
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
            "3.2",
            "",
            "mf"
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
            "ax1",
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
            "x",
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
            "y",
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
            "'",
            "",
            "s1"
          ],
          [
            "C3",
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
            "lw",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "3",
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
            "ax1",
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
            "x",
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
            "y",
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
            "120",
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
            "ax1",
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
            "Lines on top of dots",
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
            "ax2",
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
            "x",
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
            "y",
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
            "'",
            "",
            "s1"
          ],
          [
            "C3",
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
            "lw",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "3",
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
            "ax2",
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
            "x",
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
            "y",
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
            "120",
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
            "zorder",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "2.5",
            "",
            "mf"
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
            "# move dots on top of line",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "ax2",
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
            "Dots on top of lines",
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
            "tight_layout",
            "matplotlib.pyplot.tight_layout",
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
            "###############################################################################",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# Many functions that create a visible object accepts a ``zorder`` parameter.",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# Alternatively, you can call ``set_order()`` on the created object later.",
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
            "x",
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
            "7.5",
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
            "rcParams",
            "matplotlib.RcParams",
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
            "lines.linewidth",
            "",
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
            "x",
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
            "builtins.tuple",
            ""
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
            "zorder=2",
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
            "zorder",
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
            "# bottom",
            "",
            "c1"
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
            "x",
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
            "builtins.tuple",
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
            "zorder=3",
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
            "  ",
            "",
            ""
          ],
          [
            "zorder",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "3",
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
            "zorder=2.5",
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
            "lightgrey",
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
            "zorder",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "2.5",
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
            "title",
            "matplotlib.pyplot.title",
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
            "Custom order of elements",
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
            "l",
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
            "upper right",
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
            "l",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "set_zorder",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "2.5",
            "",
            "mf"
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
            "# legend between blue and orange line",
            "",
            "c1"
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
        "value": "ex-zorder_demo.py-0.png"
      },
      "type": "Fig"
    },
    {
      "data": {
        "value": "ex-zorder_demo.py-1.png"
      },
      "type": "Fig"
    }
  ],
  "title": null
}