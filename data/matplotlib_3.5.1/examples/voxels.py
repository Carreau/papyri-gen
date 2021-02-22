{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          [
            "\"\"\"\n==========================\n3D voxel / volumetric plot\n==========================\n\nDemonstrates plotting 3D volumetric objects with `.Axes3D.voxels`.\n\"\"\"",
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
            "# prepare some coordinates",
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
            "y",
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
            "z",
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
            "indices",
            "numpy.core.numeric.indices",
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
            "8",
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
            "8",
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
            "8",
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
            "# draw cuboids in the top left and bottom right corners, and a link between",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "# them",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "cube1",
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
            "x",
            null,
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "<",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
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
            " ",
            "",
            ""
          ],
          [
            "&",
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
            "y",
            null,
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "<",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
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
            " ",
            "",
            ""
          ],
          [
            "&",
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
            "z",
            null,
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "<",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
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
            "cube2",
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
            "x",
            null,
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            ">",
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
            "5",
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
            "&",
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
            "y",
            null,
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            ">",
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
            "5",
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
            "&",
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
            "z",
            null,
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            ">",
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
            "5",
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
            "link",
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
            "abs",
            "builtins.abs",
            "nb"
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "x",
            null,
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
            "y",
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
            "abs",
            "builtins.abs",
            "nb"
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "y",
            null,
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
            "z",
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
            "abs",
            "builtins.abs",
            "nb"
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "z",
            null,
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
            "x",
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
            "<",
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
            "# combine the objects into a single boolean array",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "voxelarray",
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
            "cube1",
            "builtins.int",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "|",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "cube2",
            "builtins.int",
            ""
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "|",
            "",
            "o"
          ],
          [
            " ",
            "",
            ""
          ],
          [
            "link",
            "builtins.int",
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
            "# set the colors of each object",
            "",
            "c1"
          ],
          [
            "\n",
            "",
            ""
          ],
          [
            "colors",
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
            "empty",
            "numpy.empty",
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "voxelarray",
            "builtins.int",
            ""
          ],
          [
            ".",
            "",
            "o"
          ],
          [
            "shape",
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
            "dtype",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "object",
            "builtins.object",
            "nb"
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
            "colors",
            "numpy.ndarray",
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            "link",
            "builtins.int",
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
            "red",
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
            "colors",
            "numpy.ndarray",
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            "cube1",
            "builtins.int",
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
            "blue",
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
            "colors",
            "numpy.ndarray",
            ""
          ],
          [
            "[",
            "",
            ""
          ],
          [
            "cube2",
            "builtins.int",
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
            "green",
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
            "\n",
            "",
            ""
          ],
          [
            "# and plot everything",
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
            "voxels",
            null,
            ""
          ],
          [
            "(",
            "",
            ""
          ],
          [
            "voxelarray",
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
            "facecolors",
            null,
            ""
          ],
          [
            "=",
            "",
            "o"
          ],
          [
            "colors",
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
            "edgecolor",
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
        "value": "ex-voxels.py-0.png"
      },
      "type": "Fig"
    }
  ],
  "title": null
}