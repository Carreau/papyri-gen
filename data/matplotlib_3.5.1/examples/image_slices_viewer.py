{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          [
            "\"\"\"\n===================\nImage Slices Viewer\n===================\n\nScroll through 2D image slices of a 3D array.\n\"\"\"",
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
            "# Fixing random state for reproducibility",
            "",
            "c1"
          ],
          [
            "\n",
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
            "random",
            "numpy.random",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "seed",
            "numpy.random.mtrand.RandomState.seed",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "19680801",
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
            "\n",
            "",
            ""
          ],
          [
            "class",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "IndexTracker",
            "__main__.IndexTracker",
            "nc"
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
            "__init__",
            "__main__.IndexTracker.__init__",
            "fm"
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "self",
            "__main__.IndexTracker",
            "bp"
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
            "X",
            "builtins.float",
            ""
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
            "        ",
            "",
            ""
          ],
          [
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
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
            "ax",
            null,
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "        ",
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
            "use scroll wheel to navigate images",
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
            "        ",
            "",
            ""
          ],
          [
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "X",
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
            "X",
            "builtins.float",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "        ",
            "",
            ""
          ],
          [
            "rows",
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
            "cols",
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
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "slices",
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
            "X",
            "builtins.float",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "shape",
            "numpy.ndarray.shape",
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "        ",
            "",
            ""
          ],
          [
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "ind",
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
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "slices",
            null,
            ""
          ],
          [
            "/",
            "",
            "o"
          ],
          [
            "/",
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
            "        ",
            "",
            ""
          ],
          [
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "im",
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
            "imshow",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "X",
            "builtins.float",
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
            ":",
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
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "ind",
            "builtins.int",
            ""
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
            "        ",
            "",
            ""
          ],
          [
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "update",
            "__main__.IndexTracker.update",
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
            "    ",
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
            "on_scroll",
            "__main__.IndexTracker.on_scroll",
            "nf"
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "self",
            "__main__.IndexTracker",
            "bp"
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
            "event",
            null,
            ""
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
            "        ",
            "",
            ""
          ],
          [
            "print",
            "builtins.print",
            "nb"
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
            "%s",
            "",
            "si"
          ],
          [
            " ",
            "",
            "s2"
          ],
          [
            "%s",
            "",
            "si"
          ],
          [
            "\"",
            "",
            "s2"
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
            "(",
            "",
            ""
          ],
          [
            "event",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "button",
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
            "event",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "step",
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
            "        ",
            "",
            ""
          ],
          [
            "if",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "event",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "button",
            null,
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "==",
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
            "up",
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
            "\n",
            "",
            ""
          ],
          [
            "            ",
            "",
            ""
          ],
          [
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "ind",
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
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "ind",
            "builtins.int",
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
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "slices",
            null,
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "        ",
            "",
            ""
          ],
          [
            "else",
            null,
            "k"
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
            "            ",
            "",
            ""
          ],
          [
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "ind",
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
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "ind",
            "builtins.int",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "-",
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
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "slices",
            null,
            ""
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "        ",
            "",
            ""
          ],
          [
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "update",
            "__main__.IndexTracker.update",
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
            "    ",
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
            "update",
            "__main__.IndexTracker.update",
            "nf"
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "self",
            "__main__.IndexTracker",
            "bp"
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
            "        ",
            "",
            ""
          ],
          [
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "im",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "set_data",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "X",
            "builtins.float",
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
            ":",
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
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "ind",
            "builtins.int",
            ""
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
            "        ",
            "",
            ""
          ],
          [
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
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
            "'",
            "",
            "s1"
          ],
          [
            "slice ",
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
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "ind",
            "builtins.int",
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
            "        ",
            "",
            ""
          ],
          [
            "self",
            "__main__.IndexTracker",
            "bp"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "im",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "axes",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "figure",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "canvas",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "draw",
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
            "random",
            "numpy.random",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "rand",
            "numpy.random.mtrand.RandomState.rand",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "20",
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
            "20",
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
            "40",
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
            "tracker",
            "__main__.IndexTracker",
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
            "IndexTracker",
            "__main__.IndexTracker",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "ax",
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
            "X",
            "builtins.float",
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
            "canvas",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "mpl_connect",
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
            "scroll_event",
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
            "tracker",
            "__main__.IndexTracker",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "on_scroll",
            "__main__.IndexTracker.on_scroll",
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
          ]
        ],
        "out": ""
      },
      "type": "Code"
    },
    {
      "data": {
        "value": "ex-image_slices_viewer.py-0.png"
      },
      "type": "Fig"
    }
  ],
  "title": null
}