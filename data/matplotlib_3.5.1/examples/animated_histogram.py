{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          [
            "\"\"\"\n==================\nAnimated histogram\n==================\n\nUse histogram's `.BarContainer` to draw a bunch of rectangles for an animated\nhistogram.\n\"\"\"",
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
            "animation",
            "matplotlib.animation",
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
            "animation",
            "matplotlib.animation",
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
            "# Fixing bin edges",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "HIST_BINS",
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
            "4",
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
            "\n",
            "",
            ""
          ],
          [
            "# histogram our data with numpy",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "data",
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
            "randn",
            "numpy.random.mtrand.RandomState.randn",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "1000",
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
            "n",
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
            "_",
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
            "histogram",
            "numpy.lib.histograms.histogram",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "data",
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
            "HIST_BINS",
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
            "# To animate the histogram, we need an ``animate`` function, which generates",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# a random set of numbers and updates the heights of rectangles. We utilize a",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# python closure to track an instance of `.BarContainer` whose `.Rectangle`",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# patches we shall update.",
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
            "prepare_animation",
            "__main__.prepare_animation",
            "nf"
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "bar_container",
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
            "animate",
            null,
            "nf"
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "frame_number",
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
            "# simulate new data coming in",
            "",
            "c1"
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
            "data",
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
            "randn",
            "numpy.random.mtrand.RandomState.randn",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "1000",
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
            "        ",
            "",
            ""
          ],
          [
            "n",
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
            "_",
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
            "histogram",
            "numpy.lib.histograms.histogram",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "data",
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
            "HIST_BINS",
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
            "        ",
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
            "count",
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
            "rect",
            null,
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
            "zip",
            "builtins.zip",
            "nb"
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "n",
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
            "bar_container",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "patches",
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
            "            ",
            "",
            ""
          ],
          [
            "rect",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "set_height",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "count",
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
            "        ",
            "",
            ""
          ],
          [
            "return",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "bar_container",
            null,
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "patches",
            null,
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
            "return",
            null,
            "k"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "animate",
            null,
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
            "# Using :func:`~matplotlib.pyplot.hist` allows us to get an instance of",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# `.BarContainer`, which is a collection of `.Rectangle` instances. Calling",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# ``prepare_animation`` will define ``animate`` function working with supplied",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# `.BarContainer`, all this is used to setup `.FuncAnimation`.",
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
            "_",
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
            "_",
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
            "bar_container",
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
            "hist",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "data",
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
            "HIST_BINS",
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
            "\n",
            "",
            ""
          ],
          [
            "                              ",
            "",
            ""
          ],
          [
            "ec",
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
            "yellow",
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
            "fc",
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
            "green",
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
            "alpha",
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
            "top",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "55",
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
            "# set safe limit to ensure that all data is visible.",
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
            "ani",
            "matplotlib.animation.FuncAnimation",
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
            "animation",
            "matplotlib.animation",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "FuncAnimation",
            "matplotlib.animation.FuncAnimation",
            ""
          ],
          [
            "(",
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
            "prepare_animation",
            "__main__.prepare_animation",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "bar_container",
            null,
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
            "50",
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
            "                              ",
            "",
            ""
          ],
          [
            "repeat",
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
            "blit",
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
        "value": "ex-animated_histogram.py-0.png"
      },
      "type": "Fig"
    }
  ],
  "title": null
}