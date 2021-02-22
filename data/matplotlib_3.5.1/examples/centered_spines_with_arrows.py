{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          [
            "\"\"\"\n===========================\nCentered spines with arrows\n===========================\n\nThis example shows a way to draw a \"math textbook\" style plot, where the\nspines (\"axes lines\") are drawn at ``x = 0`` and ``y = 0``, and have arrows at\ntheir ends.\n\"\"\"",
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
            "# Move the left and bottom spines to x = 0 and y = 0, respectively.",
            "",
            "c1"
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
            "spines",
            null,
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            "\"",
            "",
            "s2"
          ],
          [
            "left",
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
            "\"",
            "",
            "s2"
          ],
          [
            "bottom",
            null,
            "s2"
          ],
          [
            "\"",
            "",
            "s2"
          ],
          [
            "]",
            "",
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
            "set_position",
            null,
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
            "\"",
            "",
            "s2"
          ],
          [
            "data",
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
            "# Hide the top and right spines.",
            "",
            "c1"
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
            "spines",
            null,
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            "\"",
            "",
            "s2"
          ],
          [
            "top",
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
            "\"",
            "",
            "s2"
          ],
          [
            "right",
            null,
            "s2"
          ],
          [
            "\"",
            "",
            "s2"
          ],
          [
            "]",
            "",
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
            "set_visible",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "False",
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
            "\n",
            "",
            ""
          ],
          [
            "# Draw arrows (as black triangles: \">k\"/\"^k\") at the end of the axes.  In each",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# case, one of the coordinates (0) is a data coordinate (i.e., y = 0 or x = 0,",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# respectively) and the other one (1) is an axes coordinate (i.e., at the very",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# right/top of the axes).  Also, disable clipping (clip_on=False) as the marker",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# actually spills out of the axes.",
            "",
            "c1"
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
            "\"",
            "",
            "s2"
          ],
          [
            ">k",
            "",
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
            "get_yaxis_transform",
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
            "clip_on",
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
            "\"",
            "",
            "s2"
          ],
          [
            "^k",
            "",
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
            "get_xaxis_transform",
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
            "clip_on",
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
            "\n",
            "",
            ""
          ],
          [
            "# Some sample data.",
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
            "1.",
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
        "value": "ex-centered_spines_with_arrows.py-0.png"
      },
      "type": "Fig"
    }
  ],
  "title": null
}