{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          [
            "\"\"\"\n=========\nPie Demo2\n=========\n\nMake a pie charts using `~.axes.Axes.pie`.\n\nThis example demonstrates some pie chart features like labels, varying size,\nautolabeling the percentage, offsetting a slice and adding a shadow.\n\"\"\"",
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
            "\n",
            "",
            ""
          ],
          [
            "# Some data",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "labels",
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
            "'",
            "",
            "s1"
          ],
          [
            "Frogs",
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
            "'",
            "",
            "s1"
          ],
          [
            "Hogs",
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
            "'",
            "",
            "s1"
          ],
          [
            "Dogs",
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
            "'",
            "",
            "s1"
          ],
          [
            "Logs",
            null,
            "s1"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "fracs",
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
            "15",
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
            "45",
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
            "# Make figure and axes",
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
            "axs",
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
            "# A standard pie plot",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "axs",
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
            "pie",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "fracs",
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
            "labels",
            "builtins.tuple",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "labels",
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
            "autopct",
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
            "%1.1f",
            "",
            "si"
          ],
          [
            "%%",
            "",
            "si"
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
            "shadow",
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
            "# Shift the second slice using explode",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "axs",
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
            ".",
            "",
            "o"
          ],
          [
            "pie",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "fracs",
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
            "labels",
            "builtins.tuple",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "labels",
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
            "autopct",
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
            "%.0f",
            "",
            "si"
          ],
          [
            "%%",
            "",
            "si"
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
            "shadow",
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
            "              ",
            "",
            ""
          ],
          [
            "explode",
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
            "# Adapt radius and text size for a smaller pie",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "patches",
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
            "texts",
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
            "autotexts",
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
            "axs",
            null,
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
            "pie",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "fracs",
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
            "labels",
            "builtins.tuple",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "labels",
            "builtins.tuple",
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
            "                                          ",
            "",
            ""
          ],
          [
            "autopct",
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
            "%.0f",
            "",
            "si"
          ],
          [
            "%%",
            "",
            "si"
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
            "\n",
            "",
            ""
          ],
          [
            "                                          ",
            "",
            ""
          ],
          [
            "textprops",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "{",
            "",
            ""
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "size",
            null,
            "s1"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            ":",
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
            "smaller",
            null,
            "s1"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "}",
            "",
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
            "                                          ",
            "",
            ""
          ],
          [
            "shadow",
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
            "radius",
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
            "# Make percent texts even smaller",
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
            "setp",
            "matplotlib.pyplot.setp",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "autotexts",
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
            "size",
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
            "x-small",
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
            "autotexts",
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
            ".",
            "",
            "o"
          ],
          [
            "set_color",
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
            "white",
            null,
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
            "# Use a smaller explode and turn of the shadow for better visibility",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "patches",
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
            "texts",
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
            "autotexts",
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
            "axs",
            null,
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
            ".",
            "",
            "o"
          ],
          [
            "pie",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "fracs",
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
            "labels",
            "builtins.tuple",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "labels",
            "builtins.tuple",
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
            "                                          ",
            "",
            ""
          ],
          [
            "autopct",
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
            "%.0f",
            "",
            "si"
          ],
          [
            "%%",
            "",
            "si"
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
            "\n",
            "",
            ""
          ],
          [
            "                                          ",
            "",
            ""
          ],
          [
            "textprops",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "{",
            "",
            ""
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "size",
            null,
            "s1"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            ":",
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
            "smaller",
            null,
            "s1"
          ],
          [
            "'",
            "",
            "s1"
          ],
          [
            "}",
            "",
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
            "                                          ",
            "",
            ""
          ],
          [
            "shadow",
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
            "radius",
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
            "\n",
            "",
            ""
          ],
          [
            "                                          ",
            "",
            ""
          ],
          [
            "explode",
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
            "setp",
            "matplotlib.pyplot.setp",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "autotexts",
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
            "size",
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
            "x-small",
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
            "autotexts",
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
            ".",
            "",
            "o"
          ],
          [
            "set_color",
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
            "white",
            null,
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
            "#    - `matplotlib.axes.Axes.pie` / `matplotlib.pyplot.pie`",
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
        "value": "ex-pie_demo2.py-0.png"
      },
      "type": "Fig"
    }
  ],
  "title": null
}