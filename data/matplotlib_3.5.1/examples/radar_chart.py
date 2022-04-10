{
  "children": [
    {
      "data": {
        "ce_status": "execed",
        "entries": [
          {
            "link": {
              "data": "\"\"\"\n======================================\nRadar chart (aka spider or star chart)\n======================================\n\nThis example creates a radar chart, also known as a spider or star chart [1]_.\n\nAlthough this example allows a frame of either 'circle' or 'polygon', polygon\nframes don't have proper gridlines (the lines are circles instead of polygons).\nIt's possible to get a polygon grid by setting GRIDLINE_INTERPOLATION_STEPS in\nmatplotlib.axis to the desired number of vertices, but the orientation of the\npolygon is not aligned with the radial axes.\n\n.. [1] https://en.wikipedia.org/wiki/Radar_chart\n\"\"\"",
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
              "data": "from",
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
              "data": "patches",
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
              "data": "Circle",
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
              "data": "RegularPolygon",
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
              "data": "from",
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
              "data": "path",
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
              "data": "Path",
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
              "data": "from",
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
              "data": "projections",
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
              "data": "polar",
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
              "data": "PolarAxes",
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
              "data": "from",
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
              "data": "projections",
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
              "data": "register_projection",
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
              "data": "from",
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
              "data": "spines",
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
              "data": "Spine",
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
              "data": "from",
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
              "data": "transforms",
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
              "data": "Affine2D",
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
              "data": "radar_factory",
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
              "data": "num_vars",
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
              "data": "frame",
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
              "data": "circle",
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
              "data": "\"\"\"\n    Create a radar chart with `num_vars` axes.\n\n    This function creates a RadarAxes projection and registers it.\n\n    Parameters\n    ----------\n    num_vars : int\n        Number of variables for radar chart.\n    frame : {'circle', 'polygon'}\n        Shape of frame surrounding axes.\n\n    \"\"\"",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# calculate evenly-spaced axis angles",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "theta",
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
              "data": "*",
              "type": "str"
            },
            "type": "o"
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
              "data": "num_vars",
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
              "data": "class",
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
              "data": "RadarAxes",
              "type": "str"
            },
            "type": "nc"
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
              "data": "PolarAxes",
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "name",
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
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "radar",
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# use 1 line segment to connect specified points",
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
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "RESOLUTION",
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
              "data": "1",
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "        ",
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
              "data": "__init__",
              "type": "str"
            },
            "type": "fm"
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
              "data": "self",
              "type": "str"
            },
            "type": "bp"
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
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "args",
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
              "data": "kwargs",
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
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "super",
              "type": "str"
            },
            "type": "nb"
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
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "__init__",
              "type": "str"
            },
            "type": "fm"
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
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "args",
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
              "data": "kwargs",
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
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# rotate plot such that the first axis is at the top",
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
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "self",
              "type": "str"
            },
            "type": "bp"
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
              "data": "set_theta_zero_location",
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
              "data": "N",
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
              "data": "        ",
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
              "data": "fill",
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
              "data": "self",
              "type": "str"
            },
            "type": "bp"
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
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "args",
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
              "data": "closed",
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
              "data": "True",
              "type": "str"
            },
            "type": "kc"
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
              "data": "kwargs",
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
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\"\"\"Override fill so that line is closed by default\"\"\"",
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
              "data": "            ",
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
              "data": "super",
              "type": "str"
            },
            "type": "nb"
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
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "fill",
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
              "data": "closed",
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
              "data": "closed",
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
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "args",
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
              "data": "kwargs",
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
              "data": "        ",
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
              "data": "plot",
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
              "data": "self",
              "type": "str"
            },
            "type": "bp"
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
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "args",
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
              "data": "kwargs",
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
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "\"\"\"Override plot so that line is closed by default\"\"\"",
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
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "lines",
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
              "data": "super",
              "type": "str"
            },
            "type": "nb"
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
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "plot",
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
              "data": "*",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "args",
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
              "data": "kwargs",
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
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "for",
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
              "data": "line",
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
              "data": "in",
              "type": "str"
            },
            "type": "ow"
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
              "data": "lines",
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
              "data": "                ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "self",
              "type": "str"
            },
            "type": "bp"
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
              "data": "_close_line",
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
              "data": "line",
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
              "data": "        ",
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
              "data": "_close_line",
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
              "data": "self",
              "type": "str"
            },
            "type": "bp"
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
              "data": "line",
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
              "data": "            ",
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
              "data": "line",
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
              "data": "get_data",
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
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# FIXME: markers at x[0], y[0] get doubled-up",
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
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "if",
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
              "data": "0",
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
              "data": "!=",
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
              "data": "[",
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
              "data": "1",
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
              "data": "                ",
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
              "data": "append",
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
              "data": "0",
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
              "data": "append",
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
              "data": "y",
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
              "data": "[",
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
              "data": "                ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "line",
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
              "data": "set_data",
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
              "data": "        ",
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
              "data": "set_varlabels",
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
              "data": "self",
              "type": "str"
            },
            "type": "bp"
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
              "data": "labels",
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
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "self",
              "type": "str"
            },
            "type": "bp"
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
              "data": "set_thetagrids",
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
              "data": "degrees",
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
              "data": "theta",
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
              "data": "labels",
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
              "data": "        ",
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
              "data": "_gen_axes_patch",
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
              "data": "self",
              "type": "str"
            },
            "type": "bp"
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
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# The Axes patch must be centered at (0.5, 0.5) and of radius 0.5",
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
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# in axes coordinates.",
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
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "if",
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
              "data": "frame",
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
              "data": "==",
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
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "circle",
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
              "data": "                ",
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
              "data": "Circle",
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
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "elif",
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
              "data": "frame",
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
              "data": "==",
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
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "polygon",
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
              "data": "                ",
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
              "data": "RegularPolygon",
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
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "num_vars",
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
              "data": "                                      ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "radius",
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
              "data": ".5",
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
              "data": "edgecolor",
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
              "data": "\"",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "k",
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
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "else",
              "type": "str"
            },
            "type": "k"
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
              "data": "                ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "raise",
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
              "data": "ValueError",
              "type": "str"
            },
            "type": "ne"
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
              "data": "Unknown value for ",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "frame",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": ": ",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "%s",
              "type": "str"
            },
            "type": "si"
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
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "%",
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
              "data": "frame",
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
              "data": "        ",
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
              "data": "_gen_axes_spines",
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
              "data": "self",
              "type": "str"
            },
            "type": "bp"
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
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "if",
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
              "data": "frame",
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
              "data": "==",
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
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "circle",
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
              "data": "                ",
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
              "data": "super",
              "type": "str"
            },
            "type": "nb"
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
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "_gen_axes_spines",
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
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "elif",
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
              "data": "frame",
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
              "data": "==",
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
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "polygon",
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
              "data": "                ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# spine_type must be 'left'/'right'/'top'/'bottom'/'circle'.",
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
              "data": "                ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "spine",
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
              "data": "Spine",
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
              "data": "axes",
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
              "data": "self",
              "type": "str"
            },
            "type": "bp"
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
              "data": "                              ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "spine_type",
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
              "data": "circle",
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "                              ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "path",
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
              "data": "Path",
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
              "data": "unit_regular_polygon",
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
              "data": "num_vars",
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
              "data": "                ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# unit_regular_polygon gives a polygon of radius 1 centered at",
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
              "data": "                ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# (0, 0) but we want a polygon of radius 0.5 centered at (0.5,",
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
              "data": "                ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# 0.5) in axes coordinates.",
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
              "data": "                ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "spine",
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
              "data": "set_transform",
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
              "data": "Affine2D",
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
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "scale",
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
              "data": ".5",
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
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "translate",
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
              "data": ".5",
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
              "data": ".5",
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
              "data": "                                    ",
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
              "data": "self",
              "type": "str"
            },
            "type": "bp"
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
              "data": "transAxes",
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
              "data": "{",
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
              "data": "polar",
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
              "data": ":",
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
              "data": "spine",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "}",
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
              "data": "            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "else",
              "type": "str"
            },
            "type": "k"
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
              "data": "                ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "raise",
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
              "data": "ValueError",
              "type": "str"
            },
            "type": "ne"
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
              "data": "Unknown value for ",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "frame",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "'",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": ": ",
              "type": "str"
            },
            "type": "s2"
          },
          {
            "link": {
              "data": "%s",
              "type": "str"
            },
            "type": "si"
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
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "%",
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
              "data": "frame",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "register_projection",
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
              "data": "RadarAxes",
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
              "data": "theta",
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
              "data": "example_data",
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
              "data": "# The following data is from the Denver Aerosol Sources and Health study.",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# See doi:10.1016/j.atmosenv.2008.12.017",
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
              "data": "    ",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# The data are pollution source profile estimates for five modeled",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# pollution sources (e.g., cars, wood-burning, etc) that emit 7-9 chemical",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# species. The radar charts are experimented with here to see if we can",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# nicely visualize how the modeled source profiles change across four",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# scenarios:",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#  1) No gas-phase species present, just seven particulate counts on",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#     Sulfate",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#     Nitrate",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#     Elemental Carbon (EC)",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#     Organic Carbon fraction 1 (OC)",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#     Organic Carbon fraction 2 (OC2)",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#     Organic Carbon fraction 3 (OC3)",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#     Pyrolized Organic Carbon (OP)",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#  2)Inclusion of gas-phase specie carbon monoxide (CO)",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#  3)Inclusion of gas-phase specie ozone (O3).",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "#  4)Inclusion of both gas-phase species is present...",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "data",
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
              "data": "[",
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
              "data": "        ",
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
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "Sulfate",
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
              "data": "Nitrate",
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
              "data": "EC",
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
              "data": "OC1",
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
              "data": "OC2",
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
              "data": "OC3",
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
              "data": "OP",
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
              "data": "CO",
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
              "data": "O3",
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
              "data": "        ",
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
              "data": "Basecase",
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
              "data": "[",
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
              "data": "            ",
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
              "data": "0.88",
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
              "data": "0.01",
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
              "data": "0.03",
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
              "data": "0.03",
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
              "data": "0.00",
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
              "data": "0.06",
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
              "data": "0.01",
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
              "data": "0.00",
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
              "data": "0.00",
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
              "data": "            ",
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
              "data": "0.07",
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
              "data": "0.04",
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
              "data": "0.05",
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
              "data": "0.00",
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
              "data": "0.02",
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
              "data": "0.01",
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
              "data": "0.00",
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
              "data": "0.00",
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
              "data": "            ",
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
              "data": "0.01",
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
              "data": "0.02",
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
              "data": "0.85",
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
              "data": "0.19",
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
              "data": "0.05",
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
              "data": "0.10",
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
              "data": "0.00",
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
              "data": "0.00",
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
              "data": "0.00",
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
              "data": "            ",
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
              "data": "0.02",
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
              "data": "0.01",
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
              "data": "0.07",
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
              "data": "0.01",
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
              "data": "0.21",
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
              "data": "0.12",
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
              "data": "0.98",
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
              "data": "0.00",
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
              "data": "0.00",
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
              "data": "            ",
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
              "data": "0.01",
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
              "data": "0.01",
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
              "data": "0.02",
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
              "data": "0.71",
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
              "data": "0.74",
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
              "data": "0.70",
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
              "data": "0.00",
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
              "data": "0.00",
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
              "data": "0.00",
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
              "data": "        ",
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
              "data": "With CO",
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
              "data": "[",
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
              "data": "            ",
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
              "data": "0.88",
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
              "data": "0.02",
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
              "data": "0.02",
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
              "data": "0.02",
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
              "data": "0.00",
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
              "data": "0.05",
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
              "data": "0.00",
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
              "data": "0.05",
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
              "data": "0.00",
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
              "data": "            ",
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
              "data": "0.08",
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
              "data": "0.94",
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
              "data": "0.04",
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
              "data": "0.02",
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
              "data": "0.00",
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
              "data": "0.01",
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
              "data": "0.12",
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
              "data": "0.04",
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
              "data": "0.00",
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
              "data": "            ",
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
              "data": "0.01",
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
              "data": "0.01",
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
              "data": "0.79",
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
              "data": "0.10",
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
              "data": "0.00",
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
              "data": "0.05",
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
              "data": "0.00",
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
              "data": "0.31",
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
              "data": "0.00",
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
              "data": "            ",
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
              "data": "0.00",
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
              "data": "0.02",
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
              "data": "0.03",
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
              "data": "0.38",
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
              "data": "0.31",
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
              "data": "0.31",
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
              "data": "0.00",
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
              "data": "0.59",
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
              "data": "0.00",
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
              "data": "            ",
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
              "data": "0.02",
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
              "data": "0.02",
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
              "data": "0.11",
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
              "data": "0.47",
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
              "data": "0.69",
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
              "data": "0.58",
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
              "data": "0.88",
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
              "data": "0.00",
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
              "data": "0.00",
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
              "data": "        ",
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
              "data": "With O3",
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
              "data": "[",
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
              "data": "            ",
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
              "data": "0.89",
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
              "data": "0.01",
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
              "data": "0.07",
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
              "data": "0.00",
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
              "data": "0.00",
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
              "data": "0.05",
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
              "data": "0.00",
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
              "data": "0.00",
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
              "data": "0.03",
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
              "data": "            ",
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
              "data": "0.07",
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
              "data": "0.05",
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
              "data": "0.04",
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
              "data": "0.00",
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
              "data": "0.02",
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
              "data": "0.12",
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
              "data": "0.00",
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
              "data": "0.00",
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
              "data": "            ",
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
              "data": "0.01",
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
              "data": "0.02",
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
              "data": "0.86",
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
              "data": "0.27",
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
              "data": "0.16",
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
              "data": "0.19",
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
              "data": "0.00",
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
              "data": "0.00",
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
              "data": "0.00",
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
              "data": "            ",
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
              "data": "0.01",
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
              "data": "0.03",
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
              "data": "0.00",
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
              "data": "0.32",
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
              "data": "0.29",
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
              "data": "0.27",
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
              "data": "0.00",
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
              "data": "0.00",
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
              "data": "0.95",
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
              "data": "            ",
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
              "data": "0.02",
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
              "data": "0.00",
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
              "data": "0.03",
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
              "data": "0.37",
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
              "data": "0.56",
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
              "data": "0.47",
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
              "data": "0.87",
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
              "data": "0.00",
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
              "data": "0.00",
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
              "data": "        ",
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
              "data": "CO & O3",
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
              "data": "[",
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
              "data": "            ",
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
              "data": "0.87",
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
              "data": "0.01",
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
              "data": "0.08",
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
              "data": "0.00",
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
              "data": "0.00",
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
              "data": "0.04",
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
              "data": "0.00",
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
              "data": "0.00",
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
              "data": "0.01",
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
              "data": "            ",
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
              "data": "0.09",
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
              "data": "0.02",
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
              "data": "0.03",
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
              "data": "0.00",
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
              "data": "0.01",
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
              "data": "0.13",
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
              "data": "0.06",
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
              "data": "0.00",
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
              "data": "            ",
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
              "data": "0.01",
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
              "data": "0.02",
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
              "data": "0.71",
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
              "data": "0.24",
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
              "data": "0.13",
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
              "data": "0.16",
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
              "data": "0.00",
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
              "data": "0.50",
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
              "data": "0.00",
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
              "data": "            ",
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
              "data": "0.01",
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
              "data": "0.03",
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
              "data": "0.00",
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
              "data": "0.28",
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
              "data": "0.24",
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
              "data": "0.23",
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
              "data": "0.00",
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
              "data": "0.44",
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
              "data": "0.88",
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
              "data": "            ",
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
              "data": "0.02",
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
              "data": "0.00",
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
              "data": "0.18",
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
              "data": "0.45",
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
              "data": "0.64",
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
              "data": "0.55",
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
              "data": "0.86",
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
              "data": "0.00",
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
              "data": "0.16",
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
              "data": "    ",
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
              "data": "data",
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "if",
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
              "data": "__name__",
              "type": "str"
            },
            "type": "vm"
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
              "data": "==",
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
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "__main__",
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
              "data": "N",
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
              "data": "9",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "theta",
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
              "data": "radar_factory",
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
              "data": "N",
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
              "data": "frame",
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
              "data": "polygon",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "data",
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
              "data": "example_data",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "spoke_labels",
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
              "data": "data",
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
              "data": "pop",
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
              "data": "    ",
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
              "data": "axs",
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
              "data": "figsize",
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
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "9",
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
              "data": "9",
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
              "data": " ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "nrows",
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
              "data": "2",
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
              "data": "ncols",
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
              "data": "2",
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "                            ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "subplot_kw",
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
              "data": "dict",
              "type": "str"
            },
            "type": "nb"
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
              "data": "projection",
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
              "data": "radar",
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
              "data": "fig",
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
              "data": "subplots_adjust",
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
              "data": "wspace",
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
              "data": "0.25",
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
              "data": "hspace",
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
              "data": "0.20",
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
              "data": "top",
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
              "data": "0.85",
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
              "data": "bottom",
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
              "data": "0.05",
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
              "data": "colors",
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
              "data": "b",
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
              "data": "r",
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
              "data": "g",
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
              "data": "m",
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
              "data": "y",
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
              "data": "# Plot the four cases from the example data on separate axes",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "for",
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
              "data": "ax",
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
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "title",
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
              "data": "case_data",
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
              "data": "in",
              "type": "str"
            },
            "type": "ow"
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
              "data": "zip",
              "type": "str"
            },
            "type": "nb"
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
              "data": "axs",
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
              "data": "flat",
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
              "data": "data",
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
              "data": "        ",
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
              "data": "set_rgrids",
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
              "data": "[",
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
              "data": "0.4",
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
              "data": "0.6",
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
              "data": "0.8",
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
              "data": "        ",
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
              "data": "title",
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
              "data": "weight",
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
              "data": "bold",
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
              "data": "size",
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
              "data": "medium",
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
              "data": "position",
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
              "data": "1.1",
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
              "data": "                     ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "horizontalalignment",
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
              "data": "center",
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
              "data": "verticalalignment",
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
              "data": "center",
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
              "data": "        ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "for",
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
              "data": "d",
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
              "data": "color",
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
              "data": "in",
              "type": "str"
            },
            "type": "ow"
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
              "data": "zip",
              "type": "str"
            },
            "type": "nb"
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
              "data": "case_data",
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
              "data": "colors",
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
              "data": "            ",
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
              "data": "plot",
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
              "data": "theta",
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
              "data": "d",
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
              "data": "color",
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
              "data": "            ",
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
              "data": "fill",
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
              "data": "theta",
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
              "data": "d",
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
              "data": "facecolor",
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
              "data": "color",
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
              "data": "alpha",
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
              "data": "0.25",
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
              "data": "        ",
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
              "data": "set_varlabels",
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
              "data": "spoke_labels",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "# add legend relative to top-left plot",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "labels",
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
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "Factor 1",
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
              "data": "Factor 2",
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
              "data": "Factor 3",
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
              "data": "Factor 4",
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
              "data": "Factor 5",
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
              "data": "    ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "legend",
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
              "data": "axs",
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
              "data": "0",
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
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "legend",
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
              "data": "labels",
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
              "data": "loc",
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
              "data": "(",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "0.9",
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
              "data": ".95",
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
              "data": "                              ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "labelspacing",
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
              "data": "0.1",
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
              "data": "fontsize",
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
              "data": "small",
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
              "data": "    ",
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
              "data": ".",
              "type": "str"
            },
            "type": "o"
          },
          {
            "link": {
              "data": "text",
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
              "data": "0.965",
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
              "data": "'",
              "type": "str"
            },
            "type": "s1"
          },
          {
            "link": {
              "data": "5-Factor Solution Profiles Across Four Scenarios",
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "             ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "horizontalalignment",
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
              "data": "center",
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
              "data": "black",
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
              "data": "weight",
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
              "data": "bold",
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
              "data": "\n",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "             ",
              "type": "str"
            },
            "type": ""
          },
          {
            "link": {
              "data": "size",
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
              "data": "large",
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
              "data": "    ",
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
              "data": "#    - `matplotlib.path`",
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
              "data": "#    - `matplotlib.path.Path`",
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
              "data": "#    - `matplotlib.spines`",
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
              "data": "#    - `matplotlib.spines.Spine`",
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
              "data": "#    - `matplotlib.projections`",
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
              "data": "#    - `matplotlib.projections.polar`",
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
              "data": "#    - `matplotlib.projections.polar.PolarAxes`",
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
              "data": "#    - `matplotlib.projections.register_projection`",
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
    }
  ],
  "title": null
}