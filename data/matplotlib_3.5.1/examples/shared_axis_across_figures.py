{
  "children": [
    {
      "data": {
        "ce_status": "None",
        "entries": [
          [
            "\"\"\"\nconnect the data limits on the axes in one figure with the axes in\nanother.  This is not the right way to do this for two axes in the\nsame figure -- use the sharex and sharey property in that case\n\"\"\"",
            "",
            "sd"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# -*- noplot -*-",
            "",
            "c1"
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
            "figure",
            "matplotlib.pyplot.figure",
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
            "show",
            "matplotlib.pyplot.show",
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
            "fig1",
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
            "fig2",
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
            "fig1",
            "builtins.int",
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
            "111",
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
            "fig2",
            "builtins.int",
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
            "111",
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
            "sharex",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
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
            "sharey",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "ax1",
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
            "numpy",
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
            "o",
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
            "numpy",
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
            "o",
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
            "# In the latest release, it is no longer necessary to do anything",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# special to share axes across figures:",
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
            "# ax1.sharex_foreign(ax2)",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# ax2.sharex_foreign(ax1)",
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
            "# ax1.sharey_foreign(ax2)",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# ax2.sharey_foreign(ax1)",
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