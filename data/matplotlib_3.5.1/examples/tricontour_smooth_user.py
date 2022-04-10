{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          {
            "link": {
              "data": "\"\"\"\n======================\nTricontour Smooth User\n======================\n\nDemonstrates high-resolution tricontouring on user-defined triangular grids\nwith `matplotlib.tri.UniformTriRefiner`.\n\"\"\"",
              "type": "str"
            },
            "type": "sd"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "import",
              "type": "str"
            },
            "type": "kn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "matplotlib",
              "type": "str"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": "tri",
              "type": "str"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "as",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "tri",
              "type": "str"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "import",
              "type": "str"
            },
            "type": "kn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "matplotlib",
              "type": "str"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": "pyplot",
              "type": "str"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "as",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "plt",
              "type": "str"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "import",
              "type": "str"
            },
            "type": "kn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "numpy",
              "type": "str"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "as",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": "nn"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# ----------------------------------------------------------------------------",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# Analytical test function",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# ----------------------------------------------------------------------------",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "def",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "function_z",
              "type": "str"
            },
            "type": "nf"
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "x",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "y",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "r1",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "sqrt",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.5",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "x",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "2",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "+",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.5",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "y",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "2",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "theta1",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "arctan2",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.5",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "x",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.5",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "y",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "r2",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "sqrt",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "x",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.2",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "2",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "+",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "y",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.2",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "2",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "theta2",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "arctan2",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "x",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.2",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "y",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.2",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "z",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "2",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "exp",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "r1",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "/",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "10",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "2",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "1",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "30.",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "cos",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "7.",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "theta1",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "+",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "          ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "exp",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "r2",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "/",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "10",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "2",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "1",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "30.",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "cos",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "11.",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "theta2",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "+",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "          ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.7",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "x",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "2",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "+",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "y",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "2",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "return",
              "type": "str"
            },
            "type": "k"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "max",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "z",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "z",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "/",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "max",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "z",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "-",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "min",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "z",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# ----------------------------------------------------------------------------",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# Creating a Triangulation",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# ----------------------------------------------------------------------------",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# First create the x and y coordinates of the points.",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "n_angles",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "20",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "n_radii",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "10",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "min_radius",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.15",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "radii",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "linspace",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "min_radius",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.95",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "n_radii",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "angles",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "linspace",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "2",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "pi",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "n_angles",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "endpoint",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "False",
              "type": "str"
            },
            "type": "kc"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "angles",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "repeat",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "angles",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "[",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "newaxis",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "]",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "n_radii",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "axis",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "1",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "angles",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "[",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "1",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ":",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "2",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": "]",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "+",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "pi",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "/",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "n_angles",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "x",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "radii",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "cos",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "angles",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "flatten",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "y",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "radii",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "sin",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "angles",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "flatten",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "z",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "function_z",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "x",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "y",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# Now create the Triangulation.",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# (Creating a Triangulation without specifying the triangles results in the",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# Delaunay triangulation of the points.)",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "triang",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "tri",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "Triangulation",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "x",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "y",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# Mask off unwanted triangles.",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "triang",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "set_mask",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "hypot",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "x",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "[",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "triang",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "triangles",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "]",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "mean",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "axis",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "1",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "                         ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "y",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "[",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "triang",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "triangles",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "]",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "mean",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "axis",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "1",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "                ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "<",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "min_radius",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# ----------------------------------------------------------------------------",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# Refine data",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# ----------------------------------------------------------------------------",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "refiner",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "tri",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "UniformTriRefiner",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "triang",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "tri_refi",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "z_test_refi",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "refiner",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "refine_field",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "z",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "subdiv",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "3",
              "type": "str"
            },
            "type": "mi"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# ----------------------------------------------------------------------------",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# Plot the triangulation and the high-res iso-contours",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# ----------------------------------------------------------------------------",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "fig",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "ax",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "plt",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "subplots",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "ax",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "set_aspect",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "equal",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "ax",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "triplot",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "triang",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "lw",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "0.5",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "color",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "white",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "levels",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "np",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "arange",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "1.",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.025",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "ax",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "tricontourf",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "tri_refi",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "z_test_refi",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "levels",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "levels",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "cmap",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "terrain",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "ax",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "tricontour",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "tri_refi",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "z_test_refi",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "levels",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "levels",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "              ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "colors",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "[",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "0.25",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "0.5",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "0.5",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "0.5",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "0.5",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "]",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "              ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "linewidths",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "=",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "[",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "1.0",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.5",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.5",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.5",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": ",",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.5",
              "type": "str"
            },
            "type": "mf"
          },
          {
            "link": {
              "data": "]",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "ax",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "set_title",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\"",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "High-resolution tricontouring",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "\"",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "plt",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "show",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": ")",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#############################################################################",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# .. admonition:: References",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#    The use of the following functions, methods, classes and modules is shown",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#    in this example:",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#    - `matplotlib.axes.Axes.tricontour` / `matplotlib.pyplot.tricontour`",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#    - `matplotlib.axes.Axes.tricontourf` / `matplotlib.pyplot.tricontourf`",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#    - `matplotlib.tri`",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#    - `matplotlib.tri.Triangulation`",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#    - `matplotlib.tri.UniformTriRefiner`",
              "type": "str"
            },
            "type": "c1"
          },
          {
            "link": {
              "data": "\n",
              "type": "str"
            },
            "type": ""
          }
        ],
        "out": ""
      },
      "type": "Code2"
    },
    {
      "data": {
        "value": {
          "kind": "assets",
          "module": "matplotlib",
          "path": "ex-tricontour_smooth_user.py-0.png",
          "version": "3.5.1"
        }
      },
      "type": "Fig"
    }
  ],
  "title": null
}