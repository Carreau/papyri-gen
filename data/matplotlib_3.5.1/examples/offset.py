{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          [
            "\"\"\"\n=========================\nAutomatic Text Offsetting\n=========================\n\nThis example demonstrates mplot3d's offset text display.\nAs one rotates the 3D figure, the offsets should remain oriented the\nsame way as the axis label, and should also be located \"away\"\nfrom the center of the plot.\n\nThis demo triggers the display of the offset text for the x and\ny axis by adding 1e5 to X and Y. Anything less would not\nautomatically trigger it.\n\"\"\"",
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
            ".",
            "",
            "o"
          ],
          [
            "add_subplot",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "projection",
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
            "3d",
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
            "X",
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
            "Y",
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
            "mgrid",
            "numpy.lib.index_tricks.MGridClass",
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
            ":",
            "",
            ""
          ],
          [
            "6",
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
            ":",
            "",
            ""
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
            "0",
            "",
            "mi"
          ],
          [
            ":",
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
            ":",
            "",
            ""
          ],
          [
            "0.25",
            "",
            "mf"
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
            "Z",
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
            "sqrt",
            "numpy.ufunc",
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
            "abs",
            "numpy.ufunc",
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
            "X",
            "numpy.ndarray",
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
            "Y",
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
            "plot_surface",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "X",
            "numpy.ndarray",
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
            "1e5",
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
            "Y",
            null,
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
            "1e5",
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
            "Z",
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
            "cmap",
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
            "autumn",
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
            "cstride",
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
            "rstride",
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
            "\"",
            "",
            "s2"
          ],
          [
            "X label",
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
            "\"",
            "",
            "s2"
          ],
          [
            "Y label",
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
            "set_zlabel",
            null,
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
            "Z label",
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
            "set_zlim",
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
        "value": "ex-offset.py-0.png"
      },
      "type": "Fig"
    }
  ],
  "title": null
}