{
  "children": [
    {
      "data": {
        "ce_status": "None",
        "entries": [
          [
            "#!/usr/bin/env python",
            "",
            "ch"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "\"\"\" toggle between two images by pressing \"t\"\n\nThe basic idea is to load two images (they can be different shapes) and plot\nthem to the same axes with hold \"on\".  Then, toggle the visible property of\nthem using keypress event handling\n\nIf you want two images with different shapes to be plotted with the same\nextent, they must have the same \"extent\" property\n\nAs usual, we'll define some random images for demo.  Real data is much more\nexciting!\n\nNote, on the wx backend on some platforms (eg linux), you have to\nfirst click on the figure before the keypress events are activated.\nIf you know how to fix this, please email us!\n\n\"\"\"",
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
            "pylab",
            "pylab",
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
            "*",
            "",
            "o"
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
            "# two images x1 is initially visible, x2 is not",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "x1",
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
            "100",
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
            "x2",
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
            "150",
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
            "175",
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
            "# arbitrary extent - both images must have same extent if you want",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# them to be resampled into the same axes space",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "extent",
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
            "im1",
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
            "imshow",
            "matplotlib.pyplot.imshow",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "x1",
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
            "extent",
            "builtins.tuple",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "extent",
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
            "im2",
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
            "imshow",
            "matplotlib.pyplot.imshow",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "x2",
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
            "extent",
            "builtins.tuple",
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "extent",
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
            "hold",
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
            "im2",
            null,
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
            "toggle_images",
            "__main__.toggle_images",
            "nf"
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
            "'",
            "",
            "s1"
          ],
          [
            "toggle the visible state of the two images",
            "",
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
            "    ",
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
            "key",
            null,
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "!=",
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
            "t",
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
            "return",
            null,
            "k"
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
            "b1",
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
            "im1",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "get_visible",
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
            "    ",
            "",
            ""
          ],
          [
            "b2",
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
            "im2",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "get_visible",
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
            "    ",
            "",
            ""
          ],
          [
            "im1",
            null,
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
            "not",
            null,
            "ow"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "b1",
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
            "    ",
            "",
            ""
          ],
          [
            "im2",
            null,
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
            "not",
            null,
            "ow"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "b2",
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
            "    ",
            "",
            ""
          ],
          [
            "draw",
            "matplotlib.pyplot.draw",
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
            "connect",
            "matplotlib.pyplot.connect",
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
            "key_press_event",
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
            "toggle_images",
            "__main__.toggle_images",
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