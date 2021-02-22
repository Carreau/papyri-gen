{
  "children": [
    {
      "data": {
        "ce_status": "None",
        "entries": [
          [
            "# Same as basic_example, but writes files using a single MovieWriter instance",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# without putting on screen",
            "",
            "c1"
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
            "\n",
            "",
            ""
          ],
          [
            "matplotlib",
            "matplotlib",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "use",
            "matplotlib.use",
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
            "Agg",
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
            "update_line",
            "__main__.update_line",
            "nf"
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "num",
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
            "data",
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
            "line",
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
            "line",
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
            "data",
            null,
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            ",",
            "",
            ""
          ],
          [
            ":",
            "",
            ""
          ],
          [
            "num",
            null,
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
            "line",
            null,
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
            "\n",
            "",
            ""
          ],
          [
            "# Set up formatting for the movie files",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "Writer",
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
            "writers",
            "matplotlib.animation.MovieWriterRegistry",
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
            "ffmpeg",
            null,
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
            "\n",
            "",
            ""
          ],
          [
            "writer",
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
            "Writer",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "fps",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
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
            "metadata",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
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
            "artist",
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
            "Me",
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
            "bitrate",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "1800",
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
            "25",
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
            "l",
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
            "[",
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
            "[",
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
            "'",
            "",
            "s1"
          ],
          [
            "r-",
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
            "'",
            "",
            "s1"
          ],
          [
            "x",
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
            "test",
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
            "line_ani",
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
            "fig1",
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
            "update_line",
            "__main__.update_line",
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
            "25",
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
            "fargs",
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
            "l",
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
            "interval",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
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
            "line_ani",
            "matplotlib.animation.FuncAnimation",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "save",
            "matplotlib.animation.Animation.save",
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
            "lines.mp4",
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
            "writer",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "writer",
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
            "\n",
            "",
            ""
          ],
          [
            "x",
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
            "arange",
            "numpy.arange",
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
            "9",
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
            "y",
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
            "arange",
            "numpy.arange",
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
            "9",
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
            ".",
            "",
            "o"
          ],
          [
            "reshape",
            "numpy.ndarray.reshape",
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
            "base",
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
            "hypot",
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
            "y",
            "numpy.ndarray",
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
            "ims",
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
            "add",
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
            "arange",
            "numpy.arange",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "15",
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
            "ims",
            "builtins.list",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "append",
            "builtins.list.append",
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
            "pcolor",
            "matplotlib.pyplot.pcolor",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "x",
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
            "y",
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
            "base",
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
            "add",
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
            "norm",
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
            "Normalize",
            "matplotlib.colors.Normalize",
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
            "im_ani",
            "matplotlib.animation.ArtistAnimation",
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
            "ArtistAnimation",
            "matplotlib.animation.ArtistAnimation",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "fig2",
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
            "ims",
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
            "interval",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
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
            " ",
            "",
            ""
          ],
          [
            "repeat_delay",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "3000",
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
            "    ",
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
            "im_ani",
            "matplotlib.animation.ArtistAnimation",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "save",
            "matplotlib.animation.Animation.save",
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
            "im.mp4",
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
            "writer",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "writer",
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
          ]
        ],
        "out": ""
      },
      "type": "Code"
    }
  ],
  "title": null
}