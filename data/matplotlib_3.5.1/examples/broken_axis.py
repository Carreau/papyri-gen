{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          [
            "\"\"\"\n===========\nBroken Axis\n===========\n\nBroken axis example, where the y-axis will have a portion cut out.\n\"\"\"",
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
            "pts",
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
            "*",
            "",
            "o"
          ],
          [
            ".2",
            "",
            "mf"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# Now let's make two outlier points which are far away from everything.",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "pts",
            "builtins.float",
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
            "14",
            "",
            "mi"
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
            ".8",
            "",
            "mf"
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
            "# If we were to simply plot pts, we'd lose most of the interesting",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# details due to the outliers. So let's 'break' or 'cut-out' the y-axis",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# into two portions - use the top (ax1) for the outliers, and the bottom",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# (ax2) for the details of the majority of our data",
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
            "subplots_adjust",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "hspace",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "0.05",
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
            "# adjust space between axes",
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
            "# plot the same data on both axes",
            "",
            "c1"
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
            "pts",
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
            "pts",
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
            "# zoom-in / limit the view to different portions of the data",
            "",
            "c1"
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
            "set_ylim",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            ".78",
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
            "# outliers only",
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
            "set_ylim",
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
            ".22",
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
            "# most of the data",
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
            "# hide the spines between ax and ax2",
            "",
            "c1"
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
            "spines",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "bottom",
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
            "spines",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "top",
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
            "xaxis",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "tick_top",
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
            "tick_params",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "labeltop",
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
            "  ",
            "",
            ""
          ],
          [
            "# don't put tick labels at the top",
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
            "xaxis",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "tick_bottom",
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
            "# Now, let's turn towards the cut-out slanted lines.",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# We create line objects in axes coordinates, in which (0,0), (0,1),",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# (1,0), and (1,1) are the four corners of the axes.",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# The slanted lines themselves are markers at those locations, such that the",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# lines keep their angle and position, independent of the axes size or scale",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# Finally, we need to disable clipping.",
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
            "d",
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
            ".5",
            "",
            "mf"
          ],
          [
            "  ",
            "",
            ""
          ],
          [
            "# proportion of vertical to horizontal extent of the slanted line",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "kwargs",
            "builtins.dict",
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
            "dict",
            "builtins.dict",
            "nb"
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "marker",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "[",
            "",
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
            "-",
            "",
            "o"
          ],
          [
            "d",
            "builtins.float",
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
            "d",
            "builtins.float",
            ""
          ],
          [
            ")",
            "",
            ""
          ],
          [
            "]",
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
            "markersize",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "12",
            "",
            "mi"
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
            "none",
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
            "mec",
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
            "mew",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
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
            "transAxes",
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
            "kwargs",
            "builtins.dict",
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
            "transAxes",
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
            "kwargs",
            "builtins.dict",
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
        "value": "ex-broken_axis.py-0.png"
      },
      "type": "Fig"
    }
  ],
  "title": null
}